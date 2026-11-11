"""Photocells landing page (index.html in every language). Imported by build_pages.py.
The text comes from i18n/<lang>.json; this file holds the markup, the CSS and the JS."""

APP_STORE = "https://apps.apple.com/app/id6762532696"

CSS = r"""
:root{--red:#FF2D2D;--red2:#CC1A1A;--ink:#F5F5F7;--mute:#9C9CA3;--bg:#060607;--card:#111114;--line:#232328;--green:#30D158;--fj:"Fjalla One",Impact,"Arial Narrow",sans-serif;--fx:"Fjalla One",Impact,"Arial Narrow",sans-serif;--sans:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Helvetica,Arial,sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 var(--sans);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}img{max-width:100%;display:block}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.k{font:13px/1 var(--fj);letter-spacing:.28em;text-transform:uppercase;color:var(--red)}
h1,h2,h3{font-family:var(--fj);font-weight:400;letter-spacing:.005em;margin:0;text-transform:uppercase}
h2{font-size:clamp(40px,6vw,76px);line-height:.98;margin:14px 0 18px}
p{color:var(--mute)}
/* nav */
.nav{position:absolute;inset:0 0 auto 0;z-index:5}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:76px}
.brand{display:flex;gap:10px;align-items:center;text-decoration:none;font:20px var(--fx);letter-spacing:.08em}
.brand img{width:34px;height:34px;border-radius:8px}
.nav nav{display:flex;align-items:center}.nav nav a{text-decoration:none;color:var(--mute);margin-left:22px;font-size:15px}.nav nav a:hover{color:var(--ink)}
.lang{position:relative;margin-left:22px}
.lang summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:6px;padding:6px 11px;border:1px solid var(--line);border-radius:99px;color:var(--mute);font-size:14px;letter-spacing:.04em;background:rgba(6,6,7,.5)}
.lang summary::-webkit-details-marker{display:none}.lang summary:hover,.lang[open] summary{color:var(--ink)}
.lang summary:after{content:"";width:5px;height:5px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(45deg) translateY(-2px);margin-left:2px}
.lang ul{position:absolute;right:0;top:calc(100% + 8px);z-index:10;margin:0;padding:6px;list-style:none;min-width:200px;background:#111114;border:1px solid var(--line);border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.6)}
.nav nav .lang a{display:block;margin:0;padding:8px 12px;border-radius:8px;color:var(--ink);font-size:15px}
.nav nav .lang a:hover{background:rgba(255,255,255,.06)}.nav nav .lang a[aria-current]{color:var(--red)}
/* hero */
.hero{position:relative;min-height:100vh;display:flex;align-items:center;overflow:hidden;padding:110px 0 70px;
  background:radial-gradient(60% 70% at 72% 45%,rgba(255,45,45,.22),transparent 70%),radial-gradient(40% 40% at 10% 90%,rgba(255,45,45,.08),transparent 70%),var(--bg)}
.hero:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:64px 64px;mask-image:radial-gradient(70% 70% at 60% 50%,#000,transparent)}
.beam{position:absolute;top:0;bottom:0;left:72%;width:3px;transform:translateX(-50%);background:var(--red);box-shadow:0 0 18px 4px rgba(255,45,45,.65),0 0 80px 18px rgba(255,45,45,.25);z-index:1}
.beam.flash{animation:flash .45s ease-out}
@keyframes flash{0%{box-shadow:0 0 30px 12px rgba(255,80,80,1),0 0 180px 60px rgba(255,45,45,.6);width:8px}100%{box-shadow:0 0 18px 4px rgba(255,45,45,.65),0 0 80px 18px rgba(255,45,45,.25);width:3px}}
.hero .wrap{position:relative;z-index:2;display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:center;width:100%}
.hero .wrap>div{min-width:0}.hero h1{font-size:clamp(64px,10.5vw,148px);line-height:.88;margin:18px 0 26px}
.hero h1 span{display:block}.hero h1 span:last-child{color:var(--red);text-shadow:0 0 40px rgba(255,45,45,.35)}
.lead{font-size:clamp(18px,1.6vw,21px);max-width:560px;color:#C9C9CE}
.badges{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-top:30px}
.badges a,.badges .soon{display:block;height:56px}.badges img{height:56px;width:auto}
.badges .soon{position:relative;opacity:.55;filter:grayscale(1)}
.badges .soon em{position:absolute;top:-11px;right:-8px;font:11px/1 var(--fj);letter-spacing:.14em;text-transform:uppercase;font-style:normal;background:var(--red);color:#fff;padding:6px 9px;border-radius:99px;filter:none;opacity:1}
.soonwrap{position:relative}.soonwrap em{position:absolute;top:-11px;right:-10px;z-index:2;font:11px/1 var(--fj);letter-spacing:.14em;text-transform:uppercase;font-style:normal;background:var(--red);color:#fff;padding:6px 10px;border-radius:99px;box-shadow:0 6px 18px rgba(255,45,45,.4)}
.under{font-size:14px;color:var(--mute);margin-top:14px}
/* phone */
.phone{position:relative;justify-self:center;width:min(330px,78vw);aspect-ratio:9/19.5;border-radius:52px;padding:12px;background:linear-gradient(145deg,#2a2a2f,#0d0d10);box-shadow:0 40px 120px rgba(0,0,0,.7),0 0 0 1px #333 inset,0 0 70px rgba(255,45,45,.18)}
.screen{position:relative;width:100%;height:100%;border-radius:41px;overflow:hidden;background:#000}
.screen video{width:100%;height:100%;object-fit:cover;filter:saturate(.9) contrast(1.05)}
.screen .line{position:absolute;top:0;bottom:0;left:50%;width:2px;transform:translateX(-50%);background:var(--red);box-shadow:0 0 10px rgba(255,45,45,.9)}
.pill{position:absolute;top:44px;left:50%;transform:translateX(-50%);display:flex;gap:7px;align-items:center;padding:6px 12px;border-radius:99px;background:rgba(0,0,0,.55);backdrop-filter:blur(8px);font:10px/1 var(--fj);letter-spacing:.18em;white-space:nowrap}
.pill i{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 8px var(--green)}
.island{position:absolute;top:12px;left:50%;transform:translateX(-50%);width:96px;height:28px;border-radius:20px;background:#000;z-index:3}
.hud{position:absolute;left:12px;right:12px;bottom:14px;padding:14px 16px;border-radius:24px;background:rgba(10,10,12,.72);backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.08)}
.hud small{display:block;font:10px var(--fj);letter-spacing:.2em;color:var(--mute)}
.hud b{display:block;font:56px/1 var(--fx);font-weight:400;color:var(--red);letter-spacing:.01em}.hud b span{font-size:34px;opacity:.85}
.laps{display:flex;gap:6px;margin-top:8px;font:12px var(--fx);color:#ddd}.laps span{background:rgba(255,255,255,.08);padding:4px 8px;border-radius:8px;opacity:0;transform:translateY(6px);transition:.35s}.laps span.on{opacity:1;transform:none}
.cutcard{position:absolute;left:14px;top:84px;width:76px;padding:4px;border-radius:12px;background:#151518;border:1.5px solid var(--red);opacity:0;transform:scale(.8);transform-origin:top left;transition:.25s}
.cutcard.on{opacity:1;transform:none}.cutcard canvas{width:100%;border-radius:8px;display:block}.cutcard p{margin:3px 0 0;text-align:center;font:8px var(--fj);letter-spacing:.15em;color:var(--red)}
/* stats */
.stats{border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:#09090a}
.stats .wrap{display:grid;grid-template-columns:repeat(4,1fr)}
.stat{padding:38px 18px;text-align:center;border-left:1px solid var(--line)}.stat:first-child{border-left:0}
.stat b{display:block;font:clamp(30px,4vw,52px)/1 var(--fx);font-weight:400}.stat span{color:var(--mute);font-size:14px;letter-spacing:.04em}
section{padding:130px 0}
.split{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center}
/* own: phones row */
.crowd{position:relative;height:420px}
.crowd .ph{position:absolute;bottom:0;width:150px;aspect-ratio:9/19.5;border-radius:24px;background:#0f0f12 center/cover no-repeat;border:5px solid #1c1c20;box-shadow:0 20px 50px rgba(0,0,0,.6);overflow:hidden}
.crowd .ph:after{display:none;content:"";position:absolute;top:0;bottom:0;left:50%;width:2px;background:var(--red);box-shadow:0 0 12px var(--red);transform:translateX(-50%)}
.crowd .ph:nth-child(1){left:0;bottom:10px;transform:rotate(-8deg)}.crowd .ph:nth-child(2){left:24%;transform:rotate(-2deg)}
.crowd .ph:nth-child(3){left:49%;transform:rotate(3deg)}.crowd .ph:nth-child(4){left:72%;bottom:6px;transform:rotate(9deg)}
.ticks{list-style:none;padding:0;margin:26px 0 0}.ticks li{padding:12px 0 12px 34px;border-top:1px solid var(--line);position:relative}
.ticks li:before{content:"";position:absolute;left:4px;top:50%;width:14px;height:2px;background:var(--red);box-shadow:0 0 8px var(--red)}
/* money */
.money{background:linear-gradient(180deg,#060607,#0d0606 50%,#060607)}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:46px}
.box{border-radius:26px;padding:34px;border:1px solid var(--line);background:var(--card)}
.box h3{font-size:30px;margin-bottom:18px}.box ul{list-style:none;padding:0;margin:0}.box li{padding:10px 0;border-top:1px solid var(--line);color:#C9C9CE}
.box.old{opacity:.8}.box.old h3{color:var(--mute)}.box.old li{text-decoration:line-through;text-decoration-color:rgba(255,45,45,.6)}
.box.new{border-color:rgba(255,45,45,.5);background:radial-gradient(80% 80% at 100% 0,rgba(255,45,45,.18),transparent 70%),var(--card);box-shadow:0 30px 90px rgba(255,45,45,.12)}
.box.new li:before{content:"✓";color:var(--red);margin-right:10px;font-weight:700}
.bars{margin-top:46px;display:grid;gap:16px}
.bar{display:grid;grid-template-columns:220px 1fr;gap:18px;align-items:center;font:15px var(--fj);letter-spacing:.06em;text-transform:uppercase;color:var(--mute)}
.bar i{display:flex;align-items:center;justify-content:flex-end;height:46px;border-radius:12px;padding:0 16px;font-style:normal;color:#fff;font-size:17px}
.bar.o i{width:100%;background:repeating-linear-gradient(135deg,#2a2a2f 0 14px,#232327 14px 28px)}.bar.n i{width:9%;min-width:110px;white-space:nowrap;background:linear-gradient(90deg,var(--red),var(--red2));box-shadow:0 0 30px rgba(255,45,45,.4)}
/* mix */
.track{position:relative;margin-top:60px;padding:70px 0 20px}
.track:before{content:"";position:absolute;left:4%;right:4%;top:150px;height:10px;border-radius:5px;background:repeating-linear-gradient(90deg,#1f1f23 0 40px,#18181b 40px 80px);border:1px solid #2a2a30}
.gates{position:relative;display:flex;justify-content:space-between;padding:0 2%}
.gate{width:200px;text-align:center}
.gate .dev{margin:0 auto;width:74px;height:150px;border-radius:18px;border:1px solid #34343a;background:linear-gradient(160deg,#25252a,#0e0e11);position:relative;box-shadow:0 18px 40px rgba(0,0,0,.6)}
.gate .dev:after{content:"";position:absolute;top:-60px;bottom:-60px;left:50%;width:2px;background:var(--red);box-shadow:0 0 14px var(--red);transform:translateX(-50%);opacity:.9}
.gate .dev.android{border-radius:12px}
.gate h4{font:22px var(--fj);margin:76px 0 2px;letter-spacing:.06em}.gate .os{font-size:13px;color:var(--mute);text-transform:uppercase;letter-spacing:.2em}
.gate .t{font:26px var(--fx);color:var(--red);margin-top:6px}
.runner{position:absolute;top:96px;left:3%;width:26px;height:26px;border-radius:50%;background:#fff;box-shadow:0 0 22px #fff,0 0 60px rgba(255,255,255,.4);animation:run 4.5s linear infinite}
@keyframes run{0%{left:3%}100%{left:95%}}
/* photo */
.photo{display:flex;justify-content:center}
.ph-card{position:relative;width:min(360px,80vw);padding:12px;border-radius:30px;background:var(--card);border:1.5px solid var(--red);box-shadow:0 30px 100px rgba(255,45,45,.18)}
.ph-card img{border-radius:20px;width:100%}.ph-card:after{content:"";position:absolute;top:12px;bottom:58px;left:50%;width:3px;transform:translateX(-50%);background:var(--red);box-shadow:0 0 12px var(--red)}
.ph-card p{margin:12px 0 4px;text-align:center;font:14px var(--fj);letter-spacing:.2em;color:var(--red)}
/* how */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:46px;counter-reset:s}
.step{padding:30px;border-radius:24px;background:var(--card);border:1px solid var(--line);position:relative;overflow:hidden}
.step:before{counter-increment:s;content:"0" counter(s);position:absolute;right:16px;top:-6px;font:110px/1 var(--fx);color:rgba(255,45,45,.12)}
.step h3{font-size:30px;margin-bottom:8px}.step p{margin:0}
.feats{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:26px;overflow:hidden;margin-top:46px}
.feat{background:var(--bg);padding:32px}.feat h3{font-size:22px;letter-spacing:.04em;margin-bottom:6px}.feat p{margin:0;font-size:15px}
/* shots */
.shots{display:flex;gap:22px;overflow-x:auto;padding:46px 24px 20px;scroll-snap-type:x mandatory;scrollbar-width:none}.shots::-webkit-scrollbar{display:none}
.shots img{flex:0 0 auto;width:250px;border-radius:34px;border:8px solid #1a1a1e;box-shadow:0 30px 70px rgba(0,0,0,.6);scroll-snap-align:center}
/* price */
.plans{display:grid;grid-template-columns:repeat(2,minmax(0,320px));gap:22px;justify-content:center;margin-top:46px}
.plan{position:relative;text-align:center;padding:36px;border-radius:26px;background:var(--card);border:1px solid var(--line)}
.plan.best{border-color:var(--red);box-shadow:0 30px 90px rgba(255,45,45,.15)}
.plan .tag{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:var(--red);color:#fff;font:12px var(--fj);letter-spacing:.14em;padding:6px 12px;border-radius:99px;text-transform:uppercase;white-space:nowrap}
.plan h3{font-size:22px;color:var(--mute);letter-spacing:.1em}.plan b{display:block;font:64px/1.1 var(--fx);font-weight:400;margin-top:8px}.plan span{color:var(--mute)}
.noprice .plan b{font-size:46px;line-height:1.25;margin-top:6px}.noprice .bar.n i{min-width:max-content}
.center{text-align:center}.center p{max-width:640px;margin-left:auto;margin-right:auto}
.final{padding:150px 0;text-align:center;position:relative;overflow:hidden;background:radial-gradient(50% 60% at 50% 100%,rgba(255,45,45,.25),transparent 70%)}
.final h2{font-size:clamp(48px,8vw,110px)}.final .badges{justify-content:center}
footer{border-top:1px solid var(--line);padding:34px 0 50px;color:var(--mute);font-size:14px}footer a{margin-right:18px;color:var(--mute)}
.reveal{opacity:0;transform:translateY(28px);transition:opacity .8s,transform .8s}.reveal.in{opacity:1;transform:none}
@media (max-width:900px){
 .hero .wrap,.split,.vs{grid-template-columns:1fr}.beam{left:50%;opacity:.5}.hero{padding-top:100px}.phone{margin-top:20px}
 .stats .wrap{grid-template-columns:1fr 1fr}.stat:nth-child(3){border-left:0}.stat{border-top:1px solid var(--line)}
 .steps,.feats{grid-template-columns:1fr}.bar{grid-template-columns:1fr}.crowd{height:340px}.crowd .ph{width:96px}
 .gates{gap:6px}.gate{width:auto;flex:1}.gate h4{font-size:16px}.gate .t{font-size:18px}.gate .dev{width:52px;height:108px}
 .nav nav>a{display:none}section{padding:90px 0}.plans{grid-template-columns:1fr}
}
@media (prefers-reduced-motion:reduce){.runner{animation:none}.reveal{opacity:1;transform:none;transition:none}}
"""

