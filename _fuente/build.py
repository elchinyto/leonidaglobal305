#!/usr/bin/env python3
"""Genera el sitio Leonida Global 305 (estático) en /home/claude/leonida-guia."""
import os

DEPLOY = os.environ.get("DEPLOY") == "1"
DOMAIN = "https://leonidaglobal305.com"
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if DEPLOY else "/home/claude/leonida-guia"
os.makedirs(OUT, exist_ok=True)

SITE = "Leonida Global 305"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@500&display=swap">')

CSS = r"""
/* Layout: cartel de carretera de Florida — titulares tipo billboard, columna de lectura estrecha, franja de "millas" para datos */
:root{
  --bg:#fbf6f1; --surface:#ffffff; --fg:#1d1a22; --muted:#5f5966;
  --accent:#d7265f; --teal:#0b7d77; --line:#eadfd6; --sun:#ffb347;
  --f-display:"Anton","Impact","Arial Narrow",sans-serif;
  --f-body:"Source Sans 3","Segoe UI",system-ui,sans-serif;
  --f-mono:"JetBrains Mono",ui-monospace,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#16131b; --surface:#201c27; --fg:#f3edf5; --muted:#b4abbb;
  --accent:#ff4f87; --teal:#3cc7bd; --line:#352e3e; --sun:#ffb347; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#16131b; --surface:#201c27; --fg:#f3edf5; --muted:#b4abbb;
  --accent:#ff4f87; --teal:#3cc7bd; --line:#352e3e; --sun:#ffb347; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--fg);font-family:var(--f-body);font-size:1.06rem;line-height:1.65;margin:0}
.wrap{max-width:760px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header.top{border-bottom:3px solid var(--fg)}
header.top .wrap{display:flex;flex-wrap:wrap;gap:8px 20px;align-items:baseline;justify-content:space-between;padding-block:14px}
.logo{font-family:var(--f-display);font-size:1.6rem;letter-spacing:.02em;color:var(--fg);text-decoration:none;text-transform:uppercase}
.logo span{color:var(--accent)}
.logo{display:inline-flex;align-items:center;gap:10px}
.logo img{width:48px;height:48px;flex:none}
.hero{display:flex;align-items:center;gap:24px;flex-wrap:wrap}
.hero-logo{width:min(200px,45vw);height:auto;flex:none}
.hero-txt{flex:1 1 300px;min-width:0}
nav.main{display:flex;flex-wrap:wrap;gap:4px 16px;font-weight:600;font-size:.95rem}
nav.main a{color:var(--muted);text-decoration:none}
nav.main a:hover,nav.main a:focus-visible,nav.main a[aria-current]{color:var(--accent)}
a{color:var(--accent)}
a:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
.mile{display:inline-block;font-family:var(--f-mono);font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;
  background:var(--teal);color:var(--bg);padding:2px 8px;border-radius:3px}
h1,h2{font-family:var(--f-display);font-weight:400;text-transform:uppercase;letter-spacing:.01em;text-wrap:balance;line-height:1.05}
h1{font-size:clamp(2.3rem,7vw,3.6rem);margin:.4em 0 .25em}
h2{font-size:1.7rem;margin:1.6em 0 .4em;border-top:1px solid var(--line);padding-top:.8em}
h3{font-size:1.15rem;margin:1.2em 0 .2em}
.lede{font-size:1.2rem;color:var(--muted);max-width:60ch}
.updated{font-family:var(--f-mono);font-size:.8rem;color:var(--muted)}
main{padding-block:12px 40px}
main p,main li{max-width:65ch}
.count{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}
.count div{flex:1 1 120px;border:2px solid var(--fg);padding:10px 12px;background:var(--surface)}
.count b{display:block;font-family:var(--f-display);font-size:2.2rem;font-weight:400;line-height:1;font-variant-numeric:tabular-nums;color:var(--accent)}
.count small{font-family:var(--f-mono);font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.guides{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:18px 0;padding:0;list-style:none}
.guides a{display:block;height:100%;padding:16px;background:var(--surface);border:1px solid var(--line);text-decoration:none;color:var(--fg)}
.guides a:hover{border-color:var(--accent)}
.guides h3{margin:6px 0 4px;font-family:var(--f-display);font-weight:400;text-transform:uppercase;font-size:1.3rem}
.guides p{margin:0;color:var(--muted);font-size:.95rem}
.tbl{overflow-x:auto;margin:14px 0}
table{border-collapse:collapse;width:100%;min-width:420px;font-size:.98rem}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:var(--f-mono);font-size:.75rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
td.num{font-variant-numeric:tabular-nums;font-weight:700;white-space:nowrap}
.tag{font-family:var(--f-mono);font-size:.7rem;padding:1px 6px;border-radius:3px;white-space:nowrap}
.ok{background:var(--teal);color:var(--bg)}
.no{border:1px solid var(--muted);color:var(--muted)}
.note{border-left:4px solid var(--sun);padding:8px 14px;background:var(--surface);margin:16px 0}
.aff{border:2px dashed var(--teal);padding:14px 16px;margin:22px 0;background:var(--surface)}
.aff strong{font-family:var(--f-display);font-weight:400;text-transform:uppercase;font-size:1.2rem;letter-spacing:.02em}
.aff ul{margin:6px 0 0;padding-left:1.1em}
.ad{font-family:var(--f-mono);font-size:.7rem;color:var(--muted);text-align:center;border:1px solid var(--line);padding:18px;margin:22px 0;text-transform:uppercase;letter-spacing:.1em}
.faq dt{font-weight:700;margin-top:12px}
.faq dd{margin:2px 0 0;color:var(--fg)}
footer{border-top:3px solid var(--fg);padding-block:18px 30px;font-size:.88rem;color:var(--muted)}
footer p{margin:.3em 0;max-width:70ch}
.yt{position:relative;aspect-ratio:16/9;max-width:100%;background:#000;margin:12px 0;border:2px solid var(--fg)}
.yt iframe,.yt-btn{position:absolute;inset:0;width:100%;height:100%;border:0}
.yt-btn{padding:0;cursor:pointer;background:#000;display:block}
.yt-btn img{width:100%;height:100%;object-fit:cover;display:block}
.yt-play{position:absolute;left:50%;top:50%;width:76px;height:54px;margin:-27px 0 0 -38px;background:var(--accent);border-radius:14px;box-shadow:0 4px 18px rgba(0,0,0,.45)}
.yt-play::after{content:"";position:absolute;left:30px;top:15px;border-style:solid;border-width:12px 0 12px 21px;border-color:transparent transparent transparent #fff}
.yt-btn:hover .yt-play,.yt-btn:focus-visible .yt-play{filter:brightness(1.12)}
.yt-btn:focus-visible{outline:3px solid var(--teal);outline-offset:2px}
.trailer h2{margin-bottom:.1em}
footer .autor{font-size:1rem;color:var(--fg);margin-bottom:.6em}
footer .autor a{font-weight:700}
.radios{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:16px 0}
.radio{background:var(--surface);border:1px solid var(--line);padding:0 0 14px;min-width:0;overflow:hidden}
.radio>*:not(.radio-img){margin-left:16px;margin-right:16px}
.radio-img{display:block;width:100%;height:auto;aspect-ratio:8/5;margin-bottom:12px}
.credito-img{font-size:.8rem;color:var(--muted);margin:-4px 0 12px}
.radio h3{margin:0;font-family:var(--f-display);font-weight:400;text-transform:uppercase;font-size:1.35rem;letter-spacing:.02em}
.radio .hosts{margin:6px 16px;font-weight:600;font-size:.95rem}
.radio ul{margin:0 16px;padding-left:1.1em;color:var(--muted);font-size:.93rem}
.creditos{font-size:.85rem;color:var(--muted);border-top:1px solid var(--line);padding-top:12px;margin-top:28px}
.filtros{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 10px}
.f{font:600 .9rem var(--f-body);color:var(--fg);background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:6px 14px;cursor:pointer}
.f.on{background:var(--fg);color:var(--bg);border-color:var(--fg)}
.f:focus-visible,.lugar:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
#mapa{height:min(62vh,520px);min-height:340px;border:2px solid var(--fg);background:var(--surface);z-index:0}
.mapa-error{padding:20px;color:var(--muted)}
.pin{border-radius:50%;border:3px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.45)}
.pin-juego{background:var(--teal)}
.pin-marketing{background:var(--accent)}
.tag.mk{background:var(--accent);color:var(--bg)}
.lugares{list-style:none;padding:0;margin:14px 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:8px}
.lugar{width:100%;height:100%;text-align:left;display:flex;flex-direction:column;align-items:flex-start;gap:3px;background:var(--surface);border:1px solid var(--line);padding:10px 12px;cursor:pointer;font:inherit;color:var(--fg)}
.lugar:hover{border-color:var(--accent)}
.lugar strong{font-size:1rem;line-height:1.3}
.lugar .real{font-size:.85rem;color:var(--muted);line-height:1.35}
.pop{display:flex;flex-direction:column;gap:2px;font-family:var(--f-body);max-width:240px}
.pop-t{font-family:var(--f-mono);font-size:.65rem;text-transform:uppercase;letter-spacing:.06em;color:#0b7d77}
.pop b{font-size:1rem}.pop i{font-style:normal;font-weight:600}.pop small{color:#5f5966}.pop p{margin:4px 0 0!important;font-size:.88rem;line-height:1.4}
.lang select{font:600 .9rem var(--f-body);color:var(--fg);background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:5px 8px;cursor:pointer}
.lang select:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
#gt{position:absolute;left:-9999px;top:0}
iframe.skiptranslate,.goog-te-banner-frame,#goog-gt-tt,.goog-te-balloon-frame,.VIpgJd-ZVi9od-ORHb-OEVmcd{display:none!important}
body{top:0!important}
.goog-text-highlight{background:none!important;box-shadow:none!important}
.picks{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin:16px 0}
.pick{display:flex;flex-direction:column;gap:6px;padding:16px;background:var(--surface);border:1px solid var(--line);min-width:0}
.pick-top{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap}
.price{font-family:var(--f-mono);font-size:.78rem;color:var(--muted);font-variant-numeric:tabular-nums}
.pick h3{margin:2px 0 0;font-size:1.08rem}
.pick p{margin:0;color:var(--muted);font-size:.95rem;flex:1}
.buy{align-self:flex-start;margin-top:6px;background:var(--accent);color:var(--bg);font-weight:700;text-decoration:none;padding:8px 14px;border-radius:4px;font-size:.92rem}
.buy:hover{filter:brightness(1.08)}
.disclosure{font-size:.85rem;color:var(--muted)}
"""

