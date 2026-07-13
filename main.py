import asyncio
import json
import os
import hashlib
import secrets
import time
import aiofiles
import psutil
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from urllib.parse import quote
from collections import deque, defaultdict
from pathlib import Path
import socket
import base64
from io import BytesIO
import httpx

from fastapi import FastAPI, Request, HTTPException, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import Response, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

# ─── تنظیمات ──────────────────────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("Eagle-Gateway")

IRAN_TZ = ZoneInfo("Asia/Tehran")

CONFIG = {
    "port": int(os.environ.get("PORT", 8000)),
    "secret": os.environ.get("SECRET_KEY", secrets.token_urlsafe(32)),
    "host": os.environ.get("RAILWAY_PUBLIC_DOMAIN", os.environ.get("RENDER_EXTERNAL_URL", "localhost")),
}

app = FastAPI(title="🪐 Eagle Gateway v10 Pro", docs_url=None, redoc_url=None)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# ─── State ────────────────────────────────────────────────────────────────────
DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
DATA_FILE = DATA_DIR / "eagle_state.json"
SAVE_LOCK = asyncio.Lock()

# ─── Auth ──────────────────────────────────────────────────────────────────────
SESSION_COOKIE = "eagle_session"
SESSION_TTL = 60 * 60 * 24 * 7

MAIN_ADMIN = {
    "username": "admin",
    "password_hash": hashlib.sha256(f"123456{CONFIG['secret']}".encode()).hexdigest(),
}

SESSIONS: dict = {}
SESSIONS_LOCK = asyncio.Lock()

# ─── Workspace ─────────────────────────────────────────────────────────────────
WORKSPACES: dict = {}
WORKSPACES_LOCK = asyncio.Lock()

# ─── In-Memory State ─────────────────────────────────────────────────────────
connections: dict = {}
stats = {"total_bytes": 0, "total_requests": 0, "total_errors": 0, "start_time": time.time()}
activity_logs: deque = deque(maxlen=200)
daily_traffic: dict = defaultdict(int)
device_connections: dict = {}
DEVICE_CONNECTIONS_LOCK = asyncio.Lock()
http_client: httpx.AsyncClient | None = None

# ─── Settings ─────────────────────────────────────────────────────────────────
DEFAULT_SETTINGS = {
    "clean_ips": [],
    "routes": [],
    "ad_filter_enabled": True,
    "porn_filter_enabled": True,
    "malware_filter_enabled": True,
}

PROTOCOLS = ("vless-ws",)
DEFAULT_PROTOCOL = "vless-ws"
DEFAULT_PORTS = [443, 8443, 2053, 2096, 2087, 2083, 8080]

FINGERPRINTS = {
    "chrome": "🌐 Chrome",
    "firefox": "🦊 Firefox",
    "safari": "🧭 Safari",
    "edge": "🌊 Edge",
    "ios": "📱 iOS",
    "android": "🤖 Android",
    "random": "🎲 Random",
    "none": "🚫 None",
}

# ─────────────────────────────────────────────────────────────────────────────
# ===== Functions =====
# ─────────────────────────────────────────────────────────────────────────────

def now_ir() -> datetime:
    return datetime.now(IRAN_TZ)

def hash_password(pw: str) -> str:
    return hashlib.sha256(f"{pw}{CONFIG['secret']}".encode()).hexdigest()

def generate_uuid() -> str:
    h = secrets.token_hex(16)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"

def get_host() -> str:
    return os.environ.get("RAILWAY_PUBLIC_DOMAIN", os.environ.get("RENDER_EXTERNAL_URL", CONFIG["host"]))

def fmt_bytes(b: int) -> str:
    if not b or b == 0:
        return "0 B"
    if b < 1024:
        return f"{b} B"
    if b < 1024**2:
        return f"{b/1024:.1f} KB"
    if b < 1024**3:
        return f"{b/1024**2:.2f} MB"
    if b < 1024**4:
        return f"{b/1024**3:.2f} GB"
    return f"{b/1024**4:.2f} TB"

def client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    return fwd.split(",")[0].strip() if fwd else request.client.host if request.client else "نامشخص"

def uptime() -> str:
    secs = int(time.time() - stats["start_time"])
    return f"{secs//3600:02d}:{(secs%3600)//60:02d}:{secs%60:02d}"

def parse_size_to_bytes(value: float, unit: str) -> int:
    unit = unit.upper()
    if unit == "GB":
        return int(value * 1024 ** 3)
    if unit == "MB":
        return int(value * 1024 ** 2)
    return int(value)

def is_link_expired(link: dict) -> bool:
    exp = link.get("expires_at")
    if not exp:
        return False
    try:
        return datetime.now() > datetime.fromisoformat(exp)
    except:
        return False

def is_link_allowed(link: dict | None) -> bool:
    if link is None:
        return False
    if not link.get("active", True):
        return False
    if is_link_expired(link):
        return False
    lb = link.get("limit_bytes", 0)
    if lb > 0 and link.get("used_bytes", 0) >= lb:
        return False
    return True

