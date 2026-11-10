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
 ("ufE5IOg1nUr0NbkBoT","Ski backflip","https://giphy.com/gifs/stompittutorials-skiing-backflip-stompit-ufE5IOg1nUr0NbkBoT"),
 ("p4tkbspSWPTTum4Zkc","Terrain park ski jump","https://giphy.com/gifs/sunshinevillageresort-terrain-park-laps-rat-p4tkbspSWPTTum4Zkc"),
 ("3o7TKRSGkMqOXdSU7K","Snowboard air","https://giphy.com/gifs/redbull-red-bull-snowboarding-3o7TKRSGkMqOXdSU7K"),
 ("l3nWslgFc6s1l6IX6","Snowboard send","https://giphy.com/gifs/redbull-snow-winter-snowboard-l3nWslgFc6s1l6IX6"),
]
import json as _j
HESH_LOCAL = """<section id="hesh" class="card hesh"><header><div><h2>Hesh Corner</h2><p>Certified hesh content. Nothing important here.</p></div><span class="badge open" id="gifname">TODAY</span></header>
<div class="gifbox"><iframe id="gifframe" title="Hesh gif of the day" allow="autoplay" loading="lazy"></iframe></div>
<p class="small">Gif of the day, rotates daily. <a id="giflink" target="_blank" rel="noopener">Open on GIPHY</a> &middot; via GIPHY</p></section>
<style>.gifbox{max-width:520px;margin:12px auto;aspect-ratio:16/10;background:#000;border-radius:12px;overflow:hidden}.gifbox iframe{width:100%;height:100%;aspect-ratio:auto}</style>
<script>(function(){var G=__GIFS__;var d=new Date();var day=Math.floor((d-new Date(d.getFullYear(),0,0))/864e5);var g=G[day%G.length];document.getElementById("gifframe").src="https://giphy.com/embed/"+g[0];document.getElementById("gifname").textContent=g[1].toUpperCase();document.getElementById("giflink").href=g[2];})();</script>""".replace("__GIFS__", _j.dumps(GIFS))
e=html.escape
SHARED=len(sys.argv)>2 and sys.argv[2]=='shared'
def warn(r):
    return f'<p class="warn">{e(r["warn"])}</p>' if r.get('warn') else ''
def latest(r):
    l=r.get('latest')
    if not l: return ''
    return f'<p class="latest"><b>Latest from the resort:</b> <a href="{e(l["url"])}" target="_blank" rel="noopener">{e(l["title"])}</a> <span class="small">({e(l["date"])})</span></p>'
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
            if SHARED:
                lk=u or camlink(r['id'])
                return f'<a class="camlink{" feat" if f else ""}" href="{lk}" target="_blank" rel="noopener"><span class="tag">{"LIFT CAM" if f else "CAM"}</span><b>{e(c[0])}</b><span class="go">Watch live &rarr;</span></a>'
            return f'<figure class="cam{" feat" if f else ""}"><figcaption><span class="tag">{"LIFT CAM" if f else "CAM"}</span>{e(c[0])}</figcaption>{body}</figure>'
        cams='<h3>Live cams</h3><div class="cams">'+''.join(card(c,True) for c in feat)+''.join(card(c,False) for c in rest if c[1] or SHARED)+'</div>'
        cams+=f'<p class="small">Cam blank? <a href="{camlink(r["id"])}" target="_blank" rel="noopener">Open the resort cam page</a>.</p>'
    else:
        cams='<h3>Live cams</h3><p class="nocamtxt">Mt. Baker does not publish a webcam page on its website, so there is no cam to show here.</p>'
    out.append(f'''<section id="{r['id']}" class="card"><header><div><h2>{e(r['name'])}</h2><p>{e(r['sub'])}</p></div><span class="badge {r['tone']}">{e(r['status'])}</span></header>
<div class="stats">{stats}</div>{warn(r)}<p class="note">{e(r['note'])}</p>{latest(r)}<p class="small">Source: {e(r['updated'])} · <a href="{r['link'][1]}" target="_blank" rel="noopener">{e(r['link'][0])}</a></p>{cams}</section>''')
nav=''.join(f'<a href="#{r["id"]}">{e(r["name"])}</a>' for r in d['resorts'])
page=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="color-scheme" content="dark light"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pow Report</title>
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
.warn{{margin:10px 0 0;padding:8px 12px;border:1px solid var(--bad);border-radius:10px;color:var(--bad);font-weight:600}}.latest{{margin:8px 0}}.note{{margin:6px 0}}.small{{color:var(--mut);font-size:.82rem;margin:6px 0}}a{{color:var(--acc)}}
.cams{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr));gap:14px}}
.cam{{margin:0;background:var(--bg);border:1px solid var(--line);border-radius:12px;overflow:hidden}}.cam.feat{{border-color:var(--acc)}}
figcaption{{padding:8px 12px;font-weight:600}}.tag{{background:var(--acc);color:#04202f;font-size:.68rem;font-weight:800;padding:2px 7px;border-radius:6px;margin-right:8px}}
a.camlink{{display:flex;align-items:center;gap:10px;background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--ink)}}a.camlink.feat{{border-color:var(--acc)}}a.camlink .go{{margin-left:auto;color:var(--acc);font-weight:600}}.camlink .tag{{margin:0}}
@media(min-width:760px){{.cam.feat{{grid-column:span 2}}}}
.small a{{display:inline-block;padding:8px 2px}}nav a{{min-height:36px;display:inline-flex;align-items:center}}
@media(prefers-reduced-motion:reduce){{#flyer,#rider{{animation:none!important}}}}
iframe{{display:block;width:100%;aspect-ratio:16/9;border:0;background:#000}}.nocam,.nocamtxt{{padding:24px;color:var(--mut)}}
</style></head><body><div class="wrap"><div class="top"><h1>Pow Report</h1><p>Updated {e(d['generated'])} · four mountains · courtesy of Brooks · {'tap a cam to watch it live' if SHARED else 'live cams play right here'}</p></div>
<nav>{nav}</nav>{''.join(out)}{HESH if SHARED else HESH_LOCAL}</div><script>if(location.hostname==='localhost'){{setInterval(function(){{fetch('/ping',{{cache:'no-store'}}).catch(function(){{}})}},30000)}}</script></body></html>'''
open(sys.argv[1] if len(sys.argv)>1 else 'pow.html','w',encoding='utf-8').write(page)
print(len(page))