JS = r"""
(function(){
  // Shrink the hero title until its longest word fits (long German/Polish/Russian words, narrow phones).
  var h1=document.querySelector('.hero h1');
  function fitHero(){ if(!h1) return; h1.style.fontSize=''; var fs=parseFloat(getComputedStyle(h1).fontSize), n=0;
    while(h1.scrollWidth>h1.clientWidth+1 && fs>28 && n++<40){ fs*=0.95; h1.style.fontSize=fs+'px'; } }
  fitHero(); addEventListener('resize',fitHero); if(document.fonts&&document.fonts.ready) document.fonts.ready.then(fitHero);
})();
(function(){
  var beamEl=document.querySelector('.beam'), phoneEl=document.querySelector('.phone'), heroEl=document.querySelector('.hero');
  function align(){ if(!beamEl||!phoneEl) return; var r=phoneEl.getBoundingClientRect(), h=heroEl.getBoundingClientRect(); beamEl.style.left=(r.left-h.left+r.width/2)+'px'; }
  align(); addEventListener('resize',align); addEventListener('load',align);
  var v=document.getElementById('demo'); if(!v) return;
  var beam=document.querySelector('.beam'), big=document.getElementById('bigtime'), card=document.querySelector('.cutcard'), cv=card.querySelector('canvas'), laps=document.querySelectorAll('.laps span');
  var cuts=[0.58,1.73], times=[['0:07','412'],['0:07','286']], fired=[false,false], last=0;
  function snap(){ try{ var c=cv.getContext('2d'); cv.width=108; cv.height=192; c.drawImage(v,0,0,108,192); c.fillStyle='#FF2D2D'; c.fillRect(53,0,2,192);}catch(e){} }
  function tick(){
    var t=v.currentTime;
    if(t<last){ fired=[false,false]; laps.forEach(function(l){l.classList.remove('on')}); }
    last=t;
    for(var i=0;i<cuts.length;i++){
      if(!fired[i] && t>=cuts[i]){ fired[i]=true; beam.classList.remove('flash'); void beam.offsetWidth; beam.classList.add('flash');
        big.innerHTML=times[i][0]+'<span>,'+times[i][1]+'</span>'; laps[i]&&laps[i].classList.add('on'); snap(); card.classList.add('on');
        clearTimeout(card._t); card._t=setTimeout(function(){card.classList.remove('on')},1100); }
    }
    requestAnimationFrame(tick);
  }
  v.addEventListener('play',function(){requestAnimationFrame(tick)},{once:true});
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.15});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});
})();
"""