NAV = [("index.html", "Inicio"), ("fecha-precio-ediciones.html", "Fecha y precio"),
       ("mapa-leonida.html", "Mapa"), ("personajes.html", "Personajes"), ("todo-lo-confirmado.html", "Lo confirmado"), ("leaks-cyberleek.html", "Leaks"), ("mapa-miami-real.html", "Miami real"), ("trailers-gta-6.html", "Tráilers"), ("musica-radios-gta-6.html", "Música"), ("equipo-gta-6.html", "Equipo")]

def shell(slug, title, desc, body, full_doc=True):
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == slug else ""}>{t}</a>' for h, t in NAV)
    head = (f'<title>{title}</title>'
            '<meta name="claude:viewport-fit-sides" content="cover">'
            f'<meta name="description" content="{desc}">'
            f'<link rel="canonical" href="{DOMAIN}/{"" if slug == "index.html" else slug}">'
            f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">'
            f'<meta property="og:type" content="website"><meta property="og:locale" content="es_ES">'
            f'<meta property="og:image" content="{DOMAIN}/img/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta property="og:site_name" content="Leonida Global 305"><meta property="og:url" content="{DOMAIN}/{"" if slug == "index.html" else slug}">'
            '<meta name="twitter:card" content="summary_large_image">'
            f'<meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{DOMAIN}/img/og-image.jpg">'
            '<link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32.png">'
            '<link rel="apple-touch-icon" href="img/apple-touch-icon.png"><meta name="theme-color" content="#d7265f">'
            f'{FONTS}<style>{CSS}</style>')
    page = f"""
<header class="top"><div class="wrap">
  <a class="logo notranslate" href="index.html"><img src="img/logo-96.png" srcset="img/logo-96.png 1x, img/logo-192.png 2x" width="48" height="48" alt="">Leonida Global <span>305</span></a>
  <nav class="main" aria-label="Guías">{nav}</nav>
  <div class="lang notranslate">
    <select id="lang-sel" aria-label="Idioma / Language">
      <option value="es">🌐 Español</option><option value="en">English</option><option value="pt">Português</option>
      <option value="fr">Français</option><option value="it">Italiano</option><option value="de">Deutsch</option>
    </select>
  </div>
</div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">
  <p class="autor">Creado por <strong>Ernesto</strong> · Síguelo en X: <a href="https://x.com/elchinyto_tech" target="_blank" rel="me noopener">@elchinyto_tech</a></p>
  <p>{SITE} es un sitio de fans. No está afiliado a Rockstar Games ni a Take-Two Interactive. Grand Theft Auto es marca de sus dueños.</p>
  <p>Algunos enlaces son de afiliado: si compras a través de ellos, el sitio recibe una pequeña comisión sin costo extra para ti.</p>
</div></footer>
<div id="gt" aria-hidden="true"></div>
<script>
function gtInit(){{new google.translate.TranslateElement({{pageLanguage:"es",autoDisplay:false}},"gt");}}
(function(){{
  var s=document.getElementById("lang-sel"),h=location.hostname;
  var m=document.cookie.match(/googtrans=\\/es\\/([a-z-]+)/i); if(m) s.value=m[1];
  s.addEventListener("change",function(){{
    var v=s.value,x=";expires=Thu, 01 Jan 1970 00:00:00 GMT";
    ["",";domain="+h,";domain=."+h].forEach(function(d){{document.cookie="googtrans=;path=/"+x+d;}});
    if(v!=="es"){{document.cookie="googtrans=/es/"+v+";path=/";document.cookie="googtrans=/es/"+v+";path=/;domain=."+h;}}
    location.reload();
  }});
}})();
</script>
<script src="https://translate.google.com/translate_a/element.js?cb=gtInit" async></script>"""
    if not full_doc and not DEPLOY:
        return head + page
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            + head + '</head><body>' + page + '</body></html>')

AFF = """<aside class="aff" aria-label="Recomendados">
  <strong>Prepárate para el 19 de noviembre</strong>
  <p style="margin:.3em 0 0">Teles, monitores, SSD y accesorios para GTA 6, con opciones económicas y de gama alta: <a href="equipo-gta-6.html">ver el equipo recomendado</a>.</p>
</aside>"""
AD = '<div class="ad" aria-hidden="true">Espacio publicitario</div>'
UPD = '<p class="updated">Actualizado: 24 de octubre de 2026</p>'

COLECCIONISTA = """
<h2>Caja de coleccionista: The Goodtime State – Vice City Collection</h2>
<p>Rockstar vende una caja de coleccionista oficial por <strong>$399.99</strong> en EE.UU., solo en la Rockstar Store. <strong>No incluye el juego</strong>: se compra aparte.</p>
<div class="tbl"><table>
  <thead><tr><th>Qué trae</th></tr></thead>
  <tbody>
    <tr><td>Figura de Macca the Gator (unos 15 cm, con escondite en la base)</td></tr>
    <tr><td>Gafas Oakley Frogskins</td></tr>
    <tr><td>Gorra New Era 9FORTY</td></tr>
    <tr><td>Bolso cruzado de los Cayos de Leonida</td></tr>
    <tr><td>Espejo magnético de Macca the Gator</td></tr>
    <tr><td>Vaso de chupito de Chunkee the Manatee</td></tr>
    <tr><td>Cucharilla de Vice City y llavero</td></tr>
    <tr><td>Nueve pines en una lata y nueve pegatinas</td></tr>
    <tr><td>Póster doble de 36 × 26 pulgadas con el mapa de Leonida detrás</td></tr>
  </tbody>
</table></div>
<ul>
  <li>Reservas abiertas desde el 24 de septiembre. Se envía a partir del 19 de noviembre.</li>
  <li>Una por persona, con cuenta de Rockstar Games y para mayores de 18 años.</li>
  <li>Se envía a 23 países, entre ellos EE.UU., Canadá, Reino Unido y buena parte de Europa. Latinoamérica todavía no está en la lista.</li>
  <li>Es de stock limitado: en Reino Unido se agotó en dos días.</li>
</ul>
"""


# ---------- Videos de YouTube (carga al tocar) ----------
def video(vid, titulo):
    return (f'<div class="yt"><button type="button" class="yt-btn" data-id="{vid}" data-title="{titulo}" aria-label="Ver {titulo}">'
            f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">'
            f'<span class="yt-play" aria-hidden="true"></span></button></div>')
YT_JS = """<script>
document.querySelectorAll(".yt-btn").forEach(function(b){b.addEventListener("click",function(){
  var f=document.createElement("iframe");
  f.src="https://www.youtube-nocookie.com/embed/"+b.dataset.id+"?autoplay=1&rel=0";
  f.title=b.dataset.title; f.allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen"; f.allowFullscreen=true;
  b.parentNode.replaceChild(f,b);
});});
</script>"""
TRAILERS = [
    ("rz1B4B2yBZY", "Tráiler de lanzamiento", "15 de octubre de 2026", "Grabado dentro del juego en PS5. Un golpe fácil sale mal y Jason y Lucia terminan metidos en una conspiración que cruza todo Leonida. Suena \"Flower in a Hurricane\", de Justice con Tame Impala, SZA y King Gizzard &amp; The Lizard Wizard."),
    ("VQRLujxTm3c", "Tráiler 2", "6 de mayo de 2025", "Presentó por su nombre a Jason Duval y Lucia Caminos, y al reparto: Cal Hampton, Brian Heder, Boobie Ike, Dre'Quan Priest, Real Dimez y Raul Bautista."),
    ("QdBZY2fkU-0", "Tráiler 1", "5 de diciembre de 2023", "El primer vistazo: Lucia en prisión, Vice City de vuelta, los Cayos y el estado de Leonida. Con \"Love Is a Long Road\" de Tom Petty."),
]

# ---------- Inicio ----------
index = f"""
<span class="mile">Guías de GTA 6</span>
<h1>Todo GTA&nbsp;6, claro y al día</h1>
<p class="lede">Fecha, precio, mapa de Leonida, personajes y, desde el día del lanzamiento, guías de misiones, robos, autos y secretos.</p>
<div class="count" id="count" aria-live="polite">
  <div><b id="d">--</b><small>días</small></div>
  <div><b id="h">--</b><small>horas</small></div>
  <div><b id="m">--</b><small>minutos</small></div>
</div>
<p class="updated">Cuenta regresiva al 19 de noviembre de 2026, 00:00 (hora de Miami). La hora exacta de desbloqueo puede variar por región.</p>
<h2>Tráiler de lanzamiento</h2>
{video("rz1B4B2yBZY", "Tráiler de lanzamiento de GTA 6")}
<p><a href="trailers-gta-6.html">Ver los tres tráilers oficiales</a></p>
{YT_JS}
<h2>Guías disponibles</h2>
<ul class="guides">
  <li><a href="fecha-precio-ediciones.html"><span class="mile">Lanzamiento</span><h3>Fecha, precio y ediciones</h3><p>Cuánto cuesta, qué trae cada edición y cuándo se puede precargar.</p></a></li>
  <li><a href="mapa-leonida.html"><span class="mile">Mapa</span><h3>Mapa de Leonida</h3><p>Las seis regiones confirmadas y su versión real en Florida.</p></a></li>
  <li><a href="todo-lo-confirmado.html"><span class="mile">Nuevo</span><h3>Todo lo confirmado</h3><p>Lo que contó Rockstar a IGN, Famitsu, Game Informer, Dazed, LOVE y Bloomberg.</p></a></li>
  <li><a href="trailers-gta-6.html"><span class="mile">Videos</span><h3>Todos los tráilers</h3><p>Los tres tráilers oficiales, incluido el de lanzamiento.</p></a></li>
  <li><a href="musica-radios-gta-6.html"><span class="mile">Música</span><h3>Radios y GTA VI: The Album</h3><p>Las emisoras con Bad Bunny, Lana Del Rey y Morgan Wallen, y el álbum oficial.</p></a></li>
  <li><a href="mapa-miami-real.html"><span class="mile">Miami real</span><h3>Vice City en el Miami real</h3><p>Mapa interactivo con los lugares reales del juego y el marketing de GTA 6 en la ciudad.</p></a></li>
  <li><a href="leaks-cyberleek.html"><span class="mile">Leaks</span><h3>Los leaks de CyberLeek</h3><p>Qué filtraron, qué ya confirmó Rockstar y cómo terminó.</p></a></li>
  <li><a href="equipo-gta-6.html"><span class="mile">Equipo</span><h3>Equipo para GTA 6</h3><p>Teles, monitores y SSD económicos y de gama alta.</p></a></li>
  <li><a href="personajes.html"><span class="mile">Historia</span><h3>Personajes</h3><p>Jason, Lucia y el reparto confirmado por Rockstar.</p></a></li>
</ul>
{AD}
<h2>Lo que viene</h2>
<p>A partir del 19 de noviembre publicaremos guías de todas las misiones, robos, ubicaciones de autos, armas, casas seguras y coleccionables, siempre probadas en el juego.</p>
{AFF}
<script>
(function(){{
  var t=new Date("2026-11-19T00:00:00-05:00").getTime();
  function tick(){{var s=Math.max(0,t-Date.now()),
    d=Math.floor(s/864e5),h=Math.floor(s%864e5/36e5),m=Math.floor(s%36e5/6e4);
    document.getElementById("d").textContent=d;
    document.getElementById("h").textContent=h;
    document.getElementById("m").textContent=m;}}
  tick(); setInterval(tick,30000);
}})();
</script>"""

