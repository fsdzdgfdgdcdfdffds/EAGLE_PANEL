# pages.py - تخت جمشید 🏛️ نسخه کامل نهایی

import json

# ==== لاگین ====
LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🏛️ ورود · تخت جمشید</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#f5f0e8;--card:rgba(255,252,245,0.85);--card-b:rgba(184,150,100,0.2);--accent:#C9A84C;--accent2:#D4AF37;--accent3:#B8963C;--t1:#2C1810;--t2:#8B7355;--t3:#A89070;--border:rgba(184,150,100,0.15);--glow:0 0 80px rgba(212,175,55,0.05)}
body{font-family:'Vazirmatn',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#f5f0e8,#e8ddcc,#f5f0e8);padding:20px;color:var(--t1);position:relative;overflow:hidden}
.stars{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.star{position:absolute;border-radius:50%;background:#C9A84C;animation:twinkle 3s ease-in-out infinite;opacity:0.15}
@keyframes twinkle{0%,100%{opacity:0.1}50%{opacity:0.3}}
.glow-orb{position:fixed;border-radius:50%;filter:blur(150px);z-index:0;animation:orbFloat 6s ease-in-out infinite;pointer-events:none}
.orb1{width:500px;height:500px;background:rgba(212,175,55,0.04);top:-200px;right:-100px}
.orb2{width:400px;height:400px;background:rgba(184,150,100,0.03);bottom:-100px;left:-80px;animation-delay:2s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(30px,-30px) scale(1.1)}}
.container{position:relative;z-index:10;display:grid;grid-template-columns:1fr 1fr;max-width:1100px;width:100%;background:var(--card);backdrop-filter:blur(30px);border-radius:24px;border:1px solid var(--border);overflow:hidden;box-shadow:var(--glow),0 25px 80px rgba(0,0,0,0.06)}
.login-section{padding:48px 40px}
.brand{display:flex;align-items:center;gap:12px;margin-bottom:32px}
.brand-icon{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,#C9A84C,#D4AF37,#B8963C);display:flex;align-items:center;justify-content:center;font-size:22px;box-shadow:0 0 40px rgba(212,175,55,0.15)}
.brand-text{font-size:16px;font-weight:800;background:linear-gradient(135deg,#D4AF37,#C9A84C);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.brand-sub{font-size:9px;color:var(--t3);-webkit-text-fill-color:var(--t3)}
.welcome{font-size:22px;font-weight:800;color:var(--t1);margin-bottom:4px}
.sub-text{font-size:13px;color:var(--t3);margin-bottom:28px}
.field{margin-bottom:18px}
.field label{display:block;font-size:10px;font-weight:600;color:var(--t2);margin-bottom:4px}
.field input{width:100%;padding:12px 14px;border-radius:10px;border:1px solid var(--border);background:rgba(255,252,245,0.5);color:var(--t1);font-family:inherit;font-size:14px;outline:none;transition:.3s}
.field input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(212,175,55,.08)}
.field input::placeholder{color:var(--t3)}
.options{display:flex;justify-content:space-between;align-items:center;margin:14px 0 20px;font-size:12px}
.options label{display:flex;align-items:center;gap:6px;color:var(--t2);cursor:pointer}
.options label input[type="checkbox"]{accent-color:var(--accent);width:16px;height:16px;cursor:pointer}
.btn-login{width:100%;padding:12px;border-radius:10px;border:none;cursor:pointer;background:linear-gradient(135deg,#C9A84C,#D4AF37,#B8963C);background-size:200% 200%;animation:gradientMove 4s ease infinite;color:#fff;font-family:inherit;font-size:15px;font-weight:700;transition:all .3s;box-shadow:0 4px 30px rgba(212,175,55,.2)}
@keyframes gradientMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-login:hover{transform:translateY(-2px);box-shadow:0 8px 40px rgba(212,175,55,.3)}
.btn-login:disabled{opacity:.5;cursor:not-allowed;transform:none}
.or-divider{display:flex;align-items:center;gap:14px;margin:20px 0;color:var(--t3);font-size:11px}
.or-divider::before,.or-divider::after{content:'';flex:1;height:1px;background:var(--border)}
.connect-btn{width:100%;padding:12px;border-radius:10px;border:1px solid var(--border);background:rgba(212,175,55,0.02);color:var(--t1);font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;transition:.3s;display:flex;align-items:center;justify-content:center;gap:8px}
.connect-btn:hover{background:rgba(212,175,55,0.04);border-color:rgba(212,175,55,0.2)}
.signup-text{text-align:center;margin-top:18px;font-size:12px;color:var(--t3)}
.signup-text a{color:var(--accent);text-decoration:none;font-weight:600}
.signup-text a:hover{text-decoration:underline}
.error-box{display:none;background:rgba(184,150,100,.08);border:1px solid rgba(184,150,100,.15);border-radius:8px;padding:10px 12px;margin-bottom:14px;font-size:12px;color:#8B7355;align-items:center;gap:8px}
.error-box.show{display:flex}
.info-section{background:linear-gradient(135deg,#f5f0e8,#e8ddcc);padding:48px 36px;display:flex;flex-direction:column;justify-content:center;border-right:1px solid var(--border)}
.info-title{font-size:22px;font-weight:800;color:var(--t1);margin-bottom:6px}
.info-sub{font-size:13px;color:var(--t3);margin-bottom:24px}
.features{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.feature{background:rgba(212,175,55,0.02);border-radius:12px;padding:14px 12px;text-align:center;border:1px solid rgba(212,175,55,0.04)}
.feature .icon{font-size:28px;display:block;margin-bottom:4px}
.feature .name{font-size:11px;font-weight:600;color:var(--t1)}
.feature .desc{font-size:8px;color:var(--t3);margin-top:2px}
.lang-toggle{position:fixed;top:20px;left:20px;z-index:50;display:flex;gap:6px;background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--border);border-radius:10px;padding:4px}
.lang-toggle button{background:none;border:none;color:var(--t3);font-family:inherit;font-size:11px;font-weight:600;padding:4px 10px;border-radius:6px;cursor:pointer;transition:.3s}
.lang-toggle button.active{background:linear-gradient(135deg,#C9A84C,#D4AF37);color:#fff}
.lang-toggle button:hover:not(.active){color:var(--t1)}
@media(max-width:900px){.container{grid-template-columns:1fr}.info-section{display:none}.login-section{padding:32px 24px}}
@media(max-width:480px){.login-section{padding:24px 16px}.welcome{font-size:19px}}
</style>
</head>
<body>
<div class="stars">
    <div class="star" style="width:2px;height:2px;top:10%;left:5%;animation-delay:0s"></div>
    <div class="star" style="width:3px;height:3px;top:20%;left:15%;animation-delay:1s"></div>
    <div class="star" style="width:1px;height:1px;top:30%;left:25%;animation-delay:2s"></div>
    <div class="star" style="width:2px;height:2px;top:15%;left:35%;animation-delay:0.5s"></div>
    <div class="star" style="width:3px;height:3px;top:40%;left:45%;animation-delay:1.5s"></div>
    <div class="star" style="width:1px;height:1px;top:25%;left:55%;animation-delay:2.5s"></div>
    <div class="star" style="width:2px;height:2px;top:50%;left:65%;animation-delay:0.7s"></div>
    <div class="star" style="width:3px;height:3px;top:60%;left:75%;animation-delay:1.8s"></div>
    <div class="star" style="width:1px;height:1px;top:70%;left:85%;animation-delay:2.2s"></div>
    <div class="star" style="width:2px;height:2px;top:80%;left:95%;animation-delay:1.2s"></div>
</div>
<div class="glow-orb orb1"></div><div class="glow-orb orb2"></div>
<div class="lang-toggle">
    <button class="active" onclick="setLang('fa')">🇮🇷 فارسی</button>
    <button onclick="setLang('en')">🇬🇧 English</button>
</div>
<div class="container">
    <div class="login-section">
        <div class="brand"><div class="brand-icon">🏛️</div><div><div class="brand-text">تخت جمشید</div><div class="brand-sub">مدیریت کاربران</div></div></div>
        <div class="welcome" id="welcome-text">خوش آمدید</div>
        <div class="sub-text" id="sub-text">وارد حساب کاربری خود شوید</div>
        <div class="error-box" id="error-box"><i class="ti ti-alert-circle"></i><span id="error-text"></span></div>
        <form id="login-form" onsubmit="handleLogin(event)">
            <div class="field"><label id="label-username">نام کاربری یا ایمیل</label><input type="text" id="username" placeholder="نام کاربری" value="admin" dir="ltr"></div>
            <div class="field"><label id="label-password">رمز عبور</label><input type="password" id="password" placeholder="رمز عبور را وارد کنید" dir="ltr"></div>
            <div class="options"><label><input type="checkbox" id="remember"> <span id="remember-text">مرا به خاطر بسپار</span></label></div>
            <button class="btn-login" type="submit" id="login-btn"><i class="ti ti-login-2"></i> <span id="login-text">ورود</span></button>
        </form>
        <div class="or-divider"><span id="or-text">یا</span></div>
        <button class="connect-btn" onclick="quickConnect()"><i class="ti ti-plug"></i> <span id="connect-text">اتصال با یک کلیک</span></button>
        <div class="signup-text" id="signup-text">حساب کاربری ندارید؟ <a href="/dashboard">ثبت نام</a></div>
    </div>
    <div class="info-section">
        <div class="info-title" id="info-title">🏛️ تخت جمشید</div>
        <div class="info-sub" id="info-sub">سریع‌ترین و امن‌ترین اتصال</div>
        <div class="features">
            <div class="feature"><span class="icon">🔒</span><div class="name" id="f-secure">امن</div><div class="desc" id="f-secure-d">حریم خصوصی شما</div></div>
            <div class="feature"><span class="icon">⚡</span><div class="name" id="f-fast">سریع</div><div class="desc" id="f-fast-d">سرعت برق آسا</div></div>
            <div class="feature"><span class="icon">🌍</span><div class="name" id="f-global">جهانی</div><div class="desc" id="f-global-d">سرورهای جهانی</div></div>
            <div class="feature"><span class="icon">🕵️</span><div class="name" id="f-anon">ناشناس</div><div class="desc" id="f-anon-d">خصوصی بمانید</div></div>
        </div>
    </div>
</div>
<script>
const translations={fa:{welcome:"خوش آمدید",sub:"وارد حساب کاربری خود شوید",username:"نام کاربری یا ایمیل",password:"رمز عبور",remember:"مرا به خاطر بسپار",login:"ورود",or:"یا",connect:"اتصال با یک کلیک",signup:"حساب کاربری ندارید؟",signup_link:"ثبت نام",secure:"امن",secure_d:"حریم خصوصی شما",fast:"سریع",fast_d:"سرعت برق آسا",global:"جهانی",global_d:"سرورهای جهانی",anon:"ناشناس",anon_d:"خصوصی بمانید",info_title:"🏛️ تخت جمشید",info_sub:"سریع‌ترین و امن‌ترین اتصال"},en:{welcome:"Welcome Back",sub:"Login to your VPN account",username:"Username or Email",password:"Password",remember:"Remember me",login:"Login",or:"OR",connect:"Connect with One Click",signup:"Don't have an account?",signup_link:"Sign up",secure:"Secure",secure_d:"Your Privacy",fast:"Fast",fast_d:"Lightning Speed",global:"Global",global_d:"Worldwide Servers",anon:"Anonymous",anon_d:"Stay Private",info_title:"🏛️ Takht-e Jamshid",info_sub:"Fastest & Most Secure Connection"}};
let currentLang=localStorage.getItem('takht-lang')||'fa';
function setLang(lang){currentLang=lang;localStorage.setItem('takht-lang',lang);document.querySelectorAll('.lang-toggle button').forEach(b=>b.classList.toggle('active',b.textContent.includes(lang==='fa'?'فارسی':'English')));updateTexts()}
function updateTexts(){const t=translations[currentLang];document.getElementById('welcome-text').textContent=t.welcome;document.getElementById('sub-text').textContent=t.sub;document.getElementById('label-username').textContent=t.username;document.getElementById('label-password').textContent=t.password;document.getElementById('remember-text').textContent=t.remember;document.getElementById('login-text').textContent=t.login;document.getElementById('or-text').textContent=t.or;document.getElementById('connect-text').textContent=t.connect;document.getElementById('signup-text').innerHTML=t.signup+' <a href="/dashboard">'+t.signup_link+'</a>';document.getElementById('f-secure').textContent=t.secure;document.getElementById('f-secure-d').textContent=t.secure_d;document.getElementById('f-fast').textContent=t.fast;document.getElementById('f-fast-d').textContent=t.fast_d;document.getElementById('f-global').textContent=t.global;document.getElementById('f-global-d').textContent=t.global_d;document.getElementById('f-anon').textContent=t.anon;document.getElementById('f-anon-d').textContent=t.anon_d;document.getElementById('info-title').textContent=t.info_title;document.getElementById('info-sub').textContent=t.info_sub}
async function handleLogin(e){e.preventDefault();const btn=document.getElementById('login-btn');const err=document.getElementById('error-box');const errText=document.getElementById('error-text');err.classList.remove('show');btn.disabled=true;btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';try{const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('password').value,remember:document.getElementById('remember').checked})});if(!r.ok){const d=await r.json().catch(()=>({}));errText.textContent=d.detail||'رمز عبور اشتباه است';err.classList.add('show');btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> '+translations[currentLang].login;return}window.location.href='/dashboard'}catch(e){errText.textContent='خطا در ارتباط با سرور';err.classList.add('show');btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> '+translations[currentLang].login}}
function quickConnect(){document.getElementById('password').value='123456';document.getElementById('remember').checked=true;document.getElementById('login-form').dispatchEvent(new Event('submit'))}
document.getElementById('password').addEventListener('keydown',(e)=>{if(e.key==='Enter')document.getElementById('login-form').dispatchEvent(new Event('submit'))});
setLang(currentLang);
</script>
</body></html>"""

# ==== داشبورد (با ۱۰ تم) ====
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🏛️ تخت جمشید · خانه</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#f5f0e8;--bg2:#e8ddcc;--bg3:#ddd0c0;--card:rgba(255,252,245,0.85);--card-b:rgba(184,150,100,0.12);--card-bh:rgba(212,175,55,0.2);--accent:#C9A84C;--accent2:#D4AF37;--accent3:#B8963C;--green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#059669;--red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#DC2626;--amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#D97706;--t1:#2C1810;--t2:#8B7355;--t3:#A89070;--sidebar-w:180px;--radius:12px;--shadow:0 8px 32px rgba(0,0,0,0.06),0 0 60px rgba(212,175,55,0.02)}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:13px;position:relative;overflow-x:hidden;transition:background .4s,color .4s}
[data-theme="dark_fire"]{--bg:#0a0a1a;--bg2:#12122a;--bg3:#1a1a3a;--card:rgba(20,10,10,0.7);--card-b:rgba(255,100,50,0.12);--card-bh:rgba(255,100,50,0.28);--accent:#FF6B35;--accent2:#FF8C00;--accent-d:rgba(255,80,20,0.08);--green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#34D399;--red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#F87171;--amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#FCD34D;--t1:#F0EEFF;--t2:#A07050;--t3:#7A4A3A;--shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(255,80,20,0.03)}
[data-theme="gold"]{--bg:#1a1208;--bg2:#2a1f0d;--bg3:#3a2a12;--card:rgba(30,20,10,0.75);--card-b:rgba(212,175,55,0.2);--card-bh:rgba(212,175,55,0.4);--accent:#D4AF37;--accent2:#F5D060;--accent-d:rgba(212,175,55,0.1);--green:#B8860B;--green-bg:rgba(184,134,11,0.08);--green-t:#DAA520;--red:#CD5C5C;--red-bg:rgba(205,92,92,0.08);--red-t:#E89696;--amber:#D4AF37;--amber-bg:rgba(212,175,55,0.08);--amber-t:#F5D060;--t1:#F5ECD7;--t2:#C4A35A;--t3:#8A7A4A;--shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(212,175,55,0.05)}
[data-theme="ocean"]{--bg:#0a1a2a;--bg2:#0f2a3a;--bg3:#143a4a;--card:rgba(10,25,45,0.75);--card-b:rgba(0,153,204,0.2);--card-bh:rgba(0,153,204,0.4);--accent:#0099CC;--accent2:#33CCFF;--accent-d:rgba(0,153,204,0.1);--green:#00A86B;--green-bg:rgba(0,168,107,0.08);--green-t:#33CC99;--red:#CD5C5C;--red-bg:rgba(205,92,92,0.08);--red-t:#E89696;--amber:#0099CC;--amber-bg:rgba(0,153,204,0.08);--amber-t:#33CCFF;--t1:#D4EEFF;--t2:#5AA8C8;--t3:#3A7A9A;--shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(0,153,204,0.05)}
[data-theme="forest"]{--bg:#081a0a;--bg2:#0d2a10;--bg3:#123a16;--card:rgba(10,30,12,0.75);--card-b:rgba(46,139,87,0.2);--card-bh:rgba(46,139,87,0.4);--accent:#2E8B57;--accent2:#4CAF50;--accent-d:rgba(46,139,87,0.1);--green:#2E8B57;--green-bg:rgba(46,139,87,0.08);--green-t:#4CAF50;--red:#CD5C5C;--red-bg:rgba(205,92,92,0.08);--red-t:#E89696;--amber:#2E8B57;--amber-bg:rgba(46,139,87,0.08);--amber-t:#4CAF50;--t1:#D4F5D4;--t2:#5AA85A;--t3:#3A7A3A;--shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(46,139,87,0.05)}
[data-theme="ruby"]{--bg:#1a0a12;--bg2:#2a0f1a;--bg3:#3a1422;--card:rgba(30,10,20,0.75);--card-b:rgba(155,45,110,0.2);--card-bh:rgba(155,45,110,0.4);--accent:#9B2D6E;--accent2:#C44A8A;--accent-d:rgba(155,45,110,0.1);--green:#A86B8A;--green-bg:rgba(168,107,138,0.08);--green-t:#C48AAA;--red:#CD5C5C;--red-bg:rgba(205,92,92,0.08);--red-t:#E89696;--amber:#9B2D6E;--amber-bg:rgba(155,45,110,0.08);--amber-t:#C44A8A;--t1:#F5D4E8;--t2:#B05A8A;--t3:#8A4A6A;--shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(155,45,110,0.05)}
[data-theme="white_fire"]{--bg:#F5E6E0;--bg2:#E8D5CC;--bg3:#F0D5C8;--card:rgba(255,245,240,0.7);--card-b:rgba(200,80,40,0.14);--card-bh:rgba(200,80,40,0.3);--accent:#E05A2A;--accent2:#CC5500;--accent-d:rgba(200,80,40,0.06);--green:#059669;--green-bg:rgba(5,150,105,0.06);--green-t:#065F46;--red:#DC2626;--red-bg:rgba(220,38,38,0.06);--red-t:#991B1B;--amber:#D97706;--amber-bg:rgba(217,119,6,0.06);--amber-t:#92400E;--t1:#2A0A05;--t2:#6A3A2A;--t3:#8A5A4A;--shadow:0 8px 32px rgba(0,0,0,0.06)}
[data-theme="white_gold"]{--bg:#F5ECD7;--bg2:#E8D5CC;--bg3:#F0E8D5;--card:rgba(255,248,235,0.7);--card-b:rgba(212,175,55,0.14);--card-bh:rgba(212,175,55,0.3);--accent:#D4AF37;--accent2:#C49A2A;--accent-d:rgba(212,175,55,0.06);--green:#B8860B;--green-bg:rgba(184,134,11,0.06);--green-t:#8A6A0A;--red:#CD5C5C;--red-bg:rgba(205,92,92,0.06);--red-t:#993A3A;--amber:#D4AF37;--amber-bg:rgba(212,175,55,0.06);--amber-t:#B8860B;--t1:#2A1A05;--t2:#6A5A2A;--t3:#8A7A4A;--shadow:0 8px 32px rgba(0,0,0,0.06)}
[data-theme="white_ocean"]{--bg:#D4EEFF;--bg2:#B8D8EE;--bg3:#C8E8FF;--card:rgba(235,248,255,0.7);--card-b:rgba(0,153,204,0.14);--card-bh:rgba(0,153,204,0.3);--accent:#0099CC;--accent2:#0077AA;--accent-d:rgba(0,153,204,0.06);--green:#00A86B;--green-bg:rgba(0,168,107,0.06);--green-t:#007A4A;--red:#CD5C5C;--red-bg:rgba(205,92,92,0.06);--red-t:#993A3A;--amber:#0099CC;--amber-bg:rgba(0,153,204,0.06);--amber-t:#0077AA;--t1:#052A3A;--t2:#2A5A7A;--t3:#3A7A9A;--shadow:0 8px 32px rgba(0,0,0,0.06)}
[data-theme="white_forest"]{--bg:#D4F5D4;--bg2:#B8E8B8;--bg3:#C8F0C8;--card:rgba(235,248,235,0.7);--card-b:rgba(46,139,87,0.14);--card-bh:rgba(46,139,87,0.3);--accent:#2E8B57;--accent2:#1A6A3A;--accent-d:rgba(46,139,87,0.06);--green:#2E8B57;--green-bg:rgba(46,139,87,0.06);--green-t:#1A6A3A;--red:#CD5C5C;--red-bg:rgba(205,92,92,0.06);--red-t:#993A3A;--amber:#2E8B57;--amber-bg:rgba(46,139,87,0.06);--amber-t:#1A6A3A;--t1:#052A0A;--t2:#2A5A2A;--t3:#3A7A3A;--shadow:0 8px 32px rgba(0,0,0,0.06)}
[data-theme="white_ruby"]{--bg:#F5D4E8;--bg2:#E8C4D8;--bg3:#F0D4E8;--card:rgba(248,235,240,0.7);--card-b:rgba(155,45,110,0.14);--card-bh:rgba(155,45,110,0.3);--accent:#9B2D6E;--accent2:#C44A8A;--accent-d:rgba(155,45,110,0.06);--green:#A86B8A;--green-bg:rgba(168,107,138,0.06);--green-t:#7A4A6A;--red:#CD5C5C;--red-bg:rgba(205,92,92,0.06);--red-t:#993A3A;--amber:#9B2D6E;--amber-bg:rgba(155,45,110,0.06);--amber-t:#C44A8A;--t1:#2A051A;--t2:#6A2A4A;--t3:#8A4A6A;--shadow:0 8px 32px rgba(0,0,0,0.06)}
.stars-bg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.star-bg{position:absolute;border-radius:50%;background:#C9A84C;animation:twinkleBg 4s ease-in-out infinite;opacity:0.1}
@keyframes twinkleBg{0%,100%{opacity:0.05}50%{opacity:0.15}}
.glow-main{position:fixed;border-radius:50%;filter:blur(200px);z-index:0;pointer-events:none}
.glow-left{width:600px;height:600px;background:rgba(212,175,55,0.02);top:-300px;left:-200px;animation:glowFloat 8s ease-in-out infinite}
.glow-right{width:500px;height:500px;background:rgba(184,150,100,0.01);bottom:-200px;right:-100px;animation:glowFloat 10s ease-in-out infinite reverse}
@keyframes glowFloat{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(50px,-30px) scale(1.1)}}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--card);backdrop-filter:blur(30px);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .4s cubic-bezier(0.34,1.56,0.64,1),background .4s;box-shadow:var(--shadow)}
.logo{display:flex;align-items:center;gap:10px;padding:16px 12px 12px;border-bottom:1px solid var(--card-b)}
.logo-icon{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,#C9A84C,#D4AF37,#B8963C);display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;box-shadow:0 0 30px rgba(212,175,55,0.1)}
.logo-name{font-size:13px;font-weight:800;background:linear-gradient(135deg,#D4AF37,#C9A84C);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.logo-sub{font-size:7px;color:var(--t3)}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0;position:relative;z-index:1}
.nav-it{display:flex;align-items:center;gap:8px;padding:8px 10px;color:var(--t3);font-size:11px;cursor:pointer;border-right:2px solid transparent;transition:all .3s cubic-bezier(0.34,1.56,0.64,1);margin:1px 4px;border-radius:6px}
.nav-it i{font-size:14px;width:18px;text-align:center;flex-shrink:0;transition:transform .3s}
.nav-it:hover{background:rgba(212,175,55,0.04);color:var(--t2)}
.nav-it:hover i{transform:scale(1.1)}
.nav-it.on{background:rgba(212,175,55,0.06);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-it.on i{color:var(--accent)}
.sb-foot{padding:10px 12px;border-top:1px solid var(--card-b)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:6px;background:var(--red-bg);color:var(--red-t);border-radius:6px;padding:6px;font-size:10px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.1);cursor:pointer;width:100%;transition:.3s}
.logout-btn:hover{background:rgba(239,68,68,0.12);transform:scale(1.02)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:48px;background:var(--card);backdrop-filter:blur(30px);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 10px;transition:background .4s}
.mob-top .ml{display:flex;align-items:center;gap:6px}
.mob-logo{width:26px;height:26px;border-radius:6px;background:linear-gradient(135deg,#C9A84C,#D4AF37);display:flex;align-items:center;justify-content:center;font-size:13px}
.mob-title{color:var(--t1);font-size:11px;font-weight:700}
.menu-btn{background:rgba(212,175,55,0.04);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:6px;font-size:14px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.3s}
.menu-btn:hover{background:rgba(212,175,55,0.08);transform:scale(1.05)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.2);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:16px 20px 80px;min-width:0;transition:margin .4s;position:relative;z-index:1}
.pg{display:none;animation:pageIn .4s cubic-bezier(0.34,1.56,0.64,1)}
.pg.on{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(20px) scale(0.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.topbar{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px}
.tb-title{font-size:17px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.tb-title i{color:var(--accent);font-size:19px}
.tb-sub{font-size:10px;color:var(--t3);margin-top:1px}
.tb-right{display:flex;align-items:center;gap:5px;flex-wrap:wrap}
.badge{font-size:8px;padding:2px 8px;border-radius:12px;font-weight:700;display:inline-flex;align-items:center;gap:3px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:rgba(212,175,55,0.08);color:var(--accent)}
.bg-fire{background:rgba(212,175,55,0.06);color:#D4AF37}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.dot{width:5px;height:5px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green);animation:dotPulse 1.5s ease-in-out infinite}
.dr{background:var(--red);animation:dotPulse 1.8s ease-in-out infinite}
.da{background:var(--amber);animation:dotPulse 2s ease-in-out infinite}
.db{background:var(--accent);animation:dotPulse 1.2s ease-in-out infinite}
@keyframes dotPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.7)}}
.stats-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-bottom:16px}
.stat-card{background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:12px 8px;transition:all .4s cubic-bezier(0.34,1.56,0.64,1);text-align:center;position:relative;overflow:hidden}
.stat-card::before{content:'';position:absolute;top:-50%;right:-50%;width:100px;height:100px;background:radial-gradient(circle,rgba(212,175,55,0.03),transparent 70%);pointer-events:none}
.stat-card:hover{border-color:var(--card-bh);transform:translateY(-4px) scale(1.02);box-shadow:var(--shadow)}
.stat-card .icon{font-size:18px;margin-bottom:3px;display:block}
.stat-card .number{font-size:18px;font-weight:800;color:var(--t1);line-height:1.2}
.stat-card .number.small{font-size:13px}
.stat-card .label{font-size:9px;color:var(--t3);margin-top:2px;font-weight:500}
.stat-card .sub{font-size:7px;color:var(--t3);margin-top:0px;opacity:.6}
.stat-mini{background:var(--card);border:1px solid var(--card-b);border-radius:8px;padding:8px 12px;display:flex;align-items:center;gap:8px;transition:all .3s cubic-bezier(0.34,1.56,0.64,1)}
.stat-mini:hover{transform:translateY(-2px);border-color:var(--card-bh)}
.stat-mini-icon{font-size:16px}
.stat-mini-num{font-size:16px;font-weight:800;color:var(--t1)}
.stat-mini-label{font-size:9px;color:var(--t3)}
.users-table{width:100%;border-collapse:collapse;font-size:12px}
.users-table thead th{padding:10px 12px;text-align:right;color:var(--t2);font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;border-bottom:1px solid var(--card-b);background:rgba(212,175,55,0.02)}
.users-table tbody td{padding:8px 12px;border-bottom:1px solid var(--card-b);color:var(--t1);vertical-align:middle}
.users-table tbody tr{transition:background .3s}
.users-table tbody tr:hover{background:rgba(212,175,55,0.02)}
.users-table .status-badge{display:inline-flex;align-items:center;gap:5px;padding:2px 10px;border-radius:12px;font-size:9px;font-weight:700}
.users-table .status-badge .status-dot{width:6px;height:6px;border-radius:50%;display:inline-block;animation:statusPulse 1.5s ease-in-out infinite}
.users-table .status-badge.active .status-dot{background:var(--green-t)}
.users-table .status-badge.expired .status-dot{background:var(--red-t)}
.users-table .status-badge.disabled .status-dot{background:var(--amber-t)}
@keyframes statusPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.6)}}
.users-table .status-badge.active{background:var(--green-bg);color:var(--green-t)}
.users-table .status-badge.expired{background:var(--red-bg);color:var(--red-t)}
.users-table .status-badge.disabled{background:var(--amber-bg);color:var(--amber-t)}
.users-table .usage-bar{display:flex;align-items:center;gap:6px}
.users-table .usage-bar .bar{width:80px;height:3px;border-radius:3px;background:rgba(212,175,55,0.05);overflow:hidden}
.users-table .usage-bar .bar .fill{height:100%;border-radius:3px;background:linear-gradient(90deg,#C9A84C,#D4AF37,#B8963C);transition:width .8s cubic-bezier(0.34,1.56,0.64,1)}
.users-table .usage-text{font-size:9px;color:var(--t2);white-space:nowrap}
.users-table .action-btns{display:flex;gap:3px;justify-content:center;flex-wrap:wrap}
.users-table .action-btns .btn{padding:2px 6px;font-size:8px;border-radius:4px}
.user-name-cell{display:flex;align-items:center;gap:6px}
.user-name-cell .avatar{width:24px;height:24px;border-radius:6px;background:linear-gradient(135deg,#C9A84C,#D4AF37);display:flex;align-items:center;justify-content:center;font-size:10px;color:#fff;flex-shrink:0;transition:transform .3s}
.user-name-cell:hover .avatar{transform:scale(1.1) rotate(-5deg)}
.user-name-cell .name{font-weight:600;color:var(--t1)}
.user-name-cell .uuid-short{font-size:7px;color:var(--t3);font-family:monospace}
.btn{font-family:inherit;font-size:10px;font-weight:600;border-radius:6px;padding:5px 10px;cursor:pointer;display:inline-flex;align-items:center;gap:4px;border:none;transition:all .3s cubic-bezier(0.34,1.56,0.64,1);white-space:nowrap}
.btn i{font-size:11px;transition:transform .3s}
.btn:hover i{transform:scale(1.1)}
.btn-p{background:linear-gradient(135deg,#C9A84C,#D4AF37,#B8963C);background-size:200% 200%;animation:btnGradient 4s ease infinite;color:#fff;box-shadow:0 3px 15px rgba(212,175,55,.15)}
@keyframes btnGradient{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 6px 25px rgba(212,175,55,.25)}
.btn-o{background:rgba(0,0,0,0.02);border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:rgba(212,175,55,0.04);transform:translateY(-1px)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.1)}
.btn-d:hover{background:rgba(239,68,68,.12);transform:translateY(-1px)}
.btn-pur{background:rgba(212,175,55,0.06);color:var(--accent);border:1px solid rgba(212,175,55,.08)}
.btn-pur:hover{background:rgba(212,175,55,0.12);transform:translateY(-1px)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,0.08)}
.btn-amber:hover{background:rgba(245,158,11,0.12);transform:translateY(-1px)}
.btn-sm{padding:2px 6px;font-size:8px;border-radius:4px}
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.3);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);backdrop-filter:blur(30px);border:1px solid var(--card-b);border-radius:14px;padding:20px 18px;max-width:560px;width:calc(100% - 20px);max-height:90vh;overflow-y:auto;position:relative;animation:modalIn .4s cubic-bezier(0.34,1.56,0.64,1);box-shadow:var(--shadow)}
@keyframes modalIn{from{opacity:0;transform:scale(0.9) translateY(20px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-close{position:absolute;top:10px;left:10px;background:rgba(212,175,55,0.04);border:1px solid var(--card-b);color:var(--t2);width:24px;height:24px;border-radius:6px;font-size:12px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:.3s}
.modal-close:hover{background:var(--red-bg);color:var(--red-t);transform:rotate(90deg)}
.modal-title{font-size:14px;font-weight:700;color:var(--t1);margin-bottom:12px;display:flex;align-items:center;gap:6px}
.modal-title i{color:var(--accent);font-size:15px}
.fg{display:flex;flex-direction:column;gap:2px;margin-bottom:8px}
.fg label{font-size:8px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em;display:flex;align-items:center;gap:3px}
.fi{width:100%;padding:6px 10px;border-radius:6px;border:1px solid var(--card-b);background:rgba(255,252,245,0.5);color:var(--t1);font-family:inherit;font-size:10px;outline:none;transition:.3s}
.fi:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(212,175,55,.06)}
.fi::placeholder{color:var(--t3)}
select.fi{appearance:none;cursor:pointer}
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px}
.conn-card{background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:10px;padding:10px 12px;transition:.3s}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.conn-card .ip{font-family:monospace;font-size:11px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:4px}
.conn-card .label{font-size:8px;color:var(--t3);margin-top:1px}
.conn-card .conn-info{display:flex;justify-content:space-between;margin-top:4px;font-size:8px;color:var(--t2);gap:3px;flex-wrap:wrap}
.conn-status-dot{display:inline-block;width:5px;height:5px;border-radius:50%;background:#059669;animation:pulse 1.5s infinite;margin-left:3px}
.settings-card{background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:14px 16px;max-width:480px;margin-bottom:10px;position:relative;overflow:hidden;transition:all .3s}
.settings-card:hover{border-color:var(--card-bh)}
.settings-card::before{content:'';position:absolute;top:-50%;right:-50%;width:150px;height:150px;background:radial-gradient(circle,rgba(212,175,55,0.02),transparent 70%);pointer-events:none}
.settings-card .title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:10px;display:flex;align-items:center;gap:6px}
.settings-card .title i{color:var(--accent)}
.settings-card .field{margin-bottom:8px}
.settings-card .field label{font-size:9px;color:var(--t3);display:block;margin-bottom:2px;font-weight:600}
.settings-card .field input{width:100%;padding:6px 10px;border-radius:6px;border:1px solid var(--card-b);background:rgba(255,252,245,0.5);color:var(--t1);font-family:inherit;font-size:11px;outline:none;transition:.3s}
.settings-card .field input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(212,175,55,.06)}
.settings-card .btn{width:100%;justify-content:center;margin-top:3px;font-size:11px;padding:6px}
.settings-card .toggle-row{display:flex;align-items:center;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--card-b)}
.settings-card .toggle-row .toggle-label{font-size:11px;color:var(--t2);display:flex;align-items:center;gap:5px}
.switch{position:relative;width:36px;height:20px;background:var(--t3);border-radius:10px;cursor:pointer;transition:.4s;flex-shrink:0}
.switch.on{background:linear-gradient(135deg,#C9A84C,#D4AF37)}
.switch .slider{position:absolute;top:2px;right:2px;width:16px;height:16px;background:#fff;border-radius:50%;transition:.4s cubic-bezier(0.34,1.56,0.64,1);box-shadow:0 2px 4px rgba(0,0,0,0.1)}
.switch.on .slider{right:18px}
.toast{position:fixed;bottom:70px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);backdrop-filter:blur(30px);border:1px solid var(--card-b);color:var(--t1);border-radius:8px;padding:8px 16px;font-size:11px;opacity:0;transition:all .4s cubic-bezier(0.34,1.56,0.64,1);z-index:999;pointer-events:none;box-shadow:var(--shadow);display:flex;align-items:center;gap:5px}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.12);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.12);background:var(--red-bg);color:var(--red-t)}
.empty{text-align:center;padding:30px 15px;color:var(--t3)}
.empty i{font-size:28px;opacity:.3;display:block;margin-bottom:6px}
.empty p{font-size:10px}
.bottom-nav{display:none;position:fixed;bottom:0;right:0;left:0;background:var(--card);backdrop-filter:blur(30px);border-top:1px solid var(--card-b);z-index:300;padding:4px 2px 6px;justify-content:space-around;align-items:center}
.bottom-nav .nav-item{display:flex;flex-direction:column;align-items:center;gap:1px;color:var(--t3);font-size:7px;cursor:pointer;padding:3px 6px;border-radius:6px;transition:all .3s;border:none;background:none;font-family:inherit;min-width:40px;position:relative}
.bottom-nav .nav-item i{font-size:16px;transition:all .3s}
.bottom-nav .nav-item:hover{color:var(--t2);transform:translateY(-2px)}
.bottom-nav .nav-item.active{color:var(--accent)}
.bottom-nav .nav-item.active i{transform:scale(1.1)}
@media(max-width:768px){.bottom-nav{display:flex !important}.main{padding-bottom:65px !important;margin-right:0 !important;padding-top:55px !important}.sidebar{transform:translateX(100%);padding-bottom:60px}.sidebar.open{transform:translateX(0)}.mob-top{display:flex}.stats-grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:480px){.stats-grid{grid-template-columns:1fr 1fr}.main{padding:50px 8px 65px}.bottom-nav .nav-item{min-width:32px;padding:2px 4px}.bottom-nav .nav-item i{font-size:14px}.bottom-nav .nav-item span{font-size:6px}.users-table thead th{font-size:7px;padding:6px 4px}.users-table tbody td{font-size:9px;padding:6px 4px}.users-table .usage-bar .bar{width:40px}.stat-mini{padding:6px 8px}.stat-mini-num{font-size:13px}}
@media(min-width:769px){.bottom-nav{display:none !important}}
body.dark-theme{--bg:#0a0a1a;--bg2:#12122a;--bg3:#1a1a3a;--card:rgba(10,10,30,0.7);--card-b:rgba(212,175,55,0.08);--card-bh:rgba(212,175,55,0.15);--t1:#F0EEFF;--t2:#8888BB;--t3:#555577;--shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(212,175,55,0.03)}
body.dark-theme .stars-bg .star-bg{background:#fff}
body.dark-theme .glow-main{display:block}
body.dark-theme .stat-card::before{background:radial-gradient(circle,rgba(212,175,55,0.03),transparent 70%)}
body.dark-theme .fi{background:rgba(0,0,20,.2)}
body.dark-theme .btn-o{background:rgba(255,255,255,0.02);border-color:var(--card-b);color:var(--t2)}
body.dark-theme .btn-o:hover{background:rgba(212,175,55,0.05)}
body.dark-theme .users-table thead th{background:rgba(212,175,55,0.02)}
body.dark-theme .users-table tbody tr:hover{background:rgba(212,175,55,0.02)}
</style>
</head>
<body>
<div class="stars-bg">
    <div class="star-bg" style="width:2px;height:2px;top:5%;left:10%;animation-delay:0s"></div>
    <div class="star-bg" style="width:3px;height:3px;top:15%;left:30%;animation-delay:1.5s"></div>
    <div class="star-bg" style="width:1px;height:1px;top:25%;left:50%;animation-delay:0.8s"></div>
    <div class="star-bg" style="width:2px;height:2px;top:40%;left:70%;animation-delay:2.2s"></div>
    <div class="star-bg" style="width:3px;height:3px;top:55%;left:15%;animation-delay:0.5s"></div>
    <div class="star-bg" style="width:1px;height:1px;top:70%;left:85%;animation-delay:1.8s"></div>
    <div class="star-bg" style="width:2px;height:2px;top:85%;left:40%;animation-delay:2.5s"></div>
</div>
<div class="glow-main glow-left"></div><div class="glow-main glow-right"></div>
<div class="toast" id="toast"></div>

<div class="modal-bg" id="modal-user">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-user')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-user-plus"></i> 🏛️ ساخت کانفیگ جدید</div>
    <div class="fg"><label><i class="ti ti-tag"></i> نام کاربری</label><input class="fi" id="user-label" placeholder="مثلاً: کاربر علی"></div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-database"></i> حجم</label><input class="fi" id="user-quota" type="number" min="0.5" step="0.5" value="2"></div>
      <div class="fg"><label><i class="ti ti-ruler"></i> واحد</label><select class="fi" id="user-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> انقضا (روز)</label><input class="fi" id="user-exp" type="number" min="0" value="30" placeholder="0=نامحدود"></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-fingerprint"></i> فینگرپرینت</label><select class="fi" id="user-fingerprint"><option value="chrome">Chrome</option><option value="firefox">Firefox</option><option value="safari">Safari</option><option value="edge">Edge</option><option value="random">Random</option><option value="none">None</option></select></div>
      <div class="fg"><label><i class="ti ti-devices"></i> محدودیت دستگاه</label><input class="fi" id="user-devices" type="number" min="0" max="10" value="1" placeholder="0=نامحدود"></div>
    </div>
    <div class="fg"><label><i class="ti ti-settings"></i> پروتکل</label><select class="fi" id="user-protocol"><option value="vless-ws">VLESS (WebSocket)</option><option value="xhttp-stream-up">XHTTP (Stream)</option></select></div>
    <div class="fg"><label><i class="ti ti-plug"></i> پورت (پیش‌فرض: 443)</label><input class="fi" id="user-port" type="number" min="1" max="65535" value="443" placeholder="443"></div>
    <div class="fg"><label><i class="ti ti-lock"></i> رمز کانفیگ (اختیاری)</label><input class="fi" id="user-password" type="password" placeholder="برای حذف/ویرایش نیاز است" dir="ltr"></div>
    <div style="display:flex;gap:8px;margin-top:16px">
      <button class="btn btn-p" onclick="saveUser()" style="flex:2"><i class="ti ti-check"></i> ساخت کانفیگ</button>
      <button class="btn btn-o" onclick="closeModal('modal-user')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<div class="modal-bg" id="modal-edit">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> 🏛️ ویرایش کانفیگ</div>
    <input type="hidden" id="edit-uuid">
    <div class="fg" id="edit-password-section">
      <label><i class="ti ti-lock"></i> 🔑 رمز کانفیگ (برای ویرایش لازم است)</label>
      <input class="fi" id="edit-password" type="password" placeholder="رمز کانفیگ را وارد کنید" dir="ltr">
    </div>
    <div class="fg"><label><i class="ti ti-tag"></i> نام کاربری</label><input class="fi" id="edit-label" placeholder="نام کاربری"></div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-database"></i> حجم (0=نامحدود)</label><input class="fi" id="edit-quota" type="number" min="0" step="0.5"></div>
      <div class="fg"><label><i class="ti ti-ruler"></i> واحد</label><select class="fi" id="edit-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> انقضا (روز)</label><input class="fi" id="edit-exp" type="number" min="0" placeholder="0=نامحدود"></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-fingerprint"></i> فینگرپرینت</label><select class="fi" id="edit-fingerprint"><option value="chrome">Chrome</option><option value="firefox">Firefox</option><option value="safari">Safari</option><option value="edge">Edge</option><option value="random">Random</option><option value="none">None</option></select></div>
      <div class="fg"><label><i class="ti ti-devices"></i> محدودیت دستگاه</label><input class="fi" id="edit-devices" type="number" min="0" max="10" placeholder="0=نامحدود"></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-settings"></i> پروتکل</label>
        <select class="fi" id="edit-protocol">
          <option value="vless-ws">VLESS (WebSocket)</option>
          <option value="xhttp-stream-up">XHTTP (Stream)</option>
        </select>
      </div>
      <div class="fg"><label><i class="ti ti-toggle-left"></i> وضعیت</label>
        <select class="fi" id="edit-status">
          <option value="true">✅ فعال</option>
          <option value="false">❌ غیرفعال</option>
        </select>
      </div>
    </div>
    <div class="fg"><label><i class="ti ti-plug"></i> پورت</label><input class="fi" id="edit-port" type="number" min="1" max="65535" placeholder="443"></div>
    <div style="display:flex;gap:8px;margin-top:16px">
      <button class="btn btn-p" onclick="saveEdit()" style="flex:2"><i class="ti ti-check"></i> ذخیره تغییرات</button>
      <button class="btn btn-o" onclick="closeModal('modal-edit')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<div class="modal-bg" id="modal-delete">
  <div class="modal" style="max-width:400px">
    <button class="modal-close" onclick="closeModal('modal-delete')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-trash"></i> 🏛️ حذف کانفیگ</div>
    <input type="hidden" id="delete-uuid">
    <p style="font-size:13px;color:var(--t2);margin-bottom:16px">برای حذف این کانفیگ، رمز آن را وارد کنید.</p>
    <div class="fg">
      <label><i class="ti ti-lock"></i> رمز کانفیگ</label>
      <input class="fi" id="delete-password" type="password" placeholder="رمز کانفیگ را وارد کنید" dir="ltr">
    </div>
    <div style="display:flex;gap:8px;margin-top:16px">
      <button class="btn btn-d" onclick="confirmDelete()" style="flex:2"><i class="ti ti-trash"></i> حذف</button>
      <button class="btn btn-o" onclick="closeModal('modal-delete')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<div class="mob-top">
  <div class="ml"><div class="mob-logo">🏛️</div><span class="mob-title">تخت جمشید</span></div>
  <div class="mob-right"><button class="theme-mob" id="theme-mob-btn" onclick="cycleTheme()"><i class="ti ti-palette" id="theme-mob-icon"></i></button><button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button></div>
</div>
<div class="overlay" id="overlay"></div>

<aside class="sidebar" id="sb">
  <div class="logo"><div class="logo-icon">🏛️</div><div><div class="logo-name">تخت جمشید</div><div class="logo-sub">مدیریت کاربران</div></div></div>
  <div class="nav-wrap">
    <div class="nav-it on" data-pg="users"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات زنده</div>
    <div class="nav-it" data-pg="support"><i class="ti ti-headset"></i> پشتیبانی</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
    <div class="nav-it" data-pg="backup"><i class="ti ti-database"></i> بکاپ</div>
  </div>
  <div class="sb-foot">
    <div style="position:relative;margin-bottom:7px">
      <button class="theme-select-btn" onclick="toggleThemeMenu()">
        <i class="ti ti-palette"></i> <span id="theme-display-label">انتخاب تم</span> <i class="ti ti-chevron-down" style="font-size:12px"></i>
      </button>
      <div class="theme-menu" id="theme-menu">
        <div class="theme-menu-item" onclick="selectTheme('dark_fire')"><span class="dot" style="background:linear-gradient(135deg,#FF6B35,#FF4500)"></span> آتشین تیره</div>
        <div class="theme-menu-item" onclick="selectTheme('gold')"><span class="dot" style="background:linear-gradient(135deg,#D4AF37,#F5D060)"></span> طلایی تیره</div>
        <div class="theme-menu-item" onclick="selectTheme('ocean')"><span class="dot" style="background:linear-gradient(135deg,#0099CC,#33CCFF)"></span> آبی اقیانوسی تیره</div>
        <div class="theme-menu-item" onclick="selectTheme('forest')"><span class="dot" style="background:linear-gradient(135deg,#2E8B57,#4CAF50)"></span> سبز جنگلی تیره</div>
        <div class="theme-menu-item" onclick="selectTheme('ruby')"><span class="dot" style="background:linear-gradient(135deg,#9B2D6E,#C44A8A)"></span> بنفش یاقوتی تیره</div>
        <div class="theme-menu-item" onclick="selectTheme('white_fire')"><span class="dot" style="background:linear-gradient(135deg,#F5E6E0,#E8D5CC)"></span> آتشین روشن</div>
        <div class="theme-menu-item" onclick="selectTheme('white_gold')"><span class="dot" style="background:linear-gradient(135deg,#F5ECD7,#E8D5CC)"></span> طلایی روشن</div>
        <div class="theme-menu-item" onclick="selectTheme('white_ocean')"><span class="dot" style="background:linear-gradient(135deg,#D4EEFF,#B8D8EE)"></span> آبی اقیانوسی روشن</div>
        <div class="theme-menu-item" onclick="selectTheme('white_forest')"><span class="dot" style="background:linear-gradient(135deg,#D4F5D4,#B8E8B8)"></span> سبز جنگلی روشن</div>
        <div class="theme-menu-item" onclick="selectTheme('white_ruby')"><span class="dot" style="background:linear-gradient(135deg,#F5D4E8,#E8C4D8)"></span> بنفش یاقوتی روشن</div>
      </div>
    </div>
    <button class="rgb-btn off" id="rgb-btn" onclick="toggleRGB()"><i class="ti ti-color-swatch"></i> <span id="rgb-label">تم RGB</span></button>
    <button class="support-btn" onclick="window.open('https://t.me/+QyEVU0FquFczYjQ0','_blank')"><i class="ti ti-brand-telegram"></i> گروه پشتیبانی</button>
    <button class="logout-btn" onclick="logout()"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>

<main class="main">
<section class="pg on" id="pg-users">
  <div class="topbar">
    <div>
      <div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد تخت جمشید</div>
      <div class="tb-sub" id="last-update">آخرین بروزرسانی: لحظه‌ای</div>
    </div>
    <div class="tb-right">
      <span class="badge bg-fire" id="online-badge"><span class="dot dg"></span> ۰ آنلاین</span>
      <button class="btn btn-p" onclick="openModal('modal-user')"><i class="ti ti-plus"></i> کانفیگ جدید</button>
    </div>
  </div>
  <div class="stats-grid">
    <div class="stat-card"><span class="icon">🔥</span><div class="number" id="online-count">۰</div><div class="label">سرویس‌های آنلاین</div><div class="sub">در حال اتصال</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">👥</span><div class="number" id="total-users">۰</div><div class="label">کل کاربران</div><div class="sub">ثبت‌شده</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">📊</span><div class="number" id="total-usage">۰</div><div class="label">مصرف کل</div><div class="sub">مگابایت</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">📱</span><div class="number" id="active-devices">۰</div><div class="label">دستگاه‌های فعال</div><div class="sub">متصل</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">⛔</span><div class="number" id="inactive-count">۰</div><div class="label">غیرفعال</div><div class="sub">غیرفعال</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">🏆</span><div class="number" id="top-user-label" style="font-size:16px">-</div><div class="label">پر مصرف‌ترین کاربر</div><div class="sub" id="top-user-usage">۰</div><div class="bar"></div></div>
  </div>
  <div id="users-grid" class="user-grid"><div class="empty"><i class="ti ti-users"></i><p>هیچ کاربری ساخته نشده</p></div></div>
</section>

<section class="pg" id="pg-connections">
  <div class="topbar"><div><div class="tb-title">🔌 اتصالات زنده</div><div class="tb-sub" id="conn-count">۰ اتصال</div></div><div class="tb-right"><span class="badge bg-green" id="conn-live-badge"><span class="dot dg pulse"></span> فعال</span><button class="btn btn-sm btn-o" onclick="loadConnections()"><i class="ti ti-refresh"></i> بروزرسانی</button></div></div>
  <div id="conns-grid" class="conn-grid"><div class="empty"><i class="ti ti-plug-off"></i><p>هیچ اتصال فعالی وجود ندارد</p></div></div>
</section>

<section class="pg" id="pg-support">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-headset"></i> پشتیبانی</div><div class="tb-sub">راهنمایی و پشتیبانی سریع</div></div></div>
  <div style="background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:24px;max-width:600px">
    <div style="font-size:16px;font-weight:700;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;gap:8px"><i class="ti ti-messages" style="color:var(--accent)"></i> ارتباط با پشتیبانی</div>
    <p style="font-size:13px;color:var(--t2);line-height:1.9;margin-bottom:16px">برای دریافت راهنمایی، پشتیبانی و پاسخ به سوالات خود، به گروه تلگرامی ما بپیوندید.</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <button class="btn btn-p" onclick="window.open('https://t.me/+QyEVU0FquFczYjQ0','_blank')" style="flex:2"><i class="ti ti-brand-telegram"></i> عضویت در گروه پشتیبانی</button>
      <button class="btn btn-o" onclick="navigator.clipboard.writeText('https://t.me/+QyEVU0FquFczYjQ0').then(()=>toast('لینک گروه کپی شد ✓','ok'))"><i class="ti ti-copy"></i> کپی لینک</button>
    </div>
    <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--card-b);display:flex;align-items:center;gap:10px;flex-wrap:wrap">
      <span class="badge bg-green"><span class="dot dg"></span> آنلاین</span>
      <span style="font-size:11px;color:var(--t3)">گروه پشتیبانی تخت جمشید · پاسخگویی سریع</span>
    </div>
  </div>
</section>

<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات پنل</div><div class="tb-sub">تنظیمات ظاهری و مدیریتی</div></div></div>
  <div class="settings-card">
    <div class="title"><i class="ti ti-color-swatch"></i> تنظیمات ظاهری</div>
    <div class="toggle-row">
      <div class="toggle-label"><i class="ti ti-color-palette" style="background:linear-gradient(135deg,#ff0000,#00ff00,#0000ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent"></i> تم RGB متحرک (کل پنل)</div>
      <div class="switch" id="rgb-switch" onclick="toggleRGB()">
        <div class="slider"></div>
      </div>
    </div>
    <div style="margin-top:12px;font-size:10px;color:var(--t3)">💡 با فعال کردن این گزینه، رنگ کل پنل هر ۲ ثانیه به صورت آرام تغییر میکند</div>
  </div>
</section>

<section class="pg" id="pg-backup">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-database"></i> مدیریت بکاپ</div><div class="tb-sub">ذخیره و بازیابی اطلاعات</div></div></div>
  <div class="settings-card">
    <div class="title"><i class="ti ti-download"></i> بکاپ‌گیری</div>
    <p style="font-size:12px;color:var(--t2);margin-bottom:16px;line-height:1.8">از اطلاعات کاربران، کانفیگ‌ها و تنظیمات بکاپ بگیرید.</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <button class="btn btn-p" onclick="createBackup()" style="flex:2"><i class="ti ti-download"></i> دانلود بکاپ</button>
      <button class="btn btn-o" onclick="document.getElementById('restore-input').click()" style="flex:1"><i class="ti ti-upload"></i> بازیابی</button>
      <input type="file" id="restore-input" accept=".json" style="display:none" onchange="restoreBackup(event)">
    </div>
    <div style="margin-top:12px;font-size:10px;color:var(--t3)">📁 فایل بکاپ با فرمت JSON ذخیره می‌شود</div>
  </div>
</section>
</main>

<script>
// ===== مدیریت تم =====
let currentTheme = localStorage.getItem('takht-theme') || 'dark_fire';
const themeList = ['dark_fire','gold','ocean','forest','ruby','white_fire','white_gold','white_ocean','white_forest','white_ruby'];
const themeNames = {
    'dark_fire':'🔥 آتشین تیره',
    'gold':'👑 طلایی تیره',
    'ocean':'🌊 آبی اقیانوسی تیره',
    'forest':'🌲 سبز جنگلی تیره',
    'ruby':'💎 بنفش یاقوتی تیره',
    'white_fire':'🔥 آتشین روشن',
    'white_gold':'👑 طلایی روشن',
    'white_ocean':'🌊 آبی اقیانوسی روشن',
    'white_forest':'🌲 سبز جنگلی روشن',
    'white_ruby':'💎 بنفش یاقوتی روشن'
};

function applyTheme(theme) {
    currentTheme = theme;
    localStorage.setItem('takht-theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
    const label = document.getElementById('theme-display-label');
    if (label) label.textContent = themeNames[theme] || 'انتخاب تم';
    document.getElementById('theme-menu').classList.remove('show');
}

function cycleTheme() {
    const idx = themeList.indexOf(currentTheme);
    const next = themeList[(idx + 1) % themeList.length];
    applyTheme(next);
    toast('🔄 ' + themeNames[next], 'ok');
}

function toggleThemeMenu() {
    document.getElementById('theme-menu').classList.toggle('show');
}

function selectTheme(theme) {
    applyTheme(theme);
    toast('✅ ' + themeNames[theme], 'ok');
}

document.addEventListener('click', function(e) {
    const menu = document.getElementById('theme-menu');
    const btn = document.querySelector('.theme-select-btn');
    if (menu && btn && !btn.contains(e.target) && !menu.contains(e.target)) {
        menu.classList.remove('show');
    }
});

applyTheme(currentTheme);

// ===== RGB =====
let rgbMode = false;

async function loadRGBStatus() {
  try {
    const r = await authF('/api/settings');
    const data = await r.json();
    rgbMode = data.rgb_mode || false;
    updateRGBUI();
  } catch(e) {}
}

function updateRGBUI() {
  const btn = document.getElementById('rgb-btn');
  const label = document.getElementById('rgb-label');
  const sw = document.getElementById('rgb-switch');
  
  if (rgbMode) {
    document.body.classList.add('rgb-mode');
    btn.classList.remove('off');
    btn.style.background = 'linear-gradient(135deg,#ff0000,#00ff00,#0000ff,#ff0000)';
    btn.style.backgroundSize = '300% 300%';
    btn.style.animation = 'btnGradient 3s ease infinite';
    label.textContent = 'RGB: روشن';
    sw.classList.add('on');
  } else {
    document.body.classList.remove('rgb-mode');
    btn.classList.add('off');
    btn.style.background = '';
    btn.style.animation = '';
    label.textContent = 'تم RGB';
    sw.classList.remove('on');
  }
}

async function toggleRGB() {
  const newState = !rgbMode;
  try {
    const r = await authF('/api/settings/rgb', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ enabled: newState })
    });
    const data = await r.json();
    rgbMode = data.rgb_mode;
    updateRGBUI();
    toast(rgbMode ? '🌈 تم RGB کل پنل فعال شد' : '🌙 تم RGB غیرفعال شد', 'ok');
  } catch(e) {
    toast('خطا در تغییر تنظیمات', 'err');
  }
}

// ===== توابع کمکی =====
function toast(msg, type='') {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show' + (type ? ' ' + type : '');
  setTimeout(() => t.classList.remove('show'), 2500);
}

function fmtB(b) {
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if (b < 1024**3) return (b/1024**2).toFixed(2) + ' MB';
  return (b/1024**3).toFixed(2) + ' GB';
}

function esc(s) {
  return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function openModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }

async function authF(url, opts={}) {
  const r = await fetch(url, opts);
  if (r.status === 401) { location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}

async function logout() {
  try { await fetch('/api/logout', {method:'POST'}); } catch(e) {}
  location.href = '/login';
}

function navTo(name) {
  document.querySelectorAll('.nav-it').forEach(n => n.classList.toggle('on', n.dataset.pg === name));
  document.querySelectorAll('.pg').forEach(p => p.classList.toggle('on', p.id === 'pg-' + name));
  closeSb();
  if (name === 'users') loadUsers();
  if (name === 'connections') loadConnections();
}

document.querySelectorAll('.nav-it').forEach(el => {
  el.addEventListener('click', () => navTo(el.dataset.pg));
});

const sb = document.getElementById('sb'), overlay = document.getElementById('overlay');
function openSb(){ sb.classList.add('open'); overlay.classList.add('show'); }
function closeSb(){ sb.classList.remove('open'); overlay.classList.remove('show'); }
document.getElementById('open-sb').addEventListener('click', openSb);
overlay.addEventListener('click', closeSb);

// ===== بارگذاری کاربران =====
async function loadUsers() {
  try {
    const r = await authF('/api/links');
    const { links=[] } = await r.json();
    const grid = document.getElementById('users-grid');
    
    const total = links.length;
    const online = links.filter(l => l.active && !l.expired).length;
    const inactive = links.filter(l => !l.active || l.expired).length;
    const totalBytes = links.reduce((sum, l) => sum + (l.used_bytes || 0), 0);
    const devices = links.reduce((sum, l) => sum + (l.max_devices || 0), 0);
    
    document.getElementById('total-users').textContent = total;
    document.getElementById('online-count').textContent = online;
    document.getElementById('inactive-count').textContent = inactive;
    document.getElementById('total-usage').textContent = (totalBytes / (1024*1024)).toFixed(1);
    document.getElementById('active-devices').textContent = devices;
    document.getElementById('last-update').textContent = 'آخرین بروزرسانی: ' + new Date().toLocaleTimeString('fa-IR');
    document.getElementById('online-badge').innerHTML = '<span class="dot dg"></span> ' + online + ' آنلاین';
    
    try {
      const sr = await authF('/stats');
      const statsData = await sr.json();
      if (statsData.top_user) {
        document.getElementById('top-user-label').textContent = '🏛️ ' + statsData.top_user.label;
        document.getElementById('top-user-usage').textContent = statsData.top_user.used_fmt || '0';
      } else {
        document.getElementById('top-user-label').textContent = '—';
        document.getElementById('top-user-usage').textContent = '۰';
      }
    } catch(e) {}
    
    if (!links.length) {
      grid.innerHTML = '<div class="empty"><i class="ti ti-users"></i><p>هیچ کاربری ساخته نشده</p></div>';
      return;
    }
    
    const host = window.location.host;
    grid.innerHTML = links.map(l => {
      const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
      const bc = pct > 90 ? '#EF4444' : pct > 70 ? '#F59E0B' : '#C9A84C';
      const active = l.active && !l.expired;
      const subLink = `https://${host}/sub/${l.uuid}`;
      const hasPassword = l.has_password === true;
      const port = l.port || 443;
      
      const todayBytes = l.today_bytes || 0;
      const todayFmt = fmtB(todayBytes);
      const lastSeen = l.last_connected_at ? new Date(l.last_connected_at).toLocaleString('fa-IR') : '—';
      const statusText = active ? '🟢 آنلاین' : '🔴 آفلاین';
      const statusClass = active ? 'on' : 'off';
      
      return `<div class="user-card">
        <div class="head">
          <div class="name">🏛️ ${esc(l.label)} ${hasPassword ? '<span class="lock-badge"><i class="ti ti-lock"></i> رمزدار</span>' : ''}</div>
          <span class="status ${statusClass}">${statusText}</span>
        </div>
        <div class="uuid">🔑 ${esc(l.uuid)}</div>
        <div class="info">
          <span>📊 امروز: ${todayFmt}</span>
          <span>📅 آخرین اتصال: ${lastSeen}</span>
          <span>📱 ${l.max_devices === 0 ? '∞' : l.max_devices + ' دستگاه'}</span>
          <span>🔌 ${port}</span>
        </div>
        <div class="quota-info">
          <span>📊 مصرف: ${fmtB(l.used_bytes)}</span>
          <span>📦 کل: ${l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes)}</span>
        </div>
        <div class="quota-bar">
          <div class="quota-fill" style="width: ${pct}%; background: ${bc}"></div>
        </div>
        <div class="actions">
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(subLink)}').then(()=>toast('ساب‌لینک کپی شد ✓','ok'))"><i class="ti ti-link"></i> ساب</button>
          <button class="btn btn-sm btn-amber" onclick="resetUsage('${l.uuid}')"><i class="ti ti-rotate"></i> ریست</button>
          <button class="btn btn-sm btn-pur btn-icon" onclick="openEditModal('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
          <button class="btn btn-sm btn-d" onclick="openDeleteModal('${l.uuid}')"><i class="ti ti-trash"></i></button>
        </div>
      </div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== توابع ویرایش و حذف =====
async function openEditModal(uuid) {
    try {
        const r = await authF('/api/links');
        const { links=[] } = await r.json();
        const link = links.find(l => l.uuid === uuid);
        if (!link) { toast('کاربر یافت نشد', 'err'); return; }
        document.getElementById('edit-uuid').value = uuid;
        document.getElementById('edit-label').value = link.label || '';
        document.getElementById('edit-password').value = '';
        if (link.limit_bytes === 0) {
            document.getElementById('edit-quota').value = '';
        } else {
            document.getElementById('edit-quota').value = (link.limit_bytes / (1024**3)).toFixed(1);
        }
        document.getElementById('edit-unit').value = 'GB';
        if (link.expires_at) {
            const days = Math.ceil((new Date(link.expires_at) - new Date()) / (1000 * 60 * 60 * 24));
            document.getElementById('edit-exp').value = days > 0 ? days : 0;
        } else {
            document.getElementById('edit-exp').value = '';
        }
        document.getElementById('edit-fingerprint').value = link.fingerprint || 'chrome';
        document.getElementById('edit-devices').value = link.max_devices || 0;
        document.getElementById('edit-protocol').value = link.protocol || 'vless-ws';
        document.getElementById('edit-status').value = link.active ? 'true' : 'false';
        document.getElementById('edit-port').value = link.port || 443;
        if (link.has_password) {
            document.getElementById('edit-password-section').style.display = 'block';
        } else {
            document.getElementById('edit-password-section').style.display = 'none';
        }
        openModal('modal-edit');
    } catch(e) { toast('خطا در بارگذاری', 'err'); }
}

async function saveEdit() {
    const uuid = document.getElementById('edit-uuid').value;
    const password = document.getElementById('edit-password').value.trim();
    const label = document.getElementById('edit-label').value.trim() || 'کاربر';
    const quota = parseFloat(document.getElementById('edit-quota').value) || 0;
    const unit = document.getElementById('edit-unit').value || 'GB';
    const exp = parseInt(document.getElementById('edit-exp').value) || 0;
    const fingerprint = document.getElementById('edit-fingerprint').value || 'chrome';
    const devices = parseInt(document.getElementById('edit-devices').value) || 0;
    const protocol = document.getElementById('edit-protocol').value || 'vless-ws';
    const active = document.getElementById('edit-status').value === 'true';
    const port = parseInt(document.getElementById('edit-port').value) || 443;
    try {
        const r = await authF('/api/links/' + uuid, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                label, limit_value: quota, limit_unit: unit, expires_days: exp,
                fingerprint, max_devices: devices, protocol, active, password, port
            })
        });
        if (!r.ok) {
            const err = await r.json().catch(() => ({}));
            if (r.status === 403) { toast('❌ رمز کانفیگ اشتباه است!', 'err'); }
            else { throw new Error(err.detail || 'خطا'); }
            return;
        }
        closeModal('modal-edit');
        toast('🏛️ کانفیگ ویرایش شد ✓', 'ok');
        loadUsers();
    } catch(e) { toast('خطا در ویرایش: ' + e.message, 'err'); }
}

function openDeleteModal(uuid) {
    document.getElementById('delete-uuid').value = uuid;
    document.getElementById('delete-password').value = '';
    openModal('modal-delete');
}

async function confirmDelete() {
    const uuid = document.getElementById('delete-uuid').value;
    const password = document.getElementById('delete-password').value.trim();
    try {
        const r = await authF('/api/links/' + uuid, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ password })
        });
        if (!r.ok) {
            const err = await r.json().catch(() => ({}));
            if (r.status === 403) { toast('❌ رمز کانفیگ اشتباه است!', 'err'); }
            else { throw new Error(err.detail || 'خطا'); }
            return;
        }
        closeModal('modal-delete');
        toast('🏛️ کاربر حذف شد', 'ok');
        loadUsers();
    } catch(e) { toast('خطا در حذف: ' + e.message, 'err'); }
}

async function saveUser() {
  const label = document.getElementById('user-label').value.trim() || 'کاربر';
  const quota = parseFloat(document.getElementById('user-quota').value) || 2;
  const unit = document.getElementById('user-unit').value || 'GB';
  const exp = parseInt(document.getElementById('user-exp').value) || 0;
  const fingerprint = document.getElementById('user-fingerprint').value || 'chrome';
  const devices = parseInt(document.getElementById('user-devices').value) || 0;
  const protocol = document.getElementById('user-protocol').value || 'vless-ws';
  const password = document.getElementById('user-password').value.trim();
  const port = parseInt(document.getElementById('user-port').value) || 443;
  try {
    const r = await authF('/api/links', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        label, limit_value: quota, limit_unit: unit, expires_days: exp,
        fingerprint, max_devices: devices, protocol, note: '', password, port
      })
    });
    if (!r.ok) throw new Error();
    document.getElementById('user-label').value = '';
    document.getElementById('user-quota').value = '2';
    document.getElementById('user-unit').value = 'GB';
    document.getElementById('user-exp').value = '30';
    document.getElementById('user-fingerprint').value = 'chrome';
    document.getElementById('user-devices').value = '1';
    document.getElementById('user-protocol').value = 'vless-ws';
    document.getElementById('user-password').value = '';
    document.getElementById('user-port').value = '443';
    closeModal('modal-user');
    toast('🏛️ کانفیگ ساخته شد ✓', 'ok');
    loadUsers();
  } catch(e) { toast('خطا در ساخت', 'err'); }
}

async function resetUsage(uuid) {
  if (!confirm('مصرف این کاربر ریست شود؟')) return;
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ reset_usage: true })
    });
    if (!r.ok) throw new Error();
    toast('مصرف ریست شد ✓', 'ok');
    loadUsers();
  } catch(e) { toast('خطا', 'err'); }
}

async function loadConnections() {
  try {
    const r = await authF('/api/connections');
    const d = await r.json();
    const grid = document.getElementById('conns-grid');
    const count = d.count || 0;
    document.getElementById('conn-count').textContent = count + ' اتصال';
    if (!count) {
      grid.innerHTML = '<div class="empty"><i class="ti ti-plug-off"></i><p>هیچ اتصال فعالی وجود ندارد</p></div>';
      return;
    }
    grid.innerHTML = d.connections.map(c => {
      const secs = c.connected_at ? Math.max(0, Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000)) : 0;
      const dur = secs < 60 ? secs + ' ث' : secs < 3600 ? Math.floor(secs/60) + ' د' : Math.floor(secs/3600) + ' س';
      return `<div class="conn-card">
        <div class="ip"><span class="conn-status-dot"></span> ${esc(c.ip)}</div>
        <div class="label">${esc(c.label || 'نامشخص')}</div>
        <div class="conn-info">
          <span>📥 ${esc(c.bytes_fmt || '0 B')}</span>
          <span>⏱ ${dur}</span>
        </div>
      </div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

async function createBackup() {
  try {
    const r = await authF('/api/backup');
    const data = await r.json();
    const blob = new Blob([JSON.stringify(data, null, 2)], {type:'application/json'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `takht_backup_${new Date().toISOString().slice(0,10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    toast('✅ بکاپ با موفقیت دانلود شد', 'ok');
  } catch(e) { toast('خطا در بکاپ‌گیری', 'err'); }
}

async function restoreBackup(event) {
  const file = event.target.files[0];
  if (!file) return;
  try {
    const text = await file.text();
    const data = JSON.parse(text);
    const r = await authF('/api/backup/restore', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!r.ok) {
      const err = await r.json().catch(() => ({}));
      toast(err.detail || 'خطا در بازیابی', 'err');
      return;
    }
    toast('✅ بکاپ با موفقیت بازیابی شد', 'ok');
    setTimeout(() => location.reload(), 1500);
  } catch(e) { toast('خطا در بازیابی بکاپ: ' + e.message, 'err'); }
  event.target.value = '';
}

document.addEventListener('DOMContentLoaded', async () => {
  try {
    const r = await fetch('/api/me');
    const d = await r.json();
    if (!d.authenticated) location.href = '/login';
  } catch(e) { location.href = '/login'; }
  await loadRGBStatus();
  loadUsers();
  loadConnections();
  setInterval(() => {
    if (document.getElementById('pg-users').classList.contains('on')) loadUsers();
    if (document.getElementById('pg-connections').classList.contains('on')) loadConnections();
  }, 5000);
});
</script>
</body></html>"""

# ===== تابع ساب‌لینک حرفه‌ای (فقط دکمه کپی ساب با انیمیشن) =====
def get_sub_page_html(uuid: str, link: dict) -> str:
    from datetime import datetime
    from main import get_host, generate_vless_link
    
    used = link.get('used_bytes', 0)
    limit = link.get('limit_bytes', 0)
    active = link.get('active', True)
    expired = link.get('expired', False)
    label = link.get('label', 'کاربر')
    fingerprint = link.get('fingerprint', 'chrome')
    max_devices = link.get('max_devices', 0)
    protocol = link.get('protocol', 'vless-ws')
    ports = link.get('ports', [443])
    active_connections = link.get('active_connections', 0)
    active_connections_list = link.get('active_connections_list', [])
    sub_url = link.get('sub_url', '')
    
    host = get_host()
    vless_link = generate_vless_link(
        uuid, host, 
        remark=f"تخت جمشید-{label}",
        protocol=protocol,
        fingerprint=fingerprint,
        port=ports[0] if ports else 443
    )
    
    percent = 0
    if limit > 0:
        percent = min(100, (used / limit) * 100)
    
    expires_at = link.get('expires_at')
    remaining_seconds = 0
    if expires_at:
        try:
            exp_date = datetime.fromisoformat(expires_at.replace('Z', '+00:00'))
            now = datetime.now().astimezone()
            remaining_seconds = max(0, int((exp_date - now).total_seconds()))
            days_left = (exp_date - now).days
            if days_left < 0:
                days_left = 0
            days_left = f"{days_left} روز" if days_left > 0 else "منقضی"
        except:
            days_left = 'نامشخص'
    else:
        days_left = 'نامحدود'
    
    is_allowed = active and not expired
    
    def fmt_bytes(b):
        if not b or b == 0:
            return '0 B'
        if b < 1024:
            return f'{b} B'
        if b < 1024**2:
            return f'{b/1024:.1f} KB'
        if b < 1024**3:
            return f'{b/1024**2:.2f} MB'
        return f'{b/1024**3:.2f} GB'
    
    used_fmt = fmt_bytes(used)
    limit_fmt = 'نامحدود' if limit == 0 else fmt_bytes(limit)
    
    # ساخت اتصالات
    conns_html = ""
    if active_connections > 0:
        conns_html = f"""
        <div style="background:rgba(100,80,255,0.02);border:1px solid rgba(100,80,255,0.04);border-radius:12px;padding:12px 14px;margin:12px 0">
            <div style="display:flex;align-items:center;gap:6px;margin-bottom:8px;font-size:11px;color:#8888BB">
                <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:#34D399;animation:pulse 1.5s infinite"></span>
                <span style="font-weight:700;color:#34D399">{active_connections} دستگاه متصل</span>
            </div>
            <div style="display:flex;flex-wrap:wrap;gap:6px">
        """
        for conn in active_connections_list[:10]:
            ip = conn.get('ip', 'نامشخص')
            conns_html += f"""
                <span style="font-family:monospace;font-size:10px;background:rgba(100,80,255,0.04);border:1px solid rgba(100,80,255,0.04);padding:3px 10px;border-radius:6px;color:#8888BB">🔵 {ip}</span>
            """
        if len(active_connections_list) > 10:
            conns_html += f"""
                <span style="font-family:monospace;font-size:10px;background:rgba(100,80,255,0.02);padding:3px 10px;border-radius:6px;color:#555577">+{len(active_connections_list)-10} بیشتر</span>
            """
        conns_html += """
            </div>
        </div>
        """
    else:
        conns_html = f"""
        <div style="background:rgba(100,80,255,0.02);border:1px solid rgba(100,80,255,0.04);border-radius:12px;padding:10px 14px;margin:12px 0;text-align:center">
            <span style="font-size:11px;color:#555577">🔴 بدون اتصال فعال</span>
        </div>
        """
    
    # منوی تم‌ها برای ساب‌لینک
    theme_names = {
        'dark_fire':'🔥 آتشین تیره',
        'gold':'👑 طلایی تیره',
        'ocean':'🌊 آبی اقیانوسی تیره',
        'forest':'🌲 سبز جنگلی تیره',
        'ruby':'💎 بنفش یاقوتی تیره',
        'white_fire':'🔥 آتشین روشن',
        'white_gold':'👑 طلایی روشن',
        'white_ocean':'🌊 آبی اقیانوسی روشن',
        'white_forest':'🌲 سبز جنگلی روشن',
        'white_ruby':'💎 بنفش یاقوتی روشن'
    }
    theme_colors = {
        'dark_fire':'linear-gradient(135deg,#FF6B35,#FF4500)',
        'gold':'linear-gradient(135deg,#D4AF37,#F5D060)',
        'ocean':'linear-gradient(135deg,#0099CC,#33CCFF)',
        'forest':'linear-gradient(135deg,#2E8B57,#4CAF50)',
        'ruby':'linear-gradient(135deg,#9B2D6E,#C44A8A)',
        'white_fire':'linear-gradient(135deg,#F5E6E0,#E8D5CC)',
        'white_gold':'linear-gradient(135deg,#F5ECD7,#E8D5CC)',
        'white_ocean':'linear-gradient(135deg,#D4EEFF,#B8D8EE)',
        'white_forest':'linear-gradient(135deg,#D4F5D4,#B8E8B8)',
        'white_ruby':'linear-gradient(135deg,#F5D4E8,#E8C4D8)'
    }
    
    menu_items = ""
    for t in ['dark_fire','gold','ocean','forest','ruby','white_fire','white_gold','white_ocean','white_forest','white_ruby']:
        menu_items += f"""
        <div class="menu-item" data-theme="{t}" onclick="selectTheme('{t}')">
            <span class="dot" style="background:{theme_colors[t]}"></span>
            {theme_names[t]}
            <span class="check">✓</span>
        </div>
        """
    
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="dark_fire">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>🏛️ {label} · تخت جمشید</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#0a0a1a;--card:rgba(10,10,30,0.8);--card-border:rgba(100,80,255,0.06);
  --text:#F0EEFF;--text2:#8888BB;--text3:#555577;
  --accent:#7C6BFF;--accent2:#A78BFA;--accent3:#5B4BD9;
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-text:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-text:#F87171;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-text:#FCD34D;
  --shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(100,80,255,0.02);
  --transition:all 0.4s cubic-bezier(0.34,1.56,0.64,1);--radius:14px
}}
[data-theme="dark_fire"]{{--bg:#0a0a1a;--card:rgba(20,10,10,0.8);--card-border:rgba(255,100,50,0.06);--accent:#FF6B35;--accent2:#FF8C00;--text:#F0EEFF;--text2:#8A4A3A;--text3:#5A3A2A;--shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(255,80,20,0.02)}}
[data-theme="gold"]{{--bg:#1a1208;--card:rgba(30,20,10,0.8);--card-border:rgba(212,175,55,0.06);--accent:#D4AF37;--accent2:#F5D060;--text:#F5ECD7;--text2:#C4A35A;--text3:#8A7A4A;--shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(212,175,55,0.02)}}
[data-theme="ocean"]{{--bg:#0a1a2a;--card:rgba(10,25,45,0.8);--card-border:rgba(0,153,204,0.06);--accent:#0099CC;--accent2:#33CCFF;--text:#D4EEFF;--text2:#5AA8C8;--text3:#3A7A9A;--shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(0,153,204,0.02)}}
[data-theme="forest"]{{--bg:#081a0a;--card:rgba(10,30,12,0.8);--card-border:rgba(46,139,87,0.06);--accent:#2E8B57;--accent2:#4CAF50;--text:#D4F5D4;--text2:#5AA85A;--text3:#3A7A3A;--shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(46,139,87,0.02)}}
[data-theme="ruby"]{{--bg:#1a0a12;--card:rgba(30,10,20,0.8);--card-border:rgba(155,45,110,0.06);--accent:#9B2D6E;--accent2:#C44A8A;--text:#F5D4E8;--text2:#B05A8A;--text3:#8A4A6A;--shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(155,45,110,0.02)}}
[data-theme="white_fire"]{{--bg:#F5E6E0;--card:rgba(255,245,240,0.8);--card-border:rgba(200,80,40,0.06);--accent:#E05A2A;--accent2:#CC5500;--text:#2A0A05;--text2:#6A3A2A;--text3:#8A5A4A;--shadow:0 25px 80px rgba(0,0,0,0.08),0 0 120px rgba(200,80,40,0.02)}}
[data-theme="white_gold"]{{--bg:#F5ECD7;--card:rgba(255,248,235,0.8);--card-border:rgba(212,175,55,0.06);--accent:#D4AF37;--accent2:#C49A2A;--text:#2A1A05;--text2:#6A5A2A;--text3:#8A7A4A;--shadow:0 25px 80px rgba(0,0,0,0.08),0 0 120px rgba(212,175,55,0.02)}}
[data-theme="white_ocean"]{{--bg:#D4EEFF;--card:rgba(235,248,255,0.8);--card-border:rgba(0,153,204,0.06);--accent:#0099CC;--accent2:#0077AA;--text:#052A3A;--text2:#2A5A7A;--text3:#3A7A9A;--shadow:0 25px 80px rgba(0,0,0,0.08),0 0 120px rgba(0,153,204,0.02)}}
[data-theme="white_forest"]{{--bg:#D4F5D4;--card:rgba(235,248,235,0.8);--card-border:rgba(46,139,87,0.06);--accent:#2E8B57;--accent2:#1A6A3A;--text:#052A0A;--text2:#2A5A2A;--text3:#3A7A3A;--shadow:0 25px 80px rgba(0,0,0,0.08),0 0 120px rgba(46,139,87,0.02)}}
[data-theme="white_ruby"]{{--bg:#F5D4E8;--card:rgba(248,235,240,0.8);--card-border:rgba(155,45,110,0.06);--accent:#9B2D6E;--accent2:#C44A8A;--text:#2A051A;--text2:#6A2A4A;--text3:#8A4A6A;--shadow:0 25px 80px rgba(0,0,0,0.08),0 0 120px rgba(155,45,110,0.02)}}
body{{font-family:'Vazirmatn',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:16px;background:var(--bg);color:var(--text);transition:var(--transition);position:relative;overflow-x:hidden}}
.stars-container{{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}}
.star{{position:absolute;border-radius:50%;background:var(--text);animation:twinkle 4s ease-in-out infinite;opacity:0.15}}
@keyframes twinkle{{0%,100%{{opacity:0.1}}50%{{opacity:0.4}}}}
.glow-orb{{position:fixed;border-radius:50%;filter:blur(120px);z-index:0;pointer-events:none;animation:float 8s ease-in-out infinite}}
@keyframes float{{0%,100%{{transform:translate(0,0) scale(1)}}50%{{transform:translate(20px,-20px) scale(1.03)}}}}
.glow-orb1{{width:400px;height:400px;background:rgba(100,80,255,0.04);top:-100px;right:-50px}}
.glow-orb2{{width:300px;height:300px;background:rgba(167,139,250,0.03);bottom:-50px;left:-30px;animation-delay:3s}}

.theme-dropdown{{position:fixed;top:20px;left:50%;transform:translateX(-50%);z-index:100}}
.theme-dropdown .toggle-btn{{background:var(--card);backdrop-filter:blur(30px);border:1px solid var(--card-border);border-radius:14px;padding:10px 20px;color:var(--text);font-family:'Vazirmatn',sans-serif;font-size:13px;font-weight:600;cursor:pointer;display:flex;align-items:center;gap:10px;transition:var(--transition);box-shadow:0 8px 40px rgba(0,0,0,0.3)}}
.theme-dropdown .toggle-btn:hover{{border-color:var(--accent);transform:scale(1.02)}}
.theme-dropdown .toggle-btn .arrow{{transition:transform .3s;font-size:12px}}
.theme-dropdown .toggle-btn .arrow.open{{transform:rotate(180deg)}}
.theme-dropdown .menu{{display:none;position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%);background:var(--card);backdrop-filter:blur(30px);border:1px solid var(--card-border);border-radius:14px;padding:8px;min-width:200px;box-shadow:0 12px 50px rgba(0,0,0,0.4);max-height:400px;overflow-y:auto}}
.theme-dropdown .menu.open{{display:block}}
.theme-dropdown .menu-item{{display:flex;align-items:center;gap:10px;padding:8px 14px;border-radius:10px;cursor:pointer;transition:var(--transition);color:var(--text2);font-size:13px;font-weight:500}}
.theme-dropdown .menu-item:hover{{background:rgba(100,80,255,0.06);color:var(--text)}}
.theme-dropdown .menu-item .dot{{display:inline-block;width:18px;height:18px;border-radius:5px;flex-shrink:0;border:1px solid rgba(255,255,255,0.1)}}
.theme-dropdown .menu-item .check{{margin-right:auto;opacity:0;transition:opacity .2s;color:var(--accent)}}
.theme-dropdown .menu-item.active .check{{opacity:1}}
.theme-dropdown .menu-item.active{{background:rgba(100,80,255,0.06);color:var(--text)}}

.card{{position:relative;z-index:10;background:var(--card);backdrop-filter:blur(30px);border:1px solid var(--card-border);border-radius:var(--radius);padding:22px 20px 18px;max-width:420px;width:100%;box-shadow:var(--shadow);animation:cardIn 0.6s ease;transition:var(--transition);margin-top:60px}}
@keyframes cardIn{{from{{opacity:0;transform:translateY(30px) scale(0.96)}}to{{opacity:1;transform:translateY(0) scale(1)}}}}
.card-header{{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;padding-bottom:12px;border-bottom:1px solid var(--card-border)}}
.brand{{display:flex;align-items:center;gap:8px}}
.brand-icon{{width:32px;height:32px;border-radius:8px;background:linear-gradient(135deg,#7C6BFF,#5B4BD9);display:flex;align-items:center;justify-content:center;font-size:16px;box-shadow:0 0 30px rgba(100,80,255,0.15)}}
.brand-text{{font-size:11px;font-weight:700;background:linear-gradient(135deg,#A78BFA,#7C6BFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.brand-sub{{font-size:6px;color:var(--text3)}}
.user-row{{display:flex;align-items:center;justify-content:space-between;margin-bottom:2px}}
.user-name{{font-size:18px;font-weight:800;color:var(--text);display:flex;align-items:center;gap:6px}}
.status-badge{{display:inline-flex;align-items:center;gap:4px;padding:2px 10px;border-radius:12px;font-size:9px;font-weight:700}}
.status-badge.active{{background:var(--green-bg);color:var(--green-text);border:1px solid rgba(16,185,129,0.1)}}
.status-badge.inactive{{background:var(--red-bg);color:var(--red-text);border:1px solid rgba(239,68,68,0.1)}}
.uuid-box{{background:rgba(100,80,255,0.03);border:1px solid var(--card-border);border-radius:6px;padding:4px 8px;font-size:8px;font-family:monospace;color:var(--text3);word-break:break-all;cursor:pointer;transition:var(--transition);margin:4px 0 8px;text-align:center}}
.uuid-box:hover{{background:rgba(100,80,255,0.06);transform:scale(1.01)}}
.info-grid{{display:grid;grid-template-columns:1fr 1fr;gap:4px;margin:6px 0}}
.info-item{{background:rgba(100,80,255,0.02);border:1px solid var(--card-border);border-radius:6px;padding:5px 8px;display:flex;justify-content:space-between;align-items:center;transition:var(--transition)}}
.info-item:hover{{background:rgba(100,80,255,0.04)}}
.info-label{{font-size:7px;color:var(--text3);display:flex;align-items:center;gap:2px;font-weight:600}}
.info-label i{{font-size:8px;color:var(--accent)}}
.info-value{{font-size:10px;font-weight:700;color:var(--text)}}
.info-value.small{{font-size:8px}}
.timer-section{{background:linear-gradient(135deg,rgba(100,80,255,0.04),rgba(167,139,250,0.02));border:1px solid var(--card-border);border-radius:8px;padding:6px 10px;margin:6px 0;text-align:center}}
.timer-label{{font-size:7px;color:var(--text3);font-weight:600;text-transform:uppercase;letter-spacing:0.05em}}
.timer-display{{font-family:monospace;font-size:18px;font-weight:800;color:var(--accent2);letter-spacing:2px;background:rgba(0,0,0,0.2);padding:4px 10px;border-radius:6px;display:inline-block;margin-top:2px}}
.timer-display.expired{{color:var(--red-text)}}
.progress-section{{margin:6px 0}}
.progress-bar{{height:4px;border-radius:4px;background:rgba(100,80,255,0.05);overflow:hidden}}
.progress-fill{{height:100%;border-radius:4px;background:linear-gradient(90deg,#7C6BFF,#5B4BD9,#A78BFA);width:0%;transition:width 1.2s ease}}
.progress-text{{display:flex;justify-content:space-between;font-size:7px;color:var(--text3);margin-top:2px}}
.progress-text .pct{{font-weight:700;color:var(--text2)}}
.vless-section{{background:rgba(100,80,255,0.02);border:1px solid var(--card-border);border-radius:8px;padding:6px 8px;margin:6px 0}}
.vless-label{{font-size:7px;font-weight:700;color:var(--text3);text-transform:uppercase;letter-spacing:0.04em;display:flex;align-items:center;gap:4px;margin-bottom:3px}}
.vless-label i{{color:var(--accent);font-size:9px}}
.vless-link{{font-family:monospace;font-size:7px;color:var(--accent2);word-break:break-all;line-height:1.6;background:rgba(0,0,0,0.15);padding:4px 6px;border-radius:4px;border:1px solid var(--card-border)}}
.actions{{display:flex;gap:4px;margin-top:8px;flex-wrap:wrap}}
.btn{{font-family:inherit;font-size:9px;font-weight:600;border-radius:6px;padding:5px 10px;cursor:pointer;display:inline-flex;align-items:center;gap:3px;border:none;transition:var(--transition);white-space:nowrap;flex:1;justify-content:center}}
.btn i{{font-size:10px}}
.btn-success{{background:var(--green-bg);border:1px solid rgba(16,185,129,0.08);color:var(--green-text)}}
.btn-success:hover{{background:rgba(16,185,129,0.12);transform:translateY(-2px)}}
@keyframes copyAnim{{0%{{transform:scale(1)}}30%{{transform:scale(0.85)}}60%{{transform:scale(1.1)}}100%{{transform:scale(1)}}}}
.btn-success.copy-anim{{animation:copyAnim 0.5s ease}}
.btn-secondary{{background:rgba(100,80,255,0.03);border:1px solid var(--card-border);color:var(--text2)}}
.btn-secondary:hover{{background:rgba(100,80,255,0.06);color:var(--text);transform:translateY(-2px)}}
.footer{{margin-top:10px;padding-top:8px;border-top:1px solid var(--card-border);text-align:center;font-size:6px;color:var(--text3)}}
.footer .eagle{{color:var(--accent);font-weight:700}}
.toast{{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-border);color:var(--text);border-radius:8px;padding:6px 14px;font-size:9px;opacity:0;transition:var(--transition);z-index:999;pointer-events:none;box-shadow:var(--shadow);display:flex;align-items:center;gap:4px}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(16,185,129,0.15);color:var(--green-text)}}
@media(max-width:400px){{.card{{padding:14px 12px 12px;margin-top:70px}}.user-name{{font-size:15px}}.info-grid{{grid-template-columns:1fr 1fr}}.info-item{{padding:3px 6px}}.info-value{{font-size:8px}}.btn{{font-size:8px;padding:4px 8px}}.timer-display{{font-size:14px}}.theme-dropdown .toggle-btn{{padding:8px 14px;font-size:12px}}.theme-dropdown .menu{{min-width:170px}}}}
</style>
</head>
<body>
<div class="stars-container">
    <div class="star" style="width:2px;height:2px;top:8%;left:6%;animation-delay:0s"></div>
    <div class="star" style="width:3px;height:3px;top:25%;left:35%;animation-delay:1.5s"></div>
    <div class="star" style="width:1px;height:1px;top:45%;left:65%;animation-delay:0.8s"></div>
    <div class="star" style="width:2px;height:2px;top:65%;left:15%;animation-delay:2.2s"></div>
    <div class="star" style="width:3px;height:3px;top:80%;left:75%;animation-delay:0.5s"></div>
    <div class="star" style="width:1px;height:1px;top:35%;left:85%;animation-delay:1.8s"></div>
    <div class="star" style="width:2px;height:2px;top:55%;left:45%;animation-delay:2.5s"></div>
</div>
<div class="glow-orb glow-orb1"></div>
<div class="glow-orb glow-orb2"></div>
<div class="toast" id="toast"></div>

<div class="theme-dropdown">
    <button class="toggle-btn" onclick="toggleThemeMenu()">
        <span>🎨</span>
        <span id="themeDisplay">انتخاب تم</span>
        <span class="arrow" id="themeArrow">▾</span>
    </button>
    <div class="menu" id="themeMenu">
        {menu_items}
    </div>
</div>

<div class="card" id="mainCard">
    <div class="card-header">
        <div class="brand"><div class="brand-icon">🏛️</div><div><div class="brand-text">تخت جمشید</div><div class="brand-sub">اشتراک ویژه</div></div></div>
        <button class="theme-toggle" onclick="toggleTheme()" id="themeBtn">🌙</button>
    </div>

    <div class="user-row">
        <div class="user-name"><span>🏛️</span> {label}</div>
        <span class="status-badge {'active' if is_allowed else 'inactive'}">
            <i class="ti {'ti-circle-check' if is_allowed else 'ti-circle-x'}"></i>
            {'فعال' if is_allowed else 'غیرفعال'}
        </span>
    </div>
    <div class="uuid-box" onclick="copyUUID()">🔑 {uuid}</div>

    {conns_html}

    <div class="info-grid">
        <div class="info-item"><span class="info-label"><i class="ti ti-database"></i> مصرف</span><span class="info-value used">{used_fmt}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-package"></i> سهمیه</span><span class="info-value">{limit_fmt}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-devices"></i> دستگاه</span><span class="info-value">{str(max_devices) if max_devices > 0 else '∞'}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-fingerprint"></i> FP</span><span class="info-value small">{fingerprint}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-settings"></i> پروتکل</span><span class="info-value small">{protocol}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-plug"></i> پورت‌ها</span><span class="info-value small">{', '.join(str(p) for p in ports[:3])}{' +' + str(len(ports)-3) if len(ports)>3 else ''}</span></div>
    </div>

    <div class="timer-section">
        <div class="timer-label">⏱ زمان باقیمانده</div>
        <div class="timer-display" id="timerDisplay">{days_left}</div>
    </div>

    <div class="progress-section">
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
        <div class="progress-text"><span>میزان مصرف</span><span class="pct">{percent:.1f}%</span></div>
    </div>

    <div class="vless-section">
        <div class="vless-label"><i class="ti ti-link"></i> لینک کانفیگ</div>
        <div class="vless-link" id="vlessLink">{vless_link}</div>
    </div>

    <div class="actions">
        <button class="btn btn-success" onclick="copySub()" id="copySubBtn"><i class="ti ti-link"></i> کپی ساب‌لینک</button>
    </div>

    <div class="footer"><span class="eagle">🏛️</span> تخت جمشید · نسخه ۱۰</div>
</div>

<script>
// ===== داده‌ها =====
const subUrl = `{sub_url}`;
const uuid = `{uuid}`;
const remainingSeconds = {remaining_seconds};
const isExpired = {str(not is_allowed).lower()};

// ===== توابع عمومی =====
function toast(msg, type) {{
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.className = 'toast show' + (type ? ' ' + type : '');
    clearTimeout(t._timeout);
    t._timeout = setTimeout(() => t.classList.remove('show'), 2000);
}}

function copySub() {{
    const btn = document.getElementById('copySubBtn');
    navigator.clipboard.writeText(subUrl).then(() => {{
        toast('✅ ساب‌لینک کپی شد!', 'ok');
        btn.classList.add('copy-anim');
        btn.innerHTML = '<i class="ti ti-check"></i> کپی شد!';
        setTimeout(() => {{
            btn.classList.remove('copy-anim');
            btn.innerHTML = '<i class="ti ti-link"></i> کپی ساب‌لینک';
        }}, 1500);
    }}).catch(() => toast('❌ خطا در کپی', 'err'));
}}

function copyUUID() {{
    navigator.clipboard.writeText(uuid).then(() => toast('✅ کپی شد', 'ok'));
}}

// ===== مدیریت تم =====
let currentTheme = localStorage.getItem('takht-sub-theme') || 'dark_fire';
const themeList = ['dark_fire','gold','ocean','forest','ruby','white_fire','white_gold','white_ocean','white_forest','white_ruby'];
const themeNames = {{
    'dark_fire':'🔥 آتشین تیره',
    'gold':'👑 طلایی تیره',
    'ocean':'🌊 آبی اقیانوسی تیره',
    'forest':'🌲 سبز جنگلی تیره',
    'ruby':'💎 بنفش یاقوتی تیره',
    'white_fire':'🔥 آتشین روشن',
    'white_gold':'👑 طلایی روشن',
    'white_ocean':'🌊 آبی اقیانوسی روشن',
    'white_forest':'🌲 سبز جنگلی روشن',
    'white_ruby':'💎 بنفش یاقوتی روشن'
}};

function applyTheme(theme) {{
    currentTheme = theme;
    localStorage.setItem('takht-sub-theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
    document.getElementById('themeDisplay').textContent = themeNames[theme] || 'انتخاب تم';
    document.querySelectorAll('.theme-dropdown .menu-item').forEach(el => {{
        el.classList.toggle('active', el.dataset.theme === theme);
    }});
    document.getElementById('themeMenu').classList.remove('open');
    document.getElementById('themeArrow').classList.remove('open');
    document.getElementById('themeBtn').textContent = theme.startsWith('white_') ? '🌙' : '☀️';
}}

function toggleThemeMenu() {{
    const menu = document.getElementById('themeMenu');
    const arrow = document.getElementById('themeArrow');
    menu.classList.toggle('open');
    arrow.classList.toggle('open');
}}

function selectTheme(theme) {{
    applyTheme(theme);
    toast('✅ ' + themeNames[theme], 'ok');
}}

function toggleTheme() {{
    const current = currentTheme;
    const idx = themeList.indexOf(current);
    const next = themeList[(idx + 1) % themeList.length];
    selectTheme(next);
}}

document.addEventListener('click', function(e) {{
    const dropdown = document.querySelector('.theme-dropdown');
    if (dropdown && !dropdown.contains(e.target)) {{
        document.getElementById('themeMenu').classList.remove('open');
        document.getElementById('themeArrow').classList.remove('open');
    }}
}});

applyTheme(currentTheme);

// ===== تایمر زنده =====
function formatTime(seconds) {{
    if (seconds <= 0) return '⏰ منقضی شد';
    const days = Math.floor(seconds / 86400);
    const hours = Math.floor((seconds % 86400) / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    if (days > 0) {{
        return days + 'd ' + String(hours).padStart(2, '0') + 'h ' + String(mins).padStart(2, '0') + 'm';
    }}
    return String(hours).padStart(2, '0') + ':' + String(mins).padStart(2, '0') + ':' + String(secs).padStart(2, '0');
}}

function updateTimer() {{
    const el = document.getElementById('timerDisplay');
    if (isExpired) {{
        el.textContent = '⏰ منقضی شد';
        el.className = 'timer-display expired';
        return;
    }}
    if (remainingSeconds <= 0) {{
        el.textContent = '♾️ نامحدود';
        el.className = 'timer-display';
        return;
    }}
    const elapsed = Math.floor(Date.now() / 1000) - startTime;
    const remaining = Math.max(0, remainingSeconds - elapsed);
    el.textContent = formatTime(remaining);
    if (remaining === 0) {{
        el.className = 'timer-display expired';
        el.textContent = '⏰ منقضی شد';
    }}
}}

const startTime = Math.floor(Date.now() / 1000);
if (remainingSeconds > 0 && !isExpired) {{
    updateTimer();
    setInterval(updateTimer, 1000);
}} else if (isExpired) {{
    document.getElementById('timerDisplay').textContent = '⏰ منقضی شد';
    document.getElementById('timerDisplay').className = 'timer-display expired';
}}

setTimeout(() => {{
    const fill = document.getElementById('progressFill');
    if (fill) fill.style.width = '{percent:.1f}%';
}}, 100);
</script>
</body></html>"""