def generate_vless_link(uuid: str, host: str, remark: str = "", fingerprint: str = "chrome", port: int = 443) -> str:
    if not remark:
        remark = "عقاب"
    path = f"/ws/{uuid}"
    params = {
        "encryption": "none",
        "security": "tls",
        "type": "ws",
        "host": host,
        "path": path,
        "sni": host,
        "fp": fingerprint,
        "alpn": "h2,http/1.1",
    }
    query = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
    return f"vless://{uuid}@{host}:{port}?{query}#{quote(remark)}"

def log_activity(kind: str, message: str, level: str = "info"):
    activity_logs.append({
        "kind": kind,
        "level": level,
        "message": message,
        "time": datetime.now().isoformat(),
    })

# ─── State Functions ──────────────────────────────────────────────────────────

async def load_state():
    global WORKSPACES, MAIN_ADMIN
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if DATA_FILE.exists():
            async with aiofiles.open(DATA_FILE, "r") as f:
                data = json.loads(await f.read())
                WORKSPACES = data.get("workspaces", {})
                if "main_admin" in data:
                    MAIN_ADMIN["username"] = data["main_admin"].get("username", "admin")
                    MAIN_ADMIN["password_hash"] = data["main_admin"].get("password_hash", MAIN_ADMIN["password_hash"])
                logger.info(f"📂 Loaded {len(WORKSPACES)} workspaces")
    except Exception as e:
        logger.warning(f"Load state error: {e}")

async def save_state():
    async with SAVE_LOCK:
        try:
            data = {
                "workspaces": WORKSPACES,
                "main_admin": {
                    "username": MAIN_ADMIN["username"],
                    "password_hash": MAIN_ADMIN["password_hash"],
                },
                "saved_at": datetime.now().isoformat()
            }
            async with aiofiles.open(DATA_FILE, "w") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=2))
        except Exception as e:
            logger.warning(f"Save error: {e}")

# ─── Session Functions ──────────────────────────────────────────────────────

async def create_session() -> str:
    token = secrets.token_urlsafe(32)
    async with SESSIONS_LOCK:
        SESSIONS[token] = time.time() + SESSION_TTL
    return token

async def is_valid_session(token: str | None) -> bool:
    if not token:
        return False
    async with SESSIONS_LOCK:
        exp = SESSIONS.get(token)
        if exp is None or exp < time.time():
            SESSIONS.pop(token, None)
            return False
        return True

async def destroy_session(token: str | None):
    if token:
        async with SESSIONS_LOCK:
            SESSIONS.pop(token, None)

# ─── Auth Dependencies ──────────────────────────────────────────────────────

async def require_main_admin(req: Request):
    token = req.cookies.get(SESSION_COOKIE)
    if not await is_valid_session(token):
        raise HTTPException(401, "unauthorized")
    session_data = SESSIONS.get(token, {})
    if session_data.get("user_type") != "main_admin":
        raise HTTPException(403, "دسترسی محدود به ادمین اصلی")
    return token

async def require_workspace_admin(req: Request):
    token = req.cookies.get(SESSION_COOKIE)
    if not await is_valid_session(token):
        raise HTTPException(401, "unauthorized")
    session_data = SESSIONS.get(token, {})
    if session_data.get("user_type") != "workspace_admin":
        raise HTTPException(403, "دسترسی محدود به ادمین Workspace")
    workspace_id = session_data.get("workspace_id")
    if not workspace_id or workspace_id not in WORKSPACES:
        raise HTTPException(404, "Workspace یافت نشد")
    return workspace_id

# ─── Startup ─────────────────────────────────────────────────────────────────

@app.on_event("startup")
async def startup():
    global http_client
    http_client = httpx.AsyncClient(timeout=10.0)
    await load_state()
    logger.info(f"🪐 Eagle Gateway started on port {CONFIG['port']}")

@app.on_event("shutdown")
async def shutdown():
    await save_state()
    if http_client:
        await http_client.aclose()

# ─── ===== API: Login ===== ──────────────────────────────────────────────────

@app.post("/api/login")
async def api_login(req: Request):
    body = await req.json()
    username = body.get("username", "").strip()
    password = body.get("password", "").strip()
    workspace_id = body.get("workspace_id", "").strip()
    
    if username == MAIN_ADMIN["username"] and hash_password(password) == MAIN_ADMIN["password_hash"]:
        token = await create_session()
        async with SESSIONS_LOCK:
            SESSIONS[token] = {"user_type": "main_admin", "workspace_id": None}
        resp = JSONResponse({"ok": True, "is_main_admin": True})
        resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL if body.get("remember") else None, httponly=True, samesite="lax", path="/")
        return resp
    
    if workspace_id and workspace_id in WORKSPACES:
        ws = WORKSPACES[workspace_id]
        if ws.get("admin_username") == username and hash_password(password) == ws.get("admin_password_hash"):
            token = await create_session()
            async with SESSIONS_LOCK:
                SESSIONS[token] = {"user_type": "workspace_admin", "workspace_id": workspace_id}
            resp = JSONResponse({"ok": True, "workspace_name": ws.get("name")})
            resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL if body.get("remember") else None, httponly=True, samesite="lax", path="/")
            resp.set_cookie("eagle_workspace", workspace_id, max_age=SESSION_TTL if body.get("remember") else None, httponly=True, samesite="lax", path="/")
            return resp
    
    raise HTTPException(401, "نام کاربری یا رمز عبور اشتباه است")