FONTS = {
    "default": "https://fonts.googleapis.com/css2?family=Fjalla+One&display=swap",
    # Fjalla One has no Cyrillic: Oswald for the Russian display text, Fjalla kept for digits and the wordmark.
    "ru": "https://fonts.googleapis.com/css2?family=Fjalla+One&family=Oswald:wght@500;600;700&display=swap",
}

# Long compound words (German, Dutch, Polish, Russian...) must not overflow at 375 px.
# Section titles hyphenate; the hero title is shrunk to fit its longest word instead (see fitHero in JS).
HYPHENS = "h2,h3{hyphens:auto;-webkit-hyphens:auto;overflow-wrap:break-word}"


def _cjk(stack):
    """Japanese / Chinese: system fonts, no uppercase, no wide tracking, looser leading."""
    return (f':root{{--fj:{stack},sans-serif;--fx:"Fjalla One",{stack},sans-serif}}'
            "h1,h2,h3{font-weight:700;letter-spacing:0;line-break:strict}"
            "h1,h2,h3,.k,.bar,.plan .tag,.soonwrap em,.badges .soon em,.gate .os{text-transform:none}"
            ".k{letter-spacing:.14em;font-weight:700}.bar{letter-spacing:.02em}.pill,.hud small,.cutcard p,.ph-card p{letter-spacing:.06em}"
            "h2{font-size:clamp(32px,4.8vw,60px);line-height:1.2}.final h2{font-size:clamp(36px,6vw,84px)}"
            ".hero h1{font-size:clamp(48px,8.5vw,120px);line-height:1.1}"
            ".box h3,.step h3{font-size:26px}.feat h3{font-size:20px;letter-spacing:0}.gate h4{letter-spacing:0}")


