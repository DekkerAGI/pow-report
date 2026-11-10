"""Daily updater run by GitHub Actions. Fetches public resort data, updates data.json, builds site/index.html.
Every source is wrapped in try/except: if one fails, the last known numbers stay and the page says so."""
import json, re, sys, subprocess, urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

PT = ZoneInfo("America/Los_Angeles")
UA = {"User-Agent": "Mozilla/5.0 (pow-report daily updater)"}
BASE = "https://www.summitatsnoqualmie.com"

def get(url, as_json=True):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read().decode("utf-8", "replace")
    return json.loads(raw) if as_json else raw

def pt(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(PT)

def fmt_pt(iso):
    t = pt(iso)
    return t.strftime("%b %-d %-I:%M %p PT")

def inches(obj):
    try:
        return f'{float(obj["inches"]):g} in'
    except Exception:
        return None

def count(area_list, kind):
    open_n = total = 0
    for a in area_list:
        items = ((a.get(kind) or {}).get(kind[:-1]) or [])
        for it in items:
            total += 1
            if str(it.get("status", "")).strip().lower() == "open":
                open_n += 1
    return open_n, total

def find_resort(d, rid):
    return next(r for r in d["resorts"] if r["id"] == rid)

def set_stat(r, label, value):
    if value is None:
        return
    for s in r["stats"]:
        if s[0] == label:
            s[1] = value
            return
    r["stats"].append([label, value])

def summit_update(d):
    rep = get(f"{BASE}/api/reportpal?resortName=ss&useReportPal=true")
    areas = rep["facilities"]["areas"]["area"]
    by_name = {a["name"]: a for a in areas}
    locs = {l["name"]: l for l in rep["currentConditions"]["resortLocations"]["location"]}
    status = rep["operations"].get("resortStatus", "Closed")
    groups = {"alpental": [by_name.get("Alpental")], "summit": [by_name.get(n) for n in ("Summit West", "Summit Central", "Summit East")]}
    snowloc = {"alpental": locs.get("Alpental"), "summit": locs.get("Summit West")}
    for rid, grp in groups.items():
        grp = [g for g in grp if g]
        r = find_resort(d, rid)
        lo, lt = count(grp, "lifts")
        to, tt = count(grp, "trails")
        set_stat(r, "Lifts open", f"{lo} of {lt}")
        set_stat(r, "Trails open", f"{to} of {tt}")
        sl = snowloc[rid] or {}
        set_stat(r, "Base depth", inches(sl.get("base")))
        set_stat(r, "Season total", inches(sl.get("snowSeasonTotal")))
        set_stat(r, "New snow 24h", inches(sl.get("snow24Hours")))
        if lo > 0 or str(status).lower().startswith("open"):
            r["status"], r["tone"] = "OPEN", "open"
        else:
            r["status"], r["tone"] = "CLOSED", "closed"
        r["_feed_updated"] = fmt_pt(rep["updated"])
        r["_lifts_updated"] = fmt_pt(rep.get("liftsUpdated", rep["updated"]))

def weather_update(d):
    w = get(f"{BASE}/api/weather?weatherAPI=NOAAWeather&latitude=47.41988483523505&longitude=-121.4103412628174&location=&resortCode=ss")
    temp = w["currentConditions"]["temperature"]["fahrenheit"]
    days = []
    for f in w["forecasts"]:
        hi = (f.get("temperatureHigh") or {}).get("fahrenheit")
        if hi is None:
            continue
        lo = (f.get("temperatureLow") or {}).get("fahrenheit")
        day = pt(f["startDate"]).strftime("%a")
        txt = (f.get("conditionsSummaryShort") or "").lower()
        days.append(f"{day} {txt} {round(hi)}°F" + (f"/{round(lo)}°F" if lo is not None else ""))
    fc = "Forecast: " + "; ".join(days[:6]) + "." if days else ""
    for rid in ("alpental", "summit"):
        r = find_resort(d, rid)
        set_stat(r, "Temp (pass)", f"{round(temp)}°F")
        r["_weather_updated"] = fmt_pt(w["lastUpdate"])
        r["_forecast"] = fc

def roads_update(d):
    rd = get(f"{BASE}/api/reportpal-roads?resortName=ss")[0]
    e = rd["restrictionOne"]["restrictionText"]; wb = rd["restrictionTwo"]["restrictionText"]
    txt = f"I-90 {str(rd['roadCondition']).lower()}, " + ("no restrictions." if e.lower().startswith("no") and wb.lower().startswith("no") else f"eastbound: {e}; westbound: {wb}.")
    for rid in ("alpental", "summit"):
        find_resort(d, rid)["_roads"] = txt

def baker_update(d):
    html = get("https://www.mtbaker.us/snow-report/", as_json=False)
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))
    m = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4}) ?/? ?Last Updated (\d{1,2}:\d{2} ?[AP]M)", text)
    r = find_resort(d, "baker")
    if m:
        stamp = f"{m.group(1)} {m.group(2)}"
        try:
            age = (datetime.now(PT).date() - datetime.strptime(m.group(1), "%B %d, %Y").date()).days
        except Exception:
            age = None
        stale = age is not None and age >= 2
        r["warn"] = f"Heads up: Baker's own report is {age} days old. These numbers may be out of date; check the official link." if age is not None and age >= 1 else ""
        r["updated"] = f"Mt. Baker page, {stamp}" + (f" ({age} days old, stale)" if stale else "")
        if age is not None and age >= 2:
            r["note"] = "Baker's own report is stale, so these numbers are from its last update. Baker needs roughly 20 to 40 in of base plus a good forecast before opening. Check the official link for today."
    r["_baker_ok"] = bool(m)

def stevens_blog_update(d):
    posts = get("https://blog.stevenspass.com/wp-json/wp/v2/posts?per_page=1&_fields=date,link,title")
    p = posts[0]
    title = re.sub(r"<[^>]+>", "", p["title"]["rendered"]).replace("&#8211;", "-").replace("&amp;", "&").replace("&#8217;", "'")
    dt = datetime.fromisoformat(p["date"])
    find_resort(d, "stevens")["latest"] = {"title": title, "url": p["link"], "date": dt.strftime("%b %-d")}

def build_notes(d):
    for rid in ("alpental", "summit"):
        r = find_resort(d, rid)
        bits = [r.pop("_forecast", "") if rid == "summit" else "", r.pop("_roads", "")]
        r["note"] = " ".join(b for b in bits if b) or r["note"]
        fu = r.pop("_feed_updated", None); lu = r.pop("_lifts_updated", None); wu = r.pop("_weather_updated", None)
        if fu:
            r["updated"] = f"Resort feed {fu}" + (f"; weather {wu}" if wu else "") + (f"; lifts last updated {lu}" if lu and lu != fu else "")
    find_resort(d, "baker").pop("_baker_ok", None)

def main():
    d = json.load(open("data.json"))
    problems = []
    for fn in (summit_update, weather_update, roads_update, baker_update, stevens_blog_update):
        try:
            fn(d)
        except Exception as e:
            problems.append(f"{fn.__name__}: {e}")
    try:
        build_notes(d)
    except Exception as e:
        problems.append(f"build_notes: {e}")
    d["generated"] = datetime.now(PT).strftime("%a %b %-d, %Y · %-I:%M %p PT")
    if problems:
        print("PROBLEMS:", *problems, sep="\n  ")
        d["generated"] += " (some sources failed; showing last known values)"
    json.dump(d, open("data.json", "w"), indent=1, ensure_ascii=False)
    subprocess.check_call([sys.executable, "build.py", "site/index.html", "shared"])

if __name__ == "__main__":
    main()