# ---------- Fecha y precio ----------
fecha = f"""
<span class="mile">Lanzamiento</span>
<h1>GTA 6: fecha, precio y ediciones</h1>
{UPD}
<p class="lede">GTA 6 sale el <strong>19 de noviembre de 2026</strong> en PS5 y Xbox Series X|S. La edición estándar cuesta $79.99 y la Ultimate unos $100 (precios en EE.UU.).</p>
<h2>Fechas clave</h2>
<div class="tbl"><table>
  <thead><tr><th>Qué</th><th>Fecha</th><th>Estado</th></tr></thead>
  <tbody>
    <tr><td>Preventas</td><td class="num">25 jun 2026</td><td><span class="tag ok">Abiertas</span></td></tr>
    <tr><td>Precarga (digital y caja con código)</td><td class="num">12 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Lanzamiento PS5 y Xbox Series X|S</td><td class="num">19 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Versión de PC</td><td class="num">Sin fecha</td><td><span class="tag no">No anunciado</span></td></tr>
    <tr><td>Nuevo GTA Online</td><td class="num">Sin fecha</td><td><span class="tag no">No anunciado</span></td></tr>
  </tbody>
</table></div>
<h2>Precio de cada edición</h2>
<div class="tbl"><table>
  <thead><tr><th>Edición</th><th>Precio (EE.UU.)</th><th>Incluye</th></tr></thead>
  <tbody>
    <tr><td>Estándar</td><td class="num">$79.99</td><td>Juego base, Vintage Vice City Pack (si compras antes del 20 de noviembre) y un mes de GTA+.</td></tr>
    <tr><td>Ultimate</td><td class="num">~$100</td><td>Todo lo anterior más contenido extra ligado a Jason y Lucia, como armas, vehículos y ropa.</td></tr>
  </tbody>
</table></div>
<div class="note"><strong>Ojo con la edición física.</strong> La caja de tienda trae un código de descarga, no un disco con el juego. Si lo que quieres es jugar el primer día, la compra digital te deja precargar desde el 12 de noviembre sin depender del envío.</div>
{COLECCIONISTA}
{AD}
<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Hay edición de coleccionista de GTA 6?</dt><dd>Hay una caja de coleccionista de $399.99 en la Rockstar Store, pero no incluye el juego. Las ediciones del juego son solo la estándar y la Ultimate.</dd>
  <dt>¿GTA 6 sale en PS4 o Xbox One?</dt><dd>No. Solo se ha anunciado para PS5 y Xbox Series X|S.</dd>
  <dt>¿A qué hora se desbloquea?</dt><dd>Rockstar no ha confirmado la hora para cada región. Actualizaremos esta guía en cuanto se anuncie.</dd>
  <dt>¿Qué es el Vintage Vice City Pack?</dt><dd>Un paquete de objetos con estética del Vice City clásico. Lo recibe cualquiera que reserve o compre el juego antes del 20 de noviembre.</dd>
  <dt>¿Viene GTA Online incluido?</dt><dd>Rockstar no ha anunciado un modo online para el día del lanzamiento. El lanzamiento confirmado es de un jugador.</dd>
</dl>
{AFF}"""

# ---------- Mapa ----------
mapa = f"""
<span class="mile">Mapa</span>
<h1>Mapa de GTA 6: las 6 regiones de Leonida</h1>
{UPD}
<p class="lede">GTA 6 ocurre en Leonida, la versión de Rockstar del estado de Florida. Rockstar ha nombrado seis regiones. El tamaño exacto del mapa todavía no es oficial.</p>
<h2>Regiones confirmadas</h2>
<div class="tbl"><table>
  <thead><tr><th>Región</th><th>Se parece a</th><th>Qué esperar</th></tr></thead>
  <tbody>
    <tr><td><strong>Vice City</strong></td><td>Miami</td><td>Playas, rascacielos, vida nocturna y el corazón de la historia.</td></tr>
    <tr><td><strong>Leonida Keys</strong></td><td>Cayos de Florida</td><td>Islas tropicales conectadas por puentes, barcos y casas frente al mar.</td></tr>
    <tr><td><strong>Grassrivers</strong></td><td>Everglades</td><td>Pantanos, caimanes y una de las zonas naturales más grandes.</td></tr>
    <tr><td><strong>Port Gellhorn</strong></td><td>Costa del Golfo (Panhandle)</td><td>Pueblo costero venido a menos en el oeste del estado.</td></tr>
    <tr><td><strong>Ambrosia</strong></td><td>Interior rural, zona del lago Okeechobee</td><td>Zona industrial y agrícola junto al lago Leonida.</td></tr>
    <tr><td><strong>Mount Kalaga</strong></td><td>Parques y bosques del norte de Florida</td><td>Parque nacional con montañas, senderos y fauna.</td></tr>
  </tbody>
</table></div>
<div class="note"><strong>¿Qué tan grande es?</strong> Rockstar no ha dado kilómetros cuadrados. La comunidad que mapea los tráilers calcula que Leonida es bastante más grande que el mapa de GTA 5, pero son estimaciones, no datos oficiales.</div>
{AD}
<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Vuelve Vice City?</dt><dd>Sí. Vice City es la ciudad principal del juego, inspirada en el Miami actual.</dd>
  <dt>¿Se puede explorar todo el mapa desde el principio?</dt><dd>No está confirmado. En GTA anteriores algunas zonas se abrían con la historia; lo actualizaremos tras el lanzamiento.</dd>
</dl>
{AFF}"""

# ---------- Personajes ----------
pers = f"""
<span class="mile">Historia</span>
<h1>Personajes de GTA 6</h1>
{UPD}
<p class="lede">La historia gira en torno a una pareja criminal, Jason Duval y Lucia Caminos, y a un grupo de personajes de Vice City que Rockstar ya presentó en sus tráilers y en su web oficial.</p>
<h2>Protagonistas</h2>
<h3>Lucia Caminos</h3>
<p>Coprotagonista, originaria de Liberty City, y la primera protagonista femenina desarrollada a fondo en un GTA principal. Arranca la historia saliendo de la Penitenciaría de Leonida, decidida a no volver a cometer errores. Es la más impulsiva de los dos y sabe pelear.</p>
<h3>Jason Duval</h3>
<p>Ex militar que creció rodeado de estafadores y delincuentes y terminó transportando droga y robando bancos. Quiere una vida tranquila, pero los problemas no lo sueltan. Conocer a Lucia puede ser lo mejor o lo peor que le ha pasado.</p>
<h2>Personajes secundarios</h2>
<div class="tbl"><table>
  <thead><tr><th>Personaje</th><th>Quién es</th></tr></thead>
  <tbody>
    <tr><td><strong>Cal Hampton</strong></td><td>Amigo de Jason. Le encanta espiar las comunicaciones de la Guardia Costera.</td></tr>
    <tr><td><strong>Brian Heder</strong></td><td>Jefe de Jason, con negocio legal por fuera y criminal por dentro. Le deja a Jason vivir en una de sus casas.</td></tr>
    <tr><td><strong>Raul Bautista</strong></td><td>Ladrón de bancos veterano y mentor de la pareja: les enseña a planear los golpes grandes.</td></tr>
    <tr><td><strong>Boobie Ike</strong></td><td>Figura local de Vice City con negocios en la música y otros terrenos.</td></tr>
    <tr><td><strong>Dre'Quan Priest</strong></td><td>Socio de Boobie en el sello musical Only Raw Records.</td></tr>
    <tr><td><strong>Real Dimez</strong></td><td>Dúo de raperas ligado a Only Raw Records.</td></tr>
  </tbody>
</table></div>
{AD}
<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Se puede jugar con los dos protagonistas?</dt><dd>Sí, Jason y Lucia son los dos personajes jugables.</dd>
  <dt>¿Vuelven personajes de GTA anteriores?</dt><dd>Rockstar no ha confirmado regresos. Lo actualizaremos cuando haya información oficial.</dd>
</dl>
{AFF}"""

