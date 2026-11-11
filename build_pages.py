#!/usr/bin/env python3
"""Generates the Photocells site (landing, privacy, support, terms) in English and Spanish.
Run from this folder: python3 build_pages.py"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.environ.get("SITE_OUT", HERE)
BASE = os.environ.get("SITE_BASE", "https://www.photocellsapp.com/")
APP_STORE = "https://apps.apple.com/app/id6762532696"
PLAY = "https://play.google.com/store/apps/details?id=com.dprados.photocells"
MAIL = "dpappssupport@gmail.com"

CSS = """:root{--accent:#FF2D2D;--accent-dark:#CC1A1A;--bg:#fff;--surface:#F2F2F7;--text:#111114;--muted:#6E6E73;--line:#D1D1D6;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{--bg:#000;--surface:#121214;--text:#fff;--muted:#9a9aa0;--line:#2C2C2E}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:17px/1.55 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent)}main{max-width:760px;margin:0 auto;padding:24px 20px 64px}
header{display:flex;align-items:center;justify-content:space-between;max-width:760px;margin:0 auto;padding:18px 20px}
header a.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--text);font-weight:700;letter-spacing:.04em}
header img{width:36px;height:36px;border-radius:9px}nav a{margin-left:14px;font-size:15px}
h1{font-size:40px;line-height:1.1;margin:28px 0 12px;letter-spacing:-.01em}h2{font-size:22px;margin:36px 0 8px}
.lead{font-size:20px;color:var(--muted)}.hero{text-align:center;padding:24px 0 8px}.hero img{width:128px;height:128px;border-radius:28px;box-shadow:0 10px 40px rgba(255,45,45,.35)}
.cta{display:inline-block;margin:10px 6px;padding:14px 22px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent-dark));color:#fff;text-decoration:none;font-weight:600}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:28px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px}.card h3{margin:0 0 6px;font-size:17px}.card p{margin:0;color:var(--muted);font-size:15px}
details{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin:10px 0}summary{font-weight:600;cursor:pointer}
footer{max-width:760px;margin:0 auto;padding:24px 20px 48px;color:var(--muted);font-size:14px;border-top:1px solid var(--line)}footer a{margin-right:14px}
"""

T = {
    "en": {
        "lang": "en", "other": ("es", "Español"),
        "nav": ("Support", "Privacy", "Terms"),
        "foot": "Made by Diego Prados, an independent developer. © 2026 Diego Prados. Apple, iPhone and App Store are trademarks of Apple Inc. Google Play is a trademark of Google LLC.",
        "index": {
            "title": "Photocells – Timing gates from your phone's camera",
            "desc": "Photocells turns your phone's camera into a timing gate: automatic laps, splits and speed, accurate to the thousandth of a second.",
            "h1": "Your phone is a timing gate",
            "lead": "Photocells sees the moment an athlete crosses the line and records the time by itself. No stopwatch, no tapping.",
            "cta": ("Download on the App Store", "Get it on Google Play"),
            "cards": [
                ("Automatic timing", "Line up the red line with the crossing. Every pass is recorded instantly, lap after lap."),
                ("One or many phones", "Laps with a single phone, or start, splits and finish with several phones synced by a 4-digit code."),
                ("Speed and splits", "Lap and segment times, best run and speed in km/h, mph or m/s."),
                ("History by athlete", "Athletes and comments for each session, filters, and CSV or PDF export."),
                ("Private", "The camera image is analysed on the device. Nothing is recorded or uploaded. No account, no ads."),
                ("Photocells Pro", "Create sessions with a 7-day free trial. Joining a session is free."),
            ],
        },
        "privacy": {
            "title": "Privacy policy – Photocells",
            "desc": "What Photocells does with your data: camera frames never leave the device, no account, no ads, no tracking.",
            "h1": "Privacy policy",
            "body": f"""<p class="lead">Short version: Photocells has no account, no ads and no tracking. The camera image never leaves your phone.</p>
