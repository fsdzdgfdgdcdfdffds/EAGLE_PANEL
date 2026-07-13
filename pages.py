LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🪐 ورود · پنل عقاب</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0a0a1a;
  --card:rgba(10,10,30,0.75);
  --card-b:rgba(100,80,255,0.12);
  --accent:#7C6BFF;
  --accent2:#A78BFA;
  --accent3:#5B4BD9;
  --t1:#F0EEFF;
  --t2:#8888BB;
  --t3:#555577;
  --border:rgba(100,80,255,0.08);
  --glow:0 0 80px rgba(100,80,255,0.05);
}
body{font-family:'Vazirmatn',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0a0a1a,#1a0a2a,#0a0a2a);padding:20px;color:var(--t1);position:relative;overflow:hidden}
.stars{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.star{position:absolute;border-radius:50%;background:#fff;animation:twinkle 3s ease-in-out infinite}
@keyframes twinkle{0%,100%{opacity:0.2}50%{opacity:0.8}}
.glow-orb{position:fixed;border-radius:50%;filter:blur(150px);z-index:0;animation:orbFloat 6s ease-in-out infinite;pointer-events:none}
.orb1{width:500px;height:500px;background:rgba(100,80,255,0.05);top:-200px;right:-100px}
.orb2{width:400px;height:400px;background:rgba(167,139,250,0.04);bottom:-100px;left:-80px;animation-delay:2s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(30px,-30px) scale(1.1)}}
.container{position:relative;z-index:10;display:grid;grid-template-columns:1fr 1fr;max-width:1100px;width:100%;background:var(--card);backdrop-filter:blur(30px);border-radius:24px;border:1px solid var(--border);overflow:hidden;box-shadow:var(--glow),0 25px 80px rgba(0,0,0,0.6)}
.login-section{padding:48px 40px}
.brand{display:flex;align-items:center;gap:12px;margin-bottom:32px}
.brand-icon{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,#7C6BFF,#5B4BD9,#A78BFA);display:flex;align-items:center;justify-content:center;font-size:22px;box-shadow:0 0 40px rgba(100,80,255,0.2)}
.brand-text{font-size:16px;font-weight:800;background:linear-gradient(135deg,#A78BFA,#7C6BFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.brand-sub{font-size:9px;color:var(--t3);margin-top:0px;-webkit-text-fill-color:var(--t3)}
.welcome{font-size:22px;font-weight:800;color:var(--t1);margin-bottom:4px}
.sub-text{font-size:13px;color:var(--t3);margin-bottom:28px}
.field{margin-bottom:18px}
.field label{display:block;font-size:10px;font-weight:600;color:var(--t2);margin-bottom:4px}
.field input{width:100%;padding:12px 14px;border-radius:10px;border:1px solid var(--border);background:rgba(0,0,20,.3);color:var(--t1);font-family:inherit;font-size:14px;outline:none;transition:.3s}
.field input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(100,80,255,.08),0 0 30px rgba(100,80,255,.04)}
.field input::placeholder{color:var(--t3)}
.options{display:flex;justify-content:space-between;align-items:center;margin:14px 0 20px;font-size:12px}
.options label{display:flex;align-items:center;gap:6px;color:var(--t2);cursor:pointer}
.options label input[type="checkbox"]{accent-color:var(--accent);width:16px;height:16px;cursor:pointer}
.btn-login{width:100%;padding:12px;border-radius:10px;border:none;cursor:pointer;background:linear-gradient(135deg,#7C6BFF,#5B4BD9,#A78BFA);background-size:200% 200%;animation:gradientMove 4s ease infinite;color:#fff;font-family:inherit;font-size:15px;font-weight:700;transition:all .3s;box-shadow:0 4px 30px rgba(100,80,255,.25)}
@keyframes gradientMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-login:hover{transform:translateY(-2px);box-shadow:0 8px 40px rgba(100,80,255,.35)}
.btn-login:disabled{opacity:.5;cursor:not-allowed;transform:none}
.or-divider{display:flex;align-items:center;gap:14px;margin:20px 0;color:var(--t3);font-size:11px}
.or-divider::before,.or-divider::after{content:'';flex:1;height:1px;background:var(--border)}
.connect-btn{width:100%;padding:12px;border-radius:10px;border:1px solid var(--border);background:rgba(100,80,255,0.03);color:var(--t1);font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;transition:.3s;display:flex;align-items:center;justify-content:center;gap:8px}
.connect-btn:hover{background:rgba(100,80,255,0.06);border-color:rgba(100,80,255,0.2)}
.signup-text{text-align:center;margin-top:18px;font-size:12px;color:var(--t3)}
.signup-text a{color:var(--accent);text-decoration:none;font-weight:600}
.signup-text a:hover{text-decoration:underline}
.error-box{display:none;background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.15);border-radius:8px;padding:10px 12px;margin-bottom:14px;font-size:12px;color:#F87171;align-items:center;gap:8px}
.error-box.show{display:flex}
.info-section{background:linear-gradient(135deg,#0a0a1a,#1a0a2a);padding:48px 36px;display:flex;flex-direction:column;justify-content:center;border-right:1px solid var(--border)}
.info-title{font-size:22px;font-weight:800;color:var(--t1);margin-bottom:6px}
.info-sub{font-size:13px;color:var(--t3);margin-bottom:24px}
.features{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.feature{background:rgba(100,80,255,0.03);border-radius:12px;padding:14px 12px;text-align:center;border:1px solid rgba(100,80,255,0.04)}
.feature .icon{font-size:28px;display:block;margin-bottom:4px}
.feature .name{font-size:11px;font-weight:600;color:var(--t1)}
.feature .desc{font-size:8px;color:var(--t3);margin-top:2px}
.lang-toggle{position:fixed;top:20px;left:20px;z-index:50;display:flex;gap:6px;background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--border);border-radius:10px;padding:4px}
.lang-toggle button{background:none;border:none;color:var(--t3);font-family:inherit;font-size:11px;font-weight:600;padding:4px 10px;border-radius:6px;cursor:pointer;transition:.3s}
.lang-toggle button.active{background:linear-gradient(135deg,#7C6BFF,#5B4BD9);color:#fff}
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
        <div class="brand">
            <div class="brand-icon">🪐</div>
            <div>
                <div class="brand-text">پنل عقاب</div>
                <div class="brand-sub">مدیریت کاربران</div>
            </div>
        </div>
        <div class="welcome" id="welcome-text">خوش آمدید</div>
        <div class="sub-text" id="sub-text">وارد حساب کاربری خود شوید</div>
        
        <div class="error-box" id="error-box"><i class="ti ti-alert-circle"></i><span id="error-text"></span></div>
        
        <form id="login-form" onsubmit="handleLogin(event)">
            <div class="field">
                <label id="label-username">نام کاربری یا ایمیل</label>
                <input type="text" id="username" placeholder="نام کاربری" value="admin" dir="ltr">
            </div>
            <div class="field">
                <label id="label-password">رمز عبور</label>
                <input type="password" id="password" placeholder="رمز عبور را وارد کنید" dir="ltr">
            </div>
            <div class="options">
                <label><input type="checkbox" id="remember"> <span id="remember-text">مرا به خاطر بسپار</span></label>
            </div>
            <button class="btn-login" type="submit" id="login-btn"><i class="ti ti-login-2"></i> <span id="login-text">ورود</span></button>
        </form>
        
        <div class="or-divider"><span id="or-text">یا</span></div>
        
        <button class="connect-btn" onclick="quickConnect()">
            <i class="ti ti-plug"></i> <span id="connect-text">اتصال با یک کلیک</span>
        </button>
        
        <div class="signup-text" id="signup-text">
            حساب کاربری ندارید؟ <a href="/dashboard">ثبت نام</a>
        </div>
    </div>
    
    <div class="info-section">
        <div class="info-title" id="info-title">🪐 پنل عقاب</div>
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
const translations = {
    fa: {
        welcome: "خوش آمدید",
        sub: "وارد حساب کاربری خود شوید",
        username: "نام کاربری یا ایمیل",
        password: "رمز عبور",
        remember: "مرا به خاطر بسپار",
        login: "ورود",
        or: "یا",
        connect: "اتصال با یک کلیک",
        signup: "حساب کاربری ندارید؟",
        signup_link: "ثبت نام",
        secure: "امن",
        secure_d: "حریم خصوصی شما",
        fast: "سریع",
        fast_d: "سرعت برق آسا",
        global: "جهانی",
        global_d: "سرورهای جهانی",
        anon: "ناشناس",
        anon_d: "خصوصی بمانید",
        info_title: "🪐 پنل عقاب",
        info_sub: "سریع‌ترین و امن‌ترین اتصال"
    },
    en: {
        welcome: "Welcome Back",
        sub: "Login to your VPN account",
        username: "Username or Email",
        password: "Password",
        remember: "Remember me",
        login: "Login",
        or: "OR",
        connect: "Connect with One Click",
        signup: "Don't have an account?",
        signup_link: "Sign up",
        secure: "Secure",
        secure_d: "Your Privacy",
        fast: "Fast",
        fast_d: "Lightning Speed",
        global: "Global",
        global_d: "Worldwide Servers",
        anon: "Anonymous",
        anon_d: "Stay Private",
        info_title: "🪐 Eagle Panel",
        info_sub: "Fastest & Most Secure Connection"
    }
};

let currentLang = localStorage.getItem('eagle-lang') || 'fa';

function setLang(lang) {
    currentLang = lang;
    localStorage.setItem('eagle-lang', lang);
    document.querySelectorAll('.lang-toggle button').forEach(b => b.classList.toggle('active', b.textContent.includes(lang === 'fa' ? 'فارسی' : 'English')));
    updateTexts();
}

function updateTexts() {
    const t = translations[currentLang];
    document.getElementById('welcome-text').textContent = t.welcome;
    document.getElementById('sub-text').textContent = t.sub;
    document.getElementById('label-username').textContent = t.username;
    document.getElementById('label-password').textContent = t.password;
    document.getElementById('remember-text').textContent = t.remember;
    document.getElementById('login-text').textContent = t.login;
    document.getElementById('or-text').textContent = t.or;
    document.getElementById('connect-text').textContent = t.connect;
    document.getElementById('signup-text').innerHTML = t.signup + ' <a href="/dashboard">' + t.signup_link + '</a>';
    document.getElementById('f-secure').textContent = t.secure;
    document.getElementById('f-secure-d').textContent = t.secure_d;
    document.getElementById('f-fast').textContent = t.fast;
    document.getElementById('f-fast-d').textContent = t.fast_d;
    document.getElementById('f-global').textContent = t.global;
    document.getElementById('f-global-d').textContent = t.global_d;
    document.getElementById('f-anon').textContent = t.anon;
    document.getElementById('f-anon-d').textContent = t.anon_d;
    document.getElementById('info-title').textContent = t.info_title;
    document.getElementById('info-sub').textContent = t.info_sub;
}

async function handleLogin(e) {
    e.preventDefault();
    const btn = document.getElementById('login-btn');
    const err = document.getElementById('error-box');
    const errText = document.getElementById('error-text');
    
    err.classList.remove('show');
    btn.disabled = true;
    btn.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
    
    try {
        const r = await fetch('/api/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                password: document.getElementById('password').value,
                remember: document.getElementById('remember').checked
            })
        });
        
        if (!r.ok) {
            const d = await r.json().catch(() => ({}));
            errText.textContent = d.detail || 'رمز عبور اشتباه است';
            err.classList.add('show');
            btn.disabled = false;
            btn.innerHTML = '<i class="ti ti-login-2"></i> ' + translations[currentLang].login;
            return;
        }
        
        window.location.href = '/dashboard';
    } catch(e) {
        errText.textContent = 'خطا در ارتباط با سرور';
        err.classList.add('show');
        btn.disabled = false;
        btn.innerHTML = '<i class="ti ti-login-2"></i> ' + translations[currentLang].login;
    }
}

function quickConnect() {
    document.getElementById('password').value = '123456';
    document.getElementById('remember').checked = true;
    document.getElementById('login-form').dispatchEvent(new Event('submit'));
}

document.getElementById('password').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') document.getElementById('login-form').dispatchEvent(new Event('submit'));
});

setLang(currentLang);
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🪐 پنل عقاب · خانه</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0a0a1a;
  --bg2:#12122a;
  --bg3:#1a1a3a;
  --card:rgba(10,10,30,0.7);
  --card-b:rgba(100,80,255,0.08);
  --card-bh:rgba(100,80,255,0.15);
  --accent:#7C6BFF;
  --accent2:#A78BFA;
  --accent3:#5B4BD9;
  --green:#10B981;
  --green-bg:rgba(16,185,129,0.08);
  --green-t:#34D399;
  --red:#EF4444;
  --red-bg:rgba(239,68,68,0.08);
  --red-t:#F87171;
  --amber:#F59E0B;
  --amber-bg:rgba(245,158,11,0.08);
  --amber-t:#FCD34D;
  --t1:#F0EEFF;
  --t2:#8888BB;
  --t3:#555577;
  --sidebar-w:180px;
  --radius:12px;
  --shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(100,80,255,0.02);
}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:13px;position:relative;overflow-x:hidden;transition:background .4s,color .4s}
.stars-bg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.star-bg{position:absolute;border-radius:50%;background:#fff;animation:twinkleBg 4s ease-in-out infinite}
@keyframes twinkleBg{0%,100%{opacity:0.1}50%{opacity:0.4}}
.glow-main{position:fixed;border-radius:50%;filter:blur(200px);z-index:0;pointer-events:none}
.glow-left{width:600px;height:600px;background:rgba(100,80,255,0.02);top:-300px;left:-200px;animation:glowFloat 8s ease-in-out infinite}
.glow-right{width:500px;height:500px;background:rgba(167,139,250,0.02);bottom:-200px;right:-100px;animation:glowFloat 10s ease-in-out infinite reverse}
@keyframes glowFloat{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(50px,-30px) scale(1.1)}}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--card);backdrop-filter:blur(30px);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .4s cubic-bezier(0.34, 1.56, 0.64, 1),background .4s;box-shadow:var(--shadow)}
.logo{display:flex;align-items:center;gap:10px;padding:16px 12px 12px;border-bottom:1px solid var(--card-b)}
.logo-icon{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,#7C6BFF,#5B4BD9,#A78BFA);display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;box-shadow:0 0 30px rgba(100,80,255,0.15);animation:pulseLogo 3s ease-in-out infinite}
@keyframes pulseLogo{0%,100%{box-shadow:0 0 30px rgba(100,80,255,0.15)}50%{box-shadow:0 0 50px rgba(100,80,255,0.25)}}
.logo-name{font-size:13px;font-weight:800;background:linear-gradient(135deg,#A78BFA,#7C6BFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.logo-sub{font-size:7px;color:var(--t3);margin-top:0px}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0;position:relative;z-index:1}
.nav-it{display:flex;align-items:center;gap:8px;padding:8px 10px;color:var(--t3);font-size:11px;cursor:pointer;border-right:2px solid transparent;transition:all .3s cubic-bezier(0.34, 1.56, 0.64, 1);margin:1px 4px;border-radius:6px}
.nav-it i{font-size:14px;width:18px;text-align:center;flex-shrink:0;transition:transform .3s}
.nav-it:hover{background:rgba(100,80,255,0.05);color:var(--t2)}
.nav-it:hover i{transform:scale(1.1)}
.nav-it.on{background:rgba(100,80,255,0.08);color:var(--t1);border-right-color:var(--accent);font-weight:600;box-shadow:0 0 30px rgba(100,80,255,0.03)}
.nav-it.on i{color:var(--accent)}
.sb-foot{padding:10px 12px;border-top:1px solid var(--card-b)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:6px;background:var(--red-bg);color:var(--red-t);border-radius:6px;padding:6px;font-size:10px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.1);cursor:pointer;width:100%;transition:.3s}
.logout-btn:hover{background:rgba(239,68,68,0.15);transform:scale(1.02)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:48px;background:var(--card);backdrop-filter:blur(30px);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 10px;transition:background .4s}
.mob-top .ml{display:flex;align-items:center;gap:6px}
.mob-logo{width:26px;height:26px;border-radius:6px;background:linear-gradient(135deg,#7C6BFF,#5B4BD9);display:flex;align-items:center;justify-content:center;font-size:13px}
.mob-title{color:var(--t1);font-size:11px;font-weight:700}
.menu-btn{background:rgba(100,80,255,0.05);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:6px;font-size:14px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.3s}
.menu-btn:hover{background:rgba(100,80,255,0.1);transform:scale(1.05)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:190;backdrop-filter:blur(6px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:16px 20px 80px;min-width:0;transition:margin .4s;position:relative;z-index:1}
.pg{display:none;animation:pageIn .4s cubic-bezier(0.34, 1.56, 0.64, 1)}
.pg.on{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(20px) scale(0.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.topbar{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px}
.tb-title{font-size:17px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.tb-title i{color:var(--accent);font-size:19px;animation:titleIcon 3s ease-in-out infinite}
@keyframes titleIcon{0%,100%{transform:rotate(0deg)}50%{transform:rotate(-5deg)}}
.tb-sub{font-size:10px;color:var(--t3);margin-top:1px}
.tb-right{display:flex;align-items:center;gap:5px;flex-wrap:wrap}
.badge{font-size:8px;padding:2px 8px;border-radius:12px;font-weight:700;display:inline-flex;align-items:center;gap:3px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:rgba(100,80,255,0.1);color:var(--accent)}
.bg-fire{background:rgba(100,80,255,0.08);color:#A78BFA}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.dot{width:5px;height:5px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green);animation:dotPulse 1.5s ease-in-out infinite}
.dr{background:var(--red);animation:dotPulse 1.8s ease-in-out infinite}
.da{background:var(--amber);animation:dotPulse 2s ease-in-out infinite}
.db{background:var(--accent);animation:dotPulse 1.2s ease-in-out infinite}
@keyframes dotPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.7)}}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.stats-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-bottom:16px}
.stat-card{background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:12px 8px;transition:all .4s cubic-bezier(0.34, 1.56, 0.64, 1);text-align:center;position:relative;overflow:hidden}
.stat-card::before{content:'';position:absolute;top:-50%;right:-50%;width:100px;height:100px;background:radial-gradient(circle,rgba(100,80,255,0.03),transparent 70%);pointer-events:none}
.stat-card:hover{border-color:var(--card-bh);transform:translateY(-4px) scale(1.02);box-shadow:var(--shadow)}
.stat-card .icon{font-size:18px;margin-bottom:3px;display:block}
.stat-card .number{font-size:18px;font-weight:800;color:var(--t1);line-height:1.2}
.stat-card .number.small{font-size:13px}
.stat-card .label{font-size:9px;color:var(--t3);margin-top:2px;font-weight:500}
.stat-card .sub{font-size:7px;color:var(--t3);margin-top:0px;opacity:.6}

/* ===== استایل جدید کاربران ===== */
.stat-mini {
  background:var(--card);
  border:1px solid var(--card-b);
  border-radius:8px;
  padding:8px 12px;
  display:flex;
  align-items:center;
  gap:8px;
  transition:all .3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.stat-mini:hover{transform:translateY(-2px);border-color:var(--card-bh)}
.stat-mini-icon { font-size:16px; }
.stat-mini-num { font-size:16px; font-weight:800; color:var(--t1); }
.stat-mini-label { font-size:9px; color:var(--t3); }

.users-table {
  width:100%;
  border-collapse:collapse;
  font-size:12px;
}
.users-table thead th {
  padding:10px 12px;
  text-align:right;
  color:var(--t2);
  font-size:9px;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:.04em;
  border-bottom:1px solid var(--card-b);
  background:rgba(100,80,255,0.02);
}
.users-table tbody td {
  padding:8px 12px;
  border-bottom:1px solid var(--card-b);
  color:var(--t1);
  vertical-align:middle;
}
.users-table tbody tr {
  transition:background .3s;
}
.users-table tbody tr:hover {
  background:rgba(100,80,255,0.02);
}
.users-table .status-badge {
  display:inline-flex;
  align-items:center;
  gap:5px;
  padding:2px 10px;
  border-radius:12px;
  font-size:9px;
  font-weight:700;
}
.users-table .status-badge .status-dot {
  width:6px;
  height:6px;
  border-radius:50%;
  display:inline-block;
  animation:statusPulse 1.5s ease-in-out infinite;
}
.users-table .status-badge.active .status-dot { background:var(--green-t); }
.users-table .status-badge.expired .status-dot { background:var(--red-t); }
.users-table .status-badge.disabled .status-dot { background:var(--amber-t); }
@keyframes statusPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.6)}}
.users-table .status-badge.active { background:var(--green-bg); color:var(--green-t); }
.users-table .status-badge.expired { background:var(--red-bg); color:var(--red-t); }
.users-table .status-badge.disabled { background:var(--amber-bg); color:var(--amber-t); }
.users-table .usage-bar {
  display:flex;
  align-items:center;
  gap:6px;
}
.users-table .usage-bar .bar {
  width:80px;
  height:3px;
  border-radius:3px;
  background:rgba(100,80,255,0.05);
  overflow:hidden;
}
.users-table .usage-bar .bar .fill {
  height:100%;
  border-radius:3px;
  background:linear-gradient(90deg,#7C6BFF,#5B4BD9,#A78BFA);
  transition:width .8s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.users-table .usage-text {
  font-size:9px;
  color:var(--t2);
  white-space:nowrap;
}
.users-table .action-btns {
  display:flex;
  gap:3px;
  justify-content:center;
  flex-wrap:wrap;
}
.users-table .action-btns .btn {
  padding:2px 6px;
  font-size:8px;
  border-radius:4px;
}
.user-name-cell {
  display:flex;
  align-items:center;
  gap:6px;
}
.user-name-cell .avatar {
  width:24px;
  height:24px;
  border-radius:6px;
  background:linear-gradient(135deg,#7C6BFF,#5B4BD9);
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:10px;
  color:#fff;
  flex-shrink:0;
  transition:transform .3s;
}
.user-name-cell:hover .avatar{transform:scale(1.1) rotate(-5deg)}
.user-name-cell .name {
  font-weight:600;
  color:var(--t1);
}
.user-name-cell .uuid-short {
  font-size:7px;
  color:var(--t3);
  font-family:monospace;
}

.user-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:10px}
.user-card{background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:12px 14px;transition:all .4s cubic-bezier(0.34, 1.56, 0.64, 1);position:relative;overflow:hidden}
.user-card::before{content:'';position:absolute;top:-50%;right:-50%;width:150px;height:150px;background:radial-gradient(circle,rgba(100,80,255,0.02),transparent 70%);pointer-events:none}
.user-card:hover{border-color:var(--card-bh);transform:translateY(-4px)}
.user-card .head{display:flex;align-items:center;justify-content:space-between;margin-bottom:3px}
.user-card .name{font-size:12px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:4px}
.user-card .status{font-size:8px;font-weight:700;padding:1px 8px;border-radius:8px}
.user-card .status.on{background:var(--green-bg);color:var(--green-t)}
.user-card .status.off{background:var(--red-bg);color:var(--red-t)}
.user-card .uuid{font-family:monospace;font-size:7px;color:var(--t3);margin-bottom:4px;word-break:break-all}
.user-card .info{display:grid;grid-template-columns:1fr 1fr;gap:2px 8px;font-size:9px;color:var(--t2);margin-bottom:3px}
.user-card .quota-info{display:flex;justify-content:space-between;font-size:9px;color:var(--t2);margin-bottom:2px}
.user-card .quota-bar{height:3px;border-radius:2px;background:rgba(100,80,255,0.05);overflow:hidden;margin-bottom:6px}
.user-card .quota-fill{height:100%;border-radius:2px;background:linear-gradient(90deg,#7C6BFF,#5B4BD9,#A78BFA);transition:width .8s ease}
.user-card .last-seen{font-size:8px;color:var(--t3);margin-bottom:4px}
.user-card .actions{display:flex;gap:3px;flex-wrap:wrap}
.user-card .actions .btn{font-size:8px;padding:3px 6px;border-radius:4px;flex:1;justify-content:center;transition:all .3s}
.user-card .actions .btn:hover{transform:scale(1.05)}
.user-card .lock-badge{font-size:7px;color:var(--amber-t);background:var(--amber-bg);padding:0px 5px;border-radius:4px}
.btn{font-family:inherit;font-size:10px;font-weight:600;border-radius:6px;padding:5px 10px;cursor:pointer;display:inline-flex;align-items:center;gap:4px;border:none;transition:all .3s cubic-bezier(0.34, 1.56, 0.64, 1);white-space:nowrap}
.btn i{font-size:11px;transition:transform .3s}
.btn:hover i{transform:scale(1.1)}
.btn-p{background:linear-gradient(135deg,#7C6BFF,#5B4BD9,#A78BFA);background-size:200% 200%;animation:btnGradient 4s ease infinite;color:#fff;box-shadow:0 3px 15px rgba(100,80,255,.2)}
@keyframes btnGradient{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 6px 25px rgba(100,80,255,.3)}
.btn-o{background:rgba(255,255,255,0.02);border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:rgba(100,80,255,0.05);transform:translateY(-1px)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.1)}
.btn-d:hover{background:rgba(239,68,68,.15);transform:translateY(-1px)}
.btn-pur{background:rgba(100,80,255,0.08);color:var(--accent);border:1px solid rgba(100,80,255,.1)}
.btn-pur:hover{background:rgba(100,80,255,0.15);transform:translateY(-1px)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,0.1)}
.btn-amber:hover{background:rgba(245,158,11,0.15);transform:translateY(-1px)}
.btn-sm{padding:2px 6px;font-size:8px;border-radius:4px}
.btn-icon{width:22px;height:22px;padding:0;justify-content:center}
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(8px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);backdrop-filter:blur(30px);border:1px solid var(--card-b);border-radius:14px;padding:20px 18px;max-width:560px;width:calc(100% - 20px);max-height:90vh;overflow-y:auto;position:relative;animation:modalIn .4s cubic-bezier(0.34, 1.56, 0.64, 1);box-shadow:var(--shadow)}
@keyframes modalIn{from{opacity:0;transform:scale(0.9) translateY(20px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-close{position:absolute;top:10px;left:10px;background:rgba(100,80,255,0.05);border:1px solid var(--card-b);color:var(--t2);width:24px;height:24px;border-radius:6px;font-size:12px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:.3s}
.modal-close:hover{background:var(--red-bg);color:var(--red-t);transform:rotate(90deg)}
.modal-title{font-size:14px;font-weight:700;color:var(--t1);margin-bottom:12px;display:flex;align-items:center;gap:6px}
.modal-title i{color:var(--accent);font-size:15px}
.fg{display:flex;flex-direction:column;gap:2px;margin-bottom:8px}
.fg label{font-size:8px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em;display:flex;align-items:center;gap:3px}
.fi{width:100%;padding:6px 10px;border-radius:6px;border:1px solid var(--card-b);background:rgba(0,0,20,.2);color:var(--t1);font-family:inherit;font-size:10px;outline:none;transition:.3s}
.fi:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(100,80,255,.06)}
.fi::placeholder{color:var(--t3)}
select.fi{appearance:none;cursor:pointer}
.fg-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px}
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px}
.conn-card{background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:10px;padding:10px 12px;transition:.3s}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.conn-card .ip{font-family:monospace;font-size:11px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:4px}
.conn-card .label{font-size:8px;color:var(--t3);margin-top:1px}
.conn-card .conn-info{display:flex;justify-content:space-between;margin-top:4px;font-size:8px;color:var(--t2);gap:3px;flex-wrap:wrap}
.conn-status-dot{display:inline-block;width:5px;height:5px;border-radius:50%;background:#34D399;animation:pulse 1.5s infinite;margin-left:3px}
.settings-card{background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:14px 16px;max-width:480px;margin-bottom:10px;position:relative;overflow:hidden;transition:all .3s}
.settings-card:hover{border-color:var(--card-bh)}
.settings-card::before{content:'';position:absolute;top:-50%;right:-50%;width:150px;height:150px;background:radial-gradient(circle,rgba(100,80,255,0.02),transparent 70%);pointer-events:none}
.settings-card .title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:10px;display:flex;align-items:center;gap:6px}
.settings-card .title i{color:var(--accent)}
.settings-card .field{margin-bottom:8px}
.settings-card .field label{font-size:9px;color:var(--t3);display:block;margin-bottom:2px;font-weight:600}
.settings-card .field input{width:100%;padding:6px 10px;border-radius:6px;border:1px solid var(--card-b);background:rgba(0,0,20,.2);color:var(--t1);font-family:inherit;font-size:11px;outline:none;transition:.3s}
.settings-card .field input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(100,80,255,.06)}
.settings-card .btn{width:100%;justify-content:center;margin-top:3px;font-size:11px;padding:6px}
.settings-card .toggle-row{display:flex;align-items:center;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--card-b)}
.settings-card .toggle-row .toggle-label{font-size:11px;color:var(--t2);display:flex;align-items:center;gap:5px}
.switch{position:relative;width:36px;height:20px;background:var(--t3);border-radius:10px;cursor:pointer;transition:.4s;flex-shrink:0}
.switch.on{background:linear-gradient(135deg,#7C6BFF,#5B4BD9)}
.switch .slider{position:absolute;top:2px;right:2px;width:16px;height:16px;background:#fff;border-radius:50%;transition:.4s cubic-bezier(0.34, 1.56, 0.64, 1);box-shadow:0 2px 4px rgba(0,0,0,0.2)}
.switch.on .slider{right:18px}
.toast{position:fixed;bottom:70px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);backdrop-filter:blur(30px);border:1px solid var(--card-b);color:var(--t1);border-radius:8px;padding:8px 16px;font-size:11px;opacity:0;transition:all .4s cubic-bezier(0.34, 1.56, 0.64, 1);z-index:999;pointer-events:none;box-shadow:var(--shadow);display:flex;align-items:center;gap:5px}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.2);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.2);background:var(--red-bg);color:var(--red-t)}
.empty{text-align:center;padding:30px 15px;color:var(--t3)}
.empty i{font-size:28px;opacity:.3;display:block;margin-bottom:6px}
.empty p{font-size:10px}
.bottom-nav{display:none;position:fixed;bottom:0;right:0;left:0;background:var(--card);backdrop-filter:blur(30px);border-top:1px solid var(--card-b);z-index:300;padding:4px 2px 6px;justify-content:space-around;align-items:center}
.bottom-nav .nav-item{display:flex;flex-direction:column;align-items:center;gap:1px;color:var(--t3);font-size:7px;cursor:pointer;padding:3px 6px;border-radius:6px;transition:all .3s;border:none;background:none;font-family:inherit;min-width:40px;position:relative}
.bottom-nav .nav-item i{font-size:16px;transition:all .3s}
.bottom-nav .nav-item:hover{color:var(--t2);transform:translateY(-2px)}
.bottom-nav .nav-item.active{color:var(--accent)}
.bottom-nav .nav-item.active i{transform:scale(1.1)}
@media(max-width:768px){
  .bottom-nav{display:flex !important}
  .main{padding-bottom:65px !important;margin-right:0 !important;padding-top:55px !important}
  .sidebar{transform:translateX(100%);padding-bottom:60px}
  .sidebar.open{transform:translateX(0)}
  .mob-top{display:flex}
  .stats-grid{grid-template-columns:repeat(3,1fr)}
  .user-grid{grid-template-columns:1fr}
  .stat-mini{grid-template-columns:1fr 1fr}
}
@media(max-width:480px){
  .stats-grid{grid-template-columns:1fr 1fr}
  .main{padding:50px 8px 65px}
  .bottom-nav .nav-item{min-width:32px;padding:2px 4px}
  .bottom-nav .nav-item i{font-size:14px}
  .bottom-nav .nav-item span{font-size:6px}
  .users-table thead th{font-size:7px;padding:6px 4px}
  .users-table tbody td{font-size:9px;padding:6px 4px}
  .users-table .usage-bar .bar{width:40px}
  .stat-mini{padding:6px 8px}
  .stat-mini-num{font-size:13px}
}
@media(min-width:769px){.bottom-nav{display:none !important}}

/* ===== تم روشن ===== */
body.light-theme {
  --bg:#f0f0f5;
  --bg2:#e8e8f0;
  --bg3:#dddde8;
  --card:rgba(255,255,255,0.85);
  --card-b:rgba(100,80,255,0.12);
  --card-bh:rgba(100,80,255,0.2);
  --t1:#1a1a2e;
  --t2:#4a4a6a;
  --t3:#7a7a9a;
  --shadow:0 8px 32px rgba(0,0,0,0.08),0 0 60px rgba(100,80,255,0.02);
}
body.light-theme .stars-bg .star-bg { background:#8888BB; }
body.light-theme .glow-main { display:none; }
body.light-theme .stat-card::before { background:radial-gradient(circle,rgba(100,80,255,0.05),transparent 70%); }
body.light-theme .fi { background:rgba(255,255,255,0.7); }
body.light-theme .btn-o { background:rgba(0,0,0,0.03); border-color:rgba(100,80,255,0.1); color:var(--t2); }
body.light-theme .btn-o:hover { background:rgba(100,80,255,0.06); }
body.light-theme .users-table thead th { background:rgba(100,80,255,0.03); }
body.light-theme .users-table tbody tr:hover { background:rgba(100,80,255,0.03); }
body.light-theme .stat-mini { background:rgba(255,255,255,0.8); }
body.light-theme .conn-card { background:rgba(255,255,255,0.8); }
body.light-theme .user-card { background:rgba(255,255,255,0.8); }
body.light-theme .settings-card { background:rgba(255,255,255,0.8); }
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

<!-- ===== مودال ساخت کاربر با انتخاب پورت ===== -->
<div class="modal-bg" id="modal-user">
  <div class="modal" style="max-width:560px;">
    <button class="modal-close" onclick="closeModal('modal-user')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-user-plus"></i> ساخت کاربر جدید</div>
    
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="fg" style="grid-column:1/2;">
        <label><i class="ti ti-tag"></i> نام کاربری</label>
        <input class="fi" id="user-label" placeholder="مثلاً: علی" value="کاربر">
      </div>
      
      <div class="fg">
        <label><i class="ti ti-database"></i> حجم (GB)</label>
        <input class="fi" id="user-quota" type="number" min="0.5" step="0.5" value="2">
      </div>
      
      <div class="fg">
        <label><i class="ti ti-calendar"></i> انقضا (روز)</label>
        <input class="fi" id="user-exp" type="number" min="0" value="30">
      </div>
      
      <div class="fg">
        <label><i class="ti ti-devices"></i> دستگاه</label>
        <input class="fi" id="user-devices" type="number" min="0" max="10" value="1">
      </div>
    </div>
    
    <div class="fg">
      <label><i class="ti ti-fingerprint"></i> انگشت‌نگاری (فینگرپرینت)</label>
      <select class="fi" id="user-fingerprint">
        <option value="chrome">🌐 Chrome</option>
        <option value="firefox">🦊 Firefox</option>
        <option value="safari">🧭 Safari</option>
        <option value="edge">🌊 Edge</option>
        <option value="ios">📱 iOS</option>
        <option value="android">🤖 Android</option>
        <option value="safari_ios">🍏 Safari iOS</option>
        <option value="random">🎲 Random</option>
        <option value="none">🚫 None</option>
      </select>
    </div>
    
    <!-- ===== انتخاب پورت‌ها ===== -->
    <div class="fg">
      <label><i class="ti ti-plug"></i> پورت‌ها (انتخاب چندگانه)</label>
      <div style="display:flex;flex-wrap:wrap;gap:6px;padding:6px 0;">
        <label style="display:flex;align-items:center;gap:4px;font-size:10px;color:var(--t2);cursor:pointer;background:rgba(100,80,255,0.03);padding:3px 8px;border-radius:4px;border:1px solid var(--card-b);">
          <input type="checkbox" class="port-check" value="443" checked> 443
        </label>
        <label style="display:flex;align-items:center;gap:4px;font-size:10px;color:var(--t2);cursor:pointer;background:rgba(100,80,255,0.03);padding:3px 8px;border-radius:4px;border:1px solid var(--card-b);">
          <input type="checkbox" class="port-check" value="8443"> 8443
        </label>
        <label style="display:flex;align-items:center;gap:4px;font-size:10px;color:var(--t2);cursor:pointer;background:rgba(100,80,255,0.03);padding:3px 8px;border-radius:4px;border:1px solid var(--card-b);">
          <input type="checkbox" class="port-check" value="2053"> 2053
        </label>
        <label style="display:flex;align-items:center;gap:4px;font-size:10px;color:var(--t2);cursor:pointer;background:rgba(100,80,255,0.03);padding:3px 8px;border-radius:4px;border:1px solid var(--card-b);">
          <input type="checkbox" class="port-check" value="2096"> 2096
        </label>
        <label style="display:flex;align-items:center;gap:4px;font-size:10px;color:var(--t2);cursor:pointer;background:rgba(100,80,255,0.03);padding:3px 8px;border-radius:4px;border:1px solid var(--card-b);">
          <input type="checkbox" class="port-check" value="2087"> 2087
        </label>
        <label style="display:flex;align-items:center;gap:4px;font-size:10px;color:var(--t2);cursor:pointer;background:rgba(100,80,255,0.03);padding:3px 8px;border-radius:4px;border:1px solid var(--card-b);">
          <input type="checkbox" class="port-check" value="2083"> 2083
        </label>
        <label style="display:flex;align-items:center;gap:4px;font-size:10px;color:var(--t2);cursor:pointer;background:rgba(100,80,255,0.03);padding:3px 8px;border-radius:4px;border:1px solid var(--card-b);">
          <input type="checkbox" class="port-check" value="8080"> 8080
        </label>
        <label style="display:flex;align-items:center;gap:4px;font-size:10px;color:var(--t2);cursor:pointer;background:rgba(100,80,255,0.03);padding:3px 8px;border-radius:4px;border:1px solid var(--card-b);">
          <input type="checkbox" class="port-check" value="80"> 80
        </label>
      </div>
      <div style="font-size:7px;color:var(--t3);margin-top:2px;">💡 هر پورت = یک کانفیگ جداگانه در ساب‌لینک</div>
    </div>
    
    <div class="fg">
      <label><i class="ti ti-lock"></i> رمز (اختیاری)</label>
      <input class="fi" id="user-password" type="password" placeholder="برای ویرایش/حذف" dir="ltr">
    </div>
    
    <div style="display:flex;gap:6px;margin-top:10px">
      <button class="btn btn-p" onclick="saveUser()" style="flex:2"><i class="ti ti-check"></i> ساخت کاربر</button>
      <button class="btn btn-o" onclick="closeModal('modal-user')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<!-- ===== مودال ویرایش ===== -->
<div class="modal-bg" id="modal-edit">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کاربر</div>
    <input type="hidden" id="edit-uuid">
    
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="fg" style="grid-column:1/2;">
        <label><i class="ti ti-tag"></i> نام</label>
        <input class="fi" id="edit-label" placeholder="نام کاربری">
      </div>
      
      <div class="fg" id="edit-password-section">
        <label><i class="ti ti-lock"></i> رمز جدید</label>
        <input class="fi" id="edit-password" type="password" placeholder="برای تغییر" dir="ltr">
      </div>
      
      <div class="fg">
        <label><i class="ti ti-database"></i> حجم (GB)</label>
        <input class="fi" id="edit-quota" type="number" min="0" step="0.5">
      </div>
      
      <div class="fg">
        <label><i class="ti ti-calendar"></i> انقضا (روز)</label>
        <input class="fi" id="edit-exp" type="number" min="0">
      </div>
      
      <div class="fg">
        <label><i class="ti ti-devices"></i> دستگاه</label>
        <input class="fi" id="edit-devices" type="number" min="0" max="10">
      </div>
      
      <div class="fg">
        <label><i class="ti ti-toggle-left"></i> وضعیت</label>
        <select class="fi" id="edit-status">
          <option value="true">✅ فعال</option>
          <option value="false">❌ غیرفعال</option>
        </select>
      </div>
    </div>
    
    <div class="fg">
      <label><i class="ti ti-fingerprint"></i> انگشت‌نگاری</label>
      <select class="fi" id="edit-fingerprint">
        <option value="chrome">🌐 Chrome</option>
        <option value="firefox">🦊 Firefox</option>
        <option value="safari">🧭 Safari</option>
        <option value="edge">🌊 Edge</option>
        <option value="ios">📱 iOS</option>
        <option value="android">🤖 Android</option>
        <option value="safari_ios">🍏 Safari iOS</option>
        <option value="random">🎲 Random</option>
        <option value="none">🚫 None</option>
      </select>
    </div>
    
    <div style="display:flex;gap:6px;margin-top:10px">
      <button class="btn btn-p" onclick="saveEdit()" style="flex:2"><i class="ti ti-check"></i> ذخیره</button>
      <button class="btn btn-o" onclick="closeModal('modal-edit')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<!-- ===== مودال حذف ===== -->
<div class="modal-bg" id="modal-delete">
  <div class="modal" style="max-width:340px">
    <button class="modal-close" onclick="closeModal('modal-delete')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-trash"></i> حذف کاربر</div>
    <input type="hidden" id="delete-uuid">
    <p style="font-size:10px;color:var(--t2);margin-bottom:10px">برای حذف، رمز کانفیگ را وارد کنید.</p>
    <div class="fg"><label><i class="ti ti-lock"></i> رمز</label><input class="fi" id="delete-password" type="password" placeholder="رمز کانفیگ" dir="ltr"></div>
    <div style="display:flex;gap:6px;margin-top:10px">
      <button class="btn btn-d" onclick="confirmDelete()" style="flex:2"><i class="ti ti-trash"></i> حذف</button>
      <button class="btn btn-o" onclick="closeModal('modal-delete')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<!-- ===== هدر موبایل ===== -->
<div class="mob-top">
  <div class="ml"><div class="mob-logo">🪐</div><span class="mob-title">پنل عقاب</span></div>
  <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
</div>
<div class="overlay" id="overlay"></div>

<!-- ===== سایدبار ===== -->
<aside class="sidebar" id="sb">
  <div class="logo"><div class="logo-icon">🪐</div><div><div class="logo-name">پنل عقاب</div><div class="logo-sub">مدیریت کاربران</div></div></div>
  <div class="nav-wrap">
    <div class="nav-it on" data-pg="dashboard"><i class="ti ti-layout-dashboard"></
