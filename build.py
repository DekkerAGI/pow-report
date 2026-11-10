import json,html,sys
import os
d=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data.json')))
def camurl(rid,cid):
    if rid=='stevens': return f"https://player.brownrice.com/embed/{cid}"
    return f"https://camstreamer.com/embed/{cid}?enablejsapi=1&rel=0&modestbranding=1&playsinline=1"
def camlink(rid):
    return "https://www.stevenspass.com/the-mountain/mountain-conditions/mountain-cams.aspx" if rid=='stevens' else "https://www.summitatsnoqualmie.com/webcams"

HESH = """<section id="hesh" class="card hesh"><header><div><h2>Hesh Corner</h2><p>Certified hesh content. Nothing important here.</p></div><span class="badge open" id="trickname">TRICK</span></header>
<svg viewBox="0 0 400 220" class="trick" role="img" aria-label="Animated skier doing a trick off a jump"><defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fd0ff"/><stop offset="1" stop-color="#eaf6ff"/></linearGradient></defs>
<rect width="400" height="220" fill="url(#sk)" rx="12"/><polygon points="0,220 0,170 170,170 260,130 400,200 400,220" fill="#fff"/><polygon points="0,170 170,170 260,130 275,140 180,180 0,180" fill="#cfe6f5"/>
<g id="flyer"><g id="rider" style="transform-box:fill-box;transform-origin:center"><circle cx="0" cy="-26" r="7" fill="#223"/><line x1="0" y1="-19" x2="0" y2="4" stroke="#223" stroke-width="5" stroke-linecap="round"/><line x1="0" y1="-14" x2="-12" y2="-4" stroke="#223" stroke-width="4" stroke-linecap="round"/><line x1="0" y1="-14" x2="12" y2="-6" stroke="#223" stroke-width="4" stroke-linecap="round"/><line x1="0" y1="4" x2="-8" y2="18" stroke="#223" stroke-width="4" stroke-linecap="round"/><line x1="0" y1="4" x2="9" y2="17" stroke="#223" stroke-width="4" stroke-linecap="round"/><rect x="-26" y="17" width="52" height="4" rx="2" fill="#e8483c"/></g></g></svg>
<p class="small" id="trickcap">Tap the picture for a new trick.</p></section>
<style>.hesh svg{width:100%;max-width:520px;display:block;margin:12px auto;cursor:pointer}@keyframes arc{0%{transform:translate(120px,140px)}50%{transform:translate(215px,45px)}100%{transform:translate(340px,168px)}}#flyer{animation:arc 2.2s ease-in-out infinite;transform-box:view-box}@keyframes flip{0%,10%{transform:rotate(0)}70%,100%{transform:rotate(-360deg)}}@keyframes spin{0%,10%{transform:scaleX(1)}25%{transform:scaleX(-1)}40%{transform:scaleX(1)}55%{transform:scaleX(-1)}70%,100%{transform:scaleX(1)}}@keyframes grab{0%,15%{transform:rotate(0)}40%,60%{transform:rotate(-22deg) scaleX(1.05)}85%,100%{transform:rotate(0)}}#rider{animation-duration:2.2s;animation-iteration-count:infinite;animation-timing-function:ease-in-out}</style>
<script>(function(){var T=[["Backflip","flip"],["360 Spin","spin"],["Tail Grab","grab"],["Double Flip","flip"]];function go(){var t=T[Math.floor(Math.random()*T.length)];var r=document.getElementById("rider");r.style.animationName="none";void r.getBoundingClientRect();r.style.animationName=t[1];r.style.animationDuration=t[0]=="Double Flip"?"1.6s":"2.2s";document.getElementById("trickname").textContent=t[0].toUpperCase();}go();document.querySelector(".hesh svg").addEventListener("click",go);})();</script>"""