# ---------- Todo lo confirmado ----------
conf = f"""
<span class="mile">Entrevistas y prensa</span>
<h1>GTA 6: todo lo confirmado por Rockstar</h1>
{UPD}
<p class="lede">Todo lo que Rockstar ha contado a IGN, Famitsu, Kinda Funny, Game Informer, Dazed, LOVE y Bloomberg, más lo que se vio en el Extended Look y el tráiler de lanzamiento, ordenado por tema.</p>
<div class="note"><strong>Cómo leer esta guía.</strong> Todo lo que aparece aquí lo dijo Rockstar o se vio en el Extended Look del 27 de agosto. Lo que solo contaron creadores que vieron demos sin jugar va aparte, al final, marcado como reportado.</div>

<h2>La historia y la pareja</h2>
<ul>
  <li>Jason y Lucia necesitan dinero después de que un trabajo sencillo sale mal, y varios grupos van tras ellos.</li>
  <li>La historia empieza en los Cayos de Leonida, donde está la primera casa de Jason.</li>
  <li>Tú decides si actúan como pareja o solo como cómplices. El romance es opcional y no da ventajas, pero cambia cómo se desarrolla la historia.</li>
  <li>La relación sube haciendo cosas juntos: kayak, buceo, paracaídas, zoológico, minigolf, playa o robos. Si la descuidas, se pierden detalles como tomarse de la mano o besarse, aunque se puede recuperar.</li>
  <li>Se pueden llamar o mandar mensajes en cualquier momento. Ignorar un mensaje de buenas noches puede afectar la relación.</li>
  <li>Las decisiones grandes y pequeñas cambian el desenlace.</li>
</ul>

<h2>Cambiar entre Jason y Lucia</h2>
<ul>
  <li>El personaje que no controlas sigue su propia rutina: puede estar en la casa segura o en otro sitio.</li>
  <li>Si están lejos, el cambio usa una vista aérea rápida; si están cerca, es casi instantáneo.</li>
  <li>En algunas misiones el cambio está bloqueado o es automático, como una persecución tras robar un banco donde Jason dispara y Lucia maneja.</li>
</ul>

<h2>Perfil Criminal</h2>
<ul>
  <li>Un sistema nuevo registra qué tipo de criminal eres y cómo reacciona el mundo. No es bueno contra malo como el honor de RDR2 y no da descuentos en tiendas.</li>
  <li>Lo que exige una misión o defenderte de quien te ataca no cuenta en tu contra. Pasarte de lo necesario de forma constante sí lo cambia.</li>
  <li>No es lo mismo dejar a alguien fuera de combate que ejecutarlo.</li>
</ul>

<h2>Policía, estrellas y "heat"</h2>
<ul>
  <li>Un crimen solo se reporta si hay testigos o salta una alarma. Las estrellas suben con menos facilidad que antes.</li>
  <li>La policía busca tu ropa, tu apariencia y tu auto. Cambiarte de ropa en una tienda, quitarte la máscara o cambiar de auto te ayuda a escapar.</li>
  <li>Puedes separar a Jason y Lucia para perder a la policía, o que uno maneje mientras el otro dispara.</li>
  <li>Nuevo fuego de supresión: disparas cerca para abrirte paso sin matar a nadie.</li>
  <li>Las patrullas ya no aparecen en el minimapa como en GTA 5. Con tres estrellas, escapar en auto es difícil sin algo muy rápido o una moto deportiva.</li>
  <li>El dinero en efectivo que cargas se pierde si mueres o te arrestan, así que conviene depositarlo en cajeros.</li>
</ul>

{AD}

<h2>Robos</h2>
<ul>
  <li>Los robos son parte central del juego entre misiones, y se puede robar casi cualquier negocio.</li>
  <li>Puedes entrar por atrás, abrir cerraduras con una snap gun, romper cámaras y borrar las grabaciones de seguridad.</li>
  <li>Las cajas fuertes se abren con la combinación o con explosivos, aunque los explosivos pueden dañar lo de adentro.</li>
  <li>El mapa marca escondites de pandillas con cuánto efectivo y droga guardan. La droga se vende a "fences".</li>
  <li>Joyerías y bancos pequeños se pueden robar solo o en pareja.</li>
  <li>Algunas partes de la historia piden juntar dinero antes de avanzar: las misiones solas no alcanzan.</li>
</ul>

<h2>Autos y robo de vehículos</h2>
<ul>
  <li>Se acabó el robo de un botón. Los autos viejos se abren con ganzúa y los nuevos o de lujo necesitan un clonador de llaves que consigues más adelante. A un conductor siempre lo puedes sacar del auto.</li>
  <li>El escáner del teléfono muestra si el auto está cerrado, si tiene alarma o rastreador, cuánto pagan por él y cuánto cuesta registrarlo.</li>
  <li>Los autos con rastreador avisan a la policía si vas despacio. Los "fences" quitan el rastreador, y uno llamado Randy pide modelos concretos.</li>
  <li>Pay 'n' Spray registra autos robados a tu nombre, los repara y les cambia el color. Un auto dañado vale menos.</li>
  <li>Al principio puedes tener tres vehículos; para más, compras garajes. Si abandonas un auto registrado tras un crimen, la policía lo puede incautar.</li>
  <li>Hay sistema de combustible: un auto robado puede venir casi vacío.</li>
  <li>Calles más estrechas y más tráfico, incluidos embotellamientos.</li>
</ul>

<h2>Armas</h2>
<ul>
  <li>Las armas largas ya no caben en el bolsillo: van en el maletero del auto o en un casillero de Ammu-Nation. Las que compras vuelven a tu auto personal.</li>
  <li>Ammu-Nation tiene armas exclusivas por tienda y más personalización.</li>
  <li>La gente reacciona si caminas con un arma a la vista.</li>
</ul>

<h2>Vida diaria, gimnasio y aspecto</h2>
<ul>
  <li>Las casas seguras funcionan como los campamentos de RDR2 y cambian con cada capítulo.</li>
  <li>El gimnasio tiene minijuego: entrenar tres días seguidos sube salud y fuerza. Si comes de más, engordas. La comida y las bebidas dan mejoras temporales.</li>
  <li>Dormir es opcional, pero sin dormir te cansas y la salud y la resistencia se recuperan más lento.</li>
  <li>Miles de conjuntos de ropa. Tiendas y peluquerías tienen artículos según la zona; en la casa segura solo puedes cortarte o raparte.</li>
  <li>Algunas tiendas cierran de noche y se puede entrar a muchos más edificios que en GTA 5.</li>
</ul>

<h2>Teléfono, apps y transporte</h2>
<ul>
  <li>El teléfono es un objeto físico dentro del juego, ya no una pantalla superpuesta.</li>
  <li>En Snapmatic puedes seguir cuentas y ver publicaciones, pero no subir nada, porque Jason y Lucia están escondidos. Las fotos se le pueden mandar a la pareja.</li>
  <li>Ryde Me (el Uber del juego) y los autobuses sirven como viaje rápido.</li>
  <li>Manteniendo pulsada la cruceta marcas un destino sin abrir el mapa.</li>
</ul>

<h2>El mundo de Leonida</h2>
<ul>
  <li>La gente tiene alturas y cuerpos mucho más variados que en cualquier GTA anterior.</li>
  <li>Hay eventos aleatorios que pueden interrumpirte, como otro ladrón que entra a la tienda mientras la estás robando.</li>
  <li>Más anuncios de radio y TV que nunca, y en la tele del juego hay una serie animada para adultos hecha con un estudio externo.</li>
  <li>Se pueden estudiar animales como colección, igual que en RDR2, y hay pesca.</li>
  <li>Si mueres, reapareces cerca en lugar de salir del hospital.</li>
</ul>

<h2>Lo técnico</h2>
<ul>
  <li>Sin microtransacciones en el modo historia. Esto no aplica al futuro modo online.</li>
  <li>Rockstar dice que no usó IA generativa en el desarrollo.</li>
  <li>La demo corría en una PS5 base a 30 FPS. No hay modo a 60 FPS confirmado ni detalles de mejoras para PS5 Pro.</li>
  <li>La interfaz se puede personalizar para mostrar muy poca información en pantalla.</li>
</ul>

<h2>Clima y fauna (Game Informer)</h2>
<p>Game Informer dedicó su portada y 14 páginas a Leonida, con entrevistas a diseñadores de Rockstar y 12 capturas nuevas.</p>
<ul>
  <li>Hay huracanes y tormentas tropicales con nubes densas, viento fuerte y mucha lluvia. El clima es local: puede llover en una zona y no en otra.</li>
  <li>El viento se simula con detalle, incluida la brisa del mar al atardecer y cómo los edificios lo bloquean.</li>
  <li>Más de 170 especies de animales, según el reportaje: más de 60 tipos de aves y más de 30 mamíferos terrestres, además de peces y reptiles. Hay manatíes, flamencos, pelícanos y caimanes.</li>
  <li>También hay especies invasoras reales de Florida, como iguanas verdes, sapos de caña y macacos.</li>
  <li>Los animales se clasifican como raros, descubribles y legendarios.</li>
  <li>Aaron Garbut, de Rockstar North, dijo que es el mapa más grande que ha hecho el estudio, con mucho margen.</li>
  <li>Actividades mencionadas: base jumping, billar, gimnasio, kayak, minigolf, buceo, carreras callejeras y todoterreno, zoológicos, hidrodeslizadores, motos de agua y senderismo.</li>
</ul>

<h2>Jason, Lucia y Vice City (Dazed y LOVE)</h2>
<ul>
  <li>Jason es un ex militar que terminó transportando droga y robando bancos. Lucia acaba de salir de prisión y es de Liberty City.</li>
  <li>Lucia es la que empuja la relación y Jason es el contrapeso. Rockstar la define como la primera protagonista femenina desarrollada a fondo en un GTA principal.</li>
  <li>Raul Bautista es el mentor mayor que les enseña a hacer golpes grandes y conoce el mundo criminal de Vice City.</li>
  <li>El sueño americano del juego es modesto: una casa para la familia y deudas pagadas, no hacerse millonarios.</li>
  <li>El "Florida Man" de las noticias existe en el juego como "Leonida Man".</li>
  <li>La música bebe del Miami bass. Se puede seguir el ascenso del dúo Real Dimez por sus posts virales en las redes del juego.</li>
  <li>Más de 50 artistas callejeros reales pintaron murales en Stockyard, el barrio inspirado en Wynwood.</li>
  <li>Hay elecciones, carteles de campaña, llamadas automáticas y programas de radio sobre la política de Leonida, pero sin políticos reales.</li>
  <li>Ambrosia está inspirada en Clewiston y el lago Okeechobee.</li>
  <li>El equipo de manejo de vehículos incluye pilotos de carreras reales.</li>
</ul>

<h2>Tráiler de lanzamiento (15 de octubre)</h2>
<p><a href="trailers-gta-6.html">Ver el tráiler y los anteriores</a></p>
<p>Rockstar publicó sin aviso previo el tráiler de lanzamiento, de alrededor de minuto y medio y grabado íntegramente dentro del juego en una PS5.</p>
<ul>
  <li>La descripción oficial resume la historia: un golpe fácil sale mal y Jason y Lucia acaban metidos en una conspiración criminal que se extiende por todo Leonida.</li>
  <li>Jason cuenta que se metió en problemas en el ejército, lo que explica cómo terminó en el crimen.</li>
  <li>Se ven robos a bancos, tiroteos y persecuciones con la policía, y una escena íntima entre los dos que confirma que están juntos.</li>
  <li>La música es "Flower in a Hurricane", de Justice con Tame Impala, SZA y King Gizzard &amp; The Lizard Wizard. Justice es también el compositor de la banda sonora original del juego.</li>
</ul>

<h2>Detrás del desarrollo (Bloomberg)</h2>
<p>Jason Schreier, de Bloomberg, visitó Rockstar North a finales de septiembre y publicó el 14 de octubre un reportaje sobre cómo se hizo el juego.</p>
<ul>
  <li>El proyecto empezó con el nombre en clave Project Americas y la idea de cubrir zonas de Norteamérica y Sudamérica. Luego se recortó.</li>
  <li>El primer viaje de investigación a Miami fue en 2015, y la historia de Jason y Lucia estaba definida a finales de 2019.</li>
  <li>La plantilla de Rockstar pasó de 2,441 a 4,711 empleados en 12 oficinas desde RDR2. Montaron un estudio en Los Ángeles solo para los NPC.</li>
  <li>El juego tiene tres directores: Rob Nelson, Aaron Garbut y Phil Hooker.</li>
  <li>Rockstar no reveló el presupuesto, pero negó el rumor de que superó los $1,500 millones.</li>
  <li>En septiembre el equipo ya estaba corrigiendo errores, y Schreier ve el 19 de noviembre como fecha firme.</li>
  <li>Rockstar dice que la tecnología creada para GTA 6 le permitirá sacar su próximo juego mucho antes que en ocho años.</li>
</ul>

<h2>Reportado por creadores (sin confirmación oficial)</h2>
<p>Rockstar invitó a TGG, elrubius, Davy Jones y Mike ShowSha a ver gameplay en Edimburgo sin jugarlo. Estos detalles salen de lo que contaron ellos:</p>
<ul>
  <li>Desmembramiento en combate.</li>
  <li>Se pueden meter cuerpos en el maletero.</li>
  <li>Fumar llena un medidor de Focus, parecido a la Dead Eye de RDR2, que resalta policías cercanos.</li>
  <li>Hoteles y edificios explorables piso por piso con ascensores y sin pantallas de carga.</li>
  <li>Antes de acariciar un perro, el juego pide permiso al dueño.</li>
</ul>

{AFF}"""

