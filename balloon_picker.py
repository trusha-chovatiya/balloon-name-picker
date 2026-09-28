import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="Balloon Name Picker",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep balloon.jpeg in the same folder as this app.py
IMAGE_FILE = "balloon.jpeg"

if not os.path.exists(IMAGE_FILE):
    st.error("balloon.jpeg was not found. Keep balloon.jpeg in the same folder as app.py.")
    st.stop()

with open(IMAGE_FILE, "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode("utf-8")

image_src = f"data:image/jpeg;base64,{image_base64}"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {{ box-sizing:border-box; }}

html,body {{
    margin:0;
    padding:0;
    width:100%;
    min-height:100%;
}}

body {{
    font-family:"Trebuchet MS","Segoe UI",Arial,sans-serif;
    overflow-x:hidden;
    color:#54356f;
    background:
      linear-gradient(180deg,#bfe9ff 0%,#d9f4ff 35%,#fff1fb 72%,#ffe4f2 100%);
}}

/* ===== FLOATING BALLOON PARTY BACKGROUND ===== */
body:before {{
    content:"";
    position:fixed;
    inset:0;
    pointer-events:none;
    z-index:0;
    background:
      radial-gradient(circle at 15% 20%,rgba(255,255,255,.85) 0 4px,transparent 5px),
      radial-gradient(circle at 82% 16%,rgba(255,255,255,.8) 0 5px,transparent 6px),
      radial-gradient(circle at 72% 72%,rgba(255,255,255,.7) 0 4px,transparent 5px),
      radial-gradient(circle at 27% 82%,rgba(255,255,255,.75) 0 5px,transparent 6px);
    background-size:180px 180px,240px 240px,210px 210px,260px 260px;
    animation:sparkleBg 8s linear infinite;
}}

@keyframes sparkleBg {{
    0%,100% {{ opacity:.65; transform:translateY(0); }}
    50% {{ opacity:1; transform:translateY(-8px); }}
}}

.cloud {{
    position:fixed;
    z-index:0;
    pointer-events:none;
    width:180px;
    height:55px;
    border-radius:60px;
    background:rgba(255,255,255,.72);
    filter:blur(.2px);
    box-shadow:
      35px -25px 0 -2px rgba(255,255,255,.72),
      85px -15px 0 8px rgba(255,255,255,.72),
      120px 0 0 0 rgba(255,255,255,.72);
    animation:cloudMove 24s linear infinite;
}}
.cloud1 {{ top:9%; left:-220px; }}
.cloud2 {{ top:29%; left:-260px; animation-delay:-10s; transform:scale(.7); opacity:.65; }}

@keyframes cloudMove {{
    from {{ margin-left:0; }}
    to {{ margin-left:calc(100vw + 520px); }}
}}

.bg-balloon {{
    position:fixed;
    z-index:1;
    pointer-events:none;
    border-radius:50% 50% 46% 46%;
    opacity:.88;
    filter:drop-shadow(0 12px 10px rgba(70,40,90,.15));
    animation:sideBalloonFloat 4s ease-in-out infinite;
}}
.bg-balloon:after {{
    content:"";
    position:absolute;
    width:2px;
    height:85px;
    left:50%;
    top:96%;
    background:rgba(90,70,120,.32);
}}
.bg1 {{ width:72px;height:90px;left:3%;top:35%;background:linear-gradient(135deg,#ff79aa,#ff3e76); }}
.bg2 {{ width:62px;height:78px;right:4%;top:43%;background:linear-gradient(135deg,#9f75ff,#633ee8);animation-delay:-1s; }}
.bg3 {{ width:48px;height:62px;left:9%;bottom:8%;background:linear-gradient(135deg,#58d9ff,#3199f0);animation-delay:-2s; }}
.bg4 {{ width:55px;height:70px;right:12%;bottom:10%;background:linear-gradient(135deg,#ffd05c,#ff9e3d);animation-delay:-3s; }}

@keyframes sideBalloonFloat {{
    0%,100% {{ transform:translateY(0) rotate(-4deg); }}
    50% {{ transform:translateY(-24px) rotate(5deg); }}
}}

.app {{
    position:relative;
    z-index:2;
    min-height:100vh;
    padding:28px 18px 60px;
    overflow:hidden;
}}

.container {{
    position:relative;
    z-index:3;
    max-width:1180px;
    margin:auto;
}}

/* ===== HERO ===== */
.hero {{
    position:relative;
    text-align:center;
    padding:22px 10px 30px;
}}

.hero:before {{
    content:"🎈";
    position:absolute;
    left:7%;
    top:5px;
    font-size:55px;
    animation:heroBalloon 2.8s ease-in-out infinite;
}}
.hero:after {{
    content:"🎈";
    position:absolute;
    right:7%;
    top:10px;
    font-size:52px;
    animation:heroBalloon 3.1s ease-in-out infinite reverse;
}}

@keyframes heroBalloon {{
    0%,100% {{ transform:translateY(0) rotate(-7deg); }}
    50% {{ transform:translateY(-16px) rotate(7deg); }}
}}

.title {{
    margin:0;
    font-size:clamp(40px,5.5vw,72px);
    line-height:1;
    font-weight:950;
    letter-spacing:-2px;
    color:#66379a;
    text-shadow:
      0 3px 0 #fff,
      0 7px 18px rgba(102,55,154,.18);
    animation:titleBounce 3s ease-in-out infinite;
}}

@keyframes titleBounce {{
    0%,100% {{ transform:translateY(0); }}
    50% {{ transform:translateY(-5px); }}
}}

.subtitle {{
    max-width:760px;
    margin:17px auto 0;
    padding:10px 18px;
    display:inline-block;
    border-radius:999px;
    background:rgba(255,255,255,.72);
    color:#725b8b;
    font-size:16px;
    font-weight:800;
    box-shadow:0 8px 25px rgba(95,56,120,.08);
}}

/* ===== MAIN GLASS CARD ===== */
.card {{
    max-width:900px;
    margin:8px auto 0;
    padding:32px;
    border-radius:34px;
    background:
      linear-gradient(145deg,rgba(255,255,255,.93),rgba(255,247,255,.79));
    border:3px solid rgba(255,255,255,.9);
    backdrop-filter:blur(18px);
    box-shadow:
      0 30px 80px rgba(86,45,130,.18),
      inset 0 1px 0 white;
    animation:cardIn .7s cubic-bezier(.2,.8,.2,1) both;
    position:relative;
}}

.card:before {{
    content:"";
    position:absolute;
    left:20px;
    right:20px;
    top:0;
    height:7px;
    border-radius:0 0 20px 20px;
    background:linear-gradient(90deg,#ff5f9e,#9a5cff,#39c9ff,#ffbf4d,#ff5f9e);
    background-size:250% 100%;
    animation:rainbowLine 5s linear infinite;
}}

@keyframes rainbowLine {{
    from {{ background-position:0 0; }}
    to {{ background-position:250% 0; }}
}}

@keyframes cardIn {{
    from {{ opacity:0;transform:translateY(25px) scale(.97); }}
    to {{ opacity:1;transform:translateY(0) scale(1); }}
}}

.section-title {{
    color:#59347f;
    font-size:25px;
    font-weight:950;
    margin-bottom:7px;
}}

.help {{
    color:#8a769a;
    font-size:14px;
    font-weight:700;
    margin-bottom:17px;
}}

/* ===== INPUT ===== */
.add-row {{ display:flex;gap:10px; }}

.name-input {{
    flex:1;
    min-width:0;
    border:2px solid #e1d1f6;
    outline:none;
    border-radius:17px;
    padding:15px 17px;
    font-size:16px;
    color:#4c3970;
    background:rgba(255,255,255,.94);
    transition:.25s;
    box-shadow:inset 0 2px 8px rgba(100,60,140,.04);
}}

.name-input:focus {{
    border-color:#8c55df;
    box-shadow:0 0 0 6px rgba(140,85,223,.12),0 8px 20px rgba(100,60,140,.08);
    transform:translateY(-1px);
}}

.add-btn,.start-btn,.secondary-btn,.reset-btn,.change-btn {{
    border:0;
    cursor:pointer;
    font-weight:950;
    transition:transform .18s,box-shadow .18s,filter .18s;
}}
.add-btn:hover,.start-btn:hover,.secondary-btn:hover,.reset-btn:hover,.change-btn:hover {{
    transform:translateY(-3px);
    filter:brightness(1.04);
}}

.add-btn {{
    min-width:145px;
    border-radius:17px;
    color:white;
    background:linear-gradient(135deg,#7040df,#a34fe9);
    box-shadow:0 10px 25px rgba(112,64,223,.28);
}}

.name-list {{
    min-height:60px;
    margin:18px 0 6px;
    padding:13px;
    border-radius:19px;
    background:rgba(250,246,255,.82);
    border:2px dashed #dac5f5;
    display:flex;
    flex-wrap:wrap;
    align-items:center;
    gap:9px;
}}

.empty-hint {{
    color:#a08eae;
    font-size:14px;
    font-weight:700;
}}

.chip {{
    display:inline-flex;
    align-items:center;
    gap:7px;
    padding:8px 11px 8px 14px;
    border-radius:999px;
    color:#55357d;
    background:linear-gradient(135deg,#fff,#f7efff);
    border:1px solid #eadfff;
    box-shadow:0 5px 14px rgba(96,66,133,.09);
    animation:chipIn .25s ease-out both;
}}
@keyframes chipIn {{
    from {{ opacity:0;transform:scale(.75) translateY(5px); }}
    to {{ opacity:1;transform:scale(1) translateY(0); }}
}}

.remove-chip {{
    width:22px;height:22px;padding:0;border:0;border-radius:50%;
    cursor:pointer;color:#76599a;background:#eee3ff;font-weight:900;
}}

.counter {{
    color:#8b789d;
    font-size:13px;
    font-weight:800;
    margin-top:7px;
}}

.action-row {{ display:flex;gap:12px;margin-top:21px; }}

.start-btn {{
    flex:1;
    padding:16px 22px;
    border-radius:18px;
    color:white;
    font-size:17px;
    background:linear-gradient(135deg,#713bd8,#aa4ee8,#e252a8);
    background-size:200% 200%;
    box-shadow:0 13px 30px rgba(112,64,215,.29);
    animation:buttonGlow 3s ease-in-out infinite;
}}

@keyframes buttonGlow {{
    0%,100% {{ background-position:0 50%;box-shadow:0 13px 30px rgba(112,64,215,.25); }}
    50% {{ background-position:100% 50%;box-shadow:0 15px 38px rgba(208,75,174,.28); }}
}}

.secondary-btn {{
    padding:16px 20px;
    border-radius:18px;
    color:#60487d;
    background:#f0e6ff;
}}

/* ===== GAME ===== */
.game {{
    display:none;
    margin-top:20px;
    animation:gameIn .6s ease-out both;
}}
.game.active {{ display:block; }}

@keyframes gameIn {{
    from {{ opacity:0;transform:translateY(20px); }}
    to {{ opacity:1;transform:translateY(0); }}
}}

.game-top {{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:15px;
    margin:10px 0 20px;
    padding:15px 19px;
    border-radius:21px;
    background:rgba(255,255,255,.78);
    border:2px solid rgba(255,255,255,.9);
    box-shadow:0 12px 30px rgba(89,59,126,.10);
}}

.game-message {{ font-weight:950;color:#5b3e83; }}
.count {{ color:#8b789d;font-size:14px;font-weight:800; }}

.grid {{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(155px,1fr));
    gap:25px;
    justify-items:center;
    align-items:end;
    padding:12px 8px 28px;
}}

/* ===== BALLOONS ===== */
.balloon-box {{
    width:165px;
    height:220px;
    display:flex;
    justify-content:center;
    align-items:flex-start;
    position:relative;
    cursor:pointer;
    user-select:none;
    animation:
      balloonEnter .7s cubic-bezier(.2,.8,.2,1) both,
      gentleFloat 3.2s ease-in-out infinite;
    animation-delay:var(--enter-delay),calc(var(--float-delay)*-1);
}}

.balloon-box:after {{
    content:"";
    position:absolute;
    top:172px;
    left:50%;
    width:2px;
    height:48px;
    background:linear-gradient(#735b8b,transparent);
    opacity:.45;
    transform:translateX(-50%);
    pointer-events:none;
}}

@keyframes balloonEnter {{
    0% {{ opacity:0;transform:translateY(100px) scale(.55) rotate(-12deg); }}
    70% {{ opacity:1;transform:translateY(-12px) scale(1.07) rotate(5deg); }}
    100% {{ opacity:1;transform:translateY(0) scale(1) rotate(0); }}
}}

@keyframes gentleFloat {{
    0%,100% {{ transform:translateY(0) rotate(-1.5deg); }}
    50% {{ transform:translateY(-13px) rotate(2.5deg); }}
}}

.balloon {{
    width:153px;
    height:193px;
    object-fit:contain;
    transition:transform .2s ease,filter .2s ease;
    filter:drop-shadow(0 14px 10px rgba(45,30,70,.20));
}}

.balloon-box:hover .balloon {{
    transform:scale(1.09) rotate(-4deg);
    filter:drop-shadow(0 18px 13px rgba(45,30,70,.25)) brightness(1.06);
}}

.balloon-box.popping {{
    pointer-events:none;
    animation:none;
}}
.balloon-box.popping .balloon {{
    animation:fastPop .28s cubic-bezier(.2,.9,.3,1) forwards;
}}

@keyframes fastPop {{
    0% {{ transform:scale(1);opacity:1; }}
    24% {{ transform:scale(1.12);opacity:1; }}
    52% {{ transform:scale(1.42);opacity:.92; }}
    100% {{ transform:scale(.02);opacity:0; }}
}}

/* stronger, more colorful balloon variants */
.c0 .balloon {{ filter:hue-rotate(350deg) saturate(2.15) drop-shadow(0 14px 10px rgba(45,30,70,.20)); }}
.c1 .balloon {{ filter:hue-rotate(285deg) saturate(2.2) brightness(1.08) drop-shadow(0 14px 10px rgba(45,30,70,.20)); }}
.c2 .balloon {{ filter:hue-rotate(205deg) saturate(2.2) brightness(1.08) drop-shadow(0 14px 10px rgba(45,30,70,.20)); }}
.c3 .balloon {{ filter:hue-rotate(90deg) saturate(2.15) brightness(1.08) drop-shadow(0 14px 10px rgba(45,30,70,.20)); }}
.c4 .balloon {{ filter:hue-rotate(250deg) saturate(2.2) brightness(1.08) drop-shadow(0 14px 10px rgba(45,30,70,.20)); }}
.c5 .balloon {{ filter:hue-rotate(165deg) saturate(2.2) brightness(1.08) drop-shadow(0 14px 10px rgba(45,30,70,.20)); }}
.c6 .balloon {{ filter:hue-rotate(35deg) saturate(2.25) brightness(1.08) drop-shadow(0 14px 10px rgba(45,30,70,.20)); }}
.c7 .balloon {{ filter:hue-rotate(315deg) saturate(2.2) brightness(1.08) drop-shadow(0 14px 10px rgba(45,30,70,.20)); }}

/* ===== RESULT ===== */
.result {{
    min-height:112px;
    max-width:680px;
    margin:4px auto 18px;
    padding:17px 20px;
    border-radius:27px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    background:rgba(255,255,255,.86);
    border:2px solid rgba(255,255,255,.95);
    box-shadow:0 16px 40px rgba(91,59,130,.13);
}}

.result.pop {{ animation:resultPop .45s cubic-bezier(.2,.9,.3,1) both; }}

@keyframes resultPop {{
    0% {{ transform:scale(.82);opacity:.4; }}
    70% {{ transform:scale(1.05);opacity:1; }}
    100% {{ transform:scale(1);opacity:1; }}
}}

.result-small {{ font-size:14px;font-weight:800;color:#927da6; }}
.result-name {{
    margin-top:3px;
    font-size:clamp(30px,5vw,48px);
    font-weight:950;
    color:#6a3bb4;
    text-shadow:0 4px 16px rgba(106,59,180,.16);
}}

.game-actions {{ display:flex;justify-content:center;gap:10px;flex-wrap:wrap; }}
.reset-btn,.change-btn {{ padding:12px 18px;border-radius:15px; }}
.reset-btn {{ color:white;background:linear-gradient(135deg,#7040d7,#a34fe8); }}
.change-btn {{ color:#60487d;background:#eee4ff; }}

/* ===== POP REVEAL ===== */
.reveal {{
    position:fixed;
    z-index:10002;
    pointer-events:none;
    transform:translate(-50%,-50%) scale(.25);
    opacity:0;
    padding:12px 22px;
    border-radius:20px;
    background:linear-gradient(135deg,#fff,#fff5ff);
    border:3px solid white;
    color:#5e3792;
    font-size:31px;
    font-weight:950;
    white-space:nowrap;
    box-shadow:0 18px 45px rgba(60,35,90,.25);
    animation:revealName .65s cubic-bezier(.15,.85,.25,1) forwards;
}}

@keyframes revealName {{
    0% {{ opacity:0;transform:translate(-50%,-50%) scale(.25) rotate(-7deg); }}
    60% {{ opacity:1;transform:translate(-50%,-50%) scale(1.13) rotate(2deg); }}
    100% {{ opacity:1;transform:translate(-50%,-50%) scale(1) rotate(0); }}
}}

.star {{
    position:fixed;
    left:0;top:0;
    z-index:10000;
    pointer-events:none;
    font-size:27px;
    transform:translate(-50%,-50%);
    animation:starFly .72s cubic-bezier(.2,.7,.2,1) forwards;
}}

@keyframes starFly {{
    0% {{ transform:translate(-50%,-50%) scale(.25);opacity:1; }}
    100% {{ transform:translate(calc(-50% + var(--x)),calc(-50% + var(--y))) scale(1.15) rotate(220deg);opacity:0; }}
}}

.confetti {{
    position:fixed;
    width:9px;height:15px;
    z-index:10001;
    pointer-events:none;
    border-radius:2px;
    animation:confettiFly 1s cubic-bezier(.15,.75,.25,1) forwards;
}}

@keyframes confettiFly {{
    0% {{ transform:translate(-50%,-50%) rotate(0) scale(1);opacity:1; }}
    100% {{ transform:translate(calc(-50% + var(--x)),calc(-50% + var(--y))) rotate(var(--r)) scale(.65);opacity:0; }}
}}

@media(max-width:700px) {{
    .app {{ padding:18px 10px 45px; }}
    .hero:before,.hero:after {{ font-size:38px; }}
    .hero:before {{ left:1%; }}
    .hero:after {{ right:1%; }}
    .card {{ padding:23px 18px;border-radius:25px; }}
    .add-row,.action-row {{ flex-direction:column; }}
    .add-btn {{ min-height:50px; }}
    .game-top {{ flex-direction:column;text-align:center; }}
    .grid {{ grid-template-columns:repeat(2,minmax(130px,1fr));gap:13px; }}
    .balloon-box {{ width:140px;height:195px; }}
    .balloon {{ width:132px;height:170px; }}
}}
</style>
</head>

<body>
<div class="cloud cloud1"></div>
<div class="cloud cloud2"></div>
<div class="bg-balloon bg1"></div>
<div class="bg-balloon bg2"></div>
<div class="bg-balloon bg3"></div>
<div class="bg-balloon bg4"></div>

<div class="app">
<div class="container">

<div class="hero">
    <h1 class="title">🎈 Balloon Name Picker 🎈</h1>
    <div class="subtitle">
        Add your people, start the game, and pop a balloon to reveal a random name.
    </div>
</div>

<div id="setup" class="card">
    <div class="section-title">👥 Add People</div>
    <div class="help">
        Enter one name at a time. Press Enter or click Add Person.
    </div>

    <div class="add-row">
        <input id="nameInput" class="name-input"
               maxlength="40"
               autocomplete="off"
               placeholder="Enter a person's name...">
        <button id="addBtn" class="add-btn">＋ Add Person</button>
    </div>

    <div id="nameList" class="name-list"></div>
    <div id="counter" class="counter">0 / 40 people added</div>

    <div class="action-row">
        <button id="startBtn" class="start-btn">🎈 Start Balloon Game</button>
        <button id="clearBtn" class="secondary-btn">🧹 Clear All</button>
    </div>
</div>

<div id="game" class="game">
    <div class="game-top">
        <div id="message" class="game-message">Pop any balloon to reveal a name! 🎯</div>
        <div id="count" class="count"></div>
    </div>

    <div id="grid" class="grid"></div>

    <div id="result" class="result">
        <div class="result-small">Your random name will appear here</div>
        <div class="result-name">🎈 Ready?</div>
    </div>

    <div class="game-actions">
        <button id="resetBtn" class="reset-btn">🔄 Reset Game</button>
        <button id="changeBtn" class="change-btn">✏️ Change Names</button>
    </div>
</div>

</div>
</div>

<script>
const BALLOON_IMAGE = "{image_src}";

let names = [];
let remaining = [];
let audioContext = null;

const input = document.getElementById("nameInput");
const nameList = document.getElementById("nameList");
const counter = document.getElementById("counter");
const addBtn = document.getElementById("addBtn");
const clearBtn = document.getElementById("clearBtn");
const startBtn = document.getElementById("startBtn");
const resetBtn = document.getElementById("resetBtn");
const changeBtn = document.getElementById("changeBtn");
const setup = document.getElementById("setup");
const game = document.getElementById("game");
const grid = document.getElementById("grid");
const result = document.getElementById("result");
const message = document.getElementById("message");
const count = document.getElementById("count");

function renderNames() {{
    nameList.innerHTML = "";

    if (names.length === 0) {{
        const hint = document.createElement("div");
        hint.className = "empty-hint";
        hint.textContent = "No names added yet — add your first person above.";
        nameList.appendChild(hint);
    }} else {{
        names.forEach((name, index) => {{
            const chip = document.createElement("div");
            chip.className = "chip";

            const text = document.createElement("span");
            text.textContent = name;

            const remove = document.createElement("button");
            remove.className = "remove-chip";
            remove.textContent = "×";
            remove.onclick = () => {{
                names.splice(index, 1);
                renderNames();
            }};

            chip.appendChild(text);
            chip.appendChild(remove);
            nameList.appendChild(chip);
        }});
    }}

    counter.textContent = `${{names.length}} / 40 people added`;
}}

function addName() {{
    const name = input.value.trim().replace(/\\s+/g, " ");

    if (!name) {{
        input.focus();
        return;
    }}

    if (names.length >= 40) {{
        alert("Maximum 40 people are supported.");
        return;
    }}

    if (names.some(n => n.toLowerCase() === name.toLowerCase())) {{
        alert("This name is already added.");
        input.select();
        return;
    }}

    names.push(name);
    input.value = "";
    renderNames();
    input.focus();
}}

function clearNames() {{
    names = [];
    renderNames();
    input.value = "";
    input.focus();
}}

function startGame() {{
    if (names.length === 0) {{
        alert("Please add at least one name first.");
        input.focus();
        return;
    }}

    remaining = [...names];
    setup.style.display = "none";
    game.classList.add("active");
    message.textContent = "Pop any balloon to reveal a name! 🎯";

    result.innerHTML = `
        <div class="result-small">Your random name will appear here</div>
        <div class="result-name">🎈 Ready?</div>
    `;

    buildBalloons();
}}

function buildBalloons() {{
    grid.innerHTML = "";

    names.forEach((_, index) => {{
        const box = document.createElement("div");
        box.className = "balloon-box c" + (index % 8);
        box.style.setProperty("--enter-delay", (index * 0.055) + "s");
        box.style.setProperty("--float-delay", ((index % 6) * .35) + "s");

        const img = document.createElement("img");
        img.className = "balloon";
        img.src = BALLOON_IMAGE;
        img.alt = "Balloon";

        box.appendChild(img);
        box.onclick = () => popBalloon(box);

        grid.appendChild(box);
    }});

    updateCount();
}}

function updateCount() {{
    count.textContent =
        `${{remaining.length}} balloon${{remaining.length === 1 ? "" : "s"}} left`;
}}

function popBalloon(box) {{
    if (!remaining.length || box.classList.contains("popping")) return;

    const rect = box.getBoundingClientRect();
    const x = rect.left + rect.width / 2;
    const y = rect.top + rect.height * .42;

    const index = Math.floor(Math.random() * remaining.length);
    const selected = remaining.splice(index, 1)[0];

    box.classList.add("popping");

    playPopSound();
    createStars(x, y);
    createConfetti(x, y);
    showReveal(x, y, selected);

    result.classList.remove("pop");
    void result.offsetWidth;
    result.classList.add("pop");
    result.innerHTML = `
        <div class="result-small">🎉 Random name selected</div>
        <div class="result-name"></div>
    `;
    result.querySelector(".result-name").textContent = selected;

    setTimeout(() => box.remove(), 320);
    updateCount();

    if (remaining.length === 0) {{
        setTimeout(() => {{
            message.textContent = "🎊 Everyone has been revealed!";
            count.textContent = "Game complete";
            result.innerHTML = `
                <div class="result-small">🏆 All names revealed</div>
                <div class="result-name">Amazing! 🎈✨</div>
            `;
            createBigCelebration();
        }}, 450);
    }}
}}

function showReveal(x, y, name) {{
    const el = document.createElement("div");
    el.className = "reveal";
    el.textContent = name;
    el.style.left = x + "px";
    el.style.top = y + "px";
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 1150);
}}

function createStars(x, y) {{
    const icons = ["⭐","✨","🌟","💫","🎈","✨","⭐","🌟"];

    icons.forEach((icon, i) => {{
        const el = document.createElement("div");
        el.className = "star";
        el.textContent = icon;

        const angle = Math.PI * 2 / icons.length * i;
        const distance = 70 + Math.random() * 45;

        el.style.left = x + "px";
        el.style.top = y + "px";
        el.style.setProperty("--x", Math.cos(angle) * distance + "px");
        el.style.setProperty("--y", Math.sin(angle) * distance + "px");

        document.body.appendChild(el);
        setTimeout(() => el.remove(), 800);
    }});
}}

function createConfetti(x, y) {{
    const colors = [
        "#ff5c8a","#7a52e6","#4bb6ff","#ffb347",
        "#5bd68b","#ff77c8","#ffd34e","#8e7dff"
    ];

    for (let i = 0; i < 18; i++) {{
        const el = document.createElement("div");
        el.className = "confetti";

        const angle = Math.random() * Math.PI * 2;
        const distance = 75 + Math.random() * 125;

        el.style.left = x + "px";
        el.style.top = y + "px";
        el.style.background = colors[Math.floor(Math.random() * colors.length)];
        el.style.setProperty("--x", Math.cos(angle) * distance + "px");
        el.style.setProperty("--y", Math.sin(angle) * distance + "px");
        el.style.setProperty("--r", (180 + Math.random() * 540) + "deg");

        document.body.appendChild(el);
        setTimeout(() => el.remove(), 1050);
    }}
}}

function createBigCelebration() {{
    const x = innerWidth / 2;
    const y = Math.min(innerHeight * .42, 430);

    for (let i = 0; i < 35; i++) {{
        setTimeout(() => createConfetti(
            x + (Math.random() - .5) * 120,
            y + (Math.random() - .5) * 70
        ), i * 18);
    }}
}}

function getAudio() {{
    if (!audioContext) {{
        const Ctx = window.AudioContext || window.webkitAudioContext;
        if (!Ctx) return null;
        audioContext = new Ctx();
    }}

    if (audioContext.state === "suspended") audioContext.resume();
    return audioContext;
}}

function playPopSound() {{
    try {{
        const ctx = getAudio();
        if (!ctx) return;

        const now = ctx.currentTime;

        // Very short sound: no long fade or delayed audio.
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = "triangle";
        osc.frequency.setValueAtTime(240, now);
        osc.frequency.exponentialRampToValueAtTime(55, now + .075);

        gain.gain.setValueAtTime(.0001, now);
        gain.gain.exponentialRampToValueAtTime(.42, now + .005);
        gain.gain.exponentialRampToValueAtTime(.0001, now + .09);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + .095);
    }} catch (e) {{
        console.log("Pop sound unavailable.", e);
    }}
}}

function resetGame() {{
    remaining = [...names];
    message.textContent = "Pop any balloon to reveal a name! 🎯";

    result.innerHTML = `
        <div class="result-small">Your random name will appear here</div>
        <div class="result-name">🎈 Ready?</div>
    `;

    buildBalloons();
}}

function changeNames() {{
    game.classList.remove("active");
    setup.style.display = "block";
    input.focus();
    window.scrollTo({{top:0,behavior:"smooth"}});
}}

addBtn.onclick = addName;
clearBtn.onclick = clearNames;
startBtn.onclick = startGame;
resetBtn.onclick = resetGame;
changeBtn.onclick = changeNames;

input.addEventListener("keydown", e => {{
    if (e.key === "Enter") {{
        e.preventDefault();
        addName();
    }}
}});

renderNames();
</script>
</body>
</html>
"""

components.html(html_code, height=1250, scrolling=True)
