# photocellsapp.com

Website of Photocells, served by GitHub Pages at https://www.photocellsapp.com. The apex photocellsapp.com is the API server (Hetzner); it redirects browser page visits here.

All text lives in `i18n/<lang>.json` (en, es, de, fr, it, nl, pt-BR, pl, ru, ja, zh-Hans): the landing copy plus `privacy`, `support` and `terms`.
English is generated at the root, every other language in its own folder (`es/`, `de/`, `fr/`, `it/`, `nl/`, `pt-br/`, `pl/`, `ru/`, `ja/`, `zh-hans/`).
`landing.py` holds the home page markup, CSS (with per-language font overrides) and JS; `build_pages.py` holds the other pages, the language menu and the hreflang links.
Edit, then run `python3 build_pages.py` and push.
Images in `img/` (screenshots in `img/shots/<lang>-*.jpg`, made from the app's store captures), hero video in `media/`.