@app.post("/api/logout")
async def api_logout(req: Request):
    await destroy_session(req.cookies.get(SESSION_COOKIE))
    resp = JSONResponse({"ok": True})
    resp.delete_cookie(SESSION_COOKIE, path="/")
    resp.delete_cookie("eagle_workspace", path="/")
    return resp

@app.get("/api/me")
async def api_me(req: Request):
    token = req.cookies.get(SESSION_COOKIE)
    is_auth = await is_valid_session(token)
    session_data = SESSIONS.get(token, {}) if token else {}
    return {
        "authenticated": is_auth,
        "user_type": session_data.get("user_type"),
        "workspace_id": session_data.get("workspace_id"),
        "is_main_admin": session_data.get("user_type") == "main_admin",
    }

# ─── ===== API: Workspace Management (ادمین اصلی) ===== ────────────────────

@app.get("/api/admin/workspaces")
async def admin_list_workspaces(_=Depends(require_main_admin)):
    result = []
    for wid, ws in WORKSPACES.items():
        limit = ws.get("quota_limit_bytes", 0)
        used = ws.get("quota_used_bytes", 0)
        result.append({
            "id": wid,
            "name": ws.get("name"),
            "admin_username": ws.get("admin_username"),
            "created_at": ws.get("created_at"),
            "links_count": len(ws.get("links", {})),
            "quota_limit_gb": round(limit / (1024**3), 2) if limit > 0 else 0,
            "quota_used_gb": round(used / (1024**3), 2),
            "quota_percent": round((used / limit) * 100, 1) if limit > 0 else 0,
            "is_quota_exceeded": ws.get("is_quota_exceeded", False),
        })
    return {"workspaces": result}

@app.post("/api/admin/workspaces")
async def admin_create_workspace(req: Request, _=Depends(require_main_admin)):
    body = await req.json()
    name = body.get("name", "").strip()
    admin_username = body.get("admin_username", "").strip()
    admin_password = body.get("admin_password", "").strip()
    quota_gb = float(body.get("quota_gb", 0))
    
    if not name or not admin_username or not admin_password:
        raise HTTPException(400, "نام، نام کاربری و رمز عبور الزامی است")
    if len(admin_password) < 4:
        raise HTTPException(400, "رمز عبور حداقل 4 کاراکتر")
    
    for wid, ws in WORKSPACES.items():
        if ws.get("admin_username") == admin_username:
            raise HTTPException(400, "این نام کاربری قبلاً استفاده شده است")
    
    workspace_id = f"ws_{secrets.token_hex(8)}"
    async with WORKSPACES_LOCK:
        WORKSPACES[workspace_id] = {
            "name": name,
            "admin_username": admin_username,
            "admin_password_hash": hash_password(admin_password),
            "created_at": datetime.now().isoformat(),
            "active": True,
            "quota_limit_bytes": int(quota_gb * 1024**3) if quota_gb > 0 else 0,
            "quota_used_bytes": 0,
            "is_quota_exceeded": False,
            "settings": DEFAULT_SETTINGS.copy(),
            "links": {},
            "daily_traffic": {},
            "activity_logs": [],
            "stats": {"total_bytes": 0, "total_requests": 0, "total_errors": 0},
        }
    
    await save_state()
    return {"ok": True, "workspace_id": workspace_id}

@app.delete("/api/admin/workspaces/{workspace_id}")
async def admin_delete_workspace(workspace_id: str, _=Depends(require_main_admin)):
    async with WORKSPACES_LOCK:
        if workspace_id not in WORKSPACES:
            raise HTTPException(404, "Workspace یافت نشد")
        del WORKSPACES[workspace_id]
    await save_state()
    return {"ok": True}

@app.post("/api/admin/workspaces/{workspace_id}/quota")
async def admin_set_quota(workspace_id: str, req: Request, _=Depends(require_main_admin)):
    body = await req.json()
    quota_gb = float(body.get("quota_gb", 0))
    async with WORKSPACES_LOCK:
        if workspace_id not in WORKSPACES:
            raise HTTPException(404, "Workspace یافت نشد")
        WORKSPACES[workspace_id]["quota_limit_bytes"] = int(quota_gb * 1024**3) if quota_gb > 0 else 0
        WORKSPACES[workspace_id]["is_quota_exceeded"] = False
    await save_state()
    return {"ok": True}