# ---------- Leaks CyberLeek ----------
leaks = f"""
<span class="mile">Leaks</span>
<h1>Los leaks de CyberLeek: qué mostraron y qué se confirmó</h1>
{UPD}
<p class="lede">Entre agosto y octubre de 2026, un grupo que se hace llamar CyberLeek publicó clips de gameplay de GTA 6 sin permiso de Rockstar. Aquí está la cronología, qué detalles coinciden con lo que Rockstar confirmó después y en qué terminó todo.</p>
<div class="note"><strong>Aviso de spoilers.</strong> Algunos clips muestran partes de la historia, como el prólogo de Lucia en prisión. Este sitio no enlaza ni aloja el material filtrado. No descargues archivos que digan ser la build del juego: son un riesgo de virus y estafa.</div>

<h2>Cronología</h2>
<div class="tbl"><table>
  <thead><tr><th>Fecha</th><th>Qué pasó</th></tr></thead>
  <tbody>
    <tr><td class="num">18–26 ago</td><td>CyberLeek publica 16 clips en nueve días: minijuego de baloncesto en la casa segura, pelea por un choque, robo a una gasolinera, vuelo en avioneta fumigadora, pesca, discotecas, playa, una tienda en Port Gellhorn y el prólogo de Lucia en prisión. Hacía encuestas para que la gente votara qué filtrar después.</td></tr>
    <tr><td class="num">27 ago</td><td>Rockstar estrena el Extended Look en Netflix y luego en YouTube. CyberLeek se queda en silencio durante semanas.</td></tr>
    <tr><td class="num">5 oct</td><td>Aparece una encuesta misteriosa en su web, con cierre el 8 de octubre.</td></tr>
    <tr><td class="num">8 oct</td><td>Publica "Extended Leek", unos 25 minutos de gameplay con escenas de misiones, carreras en Vice City, el Thrillbilly Mud Club y personalización de autos.</td></tr>
    <tr><td class="num">11 oct</td><td>Sale otro clip más corto centrado en Lucia.</td></tr>
    <tr><td class="num">12 oct</td><td>Amenaza con filtrar una build jugable si su criptomoneda llegaba a $30 millones de capitalización o si Take-Two sacaba discos físicos.</td></tr>
    <tr><td class="num">14 oct</td><td>Según los reportes, anuncia que se retira, no publica la build y cierra su web.</td></tr>
  </tbody>
</table></div>

{AD}

<h2>Lo que mostraron los leaks y ya está confirmado</h2>
<p>Varios detalles que se vieron primero en los clips los confirmó después Rockstar en entrevistas:</p>
<div class="tbl"><table>
  <thead><tr><th>En el leak</th><th>Estado</th></tr></thead>
  <tbody>
    <tr><td>Medidor de gasolina en los autos</td><td><span class="tag ok">Confirmado</span> Kinda Funny</td></tr>
    <tr><td>Guardar cosas en el maletero</td><td><span class="tag ok">Confirmado</span> IGN y Famitsu</td></tr>
    <tr><td>Saldo en efectivo y saldo en banco separados</td><td><span class="tag ok">Confirmado</span> Famitsu</td></tr>
    <tr><td>Pesca</td><td><span class="tag ok">Confirmado</span> Famitsu</td></tr>
    <tr><td>Robos a gasolineras y tiendas</td><td><span class="tag ok">Confirmado</span> Extended Look</td></tr>
    <tr><td>Avioneta fumigadora</td><td><span class="tag ok">Confirmado</span> captura de Game Informer</td></tr>
    <tr><td>Lucia en prisión al inicio</td><td><span class="tag ok">Coincide</span> con los tráilers oficiales</td></tr>
    <tr><td>Medidor de Focus</td><td><span class="tag no">Reportado</span> por creadores invitados</td></tr>
    <tr><td>Seis estrellas de búsqueda</td><td><span class="tag no">Sin confirmar</span></td></tr>
    <tr><td>Zonas donde la policía tarda más en enterarse de un crimen</td><td><span class="tag no">Sin confirmar</span> aunque Rockstar sí dijo que sin testigos no hay reporte</td></tr>
  </tbody>
</table></div>
<p>CyberLeek dijo que la build era reciente y que el juego no estaba listo. Hay indicios de lo contrario: una canción en uno de los clips apunta a una versión del año anterior, y Bloomberg reportó que en septiembre Rockstar ya estaba en fase de corrección de errores.</p>

<h2>La cripto y el dinero</h2>
<ul>
  <li>CyberLeek promocionaba una memecoin en sus videos.</li>
  <li>Dexerto reportó que el grupo ganó más de $250,000 ligados a esa moneda.</li>
  <li>Eso choca con su discurso de protesta contra la monetización de Rockstar y Take-Two.</li>
</ul>

<h2>Qué dijo Rockstar</h2>
<ul>
  <li>Rockstar lamentó que la gente viera el juego así después de tanta espera, en declaraciones recogidas por la BBC.</li>
  <li>Take-Two pidió retirar videos por derechos de autor en agosto y ha buscado órdenes judiciales para identificar al responsable.</li>
  <li>Hasta ahora nadie ha sido identificado ni acusado públicamente.</li>
</ul>

{AFF}"""

# ---------- Equipo para GTA 6 ----------
AFF_TAG = "leonida305-20"
from urllib.parse import quote_plus
def amz(q):
    return f"https://www.amazon.com/s?k={quote_plus(q)}&tag={AFF_TAG}"

def pick(tier, price, name, why, query):
    return (f'<article class="pick"><div class="pick-top"><span class="mile">{tier}</span>'
            f'<span class="price">{price}</span></div><h3>{name}</h3><p>{why}</p>'
            f'<a class="buy" href="{amz(query)}" rel="sponsored nofollow" target="_blank">Ver precios en Amazon</a></article>')