LANG_CSS = {
    "de": HYPHENS + ".hero h1{font-size:clamp(46px,8.4vw,118px)}h2{font-size:clamp(34px,5.4vw,70px)}",
    "fr": HYPHENS,
    "it": HYPHENS,
    "nl": HYPHENS + ".hero h1{font-size:clamp(50px,9vw,128px)}",
    "pt-BR": HYPHENS,
    "pl": HYPHENS + ".hero h1{font-size:clamp(50px,9vw,128px)}",
    "ru": HYPHENS + ':root{--fj:"Oswald","Fjalla One",Impact,"Arial Narrow",sans-serif;--fx:"Fjalla One","Oswald",Impact,"Arial Narrow",sans-serif}'
          "h1,h2,h3{font-weight:500}.hero h1{font-size:clamp(46px,8.4vw,118px);line-height:.95}h2{font-size:clamp(34px,5.4vw,70px);line-height:1.04}",
    "ja": _cjk('"Hiragino Sans","Noto Sans JP"'),
    "zh-Hans": _cjk('"PingFang SC","Noto Sans SC"'),
}


def landing(lang, c, base, prefix, alternates, switcher, lang_js):
    """lang: code ("en", "pt-BR"...); c: that language's i18n dict; prefix: "" at the root, "../" in a language folder."""
    p = prefix
    badges = f"""<div class="badges">
  <a href="{APP_STORE}" aria-label="{c['as_alt']}"><img src="{p}{c['badge_as']}" alt="{c['as_alt']}" width="168" height="56"></a>
  <div class="soonwrap" aria-label="{c['gp_alt']} · {c['soon']}"><em>{c['soon']}</em><span class="soon"><img src="{p}{c['badge_gp']}" alt="{c['gp_alt']}" height="56"></span></div>
</div>"""
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in c["stats"])
    gates = "".join(f'<div class="gate"><div class="dev {"android" if os_ == "Android" else ""}"></div><h4>{n}</h4><div class="os">{os_}</div><div class="t">{t}</div></div>' for n, os_, t in c["gates"])
    steps = "".join(f'<div class="step reveal"><h3>{h}</h3><p>{d}</p></div>' for h, d in c["how"])
    feats = "".join(f'<div class="feat"><h3>{h}</h3><p>{d}</p></div>' for h, d in c["feats"])
    shots = "".join(f'<img src="{p}img/shots/{c["shot_lang"]}-{n}.jpg" alt="" loading="lazy" width="250">' for n in ("1-session", "2-photo", "3-linear", "4-summary", "5-history", "6-home"))
    body_class = "" if c["price_shown"] else ' class="noprice"'
    plans = "".join(f'<div class="plan{" best" if i == 1 else ""}">{"<span class=tag>" + c["save"] + "</span>" if i == 1 else ""}<h3>{n}</h3><b>{pr}</b><span>{per}</span></div>' for i, (n, pr, per) in enumerate(c["plans"]))
    nav = c["nav"]
    ticks = "".join(f"<li>{x}</li>" for x in c["own_points"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{c['title']}</title>
<meta name="description" content="{c['desc']}">
<meta name="theme-color" content="#060607">
<link rel="icon" type="image/png" sizes="64x64" href="{p}img/favicon-64.png">
<link rel="apple-touch-icon" href="{p}img/apple-touch-icon.png">
<meta name="apple-itunes-app" content="app-id=6762532696">
{alternates}
<meta property="og:title" content="{c['title']}">
<meta property="og:description" content="{c['desc']}">
<meta property="og:image" content="{base}img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS.get(lang, FONTS['default'])}" rel="stylesheet">
<style>{CSS}{LANG_CSS.get(lang, '')}</style>
</head>
<body{body_class}>
<header class="nav"><div class="wrap"><a class="brand" href="./"><img src="{p}img/icon-256.png" alt="">PHOTOCELLS</a>
<nav><a href="#how">{c['how_k']}</a><a href="#price">{c['price_k']}</a><a href="support.html">{nav[0]}</a>{switcher}</nav></div></header>

<div class="hero">
  <div class="beam" aria-hidden="true"></div>
  <div class="wrap">
    <div>
      <div class="k">{c['eyebrow']}</div>
      <h1>{''.join(f'<span>{x}</span>' for x in c['h1'])}</h1>
      <p class="lead">{c['lead']}</p>
      {badges}
      <p class="under">{c['under_cta']}</p>
    </div>
    <div class="phone" aria-hidden="true"><div class="screen">
      <div class="island"></div>
      <video id="demo" autoplay muted loop playsinline preload="auto" poster="{p}media/crossing-poster.jpg">
        <source src="{p}media/crossing.webm" type="video/webm"><source src="{p}media/crossing.mp4" type="video/mp4"></video>
      <div class="line"></div>
      <div class="pill"><i></i>{c['demo_pill']}</div>
      <div class="cutcard"><canvas></canvas><p>{c['demo_cut']}</p></div>
      <div class="hud"><small>{c['demo_label']}</small><b id="bigtime">0:07<span>,412</span></b>
        <div class="laps"><span>#1 0:07,412</span><span>#2 0:07,286</span></div></div>
    </div></div>
  </div>
</div>

<div class="stats"><div class="wrap">{stats}</div></div>

<section><div class="wrap split">
  <div class="reveal"><div class="k">{c['own_k']}</div><h2>{c['own_h']}</h2><p>{c['own_p']}</p><ul class="ticks">{ticks}</ul></div>
  <div class="crowd reveal" aria-hidden="true">{''.join(f'<div class="ph" style="background-image:url({p}img/shots/{c["shot_lang"]}-{n}.jpg)"></div>' for n in ("1-session", "2-photo", "3-linear", "5-history"))}</div>
</div></section>

<section class="money"><div class="wrap">
  <div class="center reveal"><div class="k">{c['money_k']}</div><h2>{c['money_h']}</h2><p>{c['money_p']}</p></div>
  <div class="vs">
    <div class="box old reveal"><h3>{c['old_t']}</h3><ul>{''.join(f'<li>{x}</li>' for x in c['old'])}</ul></div>
    <div class="box new reveal"><h3>{c['new_t']}</h3><ul>{''.join(f'<li>{x}</li>' for x in c['new'])}</ul></div>
  </div>
  <div class="bars reveal">
    <div class="bar o"><span>{c['bar_old']}</span><i>{c['bar_old_v']}</i></div>
    <div class="bar n"><span>{c['bar_new']}</span><i>{c['bar_new_v']}</i></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="center reveal"><div class="k">{c['mix_k']}</div><h2>{c['mix_h']}</h2><p>{c['mix_p']}</p></div>
  <div class="track reveal" aria-hidden="true"><div class="runner"></div><div class="gates">{gates}</div></div>
</div></section>

<section><div class="wrap split">
  <div class="photo reveal"><div class="ph-card"><img src="{p}img/crossing.jpg" alt="" loading="lazy" width="336"><p>{c['demo_cut']} · 0:07,286</p></div></div>
  <div class="reveal"><div class="k">{c['photo_k']}</div><h2>{c['photo_h']}</h2><p>{c['photo_p']}</p></div>
</div></section>

<section id="how"><div class="wrap">
  <div class="reveal"><div class="k">{c['how_k']}</div><h2>{c['how_h']}</h2></div>
  <div class="steps">{steps}</div>
  <div class="reveal" style="margin-top:110px"><div class="k">{c['feat_k']}</div><h2>{c['feat_h']}</h2></div>
  <div class="feats reveal">{feats}</div>
</div></section>

<section style="padding-bottom:60px"><div class="wrap reveal"><div class="k">{c['shots_k']}</div><h2>{c['shots_h']}</h2></div>
  <div class="shots">{shots}</div></section>

<section id="price"><div class="wrap center">
  <div class="reveal"><div class="k">{c['price_k']}</div><h2>{c['price_h']}</h2></div>
  <div class="plans reveal">{plans}</div>
  <p class="reveal" style="margin-top:22px">{c['price_note']}</p>
</div></section>

<div class="final"><div class="wrap"><h2>{c['final_h']}</h2>{badges}</div></div>

<footer><div class="wrap"><a href="support.html">{nav[0]}</a> <a href="privacy.html">{nav[1]}</a> <a href="terms.html">{nav[2]}</a> <a href="mailto:dpappssupport@gmail.com">dpappssupport@gmail.com</a><p>{c['foot']}</p></div></footer>
<script>{JS}{lang_js}</script>
</body>
</html>
"""