@app.post("/api/admin/workspaces/{workspace_id}/quota/reset")
async def admin_reset_quota(workspace_id: str, _=Depends(require_main_admin)):
    async with WORKSPACES_LOCK:
        if workspace_id not in WORKSPACES:
            raise HTTPException(404, "Workspace یافت نشد")
        ws = WORKSPACES[workspace_id]
        ws["quota_used_bytes"] = 0
        ws["is_quota_exceeded"] = False
        for link in ws.get("links", {}).values():
            link["used_bytes"] = 0
    await save_state()
    return {"ok": True}

# ─── ===== API: Workspace (برای ادمین) ===== ─────────────────────────────────

@app.get("/api/workspace/info")
async def workspace_get_info(workspace_id=Depends(require_workspace_admin)):
    ws = WORKSPACES.get(workspace_id, {})
    limit = ws.get("quota_limit_bytes", 0)
    used = ws.get("quota_used_bytes", 0)
    return {
        "id": workspace_id,
        "name": ws.get("name"),
        "links_count": len(ws.get("links", {})),
        "quota": {
            "limit_gb": round(limit / (1024**3), 2) if limit > 0 else 0,
            "used_gb": round(used / (1024**3), 2),
            "percent": round((used / limit) * 100, 1) if limit > 0 else 0,
            "is_exceeded": ws.get("is_quota_exceeded", False),
        },
        "admin_username": ws.get("admin_username"),
    }

@app.post("/api/workspace/change-password")
async def workspace_change_password(req: Request, workspace_id=Depends(require_workspace_admin)):
    body = await req.json()
    old = body.get("old_password", "").strip()
    new = body.get("new_password", "").strip()
    if not old or not new or len(new) < 4:
        raise HTTPException(400, "رمز جدید حداقل 4 کاراکتر")
    async with WORKSPACES_LOCK:
        ws = WORKSPACES.get(workspace_id)
        if not ws:
            raise HTTPException(404, "Workspace یافت نشد")
        if hash_password(old) != ws.get("admin_password_hash"):
            raise HTTPException(403, "رمز فعلی اشتباه است")
        ws["admin_password_hash"] = hash_password(new)
    await save_state()
    return {"ok": True, "message": "رمز عبور تغییر کرد"}

@app.post("/api/workspace/change-username")
async def workspace_change_username(req: Request, workspace_id=Depends(require_workspace_admin)):
    body = await req.json()
    new_username = body.get("new_username", "").strip()
    if not new_username or len(new_username) < 3:
        raise HTTPException(400, "نام کاربری جدید حداقل 3 کاراکتر باشد")
    async with WORKSPACES_LOCK:
        ws = WORKSPACES.get(workspace_id)
        if not ws:
            raise HTTPException(404, "Workspace یافت نشد")
        ws["admin_username"] = new_username
    await save_state()
    return {"ok": True, "message": "نام کاربری تغییر کرد"}

# ─── ===== API: Workspace Links ===== ────────────────────────────────────────

