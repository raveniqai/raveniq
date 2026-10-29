#!/usr/bin/env python3
"""Render the RavenIQ home page into docs/ (GitHub Pages). Standard library only.   python3 build.py
Apps come from apps.json; adding one adds a card. Nothing here names a person or a place."""
import html, json, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parent; OUT = ROOT / "docs"
SITE = "https://raveniq.ai"; EMAIL = "support@raveniq.ai"
apps = json.loads((ROOT / "apps.json").read_text(encoding="utf-8"))["apps"]
e = html.escape

def card(a):
    store = f'<a class="store" href="{e(a["store_url"])}">View on the App Store</a>' if a.get("store_url") else '<span class="soon">Coming to the App Store</span>'
    return f'''<article class="card" style="--app:{e(a["accent"])}">
  <div class="top"><h3>{e(a["name"])}</h3><span class="tag">{e(a["status"])}</span></div>
  <p class="tagline">{e(a["tagline"])}</p>
  <p>{e(a["blurb"])}</p>
  <p class="links"><a class="open" href="{e(a["url"])}">Learn more</a> {store}</p>
</article>'''

page = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>RavenIQ</title>
<meta name="description" content="RavenIQ makes small, calm, private iPhone apps. Forma coaches training and nutrition. Damla shows your cash flow.">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F5F7FA" media="(prefers-color-scheme: light)"><meta name="theme-color" content="#0A1420" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{SITE}/">
<link rel="icon" type="image/svg+xml" href="mark.svg"><link rel="icon" type="image/png" href="favicon-32.png" sizes="32x32"><link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="style.css">
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="wrap bar"><a class="brand" href="./"><img src="mark.svg" width="32" height="32" alt="">RavenIQ</a><nav aria-label="Main"><a href="#why">Mission</a><a href="#apps">Apps</a><a href="#approach">Approach</a><a href="#contact">Contact</a></nav></header>
<main id="main" class="wrap">
<section class="hero"><h1>Small, calm, private apps for your iPhone.</h1>
<p class="lead">RavenIQ builds focused tools that do one job well, keep your data on your phone, and stay out of your way.</p></section>
</main>
<section id="why" class="band"><div class="wrap inner">
<div class="statement"><p class="eyebrow">Our vision</p><p class="big">A growing family of small, well-made apps, each solving one real problem, that people trust because their data stays on their own phone.</p></div>
<div class="statement"><p class="eyebrow">Our mission</p><p class="mid">To build useful, trustworthy software that makes everyday life simpler and calmer.</p></div>
</div></section>
<main class="wrap">
<section id="apps"><h2>Apps</h2>
<div class="grid">
{chr(10).join(card(a) for a in apps)}
<article class="card more"><h3>More on the way</h3><p>New apps will appear here as they are ready. Each one starts from a real, everyday problem.</p></article>
</div></section>
<section id="approach"><h2>How we build</h2>
<ul class="points">
<li><strong>Your data stays with you.</strong> No accounts, no ads, no tracking, no analytics.</li>
<li><strong>Numbers you can trust.</strong> Calculations are done by ordinary, tested code. AI only helps with reading and explaining, and never invents the figures.</li>
<li><strong>Works offline.</strong> Nothing important waits for a server.</li>
<li><strong>Made for everyone.</strong> Large text, VoiceOver, light and dark.</li>
</ul></section>
<section id="contact"><h2>Contact</h2>
<p>Questions, feedback or a bug: <span class="email">{EMAIL}</span></p></section>
</main>
<footer class="wrap foot"><p>&copy; RavenIQ. Apps are information tools, not medical or financial advice.</p></footer>
</body></html>'''

css = '''/* One stylesheet, system fonts, no external resources. */
:root{--bg:#F5F7FA;--surface:#FFF;--text:#101A26;--muted:#4A5868;--line:#D8DFE8;--accent:#0B6E5B;--band:#0E1B2B;--band-text:#F2F7FA;--band-muted:#B7C6D3;--band-accent:#4FD1B0;--font:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
@media (prefers-color-scheme:dark){:root{--bg:#0A1420;--surface:#122030;--text:#E9F1F6;--muted:#9DB0BF;--line:#243548;--accent:#4FD1B0;--band:#122A3F;--band-text:#F2F7FA;--band-muted:#B7C6D3;--band-accent:#4FD1B0}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:1rem/1.6 var(--font)}
.wrap{width:100%;max-width:56rem;margin:0 auto;padding-inline:1rem}
a{color:var(--accent);text-underline-offset:.15em}:focus-visible{outline:3px solid var(--accent);outline-offset:2px;border-radius:4px}
.skip{position:absolute;left:-999px;background:var(--surface);padding:.75rem 1rem}.skip:focus{left:0;z-index:5}
.bar{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.25rem 1rem;padding-block:.5rem}
.brand{display:inline-flex;align-items:center;gap:.6rem;min-height:44px;font-weight:800;font-size:1.2rem;letter-spacing:.01em;color:var(--text);text-decoration:none}.brand img{border-radius:8px}
nav{display:flex;flex-wrap:wrap}nav a{display:inline-flex;align-items:center;min-height:44px;padding:0 .7rem;color:var(--text);text-decoration:none;border-radius:8px}nav a:hover{color:var(--accent)}
main{padding-block:1rem 3rem}
h1,h2,h3{line-height:1.2;text-wrap:balance}
.hero{padding-block:3rem 1.5rem}h1{font-size:clamp(2rem,7vw,3.4rem);margin:0 0 1rem;max-width:20ch}.lead{font-size:1.2rem;color:var(--muted);max-width:36rem;margin:0}
h2{font-size:1.5rem;margin:2.6rem 0 1rem}h3{font-size:1.25rem;margin:0}
.grid{display:grid;gap:1rem;grid-template-columns:1fr}@media(min-width:44rem){.grid{grid-template-columns:1fr 1fr}.more{grid-column:1/-1}}
.card{background:var(--surface);border:1px solid var(--line);border-top:5px solid var(--app,var(--line));border-radius:16px;padding:1.2rem;min-width:0}
.card p{margin:.6rem 0 0}.top{display:flex;justify-content:space-between;align-items:center;gap:.5rem}
.tag{font-size:.78rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:.15rem .6rem}
.tagline{font-weight:600}.links{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;margin-top:1rem!important}
.open{display:inline-flex;align-items:center;min-height:44px;padding:0 1.1rem;background:var(--app,var(--accent));color:#fff;font-weight:700;border-radius:12px;text-decoration:none}
.store,.soon{color:var(--muted);font-size:.92rem}.more{border-top-color:var(--line);border-style:dashed}
.duo{display:grid;gap:1rem;grid-template-columns:1fr}@media(min-width:44rem){.duo{grid-template-columns:1fr 1fr}}
.band{background:var(--band);color:var(--band-text);margin-block:1.5rem 0;padding-block:3.5rem}
.inner{display:grid;gap:2.5rem}@media(min-width:48rem){.inner{grid-template-columns:3fr 2fr;gap:4rem;align-items:start}}
.statement p{margin:0}.eyebrow{font-size:.8rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--band-accent);margin-bottom:.8rem!important}
.big{font-size:clamp(1.55rem,4.2vw,2.35rem);line-height:1.25;font-weight:700;text-wrap:balance}
.mid{font-size:clamp(1.15rem,2.6vw,1.45rem);line-height:1.4;color:var(--band-muted);text-wrap:balance}
.points{padding-left:1.2rem}.points li{margin-bottom:.6rem}.email{font-weight:700;user-select:all}
.foot{border-top:1px solid var(--line);padding-block:1.2rem 2rem;color:var(--muted);font-size:.9rem}
'''
OUT.mkdir(exist_ok=True)
(OUT / "index.html").write_text(page, encoding="utf-8"); (OUT / "style.css").write_text(css, encoding="utf-8")
(OUT / "404.html").write_text(page.replace("<title>RavenIQ</title>", '<title>Page not found - RavenIQ</title><base href="/">').replace('<section class="hero"><h1>Small, calm, private apps for your iPhone.</h1>', '<section class="hero"><h1>That page does not exist.</h1><p class="lead"><a href="./">Go to the RavenIQ home page</a></p><span hidden>').replace("</p></section>\n<section id=\"apps\">", "</p></span></section>\n<section id=\"apps\">",1), encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n"); (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE}/</loc></url></urlset>\n')
(OUT / "CNAME").write_text("raveniq.ai\n")
for f in ["mark.svg", "favicon-32.png", "apple-touch-icon.png"]: shutil.copy(ROOT / "assets" / f, OUT / f)
print("built", len(apps), "apps")
