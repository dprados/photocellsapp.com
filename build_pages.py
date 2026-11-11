#!/usr/bin/env python3
"""Generates the Photocells site (landing, privacy, support, terms) in every language.
All text lives in i18n/<lang>.json. English goes at the root, every other language in its own folder.
Run from this folder: python3 build_pages.py"""
import json
import os

from landing import landing

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.environ.get("SITE_OUT", HERE)
BASE = os.environ.get("SITE_BASE", "https://www.photocellsapp.com/")
MAIL = "dpappssupport@gmail.com"

# (code used in <html lang>, hreflang and i18n/<code>.json; output folder, "" = site root)
LANGS = [
    ("en", ""), ("es", "es"), ("de", "de"), ("fr", "fr"), ("it", "it"), ("nl", "nl"),
    ("pt-BR", "pt-br"), ("pl", "pl"), ("ru", "ru"), ("ja", "ja"), ("zh-Hans", "zh-hans"),
]
FOLDER = dict(LANGS)
T = {code: json.load(open(os.path.join(HERE, "i18n", code + ".json"), encoding="utf-8")) for code, _ in LANGS}
PAGES = ("index", "privacy", "support", "terms")

CSS = """:root{--accent:#FF2D2D;--accent-dark:#CC1A1A;--bg:#fff;--surface:#F2F2F7;--text:#111114;--muted:#6E6E73;--line:#D1D1D6;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{--bg:#000;--surface:#121214;--text:#fff;--muted:#9a9aa0;--line:#2C2C2E}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:17px/1.55 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Helvetica,Arial,sans-serif;overflow-wrap:break-word}
a{color:var(--accent)}main{max-width:760px;margin:0 auto;padding:24px 20px 64px}
header{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;max-width:760px;margin:0 auto;padding:18px 20px}
header a.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--text);font-weight:700;letter-spacing:.04em}
header img{width:36px;height:36px;border-radius:9px}header nav{display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px;margin-left:auto}nav a{font-size:15px}
@media (max-width:560px){header nav{order:3;width:100%;margin-left:0}header details.lang{margin-left:auto}}
h1{font-size:40px;line-height:1.1;margin:28px 0 12px;letter-spacing:-.01em;hyphens:auto;-webkit-hyphens:auto}h2{font-size:22px;margin:36px 0 8px}
.lead{font-size:20px;color:var(--muted)}
details{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin:10px 0}summary{font-weight:600;cursor:pointer}
footer{max-width:760px;margin:0 auto;padding:24px 20px 48px;color:var(--muted);font-size:14px;border-top:1px solid var(--line)}footer a{margin-right:14px}
details.lang{position:relative;margin:0;padding:0;border-radius:99px}
.lang summary{list-style:none;display:flex;align-items:center;gap:6px;padding:5px 10px;font-size:14px;font-weight:600;color:var(--text)}
.lang summary::-webkit-details-marker{display:none}
.lang summary:after{content:"";width:5px;height:5px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(45deg) translateY(-2px);margin-left:2px}
.lang ul{position:absolute;right:0;top:calc(100% + 6px);z-index:10;margin:0;padding:6px;list-style:none;min-width:200px;background:var(--bg);border:1px solid var(--line);border-radius:14px;box-shadow:0 14px 40px rgba(0,0,0,.18)}
.lang li a{display:block;padding:8px 12px;border-radius:8px;color:var(--text);text-decoration:none;font-size:15px}
.lang li a:hover{background:var(--surface)}.lang li a[aria-current]{color:var(--accent);font-weight:600}
"""

# Closes the language menu on an outside click or Escape.
LANG_JS = "document.addEventListener('click',function(e){document.querySelectorAll('details.lang[open]').forEach(function(d){if(!d.contains(e.target))d.removeAttribute('open')})});document.addEventListener('keydown',function(e){if(e.key==='Escape')document.querySelectorAll('details.lang[open]').forEach(function(d){d.removeAttribute('open')})});"

GLOBE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19M12 2.5c2.6 2.8 3.9 6 3.9 9.5s-1.3 6.7-3.9 9.5c-2.6-2.8-3.9-6-3.9-9.5s1.3-6.7 3.9-9.5z"/></svg>'


def file_of(name):
    return "" if name == "index" else name + ".html"


def url_of(code, name):
    folder = FOLDER[code]
    return BASE + (folder + "/" if folder else "") + file_of(name)


def rel_href(from_code, to_code, name):
    """Relative link from a page in one language to the same page in another."""
    if from_code == to_code:
        return file_of(name) or "./"
    prefix = "" if FOLDER[from_code] == "" else "../"
    folder = FOLDER[to_code]
    href = prefix + (folder + "/" if folder else "") + file_of(name)
    return href or "./"


def alternates(code, name):
    links = [f'<link rel="canonical" href="{url_of(code, name)}">']
    links += [f'<link rel="alternate" hreflang="{c}" href="{url_of(c, name)}">' for c, _ in LANGS]
    links.append(f'<link rel="alternate" hreflang="x-default" href="{url_of("en", name)}">')
    return "\n".join(links)


def switcher(code, name):
    t = T[code]
    items = "".join(
        f'<li><a href="{rel_href(code, c, name)}" hreflang="{c}" lang="{c}"{" aria-current=page" if c == code else ""}>{T[c]["lang_name"]}</a></li>'
        for c, _ in LANGS)
    short = code.split("-")[0].upper()
    return (f'<details class="lang"><summary aria-label="{t["lang_label"]}: {t["lang_name"]}">{GLOBE}{short}</summary>'
            f'<ul>{items}</ul></details>')


def page(code, name):
    t = T[code]
    p = t[name]
    prefix = "" if FOLDER[code] == "" else "../"
    nav = t["nav"]
    return f"""<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<link rel="icon" type="image/png" sizes="64x64" href="{prefix}img/favicon-64.png">
<link rel="icon" type="image/png" sizes="32x32" href="{prefix}img/favicon-32.png">
<link rel="apple-touch-icon" href="{prefix}img/apple-touch-icon.png">
<meta name="apple-itunes-app" content="app-id=6762532696">
{alternates(code, name)}
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:image" content="{BASE}img/icon-256.png">
<style>{CSS}</style>
</head>
<body>
<header><a class="brand" href="./"><img src="{prefix}img/icon-256.png" alt="">PHOTOCELLS</a>
<nav><a href="support.html">{nav[0]}</a><a href="privacy.html">{nav[1]}</a></nav>{switcher(code, name)}</header>
<main><h1>{p['h1']}</h1>{p['body']}</main>
<footer><a href="support.html">{nav[0]}</a> <a href="privacy.html">{nav[1]}</a> <a href="terms.html">{nav[2]}</a> <a href="mailto:{MAIL}">{MAIL}</a><p>{t['page_foot']}</p></footer>
<script>{LANG_JS}</script>
</body>
</html>
"""


if __name__ == "__main__":
    for code, folder in LANGS:
        out = os.path.join(OUT_ROOT, folder) if folder else OUT_ROOT
        os.makedirs(out, exist_ok=True)
        for name in PAGES:
            path = os.path.join(out, "index.html" if name == "index" else name + ".html")
            if name == "index":
                html = landing(code, T[code], BASE, "" if not folder else "../",
                               alternates(code, name), switcher(code, name), LANG_JS)
            else:
                html = page(code, name)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            print(os.path.relpath(path, HERE))