equipo = f"""
<span class="mile">Equipo</span>
<h1>Todo lo que necesitas para jugar GTA 6</h1>
{UPD}
<p class="lede">Tele, monitor, almacenamiento, sillas, accesorios, libros y merch para tener todo listo antes del 19 de noviembre, con opciones económicas y de gama alta.</p>
<p class="disclosure">Como afiliado de Amazon, este sitio gana una comisión por compras que califiquen, sin costo extra para ti. Los precios cambian a menudo: revisa el precio final en la tienda.</p>

<div class="note"><strong>Antes de comprar, esto importa.</strong> En la demo de prensa GTA 6 corría a 30 FPS en una PS5 normal, y Rockstar no ha confirmado un modo a 60 FPS. Por eso, para este juego pesa más una buena imagen (HDR, contraste, colores) que una tasa de refresco altísima. Aun así, busca HDMI 2.1 y VRR: son los que te dejan aprovechar un posible modo rendimiento o la PS5 Pro.</div>

<h2>Televisores</h2>
<div class="picks">
  {pick("Económica", "menos de $600", "TCL serie QM6 / QM7 o Hisense serie U7", "Mini-LED con buen brillo para el HDR del sol de Vice City, 120 Hz y HDMI 2.1 con VRR. La mejor relación calidad-precio para consola.", "TCL QM7 mini LED 4K 55 pulgadas")}
  {pick("Media", "$600 a $1,200", "Hisense serie U8 o LG OLED serie B", "Un salto en contraste y brillo. La OLED de LG da negros perfectos para las noches de Vice City; la Hisense brilla más si tu sala tiene mucha luz.", "LG OLED B series 55 4K 120Hz")}
  {pick("Gama alta", "más de $1,500", "LG OLED C6, Samsung OLED S95H o Sony Bravia 8", "OLED de primera con 4K a 120 Hz, VRR y HDMI 2.1. RTINGS pone a la Samsung S95H como la mejor tele que ha probado para PS5.", "LG OLED C6 65 pulgadas")}
</div>

{AD}

<h2>Monitores</h2>
<p>Un monitor sirve si juegas en tu cuarto o en un escritorio. Ojo: casi ninguno trae buenas bocinas, así que suma unos audífonos.</p>
<div class="picks">
  {pick("Económico", "menos de $350", "Asus TUF Gaming VG289Q", "4K de 28 pulgadas a 60 Hz. Para un juego que corre a 30 FPS en consola, cumple de sobra. No tiene HDMI 2.1.", "Asus TUF Gaming VG289Q 4K monitor")}
  {pick("Medio", "", "Gigabyte M32UC", "4K curvo de 32 pulgadas a 144 Hz con HDMI 2.1. Listo para un modo rendimiento si llega.", "Gigabyte M32UC 4K 144Hz monitor")}
  {pick("Gama alta", "alrededor de $1,000", "Alienware AW3225QF o Asus ROG Swift OLED PG27UCDM", "Paneles QD-OLED 4K con contraste perfecto. El Alienware trae HDMI 2.1; RTINGS considera el Asus su mejor monitor para PS5.", "Alienware AW3225QF QD-OLED 4K")}
</div>

<h2>Almacenamiento</h2>
<p>Rockstar no ha dicho cuánto pesa el juego. Las filtraciones hablan de cerca de 200 GB, así que conviene tener espacio de sobra antes de la precarga del 12 de noviembre.</p>
<div class="picks">
  {pick("PS5", "1 a 2 TB", "SSD M.2 PCIe 4.0 con disipador", "Sony pide un SSD Gen4 con disipador. Modelos como el WD_BLACK SN850X o el Samsung 990 Pro con disipador se instalan en minutos.", "WD_BLACK SN850X heatsink PS5 2TB")}
  {pick("Xbox Series X|S", "1 a 2 TB", "Tarjeta de expansión de almacenamiento", "La forma oficial de ampliar la memoria rápida de Xbox: se conecta atrás y listo.", "Xbox Series X storage expansion card 2TB")}
</div>

<h2>Sillas gaming</h2>
<p>GTA 6 se va a jugar en sesiones largas. Una buena silla se nota en la espalda después de tres horas en Vice City.</p>
<div class="picks">
  {pick("Económica", "unos $200 a $270", "Corsair TC100 Relaxed", "Acolchado cómodo y diseño discreto a buen precio. Es de las mejores económicas, aunque armarla lleva un rato.", "Corsair TC100 Relaxed gaming chair")}
  {pick("Media", "unos $450 a $550", "Secretlab Titan Evo", "La silla gaming más recomendada: soporte lumbar ajustable, cojín magnético para la cabeza y reposabrazos 4D. Viene en varias tallas.", "Secretlab Titan Evo gaming chair")}
  {pick("Para personas grandes", "unos $500", "AndaSeat Kaiser 4 XL", "Asiento amplio para personas altas o corpulentas, con cojín lumbar cómodo.", "AndaSeat Kaiser 4 XL gaming chair")}
  {pick("Gama alta", "unos $2,400", "Herman Miller x Logitech Embody", "Ergonomía de primer nivel y 12 años de garantía. Llega armada. Es carísima y no trae reposacabezas.", "Herman Miller Logitech Embody gaming chair")}
</div>

<h2>Accesorios</h2>
<div class="picks">
  {pick("Mando PS5", "", "DualSense extra", "Para sesiones largas sin quedarte sin batería. Rockstar ajustó la vibración háptica y los gatillos del DualSense para manejar en GTA 6.", "DualSense controller PS5")}
  {pick("Mando Xbox económico", "menos de $50", "GameSir G7 SE", "Mando con licencia oficial de Xbox, con sticks Hall Effect que no sufren drift y botones traseros programables. Funciona en Xbox Series X|S y PC.", "GameSir G7 SE Xbox controller")}
  {pick("Mando Xbox con estilo", "unos $90", "Turtle Beach Pacific Skyline", "Inalámbrico, con palmeras y colores pastel muy a tono con Vice City, luces RGB, sticks TMR sin drift y dos botones traseros. Funciona en Xbox Series X|S, Xbox One y PC.", "Turtle Beach Pacific Skyline wireless controller")}
  {pick("Audio", "", "Audífonos gaming", "Para escuchar la radio de Vice City y los diálogos de los NPC sin molestar a nadie en casa.", "PS5 Xbox gaming headset wireless")}
  {pick("Tarjetas", "", "Tarjeta de PlayStation Store o Xbox", "Para comprar la versión digital y precargar el 12 de noviembre.", "PlayStation Store gift card")}
</div>
<h2>Libros y cómics</h2>
<div class="picks">
  {pick("Cómic", "", "American Caper, volumen 1: Red-Pilled Blues", "El cómic de Dan Houser, cofundador de Rockstar y guionista de GTA y Red Dead. Una historia de crimen y sátira de Estados Unidos con el humor que hizo famosa a la saga.", "American Caper Volume 1 Red-Pilled Blues Dan Houser")}
  {pick("Cómic", "", "American Caper, volumen 2: Cowboys and Conspiracies", "La continuación de la serie de Dan Houser. Para leer después del primero.", "American Caper Volume 2 Cowboys and Conspiracies")}
  {pick("Humor", "", "Life Before GTA 6", "Libro de humor no oficial sobre todo lo que nos pasó mientras esperábamos GTA 6. Buen regalo para el amigo que lleva años contando los días.", "Life Before GTA 6 Zane Ark")}
</div>

<h2>Merch y decoración</h2>
<div class="picks">
  {pick("Decoración", "", "Imanes estilo GTA (12 piezas)", "Doce imanes de vinilo con el \"Wasted\", autos, billetes y el minimapa. Para la nevera, el casillero o el auto. Producto no oficial.", "Babymiu Wasted car adventure game fridge magnet 12 pack")}
  {pick("Parche", "", "Parche bordado \"Wasted\"", "El mensaje más famoso de la saga en un parche con velcro, para la mochila, la gorra o la chaqueta. Producto no oficial.", "Artistry Bloom Wasted patch hook and loop")}
</div>"""

# ---------- Mapa real de Miami ----------
import json as _json
LUGARES = [
  # tipo: juego | marketing
  ("juego", "Sahara Arena", "Kaseya Center", "601 Biscayne Blvd, Miami", 25.7814, -80.1870, "La arena de los Miami Heat aparece en el juego como Sahara Arena, en la orilla de la bahía."),
  ("juego", "Galina Ballet Opera House y Vice City Concert Hall", "Adrienne Arsht Center (Knight Concert Hall)", "1300 Biscayne Blvd, Miami", 25.7873, -80.1897, "El centro de artes escénicas de Miami tiene su versión en el juego, con todo y sala de conciertos."),
  ("juego", "Megamundo", "One Biscayne Tower", "2 S Biscayne Blvd, Miami", 25.7741, -80.1872, "Rascacielos del downtown recreado en el juego como Megamundo."),
  ("juego", "Heath Tower", "Miami Tower", "100 SE 2nd St, Miami", 25.7726, -80.1916, "El rascacielos que cambia de color por la noche, uno de los más reconocibles del skyline."),
  ("juego", "Arcadia Towers", "Vizcayne", "244 Biscayne Blvd, Miami", 25.7766, -80.1878, "Las torres gemelas de condos frente al Bayside, en pleno downtown."),
  ("juego", "NINE1NINE", "E11EVEN Miami", "29 NE 11th St, Miami", 25.7849, -80.1919, "La discoteca 24 horas más famosa de Miami. En el juego se llama NINE1NINE."),
  ("juego", "The Sumerian", "Marriott Miami Biscayne Bay", "1633 N Bayshore Dr, Miami", 25.7920, -80.1866, "El hotel de la bahía recreado como The Sumerian."),
  ("juego", "Sahara HQ", "Brickell Arch", "1395 Brickell Ave, Miami", 25.7593, -80.1925, "El edificio de arco en Brickell, el distrito financiero."),
  ("juego", "Torre de Brickell en el tráiler", "Brickell on the River", "31 SE 5th St, Miami", 25.7697, -80.1913, "Las torres junto al río Miami que se ven en el tráiler."),
  ("juego", "Fleeca Field", "loanDepot park", "501 Marlins Way, Miami", 25.7781, -80.2196, "El estadio de los Marlins, rebautizado con el banco Fleeca de la saga."),
  ("juego", "Stockyard", "Wynwood Walls", "2516 NW 2nd Ave, Miami", 25.8010, -80.1994, "Wynwood inspira el barrio de Stockyard. Rockstar contrató a más de 50 artistas callejeros reales para pintar sus murales."),
  ("juego", "Comisaría de Vice City", "Miami Police Department", "400 NW 2nd Ave, Miami", 25.7787, -80.1972, "La sede de la policía de Miami tiene su versión en el juego."),
  ("juego", "Aeropuerto de Vice City (VCIA)", "Aeropuerto Internacional de Miami", "2100 NW 42nd Ave, Miami", 25.7959, -80.2870, "La torre de control, la estación del metro y hasta el edificio de Signature Flight Support están recreados."),
  ("juego", "Edificio de Lucia", "Bayshore Drive, frente a Quantum on the Bay", "N Bayshore Dr, Miami", 25.7951, -80.1871, "Un fan ubicó aquí el edificio de Lucia. El edificio real fue demolido en 2023."),
  ("juego", "Hotel Dixon", "Hotel Victor", "1144 Ocean Dr, Miami Beach", 25.7811, -80.1302, "Hotel art déco de Ocean Drive, recreado como Hotel Dixon."),
  ("juego", "Hotel Boardwalk", "Hotel Breakwater", "940 Ocean Dr, Miami Beach", 25.7794, -80.1309, "Su letrero art déco es uno de los iconos de Ocean Drive."),
  ("juego", "Hotel del tráiler en South Pointe", "Hilton Bentley Miami/South Beach", "101 Ocean Dr, Miami Beach", 25.7686, -80.1336, "Hotel del extremo sur de Miami Beach que aparece en el tráiler."),
  ("juego", "Hotel de Collins Avenue", "Loews Miami Beach Hotel", "1601 Collins Ave, Miami Beach", 25.7881, -80.1291, "Hotel de Collins Avenue identificado en el juego."),
  ("juego", "Effluvia (comparación de fans)", "Juvia (cerrado)", "1111 Lincoln Rd, Miami Beach", 25.7908, -80.1405, "El rooftop bar de Effluvia que se vio en el Extended Look recuerda a Juvia, el rooftop de Lincoln Road que ya cerró."),
  ("juego", "Puente de los Cayos de Leonida", "Seven Mile Bridge", "Overseas Hwy, Cayos de Florida", 24.7039, -81.1530, "El puente que une los Cayos sale en el tráiler y es la entrada a los Cayos de Leonida."),
  ("marketing", "Letrero \"Welcome to Vice City\"", "Techo del Kaseya Center", "601 Biscayne Blvd, Miami", 25.7818, -80.1865, "Letrero iluminado en rosa sobre el techo de la arena. Según reportes, el acuerdo ronda los $975,000."),
  ("marketing", "A Night in Vice City", "Kaseya Center", "601 Biscayne Blvd, Miami", 25.7810, -80.1875, "El 18 de noviembre, Heat vs. Bucks con cancha y uniformes de Vice City. Dentro de la arena ya hay un mostrador de Burger Shot con su fachada roja y menús del juego, y la tienda de los Heat vende camisetas y gorras de Vice City."),
  ("marketing", "Sombrillas y tumbonas de Vice City", "Playa de Miami Beach", "South Beach, Miami Beach", 25.7838, -80.1283, "Desde el 15 de octubre y hasta el 31 de diciembre, las sillas, sombrillas y cabañas de Boucher Brothers en la playa llevan la marca de Vice City."),
  ("marketing", "Banners de GTA 6", "Zona de eventos del downtown", "Downtown Miami (zona aproximada)", 25.7752, -80.1920, "Desde el 15 de octubre, la ciudad permite banners de GTA 6 en una zona del downtown, por un máximo de 56 días. Por estas calles también circulan autobuses con \"I ♥ Vice City\"."),
  ("marketing", "Pantallas y \"In for VI\"", "Hard Rock Stadium", "347 Don Shula Dr, Miami Gardens", 25.9580, -80.2389, "En el Dolphins vs. Bengals del 11 de octubre hubo anuncios de GTA 6 y un gráfico \"In for VI\" en los touchdowns."),
  ("marketing", "Banner doble de GTA 6", "Hotel YVE", "146 Biscayne Blvd, Miami", 25.7747, -80.1876, "Desde el 19 de octubre, la fachada del hotel tiene un banner doble de GTA 6 frente a Biscayne Boulevard."),
  ("marketing", "Mural \"Good Idea\" de Ron English", "Wynwood", "Wynwood Arts District, Miami", 25.802404, -80.202064, "Uno de los murales de Vice City pintados en Wynwood en octubre. Por la zona también están \"We ♥ Vice City\" de Queen Andrea, \"Eyes\" de Enjoy Denial y uno de un caimán con una mujer y una bolsa de dinero."),
  ("marketing", "Murales de Tatiana Suarez y \"Camouflage\"", "Wynwood", "Wynwood Arts District, Miami", 25.800089, -80.202225, "Dos murales más de la campaña de Vice City, pintados a mediados de octubre."),
  ("marketing", "Pantallas de Vice City", "NW 26th St", "NW 26th St, Wynwood (zona aproximada)", 25.8007, -80.2010, "Pantallas digitales de la calle con anuncios de Vice City."),
  ("marketing", "Carrito \"Welcome to Vice City\"", "Collins Ave y 5th St", "Collins Ave & 5th St, Miami Beach", 25.7737, -80.1336, "Un carrito con el mensaje \"Welcome to Vice City\" en plena South Beach."),
  ("marketing", "Columnas del Metrorail", "Metrorail de Miami", "Downtown Miami (zona aproximada)", 25.7740, -80.1962, "Columnas del Metrorail forradas con los colores de GTA 6."),
]
_lugares_js = _json.dumps([dict(t=t, g=g, r=r, a=a, lat=la, lng=ln, d=d) for (t, g, r, a, la, ln, d) in LUGARES], ensure_ascii=False)