@app.get("/api/workspace/links")
async def workspace_list_links(req: Request, workspace_id=Depends(require_workspace_admin)):
    ws = WORKSPACES.get(workspace_id, {})
    links = ws.get("links", {})
    host = get_host()
    result = []
    for uid, d in links.items():
        ports = d.get("ports", [443])
        first_port = ports[0] if ports else 443
        label = d.get("label", "کاربر")
        clean_ip = d.get("clean_ip")
        result.append({
            "uuid": uid,
            **d,
            "ports": ports,
            "expired": is_link_expired(d),
            "has_password": d.get("password_hash") is not None,
            "vless_link": generate_vless_link(uid, host, remark=f"عقاب-{label}",
                fingerprint=d.get("fingerprint", "chrome"), port=first_port),
            "sub_url": f"https://{host}/sub/{uid}"
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result}

@app.post("/api/workspace/links")
async def workspace_create_link(req: Request, workspace_id=Depends(require_workspace_admin)):
    body = await req.json()
    label = (body.get("label") or "کاربر").strip()[:60]
    quota = float(body.get("limit_value") or 0)
    limit_bytes = 0 if quota <= 0 else parse_size_to_bytes(quota, "GB")
    exp_days = int(body.get("expires_days") or 30)
    expires_at = (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    max_devices = int(body.get("max_devices", 0))
    fingerprint = body.get("fingerprint", "chrome")
    if fingerprint not in FINGERPRINTS:
        fingerprint = "chrome"
    password_hash = hash_password(body.get("password", "").strip()) if body.get("password") else None
    clean_ip = body.get("clean_ip") or None
    ports = body.get("ports", [443])
    if not isinstance(ports, list) or not ports:
        ports = [443]
    ports = [p for p in ports if isinstance(p, int) and 1 <= p <= 65535] or [443]

    uid = generate_uuid()
    async with WORKSPACES_LOCK:
        if workspace_id not in WORKSPACES:
            raise HTTPException(404, "Workspace یافت نشد")
        WORKSPACES[workspace_id]["links"][uid] = {
            "label": label, "limit_bytes": limit_bytes, "used_bytes": 0,
            "created_at": datetime.now().isoformat(), "active": True,
            "expires_at": expires_at, "protocol": "vless-ws",
            "max_devices": max_devices, "fingerprint": fingerprint,
            "password_hash": password_hash, "ports": ports, "clean_ip": clean_ip,
        }
    
    await save_state()
    host = get_host()
    main_link = generate_vless_link(uid, host, remark=f"عقاب-{label}",
                                    fingerprint=fingerprint, port=ports[0])
    return {"uuid": uid, **WORKSPACES[workspace_id]["links"][uid], "has_password": password_hash is not None,
            "vless_link": main_link, "sub_url": f"https://{host}/sub/{uid}"}

@app.patch("/api/workspace/links/{uid}")
async def workspace_update_link(uid: str, req: Request, workspace_id=Depends(require_workspace_admin)):
    body = await req.json()
    async with WORKSPACES_LOCK:
        if workspace_id not in WORKSPACES:
            raise HTTPException(404, "Workspace یافت نشد")
        ws = WORKSPACES[workspace_id]
        if uid not in ws.get("links", {}):
            raise HTTPException(404, "کاربر یافت نشد")
        link = ws["links"][uid]
        
        if link.get("password_hash"):
            pw = body.get("password", "").strip()
            if not pw or hash_password(pw) != link["password_hash"]:
                raise HTTPException(403, "رمز کانفیگ اشتباه است")
        if "label" in body:
            link["label"] = str(body["label"])[:60]
        if "limit_value" in body:
            lv = float(body["limit_value"] or 0)
            link["limit_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, "GB")
        if "expires_days" in body:
            ed = int(body["expires_days"] or 0)
            link["expires_at"] = (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
        if "max_devices" in body:
            link["max_devices"] = int(body["max_devices"])
        if "fingerprint" in body and body["fingerprint"] in FINGERPRINTS:
            link["fingerprint"] = body["fingerprint"]
        if "clean_ip" in body:
            link["clean_ip"] = body["clean_ip"] or None
        if "active" in body:
            link["active"] = bool(body["active"])
        if "reset_usage" in body and body["reset_usage"]:
            link["used_bytes"] = 0
        if "ports" in body and isinstance(body["ports"], list):
            ports = [p for p in body["ports"] if isinstance(p, int) and 1 <= p <= 65535]
            if ports:
                link["ports"] = ports
    
    await save_state()
    return {"ok": True}

@app.delete("/api/workspace/links/{uid}")
async def workspace_delete_link(uid: str, req: Request, workspace_id=Depends(require_workspace_admin)):
    body = await req.json()
    async with WORKSPACES_LOCK:
        if workspace_id not in WORKSPACES:
            raise HTTPException(404, "Workspace یافت نشد")
        ws = WORKSPACES[workspace_id]
        if uid not in ws.get("links", {}):
            raise HTTPException(404, "کاربر یافت نشد")
        link = ws["links"][uid]
        if link.get("password_hash"):
            pw = body.get("password", "").strip()
            if not pw or hash_password(pw) != link["password_hash"]:
                raise HTTPException(403, "رمز کانفیگ اشتباه است")
        del ws["links"][uid]
    
    await save_state()
    return {"ok": True}

# ─── ===== API: Workspace Settings ===== ──────────────────────────────────────

@app.get("/api/workspace/settings")
async def workspace_get_settings(workspace_id=Depends(require_workspace_admin)):
    ws = WORKSPACES.get(workspace_id, {})
    return ws.get("settings", DEFAULT_SETTINGS.copy())

@app.post("/api/workspace/settings")
async def workspace_update_settings(req: Request, workspace_id=Depends(require_workspace_admin)):
    body = await req.json()
    async with WORKSPACES_LOCK:
        if workspace_id not in WORKSPACES:
            raise HTTPException(404, "Workspace یافت نشد")
        for key, value in body.items():
            if key in DEFAULT_SETTINGS:
                WORKSPACES[workspace_id]["settings"][key] = value
    await save_state()
    return {"ok": True}

@app.get("/api/workspace/clean-ips")
async def workspace_get_clean_ips(workspace_id=Depends(require_workspace_admin)):
    ws = WORKSPACES.get(workspace_id, {})
    return {"clean_ips": ws.get("settings", {}).get("clean_ips", [])}

@app.post("/api/workspace/clean-ips")
async def workspace_add_clean_ip(req: Request, workspace_id=Depends(require_workspace_admin)):
    body = await req.json()
    ip = body.get("ip", "").strip()
    provider = body.get("provider", "Unknown")
    if not ip:
        raise HTTPException(400, "IP نمی‌تواند خالی باشد")
    async with WORKSPACES_LOCK:
        clean_ips = WORKSPACES[workspace_id]["settings"].get("clean_ips", [])
        for item in clean_ips:
            if item.get("ip") == ip:
                raise HTTPException(400, "این IP قبلاً اضافه شده است")
        clean_ips.append({"ip": ip, "provider": provider, "active": True})
        WORKSPACES[workspace_id]["settings"]["clean_ips"] = clean_ips
    await save_state()
    return {"ok": True}

@app.delete("/api/workspace/clean-ips/{ip}")
async def workspace_delete_clean_ip(ip: str, workspace_id=Depends(require_workspace_admin)):
    async with WORKSPACES_LOCK:
        clean_ips = WORKSPACES[workspace_id]["settings"].get("clean_ips", [])
        WORKSPACES[workspace_id]["settings"]["clean_ips"] = [item for item in clean_ips if item.get("ip") != ip]
    await save_state()
    return {"ok": True}

@app.get("/api/workspace/routes")
async def workspace_get_routes(workspace_id=Depends(require_workspace_admin)):
    ws = WORKSPACES.get(workspace_id, {})
    return {"routes": ws.get("settings", {}).get("routes", [])}

@app.post("/api/workspace/routes")
async def workspace_add_route(req: Request, workspace_id=Depends(require_workspace_admin)):
    body = await req.json()
    domain = body.get("domain", "").strip()
    route_type = body.get("type", "direct")
    if not domain:
        raise HTTPException(400, "دامنه نمی‌تواند خالی باشد")
    async with WORKSPACES_LOCK:
        routes = WORKSPACES[workspace_id]["settings"].get("routes", [])
        routes.append({"domain": domain, "type": route_type, "active": True})
        WORKSPACES[workspace_id]["settings"]["routes"] = routes
    await save_state()
    return {"ok": True}

@app.delete("/api/workspace/routes/{domain}")
async def workspace_delete_route(domain: str, workspace_id=Depends(require_workspace_admin)):
    async with WORKSPACES_LOCK:
        routes = WORKSPACES[workspace_id]["settings"].get("routes", [])
        WORKSPACES[workspace_id]["settings"]["routes"] = [r for r in routes if r.get("domain") != domain]
    await save_state()
    return {"ok": True}

@app.get("/api/workspace/filters")
async def workspace_get_filters(workspace_id=Depends(require_workspace_admin)):
    ws = WORKSPACES.get(workspace_id, {})
    settings = ws.get("settings", {})
    return {
        "ad_filter_enabled": settings.get("ad_filter_enabled", True),
        "porn_filter_enabled": settings.get("porn_filter_enabled", True),
        "malware_filter_enabled": settings.get("malware_filter_enabled", True),
    }

@app.post("/api/workspace/filters")
async def workspace_update_filters(req: Request, workspace_id=Depends(require_workspace_admin)):
    body = await req.json()
    async with WORKSPACES_LOCK:
        settings = WORKSPACES[workspace_id]["settings"]
        if "ad_filter_enabled" in body:
            settings["ad_filter_enabled"] = bool(body["ad_filter_enabled"])
        if "porn_filter_enabled" in body:
            settings["porn_filter_enabled"] = bool(body["porn_filter_enabled"])
        if "malware_filter_enabled" in body:
            settings["malware_filter_enabled"] = bool(body["malware_filter_enabled"])
    await save_state()
    return {"ok": True}

@app.get("/api/workspace/stats")
async def workspace_stats(workspace_id=Depends(require_workspace_admin)):
    ws = WORKSPACES.get(workspace_id, {})
    links = ws.get("links", {})
    return {
        "links_count": len(links),
        "active_links": sum(1 for l in links.values() if l.get("active", True) and not is_link_expired(l)),
        "total_used": sum(l.get("used_bytes", 0) for l in links.values()),
        "total_used_fmt": fmt_bytes(sum(l.get("used_bytes", 0) for l in links.values())),
        "connections": len(connections),
    }

@app.get("/api/workspace/logs")
async def workspace_get_logs(req: Request, workspace_id=Depends(require_workspace_admin)):
    ws = WORKSPACES.get(workspace_id, {})
    logs = ws.get("activity_logs", [])
    return {"logs": list(logs)[-50:]}

# ─── ===== API: Dashboard ===== ─────────────────────────────────────────────

@app.get("/api/dashboard/stats")
async def dashboard_stats(req: Request):
    disk = psutil.disk_usage('/')
    return {
        "traffic": {"total": stats["total_bytes"], "total_fmt": fmt_bytes(stats["total_bytes"])},
        "requests": stats["total_requests"],
        "uptime": uptime(),
        "disk": {"total_fmt": fmt_bytes(disk.total), "used_fmt": fmt_bytes(disk.used), "free_fmt": fmt_bytes(disk.free)},
        "connections": len(connections),
        "speed": {"download_fmt": "0 B/s"},
        "links_count": 0,
        "active_links": 0,
    }

@app.get("/api/connections")
async def get_connections():
    result = []
    for c in connections.values():
        result.append({
            "ip": c.get("ip", "نامشخص"),
            "bytes": c.get("bytes", 0),
            "bytes_fmt": fmt_bytes(c.get("bytes", 0)),
            "connected_at": c.get("connected_at"),
        })
    return {"connections": result, "count": len(result)}

# ─── ===== WebSocket Tunnel ===== ─────────────────────────────────────────────

RELAY_BUF = 512 * 1024

def _ws_ip(ws):
    fwd = ws.headers.get("x-forwarded-for")
    return fwd.split(",")[0].strip() if fwd else ws.client.host if ws.client else "نامشخص"

async def parse_vless_header(chunk: bytes):
    if len(chunk) < 24:
        raise ValueError("chunk too small")
    pos = 1 + 16
    addon_len = chunk[pos]
    pos += 1 + addon_len
    command = chunk[pos]
    pos += 1
    port = int.from_bytes(chunk[pos:pos+2], "big")
    pos += 2
    addr_type = chunk[pos]
    pos += 1
    if addr_type == 1:
        address = ".".join(str(b) for b in chunk[pos:pos+4])
        pos += 4
    elif addr_type == 2:
        dlen = chunk[pos]
        pos += 1
        address = chunk[pos:pos+dlen].decode("utf-8", errors="ignore")
        pos += dlen
    elif addr_type == 3:
        ab = chunk[pos:pos+16]
        pos += 16
        address = ":".join(f"{ab[i]:02x}{ab[i+1]:02x}" for i in range(0, 16, 2))
    else:
        raise ValueError(f"unknown addr type: {addr_type}")
    return command, address, port, chunk[pos:]

async def check_and_use(uid: str, n: int, workspace_id: str) -> bool:
    ws = WORKSPACES.get(workspace_id, {})
    links = ws.get("links", {})
    link = links.get(uid)
    if not link or not is_link_allowed(link):
        return False
    link["used_bytes"] = link.get("used_bytes", 0) + n
    ws["quota_used_bytes"] = ws.get("quota_used_bytes", 0) + n
    return True

async def relay_ws_to_tcp(ws, writer, conn_id, uid, workspace_id):
    try:
        while True:
            msg = await ws.receive()
            if msg["type"] == "websocket.disconnect":
                break
            data = msg.get("bytes") or (msg.get("text") or "").encode()
            if not data:
                continue
            if not await check_and_use(uid, len(data), workspace_id):
                await ws.close(code=1008, reason="quota/disabled")
                break
            if conn_id in connections:
                connections[conn_id]["bytes"] = connections[conn_id].get("bytes", 0) + len(data)
            writer.write(data)
            if writer.transport.get_write_buffer_size() > RELAY_BUF:
                await writer.drain()
    except:
        pass
    finally:
        try:
            writer.write_eof()
        except:
            pass

async def relay_tcp_to_ws(ws, reader, conn_id, uid, workspace_id):
    first = True
    try:
        while True:
            data = await reader.read(RELAY_BUF)
            if not data:
                break
            if not await check_and_use(uid, len(data), workspace_id):
                await ws.close(code=1008, reason="quota/disabled")
                break
            if conn_id in connections:
                connections[conn_id]["bytes"] = connections[conn_id].get("bytes", 0) + len(data)
            payload = (b"\x00\x00" + data) if first else data
            first = False
            await ws.send_bytes(payload)
    except:
        pass

@app.websocket("/ws/{uuid}")
async def websocket_tunnel(ws: WebSocket, uuid: str):
    await ws.accept()
    workspace_id = ws.headers.get("X-Workspace-ID")
    if not workspace_id:
        cookie_header = ws.headers.get("cookie", "")
        for cookie in cookie_header.split(";"):
            if "eagle_workspace=" in cookie:
                workspace_id = cookie.split("eagle_workspace=")[1].strip()
                break
    
    if not workspace_id or workspace_id not in WORKSPACES:
        await ws.close(code=1008, reason="workspace not found")
        return
    
    client_ip = _ws_ip(ws)
    ws_data = WORKSPACES.get(workspace_id, {})
    links = ws_data.get("links", {})
    link = links.get(uuid)
    if not link:
        await ws.close(code=1008, reason="user not found")
        return
    if not is_link_allowed(link):
        await ws.close(code=1008, reason="not authorized")
        return

    conn_id = secrets.token_urlsafe(6)
    connections[conn_id] = {"uuid": uuid, "ip": client_ip, "transport": "vless-ws",
                            "connected_at": datetime.now().isoformat(), "bytes": 0}
    writer = None

    try:
        first_msg = await asyncio.wait_for(ws.receive(), timeout=15.0)
        if first_msg["type"] == "websocket.disconnect":
            return
        first_chunk = first_msg.get("bytes") or (first_msg.get("text") or "").encode()
        if not first_chunk:
            return
        command, address, port, payload = await parse_vless_header(first_chunk)
        if not await check_and_use(uuid, len(first_chunk), workspace_id):
            await ws.close(code=1008, reason="quota/disabled")
            return
        
        if conn_id in connections:
            connections[conn_id]["bytes"] = connections[conn_id].get("bytes", 0) + len(first_chunk)

        reader, writer = await asyncio.wait_for(asyncio.open_connection(address, port), timeout=10.0)
        if writer:
            sock = writer.transport.get_extra_info('socket')
            if sock:
                sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        if payload:
            writer.write(payload)
            await writer.drain()

        done, pending = await asyncio.wait(
            {asyncio.create_task(relay_ws_to_tcp(ws, writer, conn_id, uuid, workspace_id)),
             asyncio.create_task(relay_tcp_to_ws(ws, reader, conn_id, uuid, workspace_id))},
            return_when=asyncio.FIRST_COMPLETED
        )
        for t in pending:
            t.cancel()
            try:
                await t
            except:
                pass
        await save_state()
    except:
        pass
    finally:
        if writer:
            try:
                writer.close()
                await writer.wait_closed()
            except:
                pass
        connections.pop(conn_id, None)

# ─── ===== Subscriptions ===== ────────────────────────────────────────────────

@app.get("/sub/{uuid}")
async def subscription_single(req: Request, uuid: str):
    import base64
    workspace_id = req.headers.get("X-Workspace-ID")
    if not workspace_id:
        cookie_header = req.headers.get("cookie", "")
        for cookie in cookie_header.split(";"):
            if "eagle_workspace=" in cookie:
                workspace_id = cookie.split("eagle_workspace=")[1].strip()
                break
    
    if not workspace_id or workspace_id not in WORKSPACES:
        return HTMLResponse("""<html><body><h1>Workspace یافت نشد</h1></body></html>""", status_code=404)
    
    ua = req.headers.get("user-agent", "").lower()
    is_browser = any(b in ua for b in ["chrome", "firefox", "safari", "edge", "opera", "brave", "msie", "trident"])
    
    ws = WORKSPACES.get(workspace_id, {})
    links = ws.get("links", {})
    link = links.get(uuid)
    
    if not link:
        if is_browser:
            return HTMLResponse("""<html><body><h1>کاربر یافت نشد</h1></body></html>""", status_code=404)
        raise HTTPException(404, "user not found")
    if not is_link_allowed(link):
        if is_browser:
            return HTMLResponse("""<html><body><h1>کاربر غیرفعال</h1></body></html>""", status_code=403)
        raise HTTPException(403, "user disabled or expired")
    
    host = get_host()
    ports = link.get("ports", [443])
    vless_links = []
    for port in ports:
        vless_links.append(generate_vless_link(uuid, host, remark=link.get("label", "کاربر"),
                                               fingerprint=link.get("fingerprint", "chrome"), port=port))
    
    if not is_browser:
        userinfo = f"upload=0&download={link.get('used_bytes',0)}&total={link.get('limit_bytes',0)}"
        content = base64.b64encode("\n".join(vless_links).encode()).decode()
        return Response(content=content, media_type="text/plain",
                        headers={"Subscription-Userinfo": userinfo,
                                 "profile-title": quote(link.get("label", "کاربر"))})
    
    from pages import get_sub_page_html
    active_conns = [c for c in connections.values() if c.get("uuid") == uuid]
    link_data = {**link, "expired": is_link_expired(link), "active_connections": len(active_conns),
                 "active_connections_list": active_conns, "vless_links": vless_links,
                 "vless_link": vless_links[0] if vless_links else "", "sub_url": f"https://{host}/sub/{uuid}"}
    return HTMLResponse(content=get_sub_page_html(uuid, link_data))

# ─── ===== HTML Pages ===== ──────────────────────────────────────────────────

from pages import LOGIN_HTML, DASHBOARD_HTML

@app.get("/login")
async def login_page(req: Request):
    if await is_valid_session(req.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/dashboard")
    return HTMLResponse(content=LOGIN_HTML)

@app.get("/dashboard")
async def dashboard(req: Request):
    token = req.cookies.get(SESSION_COOKIE)
    if not await is_valid_session(token):
        return RedirectResponse(url="/login")
    return HTMLResponse(content=DASHBOARD_HTML)

@app.get("/")
async def root():
    return HTMLResponse("""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>🪐 Eagle Gateway</title>
    <style>body{font-family:sans-serif;background:#0a0a0f;color:#fff;display:flex;align-items:center;justify-content:center;height:100vh;margin:0}
    .card{text-align:center;padding:40px;background:rgba(20,20,40,0.7);border-radius:20px;border:1px solid rgba(100,80,255,0.2)}
    h1{font-size:48px;margin:0}.sub{color:#888}a{color:#7C6BFF;text-decoration:none}</style></head>
    <body><div class="card"><h1>🪐</h1><h2>Eagle Gateway v10 Pro</h2><p class="sub">پنل مدیریت فیلترشکن</p><a href="/login">ورود →</a></div></body></html>""")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=CONFIG["port"], log_level="info", workers=1)