<h2>Camera</h2><p>Photocells uses the camera to detect when someone crosses the line. Frames are analysed in memory on your device. To let you check each crossing, the app keeps the frame of each crossing in memory while the session and its summary are open, and discards it when you leave them. No photo or video is saved to your device, your history or iCloud, or sent anywhere.</p>
<h2>Sessions and our server</h2><p>To synchronise the phones of a session, Photocells uses our server (photocellsapp.com). It stores what a session needs to work: its type, the distances you enter, the participating devices and the crossing times. Devices are identified with a random token created by the app; it is not linked to your name, email, Apple Account or Google account. Data travels encrypted (HTTPS/WSS). You can ask us to delete the sessions of your device by writing to <a href="mailto:{MAIL}">{MAIL}</a>.</p>
<h2>Athletes and comments</h2><p>The athlete names and comments you add to a session are stored only on your device. They are never sent to our server. On iPhone, your history is copied to your private iCloud database (Apple's iCloud, under your account) so it is available on your other devices and after a reinstall; you can turn this off in iOS Settings → your name → iCloud. On Android, it is included in your phone's backup if you have backups enabled.</p>
<h2>Purchases</h2><p>Subscriptions are processed by Apple (App Store) or Google (Google Play). We don't receive your payment details; the app only checks whether a subscription is active.</p>
<h2>What we don't do</h2><p>No analytics or advertising SDKs, no tracking across apps or websites, no location, no contacts, no sale of data.</p>
<h2>Children</h2><p>Photocells is a general-audience sports tool and does not knowingly collect personal data from children.</p>
<h2>Contact</h2><p>Diego Prados, independent developer · <a href="mailto:{MAIL}">{MAIL}</a>. Last updated: 11 November 2026.</p>""",
        },
        "support": {
            "title": "Support – Photocells",
            "desc": "Help with Photocells: setting up the camera, sessions with several phones, subscriptions and restoring purchases.",
            "h1": "Support",
            "body": f"""<p class="lead">Can't find your answer? Write to <a href="mailto:{MAIL}">{MAIL}</a>. A real person replies.</p>
<h2>Getting good times</h2>
<details><summary>Where should I put the phone?</summary><p>At the side of the lane, at hip height if possible, pointing across the track. Line up the red line with the crossing. Keep the background still (avoid trees moving in the wind or passing traffic right behind the line).</p></details>
<details><summary>Sun and shade</summary><p>Exposure is locked when the session starts. Avoid placing the line where the light changes a lot (from strong sun to deep shade). Before the athlete starts, check that the indicator at the top of the session shows DETECTOR ACTIVO in green.</p></details>
<details><summary>A crossing was missed or an extra one appeared</summary><p>Open the session settings and use "Discard last cut" for an extra one. Check that the phone is stable and the detector indicator is green (DETECTOR ACTIVO) before the athlete arrives.</p></details>
<h2>Sessions</h2>
<details><summary>How do several phones work together?</summary><p>Create a session on one phone and share the 4-digit code. The others tap JOIN, enter the code and choose their position. Times are synchronised through our server, so every phone needs an internet connection.</p></details>
<details><summary>Athletes and comments</summary><p>Add athletes when you create a session or later from its summary, separated by commas. In History, tap an athlete to see only their sessions. This information stays on your devices.</p></details>
<h2>Subscription</h2>
<details><summary>What is free?</summary><p>Joining a session is free. Creating sessions requires Photocells Pro (7-day free trial, then monthly or yearly).</p></details>
<details><summary>Restore a purchase</summary><p>Open Settings in the app and tap Restore, signed in with the same Apple Account or Google account you used to subscribe.</p></details>
<details><summary>Manage or cancel</summary><p>iPhone: Settings app → your name → Subscriptions. Android: Google Play → Profile → Payments and subscriptions → Subscriptions. Cancel at least 24 hours before renewal.</p></details>""",
        },
        "terms": {
            "title": "Terms of use – Photocells",
            "desc": "Terms of use of the Photocells app and the Photocells Pro subscription.",
            "h1": "Terms of use",
            "body": f"""<p>By using Photocells you agree to these terms. On iPhone, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard Licensed Application End User License Agreement</a> also applies.</p>
<h2>The service</h2><p>Photocells measures times with the device camera and synchronises sessions through our server. Times depend on the device, its position, the light and the scene; they are meant for training and are not certified for official competition. We try to keep the service available but can't guarantee it will be uninterrupted.</p>
<h2>Photocells Pro</h2><p>Creating sessions requires an auto-renewing subscription (monthly or yearly) with a 7-day free trial for new subscribers. Payment is charged to your Apple Account or Google Play account when you confirm the purchase (or when the trial ends). It renews automatically unless cancelled at least 24 hours before the end of the current period. You can manage or cancel it in your App Store or Google Play account settings. Refunds are handled by Apple or Google under their policies.</p>
<h2>Acceptable use</h2><p>Don't misuse the service, interfere with other users' sessions or try to access data that isn't yours.</p>
<h2>Liability</h2><p>The app is provided "as is". To the extent permitted by law, we are not liable for indirect damages or for decisions made from the measured times.</p>
<h2>Changes and contact</h2><p>We may update these terms; the current version is always on this page. Questions: <a href="mailto:{MAIL}">{MAIL}</a>. Last updated: 11 November 2026.</p>""",
        },
    },
    "es": {
        "lang": "es", "other": ("", "English"),
        "nav": ("Soporte", "Privacidad", "Términos"),
        "foot": "Hecho por Diego Prados, desarrollador independiente. © 2026 Diego Prados. Apple, iPhone y App Store son marcas de Apple Inc. Google Play es una marca de Google LLC.",
        "index": {
            "title": "Photocells – Fotocélulas con la cámara de tu móvil",
            "desc": "Photocells convierte la cámara de tu móvil en una fotocélula: vueltas, parciales y velocidad automáticos, con precisión de milésimas.",
            "h1": "Tu móvil, una fotocélula",
            "lead": "Photocells detecta cuándo el atleta cruza la línea y guarda el tiempo solo. Sin cronómetro y sin pulsar nada.",
            "cta": ("Descargar en el App Store", "Disponible en Google Play"),
            "cards": [
                ("Cronometraje automático", "Alinea la línea roja con el paso. Cada cruce queda registrado al instante, vuelta a vuelta."),
                ("Uno o varios móviles", "Vueltas con un solo móvil, o salida, parciales y meta con varios móviles sincronizados con un código de 4 cifras."),
                ("Velocidad y parciales", "Tiempos por vuelta y segmento, mejor marca y velocidad en km/h, mph o m/s."),
                ("Historial por atleta", "Atletas y comentarios en cada sesión, filtros y exportación a CSV o PDF."),
                ("Privado", "La imagen de la cámara se analiza en el dispositivo. No se graba ni se envía nada. Sin cuenta y sin anuncios."),
                ("Photocells Pro", "Crea sesiones con 7 días de prueba gratis. Unirse a una sesión es gratis."),
            ],
        },
        "privacy": {
            "title": "Política de privacidad – Photocells",
            "desc": "Qué hace Photocells con tus datos: la imagen de la cámara no sale del dispositivo, sin cuenta, sin anuncios y sin seguimiento.",
            "h1": "Política de privacidad",
            "body": f"""<p class="lead">En resumen: Photocells no tiene cuenta, ni anuncios, ni seguimiento. La imagen de la cámara nunca sale de tu móvil.</p>
<h2>Cámara</h2><p>Photocells usa la cámara para detectar cuándo alguien cruza la línea. Las imágenes se analizan en memoria en tu dispositivo. Para que puedas comprobar cada paso, la app conserva en memoria el fotograma de cada paso mientras están abiertas la sesión y su resumen, y lo descarta al salir. No se guarda ninguna foto ni vídeo en tu dispositivo, en el historial ni en iCloud, ni se envía a ningún sitio.</p>
<h2>Sesiones y nuestro servidor</h2><p>Para sincronizar los móviles de una sesión, Photocells usa nuestro servidor (photocellsapp.com). Guarda lo necesario para que la sesión funcione: el tipo, las distancias que introduces, los dispositivos participantes y los tiempos de paso. Los dispositivos se identifican con un token aleatorio creado por la app, que no está ligado a tu nombre, correo, cuenta de Apple o de Google. Los datos viajan cifrados (HTTPS/WSS). Puedes pedirnos que borremos las sesiones de tu dispositivo escribiendo a <a href="mailto:{MAIL}">{MAIL}</a>.</p>
<h2>Atletas y comentarios</h2><p>Los nombres de atletas y los comentarios que añades a una sesión se guardan solo en tu dispositivo y nunca se envían a nuestro servidor. En iPhone, tu historial se copia en tu base de datos privada de iCloud (iCloud de Apple, en tu cuenta) para tenerlo en tus otros dispositivos y tras reinstalar; puedes desactivarlo en Ajustes de iOS → tu nombre → iCloud. En Android, se incluye en la copia de seguridad del móvil si la tienes activada.</p>
<h2>Compras</h2><p>Las suscripciones las gestionan Apple (App Store) o Google (Google Play). No recibimos tus datos de pago; la app solo comprueba si hay una suscripción activa.</p>
<h2>Lo que no hacemos</h2><p>Sin SDK de analítica ni de publicidad, sin seguimiento entre apps o webs, sin ubicación, sin contactos y sin venta de datos.</p>
<h2>Menores</h2><p>Photocells es una herramienta deportiva para todos los públicos y no recoge a sabiendas datos personales de menores.</p>
<h2>Contacto</h2><p>Diego Prados, desarrollador independiente · <a href="mailto:{MAIL}">{MAIL}</a>. Última actualización: 11 de noviembre de 2026.</p>""",
        },
        "support": {
            "title": "Soporte – Photocells",
            "desc": "Ayuda con Photocells: colocar la cámara, sesiones con varios móviles, suscripción y restaurar compras.",
            "h1": "Soporte",
            "body": f"""<p class="lead">¿No encuentras tu respuesta? Escribe a <a href="mailto:{MAIL}">{MAIL}</a>. Te contesta una persona.</p>
<h2>Tiempos fiables</h2>
<details><summary>¿Dónde pongo el móvil?</summary><p>A un lado de la calle, a la altura de la cadera si puedes, apuntando de lado a lado de la pista. Alinea la línea roja con el paso. Mejor un fondo quieto (evita árboles moviéndose con el viento o tráfico justo detrás de la línea).</p></details>
<details><summary>Sol y sombra</summary><p>La exposición se bloquea al empezar la sesión. Evita poner la línea donde la luz cambia mucho (de sol fuerte a sombra cerrada). Antes de que salga el atleta, comprueba que el indicador de arriba de la sesión marca DETECTOR ACTIVO en verde.</p></details>
<details><summary>No se registró un paso o apareció uno de más</summary><p>En los ajustes de la sesión usa «Descartar último corte» para quitar uno de más. Comprueba que el móvil está estable y que el indicador está en verde (DETECTOR ACTIVO) antes de que llegue el atleta.</p></details>
<h2>Sesiones</h2>
<details><summary>¿Cómo funcionan varios móviles juntos?</summary><p>Crea la sesión en un móvil y comparte el código de 4 cifras. Los demás pulsan UNIRSE, introducen el código y eligen su posición. Los tiempos se sincronizan con nuestro servidor, así que todos necesitan conexión a internet.</p></details>
<details><summary>Atletas y comentarios</summary><p>Añade atletas al crear la sesión o después desde su resumen, separados por comas. En el Historial, toca un atleta para ver solo sus sesiones. Esta información se queda en tus dispositivos.</p></details>
<h2>Suscripción</h2>
<details><summary>¿Qué es gratis?</summary><p>Unirse a una sesión es gratis. Crear sesiones requiere Photocells Pro (7 días de prueba gratis y después mensual o anual).</p></details>
<details><summary>Restaurar una compra</summary><p>Abre Ajustes en la app y pulsa Restaurar, con la misma cuenta de Apple o de Google con la que te suscribiste.</p></details>
<details><summary>Gestionar o cancelar</summary><p>iPhone: app Ajustes → tu nombre → Suscripciones. Android: Google Play → Perfil → Pagos y suscripciones → Suscripciones. Cancela al menos 24 horas antes de la renovación.</p></details>""",
        },
        "terms": {
            "title": "Términos de uso – Photocells",
            "desc": "Términos de uso de la app Photocells y de la suscripción Photocells Pro.",
            "h1": "Términos de uso",
            "body": f"""<p>Al usar Photocells aceptas estos términos. En iPhone también se aplica el <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrato de licencia de usuario final estándar</a> de Apple.</p>
<h2>El servicio</h2><p>Photocells mide tiempos con la cámara del dispositivo y sincroniza las sesiones con nuestro servidor. Los tiempos dependen del dispositivo, su colocación, la luz y la escena; están pensados para entrenar y no están homologados para competición oficial. Intentamos mantener el servicio disponible, pero no podemos garantizar que no tenga interrupciones.</p>
<h2>Photocells Pro</h2><p>Crear sesiones requiere una suscripción de renovación automática (mensual o anual) con 7 días de prueba gratis para nuevos suscriptores. El pago se carga a tu cuenta de Apple o de Google Play al confirmar la compra (o al terminar la prueba). Se renueva automáticamente salvo que la canceles al menos 24 horas antes del final del periodo. Puedes gestionarla o cancelarla en los ajustes de tu cuenta del App Store o de Google Play. Los reembolsos los gestionan Apple o Google según sus políticas.</p>
<h2>Uso aceptable</h2><p>No hagas un uso abusivo del servicio, no interfieras en sesiones de otros ni intentes acceder a datos que no son tuyos.</p>
<h2>Responsabilidad</h2><p>La app se ofrece «tal cual». En la medida en que lo permita la ley, no respondemos de daños indirectos ni de decisiones tomadas a partir de los tiempos medidos.</p>
<h2>Cambios y contacto</h2><p>Podemos actualizar estos términos; la versión vigente está siempre en esta página. Dudas: <a href="mailto:{MAIL}">{MAIL}</a>. Última actualización: 11 de noviembre de 2026.</p>""",
        },
    },
}


def page(lang, name):
    t = T[lang]
    p = t[name]
    prefix = "" if lang == "en" else "../"
    folder = "" if lang == "en" else lang + "/"
    file = "index.html" if name == "index" else name + ".html"
    url = BASE + folder + (file if name != "index" else "")
    alt_en = BASE + (file if name != "index" else "")
    alt_es = BASE + "es/" + (file if name != "index" else "")
    other_code, other_label = t["other"]
    other_href = (prefix + (other_code + "/" if other_code else "")) + (file if name != "index" else "")
    if name == "index":
        cards = "".join(f'<div class="card"><h3>{h}</h3><p>{d}</p></div>' for h, d in p["cards"])
        body = f"""<section class="hero"><img src="{prefix}img/icon-256.png" alt="Photocells"><h1>{p['h1']}</h1><p class="lead">{p['lead']}</p>
<a class="cta" href="{APP_STORE}">{p['cta'][0]}</a><a class="cta" href="{PLAY}">{p['cta'][1]}</a></section><div class="cards">{cards}</div>"""
    else:
        body = f"<h1>{p['h1']}</h1>{p['body']}"
    nav = t["nav"]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<link rel="icon" type="image/png" sizes="64x64" href="{prefix}img/favicon-64.png">
<link rel="icon" type="image/png" sizes="32x32" href="{prefix}img/favicon-32.png">
<link rel="apple-touch-icon" href="{prefix}img/apple-touch-icon.png">
<meta name="apple-itunes-app" content="app-id=6762532696">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="es" href="{alt_es}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:image" content="{BASE}img/icon-256.png">
<style>{CSS}</style>
</head>
<body>
<header><a class="brand" href="./"><img src="{prefix}img/icon-256.png" alt="">PHOTOCELLS</a>
<nav><a href="support.html">{nav[0]}</a><a href="privacy.html">{nav[1]}</a><a href="{other_href}" hreflang="{other_code or 'en'}">{other_label}</a></nav></header>
<main>{body}</main>
<footer><a href="support.html">{nav[0]}</a><a href="privacy.html">{nav[1]}</a><a href="terms.html">{nav[2]}</a><a href="mailto:{MAIL}">{MAIL}</a><p>{t['foot']}</p></footer>
</body>
</html>
"""


for lang in T:
    out = OUT_ROOT if lang == "en" else os.path.join(OUT_ROOT, lang)
    os.makedirs(out, exist_ok=True)
    for name in ("index", "privacy", "support", "terms"):
        file = os.path.join(out, "index.html" if name == "index" else name + ".html")
        if name == "index":
            from landing import landing
            html = landing(lang, BASE, "" if lang == "en" else "../", "es/" if lang == "en" else "../")
        else:
            html = page(lang, name)
        open(file, "w").write(html)
        print(os.path.relpath(file, HERE))