def _item(i, l):
    t, g, r, a, la, ln, d = l
    tag = '<span class="tag ok">En el juego</span>' if t == "juego" else '<span class="tag mk">Marketing</span>'
    return (f'<li data-t="{t}"><button type="button" class="lugar" data-i="{i}">'
            f'{tag}<strong>{g}</strong><span class="real">{r} · {a}</span></button></li>')

mapa_real = f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
<span class="mile">Miami real</span>
<h1>Mapa de Vice City en el Miami real</h1>
{UPD}
<p class="lede">Los lugares reales de Miami y Florida que inspiraron Vice City y los Cayos de Leonida, más todo el marketing de GTA 6 que Rockstar está montando en la ciudad.</p>
<div class="filtros" role="group" aria-label="Filtrar lugares">
  <button type="button" class="f on" data-f="todos">Todos</button>
  <button type="button" class="f" data-f="juego">En el juego</button>
  <button type="button" class="f" data-f="marketing">Marketing de GTA 6</button>
</div>
<div id="mapa" role="region" aria-label="Mapa interactivo de Miami"></div>
<p class="updated">Ubicaciones aproximadas. Toca un punto o un lugar de la lista para ver los detalles.</p>
<ul class="lugares" id="lista">{''.join(_item(i, l) for i, l in enumerate(LUGARES))}</ul>
<div class="note"><strong>De dónde salen estos datos.</strong> Las comparaciones vienen de los tráilers, el Extended Look y del mapeo de la comunidad. Algunas son de fans y Rockstar no las ha confirmado una por una. El marketing sale de anuncios de las ciudades de Miami y Miami Beach y de lo que han reportado medios y gente en la calle.</div>
{AD}
<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Vice City es Miami?</dt><dd>Sí. Vice City es la versión de Rockstar de Miami, y Leonida es su versión de Florida. Muchos edificios reales aparecen recreados con otros nombres.</dd>
  <dt>¿Dónde está el letrero de Vice City en Miami?</dt><dd>En el techo del Kaseya Center, la arena de los Miami Heat en Biscayne Boulevard.</dd>
  <dt>¿Qué pasa el 18 de noviembre en Miami?</dt><dd>Los Heat juegan "A Night in Vice City" contra los Bucks en el Kaseya Center, con cancha y uniformes temáticos, la noche antes del lanzamiento.</dd>