GIFS = [
 ("IdyhZspLSz8v7dIRz5","Snow fail"),("bXkNSePOO0JUs","Ski fail"),("yzZaHGT4DrmroFhSCA","Crash"),
 ("74u3n5M7SJx7O","Skiing FML"),("5tsljgroZCHcbk6IHg","Oof"),("6L85SZN79VxEA","Ski fail"),
 ("da81SkQHlZnHO","Jump fail"),("7aLx6EHBGyTZTNOt5G","Bad luck"),("3ohjUXJLsWfq0jfiJq","Ski fail"),
 ("24bc6h4Mo05pG4XqaU","Ski lift fail"),("l0HUp5iTjX4EQ7FjW","Ski fail"),("dhE00eldVD4qVYLGzz","Oh snap"),
 ("jsa4uq9GXUc8b2o1Pj","Snowboard fail"),("QveYuf4ZZ6a44Cbjq3","Wipe out"),("5WJ09Mca4SzernO9ZV","Ski lol"),
 ("9V5kiNQeEjYCOYOI0b","Snow lol"),("IgYDgCU3kzXW8M7ngn","Wipe out"),("3o7WIK06ZsP1otF7na","Snow fail"),
 ("xT1R9O0SrcXEAWgA9y","Snowboard fail"),("xT1R9TrQ5FJxXYFZC0","Snowboard fail"),("67YGUW9ZdnLLI4NevB","Oh snap"),
 ("3ohjV5LQl37fGh73BC","Snow fail"),("gLnkFkYgZ6OV29oXlE","Superman slide"),("2aLiVCqTZmxwXeRfMh","Flip"),
 ("9G579B3WJEpRDiB5Q3","Happy dance"),("du01oCd7HAGIfepv6h","Big jump"),("eXV1PI2KNHzc3B8WXa","Yeeew"),
 ("woaB39XsYsa7eEILsl","Send it"),("fjxyb50ECopVz7ElPL","Nailed it"),("56TW6jmxL6BfP4IMhA","Ski tricks"),
 ("roZjCXM6CSvp6","Ski trick"),("ufE5IOg1nUr0NbkBoT","Backflip"),("p4tkbspSWPTTum4Zkc","Park jump"),
 ("3o7TKRSGkMqOXdSU7K","Snowboard air"),("l3nWslgFc6s1l6IX6","Snowboard send"),
]
import json as _j
HESH_LOCAL = """<section id="hesh" class="card hesh"><header><div><h2>Hesh Corner</h2><p>Certified hesh content. Nothing important here.</p></div><span class="badge open" id="gifname">HESH</span></header>
<div class="gifbox"><video id="gifvid" autoplay muted loop playsinline preload="auto" aria-label="Random hesh gif"></video></div>
<p class="small"><button id="gifnext" type="button" class="gifbtn">Another one &#8635;</button> <a id="giflink" target="_blank" rel="noopener">Open on GIPHY</a> &middot; via GIPHY</p></section>
<style>.gifbox{max-width:560px;margin:12px auto;background:#000;border-radius:12px;overflow:hidden;display:flex;justify-content:center;min-height:200px}.gifbox video{display:block;max-width:100%;max-height:440px;width:auto;height:auto}.gifbtn{font:inherit;font-weight:700;color:var(--bg);background:var(--acc);border:0;border-radius:999px;padding:10px 16px;min-height:44px;cursor:pointer;margin-right:8px}</style>
<script>(function(){var G=__GIFS__,last=-1;function go(){var i;do{i=Math.floor(Math.random()*G.length)}while(i==last&&G.length>1);last=i;var g=G[i];var v=document.getElementById("gifvid");v.src="https://media.giphy.com/media/"+g[0]+"/giphy.mp4";v.play&&v.play().catch(function(){});document.getElementById("gifname").textContent=g[1].toUpperCase();document.getElementById("giflink").href="https://giphy.com/gifs/"+g[0];}go();document.getElementById("gifnext").addEventListener("click",go);})();</script>""".replace("__GIFS__", _j.dumps(GIFS))