</dl>
{AFF}
<script>
(function(){{
  var L_=window.L, data={_lugares_js};
  var lista=document.getElementById("lista"), btns=lista.querySelectorAll(".lugar");
  if(!L_){{document.getElementById("mapa").innerHTML='<p class="mapa-error">No se pudo cargar el mapa. La lista de lugares está abajo.</p>';return;}}
  var map=L_.map("mapa",{{scrollWheelZoom:false}}).setView([25.785,-80.19],12);
  L_.tileLayer("https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png",{{maxZoom:19,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'}}).addTo(map);
  function icon(t){{return L_.divIcon({{className:"pin pin-"+t,iconSize:[18,18],iconAnchor:[9,9],popupAnchor:[0,-8]}});}}
  function esc(s){{var e=document.createElement("span");e.textContent=s;return e.innerHTML;}}
  var marks=data.map(function(p){{
    var m=L_.marker([p.lat,p.lng],{{icon:icon(p.t),title:p.g}}).bindPopup(
      '<div class="pop"><span class="pop-t">'+(p.t==="juego"?"En el juego":"Marketing de GTA 6")+'</span><b>'+esc(p.g)+'</b><i>'+esc(p.r)+'</i><small>'+esc(p.a)+'</small><p>'+esc(p.d)+'</p></div>');
    m.addTo(map); return m;
  }});
  btns.forEach(function(b){{b.addEventListener("click",function(){{
    var i=+b.dataset.i,p=data[i]; map.flyTo([p.lat,p.lng],p.lat<25?10:16,{{duration:.8}}); marks[i].openPopup();
    document.getElementById("mapa").scrollIntoView({{behavior:"smooth",block:"center"}});
  }});}});
  document.querySelectorAll(".f").forEach(function(f){{f.addEventListener("click",function(){{
    var v=f.dataset.f; document.querySelectorAll(".f").forEach(function(x){{x.classList.toggle("on",x===f);}});
    data.forEach(function(p,i){{var show=v==="todos"||p.t===v; if(show)marks[i].addTo(map); else map.removeLayer(marks[i]);
      lista.children[i].hidden=!show;}});
  }});}});
}})();
</script>"""

# ---------- Música y radios ----------
RADIOS = [
  ("Flash FM", "Pop", "Robyn y Alex Consani", "Charli xcx, \"Good Ones\" · MGMT, \"Electric Feel\" · Zara Larsson y PinkPantheress, \"Midnight Sun (Girls Trip)\""),
  ("Cocoteo FM", "Latino actual", "Bad Bunny (El Martillo) y RaiNao (La Gata)", "Bad Bunny, \"EoO\" · Axel Rulay con Farruko y El Alfa, \"Si Es Trucho Es Trucho (Remix)\" · Romeo Santos y El Chaval de la Bachata, \"Canalla\""),
  ("Back Country Radio", "Country clásico y outlaw", "Morgan Wallen, Lana Del Rey (Delta Dawne) y Jeremy Dufrene (Mud Dog Mike)", "David Allan Coe, \"Need a Little Time Off for Bad Behavior\" · Loretta Lynn, \"Don't Come Home A-Drinkin'\" · Hank Williams Jr. y Waylon Jennings, \"The Conversation\""),
  ("The Chamber 106.6", "Metal y hard rock", "Kerry King y Tom Araya, de Slayer", "Black Sabbath, \"I\" · Pantera, \"I'm Broken\" · Slayer, \"Raining Blood\""),
  ("AfroBank FM", "Afrobeats y amapiano", "Burna Boy y Palms Trax", "Asake, \"Joha\" · Pat Thomas con Ebo Taylor, \"Gye Wani\" · DJ Lag y Robot Boii con Kamo Mphela, \"Shay'sana\""),
  ("Dirty South Classics", "Rap y hip hop del sur", "Trick Daddy y Trina", "David Banner con Lil' Flip, \"Like A Pimp\" · JT Money con Solé, \"Who Dat\" · DJ Khaled con Trick Daddy, Rick Ross y Pitbull, \"Born N Raised\""),
]
SINGLES = [
  ("Yung Lean con Future y Metro Boomin", "That's It"),
  ("Travis Scott", "RHYNO"),
  ("CA7RIEL y Paco Amoroso, PinkPantheress, Fred again.. y Etienne de Crécy", "Sexy Magic"),
  ("Morgan Wallen", "Last Thing You Need"),
  ("Rauw Alejandro", "Macacoa 2000"),
  ("Keith Richards", "Bright Lights, Big City"),
  ("Justice con Tame Impala, SZA y King Gizzard &amp; The Lizard Wizard", "Flower in a Hurricane"),
]
import re as _re
def _slug(n): return _re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")
_radios = "".join(
    f'<article class="radio"><img class="radio-img" src="img/radios/{_slug(n)}.jpg" width="800" height="500" loading="lazy" alt="Logo oficial de {n} en GTA 6"><div class="pick-top"><h3>{n}</h3><span class="tag no">{g}</span></div>'
    f'<p class="hosts">Locutores: {h}</p><ul>' + "".join(f"<li>{c.strip()}</li>" for c in s.split("·")) + '</ul></article>'
    for n, g, h, s in RADIOS)
_singles = "".join(f'<tr><td>{a}</td><td><strong>{t}</strong></td></tr>' for a, t in SINGLES)

musica = f"""
<span class="mile">Música</span>
<h1>GTA 6: radios, canciones y GTA VI: The Album</h1>
{UPD}
<p class="lede">Rockstar ya mostró seis emisoras de radio de GTA 6 con locutores famosos, como Bad Bunny, Lana Del Rey y Morgan Wallen. Además, el 19 de noviembre sale <strong>Grand Theft Auto VI: The Album</strong>, con 34 canciones originales, y la banda sonora original del juego es obra del dúo francés Justice.</p>

<h2>Las radios confirmadas</h2>
<p>Estas son las emisoras que Rockstar presentó el 8 de octubre en su web oficial. Es solo un adelanto: el juego tendrá más.</p>
<div class="radios">{_radios}</div>
<p class="credito-img">Logos de las emisoras: Rockstar Games.</p>
<div class="note"><strong>Novedad en la saga.</strong> Por primera vez la radio se puede escuchar caminando: Jason y Lucia la oyen en el teléfono con audífonos. También hay pódcast a la carta, a pie o en el auto.</div>

{AD}

<h2>GTA VI: The Album</h2>
<ul>
  <li><strong>Sale el 19 de noviembre de 2026</strong>, el mismo día que el juego.</li>
  <li><strong>34 canciones originales</strong> hechas para GTA 6.</li>
  <li>Se puede reservar en <strong>vinilo</strong> (normal y edición limitada) y <strong>CD</strong>, y guardar en las plataformas de streaming.</li>
  <li>La canción de Travis Scott la produjo Guy-Manuel de Homem-Christo, de Daft Punk.</li>
  <li><strong>Justice</strong> compuso la banda sonora original (el score) del juego. Su sencillo "Flower in a Hurricane", con Tame Impala, SZA y King Gizzard &amp; The Lizard Wizard, suena en el tráiler de lanzamiento del 15 de octubre y está incluido en el álbum.</li>
</ul>
<h3>Los 7 sencillos que ya están en streaming</h3>
<div class="tbl"><table>
  <thead><tr><th>Artista</th><th>Canción</th></tr></thead>
  <tbody>{_singles}</tbody>
</table></div>

<div class="picks">
  {pick("Vinilo", "", "GTA VI: The Album en vinilo", "Para coleccionistas: el disco oficial con las 34 canciones originales del juego.", "Grand Theft Auto VI The Album vinyl")}
  {pick("CD", "", "GTA VI: The Album en CD", "La opción más económica en físico para tener la banda sonora.", "Grand Theft Auto VI The Album CD")}
  {pick("Audio", "", "Audífonos para escuchar Leonida", "Ahora que la radio suena hasta caminando, unos buenos audífonos marcan la diferencia.", "PS5 Xbox gaming headset wireless")}
</div>

<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Bad Bunny sale en GTA 6?</dt><dd>Sí. Es locutor de Cocoteo FM, la emisora de música latina, con el nombre de El Martillo, y suena su canción "EoO".</dd>
  <dt>¿Vuelven Flash FM o V-Rock?</dt><dd>Flash FM vuelve, ahora con pop actual. V-Rock no está entre las seis emisoras presentadas hasta ahora.</dd>
  <dt>¿Cuándo sale el álbum de GTA 6?</dt><dd>El 19 de noviembre de 2026, junto con el juego. Siete canciones ya están en streaming.</dd>
  <dt>¿Quién hace la música original de GTA 6?</dt><dd>El dúo electrónico Justice compuso la banda sonora original. Rockstar lo dio a conocer con el tráiler de lanzamiento.</dd>
</dl>
{AFF}"""


# ---------- Tráilers ----------
_tr = "".join(f'<section class="trailer"><h2>{t}</h2><p class="updated">{d}</p>{video(v, t + " de GTA 6")}<p>{x}</p></section>' for v, t, d, x in TRAILERS)
trailers = f"""
<span class="mile">Videos</span>
<h1>Todos los tráilers de GTA 6</h1>
{UPD}
<p class="lede">Los tres tráilers oficiales que ha publicado Rockstar, del más nuevo al más antiguo. Toca uno para verlo aquí mismo.</p>
{_tr}
<div class="note"><strong>¿Y el Extended Look?</strong> El 27 de agosto Rockstar estrenó en Netflix y luego en YouTube un video más largo con gameplay. No es un tráiler como tal; todo lo que se vio está resumido en <a href="todo-lo-confirmado.html">Todo lo confirmado</a>.</div>
{AD}
<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Cuántos tráilers tiene GTA 6?</dt><dd>Tres oficiales: el tráiler 1 (diciembre de 2023), el tráiler 2 (mayo de 2025) y el tráiler de lanzamiento (15 de octubre de 2026).</dd>
  <dt>¿Qué canción suena en el tráiler de lanzamiento?</dt><dd>"Flower in a Hurricane", de Justice con Tame Impala, SZA y King Gizzard &amp; The Lizard Wizard. Justice también compuso la banda sonora original del juego.</dd>
  <dt>¿Los tráilers están grabados en el juego?</dt><dd>Sí. Rockstar indica que el tráiler 2 y el de lanzamiento se capturaron dentro del juego en una PS5.</dd>
</dl>
{YT_JS}
{AFF}"""

pages = {
    "trailers-gta-6.html": (trailers, "Todos los tráilers de GTA 6 | Leonida Global 305", "Mira los tres tráilers oficiales de GTA 6: el tráiler 1, el tráiler 2 y el tráiler de lanzamiento, con lo que muestra cada uno.", True),
    "musica-radios-gta-6.html": (musica, "Radios y canciones de GTA 6 y GTA VI: The Album | Leonida Global 305", "Todas las radios confirmadas de GTA 6 con sus locutores y canciones, y todo sobre GTA VI: The Album, el disco oficial de 34 canciones.", True),
    "mapa-miami-real.html": (mapa_real, "Mapa de Vice City en el Miami real | Leonida Global 305", "Mapa interactivo con los lugares reales de Miami y Florida que aparecen en GTA 6 y todo el marketing de Vice City en la ciudad.", True),
    "equipo-gta-6.html": (equipo, "Equipo para GTA 6: teles, monitores y SSD | Leonida Global 305", "Las mejores teles, monitores, SSD y accesorios para jugar GTA 6, con opciones económicas y de gama alta.", True),
    "leaks-cyberleek.html": (leaks, "Leaks de GTA 6 de CyberLeek | Leonida Global 305", "Cronología de los leaks de GTA 6 de CyberLeek, qué detalles confirmó Rockstar después y cómo terminó la filtración.", True),
    "todo-lo-confirmado.html": (conf, "GTA 6: todo lo confirmado | Leonida Global 305", "Todos los detalles de GTA 6 confirmados por Rockstar a IGN, Famitsu, Game Informer, Dazed, LOVE, Bloomberg y en el Extended Look.", True),
    "index.html": (index, "Leonida Global 305", "Guías de GTA 6: fecha, precio, mapa de Leonida, personajes, música y Vice City en el Miami real.", False),
    "fecha-precio-ediciones.html": (fecha, "GTA 6: fecha, precio y ediciones | Leonida Global 305", "GTA 6 sale el 19 de noviembre de 2026. Precio de la edición estándar y Ultimate, precarga y qué incluye cada una.", True),
    "mapa-leonida.html": (mapa, "Mapa de GTA 6: regiones de Leonida | Leonida Global 305", "Las seis regiones confirmadas del mapa de GTA 6 y su inspiración real en Florida.", True),
    "personajes.html": (pers, "Personajes de GTA 6 | Leonida Global 305", "Jason Duval, Lucia Caminos y todos los personajes confirmados de GTA 6.", True),
}
# Medios consultados por página: se muestran como mención, sin enlace.
CREDITOS = {
    "fecha-precio-ediciones.html": ["Rockstar Games", "Take-Two Interactive", "Gfinity", "tbreak", "SVG", "GTA Intel"],
    "mapa-leonida.html": ["Rockstar Games", "LOVE", "Beebom", "All Things How"],
    "personajes.html": ["Rockstar Games", "TechRadar", "PC Gamer", "Dazed", "LOVE"],
    "todo-lo-confirmado.html": ["IGN", "Famitsu", "Kinda Funny", "Game Informer", "Dazed", "LOVE", "Bloomberg (Jason Schreier)", "PC Gamer", "Kotaku", "Insider Gaming", "GTAVice.net", "iGrandTheftAuto", "Inven Global"],
    "leaks-cyberleek.html": ["Dexerto", "iGeeksBlog", "Tech Insider", "BBC"],
    "equipo-gta-6.html": ["RTINGS", "TechRadar", "GamesRadar", "Windows Central", "Turtle Beach", "PC Gamer"],
    "musica-radios-gta-6.html": ["Rockstar Games", "Forbes", "Kotaku", "Consequence", "G2A News", "Insider Gaming", "Stereogum"],
    "trailers-gta-6.html": ["Rockstar Games", "Insider Gaming", "Pure Xbox"],
    "mapa-miami-real.html": ["GTA BOOM", "Miami New Times", "Kotaku", "VGC", "GamesRadar", "Portal Viciados y @samchrme"],
}
def creditos(slug):
    c = CREDITOS.get(slug)
    return f'<p class="creditos">Información basada en: {", ".join(c)}.</p>' if c else ""

for slug, (body, title, desc, full) in pages.items():
    body = body + creditos(slug)
    with open(os.path.join(OUT, slug), "w", encoding="utf-8") as f:
        f.write(shell(slug, title, desc, body, full))
print("ok", sorted(os.listdir(OUT)))

if DEPLOY:
    import datetime
    today = datetime.date.today().isoformat()
    urls = "".join(f"<url><loc>{DOMAIN}/{'' if k == 'index.html' else k}</loc><lastmod>{today}</lastmod></url>" for k in pages)
    open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>")
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    open(os.path.join(OUT, "CNAME"), "w").write("leonidaglobal305.com\n")