BADGE={'alpental':('AL','#ff6b4a','#c2361b'),'summit':('SS','#3d9bff','#1857c4'),'baker':('MB','#9b7bff','#5a35d6'),'stevens':('SP','#2fd39a','#0f8a5f')}
def badge(rid,size=52):
    t,c1,c2=BADGE.get(rid,('??','#5cc8ff','#0a6fb0'))
    return (f'<svg class="logo" width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="g{rid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
            f'<rect width="64" height="64" rx="16" fill="url(#g{rid})"/><path d="M6 50 L22 26 L30 36 L40 18 L58 50 Z" fill="#fff" opacity=".28"/><path d="M36 24 L40 18 L44 24 L41 23 L40 25 L39 23 Z" fill="#fff"/>'
            f'<text x="32" y="56" text-anchor="middle" font-family="Segoe UI,system-ui,sans-serif" font-weight="900" font-size="15" fill="#fff" letter-spacing="1">{t}</text></svg>')
GOAT='<div class="ribbon">&#11088; Objectively the best mountain&trade; &#11088;</div><div class="sparkles" aria-hidden="true"><i>&#10024;</i><i>&#10024;</i><i>&#10024;</i><i>&#10024;</i></div>'
ICON="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"
e=html.escape
SHARED=len(sys.argv)>2 and sys.argv[2]=='shared'
d['resorts'].sort(key=lambda r:r['id']!='summit')
out=[]
for r in d['resorts']:
    stats=''.join(f'<div class="stat"><span>{e(k)}</span><b>{e(v)}</b></div>' for k,v in r['stats'])
    cams=''
    if r['cams']:
        feat=[c for c in r['cams'] if c[2]]
        rest=[c for c in r['cams'] if not c[2]]
        def card(c,f):
            u=camurl(r['id'],c[1]) if c[1] else None
            body=(f'<iframe src="{u}" loading="lazy" allow="autoplay; fullscreen" referrerpolicy="no-referrer-when-downgrade" title="{e(c[0])}"></iframe>' if u else '<div class="nocam">Open this cam on the resort site</div>')
            if SHARED and f and u:
                au=u+('&' if '?' in u else '?')+'autoplay=1&mute=1'
                return f'<figure class="cam feat"><figcaption><span class="tag">LIFT CAM</span>{e(c[0])} &middot; live</figcaption><iframe src="{au}" allow="autoplay; fullscreen; encrypted-media" allowfullscreen referrerpolicy="strict-origin-when-cross-origin" title="{e(c[0])}"></iframe></figure>'
            if SHARED:
                lk=u or camlink(r['id'])
                return f'<a class="camlink{" feat" if f else ""}" href="{lk}" target="_blank" rel="noopener"><span class="tag">{"LIFT CAM" if f else "CAM"}</span><b>{e(c[0])}</b><span class="go">Watch live &rarr;</span></a>'
            return f'<figure class="cam{" feat" if f else ""}"><figcaption><span class="tag">{"LIFT CAM" if f else "CAM"}</span>{e(c[0])}</figcaption>{body}</figure>'
        cams='<h3>Live cams</h3><div class="cams">'+''.join(card(c,True) for c in feat)+''.join(card(c,False) for c in rest if c[1] or SHARED)+'</div>'
        cams+=f'<p class="small">Cam blank? <a href="{camlink(r["id"])}" target="_blank" rel="noopener">Open the resort cam page</a>.</p>'
    else:
        cams='<h3>Live cams</h3><p class="nocamtxt">Mt. Baker does not publish a webcam page on its website, so there is no cam to show here.</p>'
    out.append(f'''<section id="{r['id']}" class="card{' goat' if r['id']=='summit' else ''}" style="--rc:{BADGE.get(r['id'],('','#5cc8ff'))[1]}">{GOAT if r['id']=='summit' else ''}<header><div class="rh">{('<span class="crown">&#128081;</span>' if r['id']=='summit' else '')}{badge(r['id'])}<div><h2>{e(r['name'])}{(' <span class="best">#1</span>') if r['id']=='summit' else ''}</h2><p>{e(r['sub'])}</p>{('<p class="brag">The undisputed king of the Cascades. Source: Brooks.</p>' if r['id']=='summit' else '<p class="notsummit">Not Summit.</p>')}</div></div><span class="badge {r['tone']}">{e(r['status'])}</span></header>
<div class="stats">{stats}</div><p class="note">{e(r['note'])}</p><p class="small">Source: {e(r['updated'])} · <a href="{r['link'][1]}" target="_blank" rel="noopener">{e(r['link'][0])}</a></p>{cams}</section>''')
nav=''.join(f'<a href="#{r["id"]}">{badge(r["id"],22)}{e(r["name"])}{" &#128081;" if r["id"]=="summit" else ""}</a>' for r in d['resorts'])+'<a href="#hesh">&#129305; Hesh</a>'
page=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="color-scheme" content="dark light"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Snow, lifts and live cams for Summit at Snoqualmie, Alpental, Mt. Baker and Stevens Pass. Updated twice a day."><meta name="theme-color" content="#0b3a5c"><meta property="og:title" content="Pow Report"><meta property="og:description" content="Snow, lifts and live cams for four Washington mountains. Updated twice a day."><meta name="apple-mobile-web-app-title" content="Pow Report"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-capable" content="yes"><link rel="icon" type="image/png" href="data:image/png;base64,{ICON}"><link rel="apple-touch-icon" href="data:image/png;base64,{ICON}"><title>Pow Report</title>
<style>
:root{{--bg:#0e1a24;--card:#16283a;--ink:#eaf2f8;--mut:#9fb4c6;--acc:#5cc8ff;--line:#244058;--bad:#ff8f6b;--good:#5fe3a1}}
@media (prefers-color-scheme:light){{:root{{--bg:#eef4f8;--card:#fff;--ink:#12212e;--mut:#51697c;--acc:#0a6fb0;--line:#d3e0ea;--bad:#b3411d;--good:#117a4a}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 "Segoe UI",system-ui,sans-serif}}
.wrap{{max-width:1100px;margin:0 auto;padding:20px 16px 48px}}
h1{{margin:0;font-size:1.9rem}}.top p{{margin:2px 0 14px;color:var(--mut)}}
nav{{position:sticky;top:0;z-index:5;background:var(--bg);padding:8px 0;display:flex;gap:8px;flex-wrap:wrap;border-bottom:1px solid var(--line);margin-bottom:18px}}
nav a{{color:var(--ink);text-decoration:none;background:var(--card);border:1px solid var(--line);padding:6px 14px;border-radius:999px;font-weight:600;font-size:.9rem}}nav a:hover{{border-color:var(--acc)}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px;margin-bottom:22px;scroll-margin-top:70px}}
.card header{{display:flex;justify-content:space-between;gap:12px;align-items:flex-start;flex-wrap:wrap}}
h2{{margin:0;font-size:1.5rem}}h3{{margin:18px 0 8px;font-size:1rem;color:var(--mut);text-transform:uppercase;letter-spacing:.06em}}header p{{margin:0;color:var(--mut)}}
.badge{{padding:5px 12px;border-radius:999px;font-weight:700;font-size:.8rem;border:1px solid}}.badge.closed{{color:var(--bad);border-color:var(--bad)}}.badge.open{{color:var(--good);border-color:var(--good)}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:16px 0}}
.stat{{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:10px 12px}}.stat span{{display:block;color:var(--mut);font-size:.78rem}}.stat b{{font-size:1.2rem}}
.note{{margin:6px 0}}.small{{color:var(--mut);font-size:.82rem;margin:6px 0}}a{{color:var(--acc)}}
.cams{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr));gap:14px}}
.cam{{margin:0;background:var(--bg);border:1px solid var(--line);border-radius:12px;overflow:hidden}}.cam.feat{{border-color:var(--acc)}}
figcaption{{padding:8px 12px;font-weight:600}}.tag{{background:var(--acc);color:#04202f;font-size:.68rem;font-weight:800;padding:2px 7px;border-radius:6px;margin-right:8px}}
a.camlink{{display:flex;align-items:center;gap:10px;background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--ink)}}a.camlink.feat{{border-color:var(--acc)}}a.camlink .go{{margin-left:auto;color:var(--acc);font-weight:600}}.camlink .tag{{margin:0}}
.cam.feat{{grid-column:1/-1}}
.small a{{display:inline-block;padding:8px 2px}}nav a{{min-height:36px;display:inline-flex;align-items:center}}
@media(prefers-reduced-motion:reduce){{#flyer,#rider{{animation:none!important}}}}
iframe{{display:block;width:100%;aspect-ratio:16/9;border:0;background:#000}}.nocam,.nocamtxt{{padding:24px;color:var(--mut)}}

.hero{{position:relative;overflow:hidden;background:linear-gradient(160deg,#0b3a5c 0%,#1a6fa3 45%,#7fc8f0 100%);color:#fff;padding:44px 16px 96px;text-align:center}}
.herotxt{{position:relative;z-index:2;max-width:760px;margin:0 auto}}.kicker{{margin:0 0 6px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:.78rem;opacity:.9}}
.hero h1{{font-size:clamp(2.4rem,7vw,4rem);font-weight:900;letter-spacing:-.02em;margin:0;text-shadow:0 4px 24px rgba(0,0,0,.25)}}.hero .sub{{margin:8px 0 16px;font-size:1.05rem;opacity:.95;color:#fff}}
.chip{{display:inline-block;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.45);backdrop-filter:blur(6px);padding:6px 14px;border-radius:999px;font-weight:600;font-size:.88rem}}
.ridge{{position:absolute;left:0;bottom:-1px;width:100%;height:110px;z-index:1}}
.flakes{{position:absolute;inset:0;background-image:radial-gradient(2px 2px at 20px 30px,#fff,transparent),radial-gradient(2px 2px at 120px 80px,#fff,transparent),radial-gradient(1.5px 1.5px at 200px 20px,#fff,transparent),radial-gradient(2.5px 2.5px at 300px 120px,#fff,transparent),radial-gradient(1.5px 1.5px at 360px 60px,#fff,transparent);background-size:400px 160px;opacity:.7;animation:snow 12s linear infinite}}
@keyframes snow{{from{{background-position:0 0}}to{{background-position:60px 160px}}}}
.wrap{{margin-top:-28px;position:relative;z-index:3}}
nav{{border-radius:999px;padding:8px;border:1px solid var(--line);background:color-mix(in srgb,var(--bg) 85%,transparent);backdrop-filter:blur(10px);justify-content:center;top:8px}}nav a{{gap:8px}}nav .logo{{border-radius:6px;flex:none}}
.card{{border-top:4px solid var(--rc,var(--acc));box-shadow:0 10px 30px rgba(0,0,0,.18);transition:transform .2s}}.rh{{display:flex;gap:14px;align-items:center}}.rh .logo{{flex:none;filter:drop-shadow(0 4px 10px rgba(0,0,0,.25))}}
h2{{font-weight:800;letter-spacing:-.01em}}.stat b{{font-size:1.35rem;font-weight:800}}.stat{{border-left:3px solid var(--rc,var(--acc))}}
.tag{{background:var(--rc,var(--acc))}}.cam.feat{{border-color:var(--rc,var(--acc))}}
@media(max-width:640px){{nav{{flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;border-radius:16px;scrollbar-width:none}}nav a{{flex:none}}}}
.goat{{scroll-margin-top:100px;position:relative;border:3px solid #f5c542;border-top:6px solid #f5c542;box-shadow:0 0 0 4px rgba(245,197,66,.25),0 18px 50px rgba(245,197,66,.35);background:linear-gradient(180deg,rgba(245,197,66,.14),transparent 140px),var(--card);padding-top:44px}}
.ribbon{{position:absolute;top:0;left:50%;transform:translate(-50%,-55%);background:linear-gradient(90deg,#f5c542,#ffe9a3,#f5c542);color:#4a3200;font-weight:900;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;padding:7px 16px;border-radius:999px;white-space:nowrap;box-shadow:0 6px 18px rgba(245,197,66,.5);animation:pulse 2.4s ease-in-out infinite}}
@keyframes pulse{{50%{{transform:translate(-50%,-55%) scale(1.06)}}}}
.goat .rh{{position:relative}}.crown{{position:absolute;left:12px;top:-26px;font-size:1.6rem;transform:rotate(-14deg);filter:drop-shadow(0 3px 4px rgba(0,0,0,.3))}}
.best{{display:inline-block;vertical-align:middle;background:#f5c542;color:#4a3200;font-size:.75rem;font-weight:900;padding:3px 9px;border-radius:8px;margin-left:6px;transform:rotate(-4deg)}}
.brag{{margin:2px 0 0!important;color:#c99a1a!important;font-weight:700;font-style:italic;font-size:.9rem}}.notsummit{{margin:2px 0 0!important;font-size:.78rem;opacity:.6;font-style:italic}}
.goat .stat{{border-left-color:#f5c542}}
.sparkles i{{position:absolute;font-style:normal;animation:twinkle 2s ease-in-out infinite;pointer-events:none}}.sparkles i:nth-child(1){{top:14px;right:18px}}.sparkles i:nth-child(2){{top:150px;right:28%;animation-delay:.5s}}.sparkles i:nth-child(3){{top:22px;left:44%;animation-delay:1s}}.sparkles i:nth-child(4){{bottom:18px;left:24px;animation-delay:1.5s}}
@keyframes twinkle{{0%,100%{{opacity:0;transform:scale(.6)}}50%{{opacity:1;transform:scale(1.15)}}}}
@media(max-width:640px){{.ribbon{{font-size:.66rem;padding:6px 12px}}}}
@media(prefers-reduced-motion:reduce){{.ribbon,.sparkles i{{animation:none}}}}
footer{{text-align:center;color:var(--mut);font-size:.85rem;padding:12px 0 8px}}
@media(prefers-reduced-motion:reduce){{.flakes{{animation:none}}}}
</style></head><body><div class="hero"><div class="flakes" aria-hidden="true"></div><svg class="ridge" viewBox="0 0 1200 160" preserveAspectRatio="none" aria-hidden="true"><path d="M0 160 L0 110 L120 70 L210 100 L330 30 L430 90 L520 60 L640 105 L760 20 L880 85 L980 55 L1090 95 L1200 60 L1200 160 Z" fill="var(--bg)" opacity=".55"/><path d="M0 160 L0 130 L160 95 L300 125 L450 80 L600 120 L780 70 L930 115 L1060 90 L1200 110 L1200 160 Z" fill="var(--bg)"/></svg>
<div class="herotxt"><p class="kicker">&#10052; Washington Cascades</p><h1>Pow Report</h1><p class="sub">Snow, lifts and live cams for four mountains, in one place.</p><span class="chip">Updated {e(d['generated'])}</span></div></div><div class="wrap"><nav>{nav}</nav>{''.join(out)}{HESH_LOCAL}<footer>Made by Brooks &middot; data from each resort's official report and NOAA &middot; refreshes twice a day</footer></div><script>if(location.hostname==='localhost'){{setInterval(function(){{fetch('/ping',{{cache:'no-store'}}).catch(function(){{}})}},30000)}}</script></body></html>'''
open(sys.argv[1] if len(sys.argv)>1 else 'pow.html','w',encoding='utf-8').write(page)
print(len(page))
