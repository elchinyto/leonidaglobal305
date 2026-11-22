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
.fotos-visita{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:14px 0 6px}
.fotos-visita figure{margin:0;min-width:0}
.fotos-visita img{width:100%;height:auto;aspect-ratio:3/4;object-fit:cover;display:block;border:1px solid var(--line)}
.fotos-visita figcaption{font-size:.8rem;color:var(--muted);margin-top:5px}
.score-fotos{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin:14px 0 6px}
.score-fotos figure{margin:0;min-width:0}
.score-fotos img{width:100%;height:auto;display:block;border:1px solid var(--line)}
.score-fotos figcaption{font-size:.82rem;color:var(--muted);margin-top:6px}
.share-x{display:inline-flex;align-items:center;gap:6px;margin:2px 0 6px;padding:7px 14px;border-radius:999px;background:var(--fg);color:var(--bg);font-weight:700;font-size:.88rem;text-decoration:none}
.share-x::before{content:"𝕏";font-weight:700}
.share-x:hover{filter:brightness(1.15)}
.share-x:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
.cd-label{margin:16px 0 -8px;font-family:var(--f-mono);font-size:.78rem;text-transform:uppercase;letter-spacing:.08em;color:var(--teal);font-weight:500}
.cd-done{font-family:var(--f-display);font-size:1.8rem;text-transform:uppercase;color:var(--accent);margin:14px 0}
.cd .count{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.cd .count div{min-width:0}
@media (max-width:480px){.cd .count b{font-size:1.8rem}.cd-sm .count b{font-size:1.4rem}.cd .count small{font-size:.62rem;letter-spacing:.03em}}
.cd-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;margin-top:6px}
.cd-sm .count{margin:14px 0 8px}
.cd-sm .count div{padding:8px 10px;border-width:1px}
.cd-sm .count b{font-size:1.6rem}
.cd-sm .cd-done{font-size:1.3rem}
.revista{display:flex;gap:22px;align-items:flex-start;flex-wrap:wrap;margin:26px 0;padding-top:18px;border-top:1px solid var(--line)}
.revista figure{margin:0;flex:0 1 260px;min-width:0}
.revista figure img{width:100%;height:auto;display:block;border:1px solid var(--line)}
.revista figcaption{font-size:.8rem;color:var(--muted);margin-top:6px}
.revista-txt{flex:1 1 300px;min-width:0}
.revista-txt h2{margin-top:0;border-top:0;padding-top:0}
.yt{position:relative;aspect-ratio:16/9;max-width:100%;background:#000;margin:12px 0;border:2px solid var(--fg)}
.yt iframe,.yt-btn{position:absolute;inset:0;width:100%;height:100%;border:0}
.yt-btn{padding:0;cursor:pointer;background:#000;display:block}
.yt-btn img{width:100%;height:100%;object-fit:cover;display:block}
.yt-play{position:absolute;left:50%;top:50%;width:76px;height:54px;margin:-27px 0 0 -38px;background:var(--accent);border-radius:14px;box-shadow:0 4px 18px rgba(0,0,0,.45)}
.yt-play::after{content:"";position:absolute;left:30px;top:15px;border-style:solid;border-width:12px 0 12px 21px;border-color:transparent transparent transparent #fff}
.yt-btn:hover .yt-play,.yt-btn:focus-visible .yt-play{filter:brightness(1.12)}
.yt-btn:focus-visible{outline:3px solid var(--teal);outline-offset:2px}
.yt-edad{position:absolute;left:10px;bottom:10px;background:rgba(0,0,0,.78);color:#fff;font:600 .8rem var(--f-body);padding:5px 10px;border-radius:4px}
.yt-nota{font-size:.85rem;color:var(--muted);margin:-4px 0 10px}
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

NAV = [("index.html", "Inicio"), ("fecha-precio-ediciones.html", "Fecha y precio"), ("hora-de-salida-gta-6.html", "Hora de salida"), ("notas-resenas-gta-6.html", "Reseñas"), ("guia-principiantes-gta-6.html", "Para empezar"), ("trofeos-logros-gta-6.html", "Trofeos"), ("trucos-gta-6.html", "Trucos"), ("robos-atracos-gta-6.html", "Robos"),
       ("mapa-leonida.html", "Mapa"), ("personajes.html", "Personajes"), ("todo-lo-confirmado.html", "Lo confirmado"), ("leaks-cyberleek.html", "Leaks"), ("mapa-miami-real.html", "Miami real"), ("trailers-gta-6.html", "Tráilers"), ("revistas-gta-6.html", "Revistas"), ("musica-radios-gta-6.html", "Música"), ("equipo-gta-6.html", "Equipo")]

# Datos estructurados para Google (JSON-LD)
import json as _jsonld, datetime as _dt
PUBLICADO = {"robos-atracos-gta-6.html": "2026-11-22", "guia-principiantes-gta-6.html": "2026-11-20", "trofeos-logros-gta-6.html": "2026-11-19", "notas-resenas-gta-6.html": "2026-11-18", "revistas-gta-6.html": "2026-10-25", "trailers-gta-6.html": "2026-10-24", "hora-de-salida-gta-6.html": "2026-10-25"}
def jsonld(slug, title, desc):
    url = f"{DOMAIN}/{'' if slug == 'index.html' else slug}"
    hoy = _dt.date.today().isoformat()
    autor = {"@type": "Person", "name": "Ernesto", "url": "https://x.com/elchinyto_tech"}
    pub = {"@type": "Organization", "name": "Leonida Global 305", "url": DOMAIN + "/",
           "logo": {"@type": "ImageObject", "url": DOMAIN + "/img/logo-192.png"}, "sameAs": ["https://x.com/elchinyto_tech"]}
    if slug == "index.html":
        data = [{"@context": "https://schema.org", "@type": "WebSite", "name": "Leonida Global 305", "url": DOMAIN + "/",
                 "inLanguage": "es", "description": desc, "publisher": pub}, dict({"@context": "https://schema.org"}, **pub)]
    else:
        data = [{"@context": "https://schema.org", "@type": "Article", "headline": title.split(" | ")[0][:110],
                 "description": desc, "inLanguage": "es", "mainEntityOfPage": url,
                 "image": DOMAIN + "/img/og-image.jpg", "datePublished": PUBLICADO.get(slug, "2026-10-23"),
                 "dateModified": hoy, "author": autor, "publisher": pub},
                {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                 {"@type": "ListItem", "position": 1, "name": "Inicio", "item": DOMAIN + "/"},
                 {"@type": "ListItem", "position": 2, "name": title.split(" | ")[0], "item": url}]}]
    return '<script type="application/ld+json">' + _jsonld.dumps(data, ensure_ascii=False).replace("</", "<\\/") + '</script>'

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
            + jsonld(slug, title, desc) +
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
  <strong>Saca el máximo a GTA 6</strong>
  <p style="margin:.3em 0 0">Teles, monitores, SSD y accesorios para GTA 6, con opciones económicas y de gama alta: <a href="equipo-gta-6.html">ver el equipo recomendado</a>.</p>
</aside>"""
AD = '<div class="ad" aria-hidden="true">Espacio publicitario</div>'
UPD = '<p class="updated">Actualizado: 22 de noviembre de 2026</p>'

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
YT_EDAD = {"tJbzMqJGH4k"}  # videos con restricción de edad: YouTube no deja verlos incrustados
def video(vid, titulo):
    if vid in YT_EDAD:
        return (f'<div class="yt"><a class="yt-btn" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener" aria-label="Ver {titulo} en YouTube">'
                f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">'
                f'<span class="yt-play" aria-hidden="true"></span><span class="yt-edad">+18 · Se abre en YouTube</span></a></div>'
                '<p class="yt-nota">Rockstar le puso restricción de edad, así que YouTube solo deja verlo en su web o app, con la sesión iniciada.</p>')
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
    ("_yl5ELcmugI", "Tráiler de precarga", "10 de noviembre de 2026", "Un clip de unos 30 segundos con escenas de Jason y Lucia, grabado en PS5, que Rockstar publicó el día que se abrió la precarga. Suena \"Blood in Your Eyes\", de Tove Lo, una canción nueva de GTA VI: The Album."),
    ("rz1B4B2yBZY", "Tráiler de lanzamiento", "15 de octubre de 2026", "Grabado dentro del juego en PS5. Un golpe fácil sale mal y Jason y Lucia terminan metidos en una conspiración que cruza todo Leonida. Suena \"Flower in a Hurricane\", de Justice con Tame Impala, SZA y King Gizzard &amp; The Lizard Wizard."),
    ("tJbzMqJGH4k", "An Extended Look", "27 de agosto de 2026", "Unos 27 minutos de juego y escenas sin cortes, estrenados primero en Netflix. Jason y Lucia escapan de una redada con la droga, cenan con Brian Heder, hacen de conductores de fuga para Raul Bautista y trabajan de seguridad en una fiesta. Todo lo que se vio está en <a href=\"todo-lo-confirmado.html\">Todo lo confirmado</a>."),
    ("VQRLujxTm3c", "Tráiler 2", "6 de mayo de 2025", "Presentó por su nombre a Jason Duval y Lucia Caminos, y al reparto: Cal Hampton, Brian Heder, Boobie Ike, Dre'Quan Priest, Real Dimez y Raul Bautista."),
    ("QdBZY2fkU-0", "Tráiler 1", "5 de diciembre de 2023", "El primer vistazo: Lucia en prisión, Vice City de vuelta, los Cayos y el estado de Leonida. Con \"Love Is a Long Road\" de Tom Petty."),
]

# ---------- Inicio ----------
index = f"""
<span class="mile">Guías de GTA 6</span>
<h1>Todo GTA&nbsp;6, claro y al día</h1>
<p class="lede">Fecha, precio, mapa de Leonida, personajes y, desde el día del lanzamiento, guías de misiones, robos, autos y secretos.</p>
<div class="cd" id="lanzamiento" data-t="2026-11-19T05:00:00Z" data-q="para que salga GTA 6" data-y="¡GTA 6 ya salió!">
  <p class="cd-label">Lanzamiento en Miami</p>
  <div class="count">
    <div><b data-u="d">--</b><small>días</small></div>
    <div><b data-u="h">--</b><small>horas</small></div>
    <div><b data-u="m">--</b><small>minutos</small></div>
  </div>
  <p class="cd-done" hidden>¡GTA 6 ya está disponible!</p>
    <a class="share-x" href="https://x.com/intent/post" target="_blank" rel="noopener">Compartir en X</a>
  <p class="updated">19 de noviembre de 2026, 00:00 (hora de Miami).</p>
</div>
<div class="cd-row">
  <div class="cd cd-sm" id="precarga" data-t="2026-11-10T05:00:00Z" data-q="para la precarga de GTA 6" data-y="¡Ya se puede precargar GTA 6!">
    <p class="cd-label">Precarga</p>
    <div class="count">
      <div><b data-u="d">--</b><small>días</small></div>
      <div><b data-u="h">--</b><small>horas</small></div>
      <div><b data-u="m">--</b><small>min</small></div>
    </div>
    <p class="cd-done" hidden>¡Ya puedes precargar!</p>
    <a class="share-x" href="https://x.com/intent/post" target="_blank" rel="noopener">Compartir en X</a>
    <p class="updated">10 de noviembre a medianoche en PS5, hora de cada país (contamos con la de Miami). En Xbox empieza a la vez en todo el mundo: 9 de noviembre a las 7:00 p.&nbsp;m. en Miami.</p>
  </div>
  <div class="cd cd-sm" id="nueva-zelanda" data-t="2026-11-18T11:00:00Z" data-q="para que Nueva Zelanda sea el primer país en jugar GTA 6" data-y="¡Nueva Zelanda ya está jugando GTA 6!">
    <p class="cd-label">Primero en jugar: Nueva Zelanda</p>
    <div class="count">
      <div><b data-u="d">--</b><small>días</small></div>
      <div><b data-u="h">--</b><small>horas</small></div>
      <div><b data-u="m">--</b><small>min</small></div>
    </div>
    <p class="cd-done" hidden>¡Ya se juega en Nueva Zelanda!</p>
    <a class="share-x" href="https://x.com/intent/post" target="_blank" rel="noopener">Compartir en X</a>
    <p class="updated">19 de noviembre, 00:00 en Nueva Zelanda (18 de noviembre, 6:00 a.&nbsp;m. en Miami), según la PlayStation Store. <a href="hora-de-salida-gta-6.html">Horas por país</a></p>
  </div>
</div>
<h2>Tráiler de lanzamiento</h2>
{video("rz1B4B2yBZY", "Tráiler de lanzamiento de GTA 6")}
<p><a href="trailers-gta-6.html">Ver todos los tráilers y el Extended Look</a></p>
{YT_JS}
<h2>Guías disponibles</h2>
<ul class="guides">
  <li><a href="robos-atracos-gta-6.html"><span class="mile">Nuevo</span><h3>Robos y atracos de GTA 6</h3><p>Tiendas, joyerías, bancos y cámaras acorazadas de hasta 205,000 dólares, y los dos grandes golpes de la historia.</p></a></li>
  <li><a href="trucos-gta-6.html"><span class="mile">Nuevo</span><h3>Trucos de GTA 6</h3><p>Cómo se desbloquean los 61 trucos, cómo meterlos y los códigos conocidos, incluido el de 250,000 dólares.</p></a></li>
  <li><a href="guia-principiantes-gta-6.html"><span class="mile">Nuevo</span><h3>Guía para empezar GTA 6</h3><p>Las 22 misiones del Capítulo 1, cómo no perder tu dinero y las primeras formas de ganar plata.</p></a></li>
  <li><a href="trofeos-logros-gta-6.html"><span class="mile">Nuevo</span><h3>Trofeos y logros de GTA 6</h3><p>Los 55 trofeos: el platino, los más difíciles y cómo se consigue cada uno.</p></a></li>
  <li><a href="notas-resenas-gta-6.html"><span class="mile">Nuevo</span><h3>Reseñas y notas de GTA 6</h3><p>99 en Metacritic: las notas de IGN, GameSpot, Game Informer, Edge y más, y lo que critica la prensa.</p></a></li>
  <li><a href="fecha-precio-ediciones.html"><span class="mile">Lanzamiento</span><h3>Fecha, precio y ediciones</h3><p>Cuánto cuesta, qué trae cada edición y cuándo se puede precargar.</p></a></li>
  <li><a href="hora-de-salida-gta-6.html"><span class="mile">Nuevo</span><h3>Hora de salida por país</h3><p>A qué hora se desbloquea GTA 6 en tu país según la PlayStation Store.</p></a></li>
  <li><a href="mapa-leonida.html"><span class="mile">Mapa</span><h3>Mapa de Leonida</h3><p>Las seis regiones confirmadas y su versión real en Florida.</p></a></li>
  <li><a href="todo-lo-confirmado.html"><span class="mile">Nuevo</span><h3>Todo lo confirmado</h3><p>Lo que contó Rockstar a IGN, Famitsu, Game Informer, Dazed, LOVE y Bloomberg.</p></a></li>
  <li><a href="trailers-gta-6.html"><span class="mile">Videos</span><h3>Todos los tráilers</h3><p>Los tres tráilers oficiales y el Extended Look.</p></a></li>
  <li><a href="revistas-gta-6.html"><span class="mile">Revistas</span><h3>Las revistas de GTA 6</h3><p>Edge, Game Informer, Dazed, TROISCOULEURS y LOVE: qué trae cada una y cómo conseguirlas.</p></a></li>
  <li><a href="musica-radios-gta-6.html"><span class="mile">Nuevo</span><h3>Radios y GTA VI: The Album</h3><p>Las emisoras con Bad Bunny, Lana Del Rey y Morgan Wallen, la lista filtrada de las 34 canciones de The Album y el Original Score de Justice.</p></a></li>
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
  var cds=document.querySelectorAll(".cd");
  function tick(){{cds.forEach(function(c){{
    var s=Math.max(0,new Date(c.dataset.t).getTime()-Date.now()),
      v={{d:Math.floor(s/864e5),h:Math.floor(s%864e5/36e5),m:Math.floor(s%36e5/6e4)}};
    c.querySelectorAll("[data-u]").forEach(function(b){{b.textContent=v[b.dataset.u];}});
    var done=s===0; c.querySelector(".count").hidden=done; c.querySelector(".cd-done").hidden=!done;
    var txt=done?c.dataset.y:("⏳ Faltan "+v.d+" días y "+v.h+" horas "+c.dataset.q+". Cuenta regresiva en vivo 👇");
    var url="https://leonidaglobal305.com/#"+c.id;
    c.querySelector(".share-x").href="https://x.com/intent/post?text="+encodeURIComponent(txt)+"&url="+encodeURIComponent(url)+"&hashtags=GTA6,GTAVI&via=elchinyto_tech";
  }});}}
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
    <tr><td>Precarga digital en PS5 (medianoche, hora local)</td><td class="num">10 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Precarga digital en Xbox (00:00 GMT en todo el mundo)</td><td class="num">10 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Caja con código en tiendas</td><td class="num">12 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Tamaño de la precarga</td><td class="num">Hasta 212 GB, según la consola</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Tamaño de la descarga en PS5 al abrir la precarga</td><td class="num">209.8 GB</td><td><span class="tag no">Reportado</span></td></tr>
    <tr><td>Tamaño en Xbox Series X|S, según la base de datos de Microsoft</td><td class="num">209.86 GiB (unos 225 GB)</td><td><span class="tag no">Reportado</span></td></tr>
    <tr><td>Póster oficial y mapa de Leonida para descargar gratis</td><td class="num">19 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Resultados de Take-Two (último informe antes del lanzamiento)</td><td class="num">9 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Reseñas de la prensa (<a href="notas-resenas-gta-6.html">ver las notas</a>)</td><td class="num">18 nov 2026</td><td><span class="tag ok">Publicadas</span></td></tr>
    <tr><td>Lanzamiento PS5 y Xbox Series X|S</td><td class="num">19 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Primeras ventas oficiales: 3,790 millones de dólares el primer día</td><td class="num">20 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Xbox Cloud Gaming en Xbox One y Xbox Series X|S (1:00 a.&nbsp;m. hora de Miami)</td><td class="num">19 nov 2026</td><td><span class="tag ok">Confirmado</span></td></tr>
    <tr><td>Versión de PC</td><td class="num">Sin fecha (reportado: primer trimestre de 2027)</td><td><span class="tag no">No anunciado</span></td></tr>
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
<div class="note"><strong>Ojo con la edición física.</strong> La caja de tienda trae un código de descarga, no un disco con el juego. Si lo que quieres es jugar el primer día, la compra digital te deja precargar desde el 10 de noviembre sin depender del envío. La caja con código llega a las tiendas el 12.</div>
<h2>Lo nuevo de Rockstar (3 de noviembre)</h2>
<ul>
  <li><strong>La precarga se adelanta al martes 10 de noviembre.</strong> En PS5 empieza a la medianoche de cada país; en Xbox, a las 00:00 GMT en todo el mundo, que en Miami son las 7:00 p.&nbsp;m. del lunes 9.</li>
  <li>La caja con código estará en las tiendas desde el 12 de noviembre.</li>
  <li>La precarga ocupa <strong>hasta 212 GB</strong>, según la consola. Rockstar recomienda dejar espacio libre cuanto antes.</li>
  <li>El 19 de noviembre la web oficial publicará gratis, para descargar e imprimir, el <strong>póster de la portada y el mapa de Leonida</strong>.</li>
  <li>Poco después del lanzamiento, la Rockstar Store venderá ese póster en físico, a doble cara, por <strong>$0.99</strong>, o lo regalará con cualquier compra.</li>
</ul>
<h2>Ventas del primer día: 3,790 millones de dólares (20 de noviembre)</h2>
<p>Take-Two publicó un comunicado oficial con las primeras cifras del lanzamiento:</p>
<ul>
  <li>Las ventas en tienda del primer día llegaron a <strong>3,790 millones de dólares</strong> en todo el mundo, según estimaciones de la propia empresa hasta el final del 19 de noviembre.</li>
  <li>Antes del lanzamiento ya se habían vendido <strong>32.5 millones de unidades</strong>, un récord en todas las plataformas.</li>
  <li>Take-Two lo presenta como <strong>el mayor lanzamiento de la historia del entretenimiento</strong>, por encima de cualquier película, disco o juego.</li>
  <li>Sam Houser, fundador de Rockstar, dijo que el estudio entra en "un nuevo capítulo" con GTA VI y que están "muy agradecidos" por la respuesta de los jugadores.</li>
  <li>No hubo cifras de jugadores ni ventas en unidades del día del lanzamiento.</li>
</ul>
<h2>Lo que dijo Take-Two (9 de noviembre)</h2>
<p>En su último informe de resultados antes del estreno, Take-Two volvió a confirmar el 19 de noviembre y dejó varios datos:</p>
<ul>
  <li>Su CEO, Strauss Zelnick, dijo que <strong>Rockstar ya terminó el desarrollo de GTA VI</strong>. El juego está listo para salir en la fecha prevista.</li>
  <li>Las reservas van <strong>muy por encima de lo que la empresa esperaba</strong>. Zelnick habló de niveles "sin precedentes", pero no dio cifras.</li>
  <li>Take-Two mantiene su previsión de ingresos por reservas netas de <strong>8,000 a 8,200 millones de dólares</strong> para su año fiscal, que termina en marzo de 2027 y ya incluye el lanzamiento.</li>
  <li>No hubo novedades sobre la versión de PC ni sobre el nuevo GTA Online. Zelnick dijo que Rockstar contará lo que viene cuando lo decida.</li>
</ul>
<h2>Récord de reservas y Xbox One por la nube (10 de noviembre)</h2>
<ul>
  <li><strong>Sony y Microsoft confirmaron que GTA 6 es el juego más reservado de la historia</strong> en sus tiendas: PlayStation lo dijo en el PlayStation Blog y Microsoft en Xbox Wire, donde lo llama el título más reservado de todos los tiempos en la Microsoft Store.</li>
  <li>Ninguna de las dos dio cifras. La firma de análisis Sensor Tower estimaba unos 9.7 millones de reservas el 10 de noviembre. Su cálculo más reciente, del 16 de noviembre, sube a <strong>unos 14.94 millones de reservas digitales</strong> y unos <strong>1,450 millones de dólares</strong> entre PS5 y Xbox Series X|S. Es una estimación, no un dato oficial: Take-Two sigue sin dar cifras.</li>
  <li><strong>Se podrá jugar en Xbox One</strong>, pero solo en streaming por <strong>Xbox Cloud Gaming</strong>, desde el 19 de noviembre a la 1:00 a.&nbsp;m. hora de Miami (ET). También se puede jugar por la nube en Xbox Series X|S. En la nube corre con los ajustes gráficos de la Xbox Series S.</li>
  <li>El juego hay que comprarlo aparte. Desde el 11 de noviembre, en los países donde está disponible, Microsoft vende tiempo de juego en la nube sin necesidad de suscripción a Game Pass. La disponibilidad cambia según el país y el dispositivo.</li>
  <li>No hay versión nativa para PS4 ni Xbox One, y Microsoft no mencionó el streaming en PC ni en el navegador.</li>
</ul>
<div class="note"><strong>La precarga ya está abierta.</strong> Desde el 10 de noviembre puedes descargar el juego si lo compraste en digital. Al abrirse en PS5, la descarga marcaba unos 209.8 GB, según GTA BOOM. Se juega hasta que se desbloquee el 19.</div>
{COLECCIONISTA}
{AD}
<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Hay edición de coleccionista de GTA 6?</dt><dd>Hay una caja de coleccionista de $399.99 en la Rockstar Store, pero no incluye el juego. Las ediciones del juego son solo la estándar y la Ultimate.</dd>
  <dt>¿GTA 6 sale en PS4 o Xbox One?</dt><dd>En PS4, no. En Xbox One no hay versión instalable, pero Microsoft confirmó que se podrá jugar en streaming por Xbox Cloud Gaming desde el 19 de noviembre a la 1:00 a.&nbsp;m. hora de Miami. Necesitas comprar el juego y tener acceso a la nube de Xbox (Game Pass o tiempo de juego en la nube, donde se venda). Las versiones nativas son solo para PS5 y Xbox Series X|S.</dd>
  <dt>¿Cuánto vendió GTA 6 el primer día?</dt><dd>Según Take-Two, 3,790 millones de dólares en ventas en tienda el primer día, y 32.5 millones de unidades vendidas antes del lanzamiento. Es el mayor estreno de la historia del entretenimiento.</dd>
  <dt>¿Cuántas reservas tiene GTA 6?</dt><dd>Take-Two confirmó 32.5 millones de unidades vendidas antes del lanzamiento. Sony y Microsoft confirmaron que es el juego más reservado de la historia en la PlayStation Store y en la Microsoft Store, pero no dieron cifras. Sensor Tower estima unos 14.94 millones de reservas digitales entre las dos plataformas al 16 de noviembre, por unos 1,450 millones de dólares. Es una estimación, no una cifra oficial.</dd>
  <dt>¿A qué hora se desbloquea?</dt><dd>Según las fichas de la PlayStation Store, a medianoche del 19 de noviembre en la hora de cada tienda: en Miami y Nueva York a las 00:00, en España a las 00:00 y en México a las 00:00. Rockstar no lo ha anunciado de forma oficial. Tienes la tabla completa en <a href="hora-de-salida-gta-6.html">hora de salida por país</a>.</dd>
  <dt>¿Qué es el Vintage Vice City Pack?</dt><dd>Un paquete de objetos con estética del Vice City clásico. Lo recibe cualquiera que reserve o compre el juego antes del 20 de noviembre.</dd>
  <dt>¿Cuándo sale GTA 6 en PC?</dt><dd>Rockstar no lo ha anunciado. GamesBeat reportó, citando fuentes propias, que la versión de PC llegaría en el primer trimestre de 2027, pero no está confirmado.</dd>
  <dt>¿Ya hay reseñas de GTA 6?</dt><dd>Sí. Las reseñas de la prensa salieron el 18 de noviembre, un día antes del lanzamiento, y el juego tiene un 99 en Metacritic. Tienes las notas de cada medio en <a href="notas-resenas-gta-6.html">reseñas y notas de GTA 6</a>.</dd>
  <dt>¿Cuánto espacio necesito para GTA 6?</dt><dd>Rockstar dice que hasta 212 GB, según la consola. El 6 de noviembre, la base de datos de la tienda de Microsoft se actualizó y lista la versión de Xbox Series X|S en 209.86 GiB, que son unos 225 GB en la unidad que usan las consolas. Esa cifra no la dio Rockstar y puede cambiar con un parche del primer día, así que lo prudente es dejar libres unos 230 GB.</dd>
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
    <tr><td><strong>Brian Heder</strong></td><td>Jefe de Jason, con negocio legal por fuera y criminal por dentro. Le deja a Jason vivir en una de sus casas. El actor Stephen Root (<em>King of the Hill</em>) le confirmó a la agencia AP que está en el juego y dio a entender que es este personaje; Rockstar no ha publicado el reparto.</td></tr>
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
<p class="lede">Todo lo que Rockstar ha contado a IGN, Famitsu, Kinda Funny, Game Informer, Edge, Dazed, LOVE y Bloomberg, más lo que se vio en el Extended Look y el tráiler de lanzamiento, ordenado por tema.</p>
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
  <li>Rockstar confirmó que el juego apunta a <strong>30 FPS en todas las consolas</strong>, incluida la PS5 Pro. No anunció un modo a 60 FPS. Lo detallamos más abajo.</li>
  <li>La interfaz se puede personalizar para mostrar muy poca información en pantalla.</li>
</ul>

<h2>Clima y fauna (Game Informer)</h2>
<p><a href="revistas-gta-6.html">Mira nuestro ejemplar de Game Informer y las otras revistas</a></p>
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

<h2>Lo nuevo de Edge (29 de octubre)</h2>
<p>Edge visitó Rockstar North en Edimburgo y vio a Rob Nelson jugar unos 90 minutos sin guion. Hablaron también Aaron Garbut y Phil Hooker. <a href="revistas-gta-6.html">Ver la revista</a></p>
<ul>
  <li><strong>Mapa:</strong> según Rockstar, la superficie total de Leonida es "casi tan grande como los mapas jugables de GTA IV, GTA V y RDR2 juntos". Edge lo resume como unas dos veces el mapa de GTA 5.</li>
  <li><strong>Interiores:</strong> Garbut dice que hay "un orden de magnitud más" lugares con interior que en los juegos anteriores.</li>
  <li><strong>Transporte:</strong> autobuses y trenes funcionan de verdad. Hooker cuenta que está "obsesionado" con que siempre lleguen a su hora.</li>
  <li><strong>Días más largos:</strong> el ciclo de día y noche dura más que en GTA 5; los atardeceres y las noches se alargan.</li>
  <li><strong>Clima:</strong> las nubes se mueven con el viento y la humedad, las tormentas se ven formarse a lo lejos, las calles se mojan y se secan a distinto ritmo, y el mal tiempo sacude a los aviones.</li>
  <li><strong>Lo que sabe la policía:</strong> unos iconos arriba en la pantalla muestran el reporte policial: tu descripción, si vas solo o en pareja, la ropa, las cámaras de seguridad y el arma. Separarse, cambiarse o soltar el arma lo reduce.</li>
  <li><strong>Persecuciones:</strong> la policía se comunica por radio, pone bandas de clavos y tiene perros K9 que te pueden derribar.</li>
  <li><strong>Perfil Criminal:</strong> va de "Profesional" a "Irredimible", con iconos de ángel y diablo, y cambia cómo se desarrolla la historia.</li>
  <li><strong>La pareja:</strong> la cercanía entre Jason y Lucia tiene cuatro niveles. Sube con paseos por la playa, bici, gimnasio o simplemente manejando juntos. No se pueden separar del todo, y Nelson no quiso confirmar si se pueden casar.</li>
  <li><strong>Gente más viva:</strong> unas 600,000 animaciones, cada barrio con su tipo de gente, y un sistema de asco: Jason pone cara de asco al entrar en una casa que un perro dejó destrozada, sin que sea una escena preparada.</li>
  <li><strong>Autos:</strong> todos tienen indicador de gasolina y de estado del motor. Los autos de lujo que pide un fence avisan a la policía, y el pago depende de cómo llegue el auto.</li>
  <li><strong>Cómo se hizo:</strong> unas 900 personas en Rockstar North. Toronto se encarga de poblar el mundo y San Diego de los eventos aleatorios. Sam Houser revisa con Nelson cada etapa del desarrollo.</li>
  <li>Edge no trae novedades sobre GTA Online, la versión de PC ni el precio.</li>
</ul>

<h2>Gameplay nuevo en South Park (28 de octubre)</h2>
<p>El episodio "Guinea Pig on a Stick" (temporada 29, episodio 4) de South Park mostró unos 17 segundos de gameplay de GTA 6 que no se habían visto. Rockstar Games aparece en los créditos del episodio, así que es material oficial.</p>
<ul>
  <li>Jason y Lucia caminan por una playa de Vice City, con el minimapa en pantalla.</li>
  <li>Un perro hace sus necesidades en la arena y Jason recoge la bolsa con el excremento para lanzársela a un NPC. Es la primera vez que se ve en acción esta mecánica.</li>
  <li>Si la persona se defiende, la bolsa sirve como arma improvisada.</li>
</ul>

<h2>Galería de lanzamiento (5 de noviembre)</h2>
<p>A dos semanas del estreno, Rockstar subió a la web oficial de GTA VI una galería con casi 40 capturas nuevas de "Vice City y más allá". Lo que se ve en ellas:</p>
<ul>
  <li>Jason con equipo táctico bajando de un avión militar en medio de un tiroteo, con un perro con chaleco de combate al fondo.</li>
  <li>Jason y Lucia armados, redadas policiales y persecuciones a toda velocidad.</li>
  <li>Discotecas, bares de muelle y fiestas llenas de gente.</li>
  <li>Buceo en el mar, un caimán y un atardecer en el campo.</li>
  <li>Personajes nuevos sin nombre todavía, como un hombre con cicatrices y un ojo de cada color que sostiene dos reptiles muertos, o un tipo con mullet que amenaza a Jason con un cuchillo.</li>
</ul>
<p>Rockstar no puso textos ni nombres en las capturas, así que de estos personajes aún no se sabe quiénes son.</p>

<h2>Desarrollo terminado y un festival en Miami (9 y 10 de noviembre)</h2>
<ul>
  <li>En la llamada con inversores del 9 de noviembre, Strauss Zelnick, CEO de Take-Two, dijo que <strong>Rockstar terminó el desarrollo de GTA VI</strong> y que las reservas van muy por encima de lo esperado.</li>
  <li>La <strong>precarga</strong> se abrió el 10 de noviembre en PS5 y Xbox Series X|S.</li>
  <li>Sony y Microsoft confirmaron que es <strong>el juego más reservado de la historia</strong> de la PlayStation Store y de la Microsoft Store. No dieron cifras.</li>
  <li>Microsoft confirmó que GTA VI llegará a <strong>Xbox Cloud Gaming</strong> el 19 de noviembre, así que se podrá jugar en streaming en <strong>Xbox One</strong> y también en Xbox Series X|S. El juego se compra aparte. Más detalles en <a href="fecha-precio-ediciones.html">fecha, precio y ediciones</a>.</li>
  <li>Rockstar y PlayStation anunciaron <strong>GTA VI: The Festival</strong>, un concierto el 21 de noviembre en Mana Wynwood, Miami, con Travis Scott, Cardi B, Justice, Metro Boomin y otros artistas del juego. Los detalles están en la <a href="musica-radios-gta-6.html">página de música</a>.</li>
</ul>

<h2>30 FPS y mejoras en PS5 Pro (10 de noviembre)</h2>
<p>Con la apertura de la precarga, Rockstar publicó los datos técnicos del juego en consolas:</p>
<ul>
  <li><strong>30 FPS como objetivo</strong> en PS5 y Xbox Series X|S. Rockstar dice que busca exprimir al máximo las dos plataformas. No anunció un modo rendimiento ni a 60 FPS.</li>
  <li><strong>PS5 Pro:</strong> también a 30 FPS, pero con imagen más nítida gracias a <strong>PSSR</strong> (el reescalado de Sony) y <strong>sombras con trazado de rayos</strong>, que solo tiene esta consola.</li>
  <li><strong>PS5 y PS5 Pro:</strong> vibración háptica del DualSense en todo el juego, audio 3D Tempest y cargas más rápidas. Rockstar repite que el juego "se juega mejor" en PS5.</li>
  <li>Hay <strong>Remote Play</strong> en PlayStation y Xbox. En Xbox Cloud Gaming (incluida Xbox One) corre con los ajustes de la Xbox Series S.</li>
  <li>Rockstar no dio cifras de resolución.</li>
</ul>
<p>Ese mismo día salió un <a href="trailers-gta-6.html">tráiler corto de la precarga</a>, con "Blood in Your Eyes" de Tove Lo.</p>

<h2>Macca &amp; Friends, la serie animada del juego (13 de noviembre)</h2>
<p>Rockstar publicó un teaser de <strong>Macca &amp; Friends</strong>, una serie de dibujos animados que existe dentro del mundo de GTA VI. Sigue las aventuras de Macca, un caimán, y sus amigos de los pantanos por todo Leonida. Es el primer adelanto de la tele del juego, igual que en GTA V había programas para ver en el sofá de casa. Rockstar no dijo en qué canal sale ni dio más detalles.</p>

<h2>¿Cuánto dura GTA 6? (reportado, 15 de noviembre)</h2>
<p>Rockstar no ha dado una duración oficial. Esto es lo que hay a tres días del estreno:</p>
<ul>
  <li><strong>Lo único que viene de Rockstar:</strong> en una entrevista con The New York Times en agosto, Rob Nelson, codirector de Rockstar North, contó que <strong>su propia partida le llevó unas 80 horas</strong>, contando la historia y algunos objetivos opcionales con consecuencias en la trama. Es su experiencia personal, no una cifra oficial del juego.</li>
  <li><strong>Historia principal: unas 50 horas</strong> sin actividades secundarias ni misiones opcionales, según Insider Gaming (Tom Henderson), que dice haber hablado con gente que ya lo jugó. <span class="tag no">Sin confirmar</span></li>
  <li><strong>Casi 100 misiones principales repartidas en cinco capítulos</strong>, según el mismo reporte. Como referencia, GTA V tenía unas 70. <span class="tag no">Sin confirmar</span></li>
  <li><strong>Platino o 100 %: cerca de 200 horas</strong>, en buena parte por tener que fotografiar las más de 170 especies de animales de Leonida, al estilo de RDR2. <span class="tag no">Sin confirmar</span></li>
</ul>
<p>Si se cumple, la historia de GTA VI duraría más que la de GTA V (unas 32-35 horas) y quedaría a la par de Red Dead Redemption 2.</p>

<h2>Vice City llega a NBA 2K27 (16 de noviembre)</h2>
<p>2K, que pertenece a Take-Two igual que Rockstar, anunció el primer crossover entre las dos casas: la <strong>Temporada 3 de NBA 2K27</strong> gira alrededor de Vice City.</p>
<ul>
  <li><strong>Fechas:</strong> del 27 de noviembre al 15 de enero.</li>
  <li><strong>Qué trae:</strong> un parque en la playa de Vice City con hoteles pastel, superautos y una estatua de Macca the Gator, la cancha del Sahara Arena, camisetas de Vice City y Los Santos, uniformes de Burger Shot y Cluckin' Bell, y eventos por tiempo limitado como "Conquer Leonida" y un 5 contra 5 llamado "Neon vs Noir".</li>
  <li><strong>NBA 2K27 Vice City Edition:</strong> $39.99, con Bam Adebayo en la portada. Incluye el Pro Pass de la Temporada 3 y potenciadores.</li>
  <li><strong>Miembros de GTA+</strong> en PS5 y Xbox Series X|S: acceso gratis a NBA 2K27 edición estándar durante la temporada, 20 % de descuento en una compra y un paquete de objetos.</li>
  <li>No se puede jugar nada de GTA VI dentro de NBA 2K27: es contenido de ropa, canchas y eventos.</li>
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

<div class="note"><strong>Antes de comprar, esto importa.</strong> Rockstar confirmó que GTA 6 apunta a 30 FPS en todas las consolas, incluida la PS5 Pro, sin modo a 60 FPS anunciado. Por eso, para este juego pesa más una buena imagen (HDR, contraste, colores) que una tasa de refresco altísima. Aun así, HDMI 2.1 y VRR te sirven para otros juegos y por si llega un modo rendimiento más adelante. Si tienes PS5 Pro, ganas imagen más nítida (PSSR) y sombras con trazado de rayos.</div>

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
<p>Rockstar confirmó que la precarga ocupa <strong>hasta 212 GB</strong>, según la consola. Con una PS5 de 1 TB casi llena, vas a necesitar más espacio antes de la precarga del 10 de noviembre.</p>
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
  {pick("Tarjetas", "", "Tarjeta de PlayStation Store o Xbox", "Para comprar la versión digital y precargarla desde el 10 de noviembre.", "PlayStation Store gift card")}
</div>
<div class="note"><strong>Mandos oficiales de edición limitada.</strong> Sony vende dos DualSense de GTA VI, uno negro (la noche de Vice City) y otro blanco (el amanecer), con acabado tornasolado, palmeras en relieve y el logo del juego. Cuestan $84.99 (€84.99, £74.99) y salen a partir del 19 de noviembre. Son de stock limitado: el blanco se vende en PlayStation Direct y tiendas participantes, y el negro sobre todo en PlayStation Direct.</div>
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
  ("juego", "NINE1NINE", "E11EVEN Miami", "29 NE 11th St, Miami", 25.7849, -80.1919, "La discoteca 24 horas más famosa de Miami. En el juego se llama NINE1NINE. El viernes 6 de noviembre de 2026 el club se cambia el nombre a NINE1NINE por una noche, con Flo Rida de cabeza de cartel (mayores de 21, entradas en la web del club). Es una promoción del propio E11EVEN, no un evento de Rockstar."),
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
  ("marketing", "Letrero \"Welcome to Vice City\"", "Techo del Kaseya Center", "601 Biscayne Blvd, Miami", 25.7818, -80.1865, "Letrero iluminado en rosa sobre el techo de la arena. El condado de Miami-Dade confirmó que este acuerdo es de $975,000 y que ese dinero va al parque de Dan Paul Plaza, detrás de la arena."),
  ("marketing", "A Night in Vice City", "Kaseya Center", "601 Biscayne Blvd, Miami", 25.7810, -80.1875, "El 18 de noviembre, Heat vs. Bucks con cancha y uniformes de Vice City. Dentro de la arena ya funcionan un Burger Shot y un Cluckin' Bell que sirven comida de verdad (el Burger Shot ocupa el puesto que antes era de Skinny Louie), y la tienda de los Heat vende camisetas y gorras de Vice City."),
  ("marketing", "Sombrillas y tumbonas de Vice City", "Playa de Miami Beach", "South Beach, Miami Beach", 25.7838, -80.1283, "Desde el 15 de octubre y hasta el 31 de diciembre, las sillas, sombrillas y cabañas de Boucher Brothers en la playa llevan la marca de Vice City."),
  ("marketing", "Banners de GTA 6", "Zona de eventos del downtown", "Downtown Miami (zona aproximada)", 25.7752, -80.1920, "Desde el 15 de octubre, la ciudad permite banners de GTA 6 en una zona del downtown, por un máximo de 56 días. Por estas calles también circulan autobuses con \"I ♥ Vice City\"."),
  ("marketing", "Pantallas y \"In for VI\"", "Hard Rock Stadium", "347 Don Shula Dr, Miami Gardens", 25.9580, -80.2389, "En el Dolphins vs. Bengals del 11 de octubre hubo anuncios de GTA 6 y un gráfico \"In for VI\" en los touchdowns."),
  ("marketing", "Banner doble de GTA 6", "Hotel YVE", "146 Biscayne Blvd, Miami", 25.7747, -80.1876, "Desde el 19 de octubre, la fachada del hotel tiene un banner doble de GTA 6 frente a Biscayne Boulevard."),
  ("marketing", "Mural \"Good Idea\" de Ron English", "Wynwood", "Wynwood Arts District, Miami", 25.802404, -80.202064, "Uno de los murales de Vice City pintados en Wynwood en octubre. Por la zona también están \"We ♥ Vice City\" de Queen Andrea, \"Eyes\" de Enjoy Denial y uno de un caimán con una mujer y una bolsa de dinero."),
  ("marketing", "Murales de Tatiana Suarez y \"Camouflage\"", "Wynwood", "Wynwood Arts District, Miami", 25.800089, -80.202225, "Dos murales más de la campaña de Vice City, pintados a mediados de octubre."),
  ("marketing", "Pantallas de Vice City", "NW 26th St", "NW 26th St, Wynwood (zona aproximada)", 25.8007, -80.2010, "Pantallas digitales de la calle con anuncios de Vice City."),
  ("marketing", "Carrito \"Welcome to Vice City\"", "Collins Ave y 5th St", "Collins Ave & 5th St, Miami Beach", 25.7737, -80.1336, "Un carrito con el mensaje \"Welcome to Vice City\" en plena South Beach."),
  ("marketing", "Y Hotel (planeado)", "W South Beach", "2201 Collins Ave, Miami Beach", 25.7969, -80.1279, "Según documentos de la ciudad de Miami Beach, el hotel W se convierte en el Y Hotel del juego: lona en la fachada y una \"Y\" gigante en lugar de la \"W\" de la terraza del spa, hasta el 31 de diciembre. El acuerdo es de $650,000 y depende de los permisos de la ciudad."),
  ("marketing", "Letrero \"Vice Beach\" (planeado)", "Lummus Park", "1130 Ocean Dr, Miami Beach", 25.7812, -80.1294, "Un letrero rosa de unos 10 metros de ancho, como el del techo del Kaseya Center. Según los planos presentados a la ciudad, se instala del 26 al 31 de octubre y queda a la vista desde el 1 de noviembre hasta mediados de enero."),
  ("marketing", "Muscle Beach en rosa (planeado)", "Muscle Beach South Beach", "873 Ocean Dr, Miami Beach", 25.7779, -80.1297, "Los planes incluyen pintar de rosa los aparatos del gimnasio al aire libre y poner la marca Vice Beach. Las obras son del 26 al 31 de octubre, de noche, y debería verse así desde el 1 de noviembre."),
  ("marketing", "Iluminación de Vice City en el aeropuerto (planeado)", "Aeropuerto Internacional de Miami (MIA)", "2100 NW 42nd Ave, Miami", 25.7953, -80.2775, "Parte del paquete de $3.9 millones que anunció el condado de Miami-Dade el 28 de octubre: iluminación temática y anuncios de GTA 6 en los pasillos que unen los garajes con las terminales. Los diseños aún necesitan la aprobación del condado."),
  ("marketing", "Iluminación de Vice City en el puerto (planeado)", "PortMiami", "Dodge Island, Miami", 25.7720, -80.1640, "El mismo paquete del condado incluye iluminación temática y anuncios en PortMiami. Rockstar paga la instalación, el mantenimiento y el retiro."),
  ("marketing", "Columnas del Metrorail", "Metrorail de Miami", "Downtown Miami (zona aproximada)", 25.7740, -80.1962, "Columnas del Metrorail forradas con los colores de GTA 6."),
  ("marketing", "GTA VI: The Festival (21 de noviembre)", "Mana Wynwood", "318 NW 23rd St, Miami", 25.7993, -80.1990, "Rockstar y PlayStation celebran el lanzamiento con un festival el sábado 21 de noviembre: Travis Scott, Cardi B, Justice, Metro Boomin, Tainy, Rauw and Friends y más. Las entradas solo se compran con el código del sorteo oficial. Mayores de 17 años."),
  ("marketing", "Cervezas de GTA 6", "Tripping Animals Brewing", "2685 NW 105th Ave, Doral", 25.8008, -80.3683, "La cervecería de Doral fabrica Pißwasser, Patriot y No Mames Vice City, las cervezas del juego. Las venden en su taproom, que está decorado con la marca de GTA 6."),
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
<h2>Lo visitamos: las cervezas de GTA 6 en Tripping Animals</h2>
<p>En Tripping Animals Brewing, una cervecería de Doral (2685 NW 105th Ave), venden las versiones reales de las cervezas del juego. Fuimos y estas son nuestras fotos.</p>
<ul>
  <li><strong>Pißwasser</strong>, una pils, y <strong>Patriot</strong>, de 4.2 % de alcohol: las dos cervezas de siempre de la saga.</li>
  <li><strong>No Mames Vice City</strong>, una lager de 6 % con un chihuahua con gafas y cadena de Vice City en la lata.</li>
  <li>En las ventanas del local están los logos de Pißwasser, Patriot y el "VI" de GTA 6, y dentro hay pelotas de playa con el logo y la mascota de la cervecería.</li>
  <li>Allí también conseguimos fundas para latas y pegatinas de "I ♥ Vice City" con la marca de GTA VI.</li>
</ul>
<div class="fotos-visita">
  <figure><img src="img/miami/tripping-animals-fachada.jpg" width="900" height="1200" loading="lazy" alt="Fachada de Tripping Animals Brewing en Doral con los logos de Pißwasser, Patriot y VI en las ventanas"><figcaption>La fachada, con Pißwasser, Patriot y el VI en las ventanas.</figcaption></figure>
  <figure><img src="img/miami/tripping-animals-latas.jpg" width="900" height="1200" loading="lazy" alt="Latas de Patriot Beer y No Mames Vice City Lager"><figcaption>Patriot y No Mames Vice City.</figcaption></figure>
  <figure><img src="img/miami/tripping-animals-merch.jpg" width="900" height="1200" loading="lazy" alt="Latas de No Mames Vice City con pegatinas I love Vice City de GTA VI"><figcaption>Las pegatinas de "I ♥ Vice City".</figcaption></figure>
  <figure><img src="img/miami/tripping-animals-pelota-vi.jpg" width="900" height="1200" loading="lazy" alt="Pelota de playa con el logo VI de GTA 6 junto a la mascota chihuahua de la cervecería"><figcaption>La pelota de playa con el logo VI.</figcaption></figure>
</div>
<p class="credito-img">Fotos: Leonida Global 305. Solo para mayores de 21 años; bebe con responsabilidad.</p>

<div class="note"><strong>De dónde salen estos datos.</strong> Las comparaciones vienen de los tráilers, el Extended Look y del mapeo de la comunidad. Algunas son de fans y Rockstar no las ha confirmado una por una. El marketing sale de anuncios del condado de Miami-Dade, de las ciudades de Miami y Miami Beach y de lo que han reportado medios y gente en la calle.</div>
{AD}
<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Vice City es Miami?</dt><dd>Sí. Vice City es la versión de Rockstar de Miami, y Leonida es su versión de Florida. Muchos edificios reales aparecen recreados con otros nombres.</dd>
  <dt>¿Dónde está el letrero de Vice City en Miami?</dt><dd>En el techo del Kaseya Center, la arena de los Miami Heat en Biscayne Boulevard.</dd>
  <dt>¿Dónde va a estar el letrero de Vice Beach?</dt><dd>En Lummus Park, frente al 1130 de Ocean Drive, en Miami Beach. Según los planos presentados a la ciudad, se instala a finales de octubre y estaría listo el 1 de noviembre, siempre que la ciudad dé los permisos.</dd>
  <dt>¿Cuánto paga Rockstar al condado de Miami-Dade?</dt><dd>Unos $3.9 millones, según anunció la alcaldesa Daniella Levine Cava el 28 de octubre. Incluye el letrero del Kaseya Center ($975,000), iluminación temática en el aeropuerto y en PortMiami, anuncios en los pasillos del aeropuerto y gabinetes de semáforos forrados con la marca del juego en todo el condado. Los diseños dependen de la aprobación del condado, y varios comisionados y la sheriff criticaron que no se votara en la comisión.</dd>
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
<h1>GTA 6: radios, canciones, The Album y Original Score</h1>
{UPD}
<p class="lede">Rockstar ya mostró seis emisoras de radio de GTA 6 con locutores famosos, como Bad Bunny, Lana Del Rey y Morgan Wallen. Además, el 19 de noviembre sale <strong>Grand Theft Auto VI: The Album</strong>, con 34 canciones originales, y la banda sonora original del juego es obra del dúo francés Justice, que la lanza el 11 de diciembre.</p>

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
  <li>El tráiler de la precarga, del 10 de noviembre, adelantó otra canción del álbum: <strong>"Blood in Your Eyes", de Tove Lo</strong>.</li>
</ul>
<h3>Los 7 sencillos que ya están en streaming</h3>
<div class="tbl"><table>
  <thead><tr><th>Artista</th><th>Canción</th></tr></thead>
  <tbody>{_singles}</tbody>
</table></div>

<h3>La lista completa de The Album (filtrada, sin confirmar)</h3>
<p>El 14 de noviembre se filtró la lista de las 34 canciones. Según NME, una tienda de discos vendió un vinilo antes de tiempo y las fotos de la contraportada se difundieron en redes. Rockstar no ha publicado la lista oficial, así que tómala como <span class="tag no">Reportado</span> hasta el 19 de noviembre. Las canciones que ya se conocían aparecen en el orden filtrado, lo que le da credibilidad.</p>
<p>Estos son los artistas que aparecen, en el orden de la lista filtrada:</p>
<ol>
  <li>Justice con Michael McDonald</li>
  <li>Yung Lean con Future y Metro Boomin ("That's It")</li>
  <li>Playboi Carti</li>
  <li>Travis Scott ("RHYNO")</li>
  <li>CA7RIEL y Paco Amoroso, PinkPantheress, Fred again.. y Étienne de Crécy ("Sexy Magic")</li>
  <li>Justice con Tame Impala, SZA y King Gizzard &amp; The Lizard Wizard ("Flower in a Hurricane")</li>
  <li>Dua Lipa</li>
  <li>Morgan Wallen ("Last Thing You Need")</li>
  <li>Jhayco</li>
  <li>Fuerza Regida</li>
  <li>Rauw Alejandro ("Macacoa 2000")</li>
  <li>A Boogie Wit Da Hoodie con Elkan</li>
  <li>Burna Boy</li>
  <li>Gunna</li>
  <li>Kodak Black y Don Toliver</li>
  <li>Young Thug</li>
  <li>Tee Grizzley</li>
  <li>Don Toliver</li>
  <li>Cardi B</li>
  <li>JT</li>
  <li>Jennie</li>
  <li>Tove Lo ("Blood in Your Eyes")</li>
  <li>Zara Larsson</li>
  <li>Camila Cabello</li>
  <li>Fcukers</li>
  <li>Arca</li>
  <li>Rina Sawayama</li>
  <li>Rose Gray</li>
  <li>Lana Del Rey</li>
  <li>Kali Uchis y Helado Negro</li>
  <li>Omar Apollo</li>
  <li>Keith Richards ("Bright Lights, Big City")</li>
  <li>Jesse Johnson y Dâm-Funk</li>
  <li>Stanley Clarke, Yussef Dayes y Robert Glasper</li>
</ol>
<div class="note"><strong>Mucho latino en la lista.</strong> Si la filtración es correcta, además de Rauw Alejandro y CA7RIEL y Paco Amoroso, el álbum trae a Jhayco, Fuerza Regida, Arca, Kali Uchis con Helado Negro y Omar Apollo. NME cuenta que el tema de Lana Del Rey es una canción suya que llevaba más de diez años sin publicar.</div>

<div class="picks">
  {pick("Vinilo", "", "GTA VI: The Album en vinilo", "Para coleccionistas: el disco oficial con las 34 canciones originales del juego.", "Grand Theft Auto VI The Album vinyl")}
  {pick("CD", "", "GTA VI: The Album en CD", "La opción más económica en físico para tener la banda sonora.", "Grand Theft Auto VI The Album CD")}
  {pick("Audio", "", "Audífonos para escuchar Leonida", "Ahora que la radio suena hasta caminando, unos buenos audífonos marcan la diferencia.", "PS5 Xbox gaming headset wireless")}
</div>

<h2>GTA VI: Original Score, de Justice</h2>
<p>Es la música original que suena en el juego durante las misiones y las persecuciones, aparte de las radios y de The Album. La compuso el dúo francés <strong>Justice</strong>.</p>
<ul>
  <li><strong>Sale el 11 de diciembre de 2026</strong>, unas semanas después del juego.</li>
  <li><strong>30 temas</strong>, más temas extra en las versiones digitales.</li>
  <li>Desde el 29 de octubre ya está en streaming <strong>"Pusher"</strong>, con el DJ francés Gesaffelstein. También forma parte "Flower in a Hurricane", el tema del tráiler de lanzamiento.</li>
  <li>Se puede reservar en <strong>CD doble</strong> y en <strong>vinilo triple</strong>, normal o en edición limitada transparente.</li>
</ul>
<div class="tbl"><table>
  <thead><tr><th>Formato</th><th>Precio en EE.UU.</th></tr></thead>
  <tbody>
    <tr><td>Vinilo triple transparente (edición limitada)</td><td class="num">$59.99</td></tr>
    <tr><td>Vinilo triple negro</td><td class="num">$54.99</td></tr>
    <tr><td>CD doble</td><td class="num">$21.99</td></tr>
  </tbody>
</table></div>
<p class="disclosure">Precios de la tienda Rough Trade. Pueden variar en otras tiendas.</p>
<div class="score-fotos">
  <figure><img src="img/musica/original-score-vinilo.jpg" width="900" height="882" loading="lazy" alt="Vinilo triple transparente de GTA VI: Original Score by Justice con su carpeta desplegable"><figcaption>Vinilo triple, edición transparente.</figcaption></figure>
  <figure><img src="img/musica/original-score-cd.jpg" width="900" height="877" loading="lazy" alt="CD doble de GTA VI: Original Score by Justice con su estuche desplegable"><figcaption>CD doble con estuche desplegable.</figcaption></figure>
</div>
<p class="credito-img">Imágenes: Rockstar Games.</p>

<h2>GTA VI: The Festival (21 de noviembre, Miami)</h2>
<p>Rockstar Games y PlayStation organizan un festival de música en vivo para celebrar el lanzamiento, dos días después de que salga el juego. Es un evento real, no dentro del juego.</p>
<ul>
  <li><strong>Cuándo:</strong> sábado 21 de noviembre de 2026. La hora y el horario de cada artista aún no se han publicado.</li>
  <li><strong>Dónde:</strong> Mana Wynwood, 318 NW 23rd St, Miami. Puedes verlo en el <a href="mapa-miami-real.html">mapa de Miami real</a>.</li>
  <li><strong>Cartel:</strong> Travis Scott (Cactus Jack presenta, con Don Toliver, Kodak Black y SoFaygo), Cardi B, Ca7riel y Paco Amoroso, Justice (DJ set), Metro Boomin, Nick León b2b DJ Python, Prospa b2b Skream, Rauw and Friends, Suero, Tainy y The Dare b2b Fcukers (DJ set).</li>
  <li><strong>Entradas:</strong> no se venden al público general. Hubo un sorteo gratuito en la web oficial del festival, abierto hasta el 10 de noviembre a las 4:00 p.&nbsp;m. hora de Miami, una inscripción por persona. Los ganadores reciben un código por SMS para comprar entradas el 11 de noviembre a las 12:00 p.&nbsp;m., por orden de llegada. Tener código no garantiza entrada.</li>
  <li>Hay que tener <strong>17 años o más</strong>.</li>
</ul>
<div class="note"><strong>Cuidado con la reventa.</strong> Los códigos son de un solo uso y no se pueden vender ni pasar a otra persona. Si alguien te ofrece uno o entradas por redes sociales, lo más probable es que sea una estafa.</div>

<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Cómo consigo entradas para GTA VI: The Festival?</dt><dd>Solo con el código del sorteo oficial, que cerró el 10 de noviembre. Con el código se compran las entradas desde el 11 de noviembre a las 12:00 p.&nbsp;m. hora de Miami, hasta agotarse.</dd>
  <dt>¿Bad Bunny sale en GTA 6?</dt><dd>Sí. Es locutor de Cocoteo FM, la emisora de música latina, con el nombre de El Martillo, y suena su canción "EoO".</dd>
  <dt>¿Vuelven Flash FM o V-Rock?</dt><dd>Flash FM vuelve, ahora con pop actual. V-Rock no está entre las seis emisoras presentadas hasta ahora.</dd>
  <dt>¿Cuándo sale el álbum de GTA 6?</dt><dd>El 19 de noviembre de 2026, junto con el juego. Siete canciones ya están en streaming.</dd>
  <dt>¿Qué artistas salen en GTA VI: The Album?</dt><dd>Rockstar ha confirmado a Travis Scott, Morgan Wallen, Rauw Alejandro, Yung Lean, Keith Richards, Tove Lo, Justice y CA7RIEL y Paco Amoroso, entre otros. La lista filtrada el 14 de noviembre suma a Dua Lipa, Playboi Carti, Cardi B, Jennie, Camila Cabello, Lana Del Rey, Fuerza Regida y Jhayco, pero no es oficial hasta que salga el álbum.</dd>
  <dt>¿Quién hace la música original de GTA 6?</dt><dd>El dúo electrónico Justice compuso la banda sonora original. Rockstar lo dio a conocer con el tráiler de lanzamiento.</dd>
  <dt>¿Cuándo sale el Original Score de GTA 6?</dt><dd>El 11 de diciembre de 2026, en streaming, CD y vinilo. El tema "Pusher", con Gesaffelstein, ya se puede escuchar.</dd>
  <dt>¿Qué diferencia hay entre The Album y el Original Score?</dt><dd>The Album trae 34 canciones de artistas como Travis Scott o Rauw Alejandro y sale el 19 de noviembre. El Original Score es la música instrumental del juego hecha por Justice y sale el 11 de diciembre.</dd>
</dl>
{AFF}"""


# ---------- Hora de salida ----------
HORAS = [
  # (UTC, países)
  ("11:00 · 18 nov", "Nueva Zelanda"),
  ("13:00 · 18 nov", "Australia"),
  ("15:00 · 18 nov", "Japón y Corea del Sur"),
  ("16:00 · 18 nov", "Hong Kong, Malasia, Singapur y Taiwán"),
  ("17:00 · 18 nov", "Indonesia y Tailandia"),
  ("18:30 · 18 nov", "India"),
  ("20:00 · 18 nov", "Emiratos Árabes Unidos"),
  ("21:00 · 18 nov", "Arabia Saudita y Turquía"),
  ("22:00 · 18 nov", "Bulgaria, Chipre, Finlandia, Grecia, Israel, Rumanía, Sudáfrica y Ucrania"),
  ("23:00 · 18 nov", "España, Francia, Alemania, Italia, Países Bajos, Bélgica, Polonia, Suecia, Suiza y el resto de Europa central"),
  ("00:00 · 19 nov", "Reino Unido, Irlanda, Portugal e Islandia"),
  ("03:00 · 19 nov", "Argentina, Brasil, Chile, Paraguay y Uruguay"),
  ("04:00 · 19 nov", "Bolivia"),
  ("05:00 · 19 nov", "Estados Unidos, Canadá, Colombia, Ecuador, Panamá y Perú"),
  ("06:00 · 19 nov", "México, Costa Rica, El Salvador, Guatemala, Honduras y Nicaragua"),
]
_horas = "".join(f'<tr><td class="num">{u}</td><td>{p}</td></tr>' for u, p in HORAS)
hora = f"""
<span class="mile">Lanzamiento</span>
<h1>¿A qué hora sale GTA 6 en tu país?</h1>
{UPD}
<p class="lede">GTA 6 se desbloquea a la <strong>medianoche del 19 de noviembre</strong> en la hora de cada tienda, según las fichas de la PlayStation Store. Nueva Zelanda es el primer país en jugarlo y México y Centroamérica, los últimos.</p>
<div class="note"><strong>Ojo: no es un anuncio oficial.</strong> Estos horarios salen de las fichas de GTA 6 en la PlayStation Store de cada país. Rockstar y Sony no han publicado un horario por país y lo pueden cambiar antes del lanzamiento. Si cambia, lo actualizamos aquí.</div>

<h2>Hora de salida en Latinoamérica, España y EE.UU.</h2>
<div class="tbl"><table>
  <thead><tr><th>País</th><th>Hora local</th></tr></thead>
  <tbody>
    <tr><td>España (península y Baleares)</td><td class="num">00:00 · 19 nov</td></tr>
    <tr><td>Islas Canarias</td><td class="num">23:00 · 18 nov</td></tr>
    <tr><td>Argentina, Chile, Uruguay, Paraguay y Brasil</td><td class="num">00:00 · 19 nov</td></tr>
    <tr><td>Bolivia</td><td class="num">00:00 · 19 nov</td></tr>
    <tr><td>Colombia, Perú, Ecuador y Panamá</td><td class="num">00:00 · 19 nov</td></tr>
    <tr><td>México, Guatemala, Honduras, El Salvador, Nicaragua y Costa Rica</td><td class="num">00:00 · 19 nov</td></tr>
    <tr><td>EE.UU. costa este (Miami, Nueva York)</td><td class="num">00:00 · 19 nov</td></tr>
    <tr><td>EE.UU. hora del centro (Texas, Chicago)</td><td class="num">23:00 · 18 nov</td></tr>
    <tr><td>EE.UU. costa oeste (Los Ángeles)</td><td class="num">21:00 · 18 nov</td></tr>
  </tbody>
</table></div>
<p>En EE.UU. la tienda abre a la vez en todo el país, a medianoche de la costa este. Por eso en el centro y en el oeste se puede jugar desde la noche del 18. Lo mismo pasa en las zonas de Canadá y Brasil que van por detrás de la hora de la tienda.</p>

{AD}

<h2>Todos los países, en hora UTC</h2>
<p>Para comparar países, aquí está cada apertura en hora UTC. En todos los casos es la medianoche en la hora de esa tienda.</p>
<div class="tbl"><table>
  <thead><tr><th>Hora UTC</th><th>Países</th></tr></thead>
  <tbody>{_horas}</tbody>
</table></div>

<h2>Precarga, Xbox y edición en caja</h2>
<ul>
  <li><strong>Precarga:</strong> en PS5 empieza el 10 de noviembre a la medianoche de cada país. En Xbox empieza a la vez en todo el mundo el 10 de noviembre a las 00:00 GMT, que en Miami es el 9 a las 7:00 p.&nbsp;m. La caja con código llega a las tiendas el 12. El día del lanzamiento solo esperas a que se desbloquee.</li>
  <li><strong>Xbox Cloud Gaming:</strong> Microsoft confirmó que en la nube (incluida Xbox One) se puede jugar desde el 19 de noviembre a la 1:00 a.&nbsp;m. hora de Miami (ET), que son las 6:00 UTC, las 7:00 en la España peninsular y las 0:00 en el centro de México.</li>
  <li><strong>Xbox:</strong> la Microsoft Store confirma el 19 de noviembre, pero todavía no muestra un horario por país. Lo normal es que se parezca al de PlayStation, aunque no está confirmado.</li>
  <li><strong>Caja de tienda:</strong> trae un código de descarga, no el juego en disco, así que se desbloquea a la misma hora que la versión digital y necesitas internet para bajarlo.</li>
  <li><strong>Espacio:</strong> Rockstar confirmó que la precarga ocupa hasta 212 GB, según la consola. Déjalo libre antes del 10 de noviembre.</li>
  <li><strong>Primer parche (reportado):</strong> desde el 13 de noviembre se está descargando la <strong>actualización 1.002.000</strong>, de alrededor de 1 GB en PS5 según usuarios que siguen las descargas. Llega por tandas, así que puede que aún no te salga. Rockstar no publicó notas del parche ni explicó qué cambia. Deja la consola encendida o en reposo con internet para tenerla lista antes del 19.</li>
</ul>

<h2>Directo de 24 horas en YouTube</h2>
<p>YouTube anunció un directo de 24 horas para el lanzamiento en su canal oficial (@YouTube), con más de 30 creadores de más de una docena de países jugando GTA VI, programas en vivo y cobertura desde Miami. Es un evento de YouTube, no de Rockstar.</p>
<div class="tbl"><table>
  <thead><tr><th>Lugar</th><th>Previa (con RDCWorld)</th><th>Empieza el maratón</th></tr></thead>
  <tbody>
    <tr><td>Miami / EE.UU. costa este</td><td class="num">23:00 · 18 nov</td><td class="num">00:00 · 19 nov</td></tr>
    <tr><td>México (centro)</td><td class="num">22:00 · 18 nov</td><td class="num">23:00 · 18 nov</td></tr>
    <tr><td>Colombia, Perú y Ecuador</td><td class="num">23:00 · 18 nov</td><td class="num">00:00 · 19 nov</td></tr>
    <tr><td>Argentina y Chile</td><td class="num">01:00 · 19 nov</td><td class="num">02:00 · 19 nov</td></tr>
    <tr><td>España (península)</td><td class="num">05:00 · 19 nov</td><td class="num">06:00 · 19 nov</td></tr>
    <tr><td>UTC</td><td class="num">04:00 · 19 nov</td><td class="num">05:00 · 19 nov</td></tr>
  </tbody>
</table></div>
<p>Entre los creadores anunciados están JuanSGuarnizo y Rivers, además de Caylus, Jelly, Zhong, Jake Baldino, Cinna, Loserfruit, Kinda Funny Games y Total Gaming. YouTube también dio sus cifras: más de 40.000 millones de vistas en videos de GTA VI antes del lanzamiento.</p>

<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿A qué hora empieza el directo de 24 horas de GTA 6 en YouTube?</dt><dd>La previa empieza el 18 de noviembre a las 11:00 p.&nbsp;m. hora de Miami y el maratón de 24 horas arranca a la medianoche del 19, en el canal oficial de YouTube.</dd>
  <dt>¿A qué hora sale GTA 6 en México?</dt><dd>A las 00:00 del 19 de noviembre, hora del centro de México, según la PlayStation Store.</dd>
  <dt>¿A qué hora sale GTA 6 en España?</dt><dd>A las 00:00 del 19 de noviembre en la península; en Canarias, a las 23:00 del 18.</dd>
  <dt>¿A qué hora sale GTA 6 en Argentina, Colombia o Chile?</dt><dd>A las 00:00 del 19 de noviembre, hora local, según la PlayStation Store.</dd>
  <dt>¿Se puede jugar antes cambiando la región a Nueva Zelanda?</dt><dd>El juego se desbloquea según la región de la cuenta y de la tienda donde lo compraste. Cambiar de región no está garantizado que funcione y puede darte problemas con la compra, así que no lo recomendamos. El 17 de noviembre se reportaron algunas cuentas de PlayStation suspendidas (error WS-116331-5) entre gente que probó el truco de Nueva Zelanda, aunque no está claro que la causa sea el cambio de región. Sony no ha comentado nada.</dd>
  <dt>¿Rockstar confirmó estos horarios?</dt><dd>No. Rockstar solo ha confirmado la fecha del 19 de noviembre. Los horarios son los que aparecen en la PlayStation Store y pueden cambiar.</dd>
</dl>
{AFF}"""

# ---------- Tráilers ----------
_tr = "".join(f'<section class="trailer"><h2>{t}</h2><p class="updated">{d}</p>{video(v, t + " de GTA 6")}<p>{x}</p></section>' for v, t, d, x in TRAILERS)
trailers = f"""
<span class="mile">Videos</span>
<h1>Todos los tráilers de GTA 6 y el Extended Look</h1>
{UPD}
<p class="lede">Los tráilers oficiales de Rockstar, incluido el corto de la precarga, y el Extended Look, el video de casi media hora con gameplay, del más nuevo al más antiguo. Toca uno para verlo aquí mismo.</p>
{_tr}
{AD}
<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Cuántos tráilers tiene GTA 6?</dt><dd>Cuatro oficiales: el tráiler 1 (diciembre de 2023), el tráiler 2 (mayo de 2025), el tráiler de lanzamiento (15 de octubre de 2026) y el corto de la precarga (10 de noviembre de 2026). Además está el Extended Look (27 de agosto de 2026), un video más largo con gameplay.</dd>
  <dt>¿Qué canción suena en el tráiler de la precarga?</dt><dd>"Blood in Your Eyes", de Tove Lo, una de las canciones nuevas de GTA VI: The Album.</dd>
  <dt>¿Dónde ver el Extended Look de GTA 6?</dt><dd>Se estrenó en Netflix y seis horas después llegó gratis al canal de YouTube de Rockstar. Lo puedes ver en esta misma página.</dd>
  <dt>¿Qué canción suena en el tráiler de lanzamiento?</dt><dd>"Flower in a Hurricane", de Justice con Tame Impala, SZA y King Gizzard &amp; The Lizard Wizard. Justice también compuso la banda sonora original del juego.</dd>
  <dt>¿Los tráilers están grabados en el juego?</dt><dd>Sí. Rockstar indica que el tráiler 2, el de lanzamiento y el de la precarga se capturaron dentro del juego en una PS5.</dd>
</dl>
{YT_JS}
{AFF}"""

# ---------- Revistas ----------
revistas = f"""
<span class="mile">Revistas</span>
<h1>Las revistas de GTA 6: Edge, Game Informer, Dazed, TROISCOULEURS y LOVE</h1>
{UPD}
<p class="lede">Cinco revistas le dedicaron portada y entrevistas a GTA 6 antes del lanzamiento. Estas son las ediciones, lo que trae cada una y cómo conseguirlas. Las fotos de Game Informer y Dazed son de nuestros propios ejemplares.</p>

<section class="revista">
  <div class="revista-txt">
    <h2>Edge, número 430</h2>
    <p class="updated">29 de octubre de 2026 · especial de Navidad · Reino Unido</p>
    <p>La revista británica de videojuegos más veterana le dedicó a GTA 6 una <strong>portada desplegable de doble cara</strong> con Jason y Lucia, y un <strong>reportaje de 16 páginas</strong> firmado por Simon Parkin desde Rockstar North.</p>
    <ul>
      <li>Rob Nelson jugó unos 90 minutos sin guion delante de la revista. También hablan Aaron Garbut y Phil Hooker.</li>
      <li>El dato estrella: Leonida es casi tan grande como los mapas de GTA IV, GTA V y RDR2 juntos.</li>
      <li>Más de diez capturas nuevas hechas para el reportaje.</li>
      <li>Todo lo que cuenta está resumido en <a href="todo-lo-confirmado.html">Todo lo confirmado</a>.</li>
    </ul>
    <p><strong>Cómo conseguirla:</strong> el reportaje completo se puede leer gratis en la web de GamesRadar+ desde el 29 de octubre. La revista impresa está en quioscos de Reino Unido, y los suscriptores nuevos fuera de Reino Unido reciben gratis la edición digital.</p>
  </div>
</section>

<section class="revista">
  <figure><img src="img/revistas/game-informer-gta-6.jpg" width="900" height="1200" loading="lazy" alt="Ejemplar físico de Game Informer con Jason y Lucia en un convertible rojo frente al skyline de Vice City"><figcaption>Nuestro ejemplar de Game Informer.</figcaption></figure>
  <div class="revista-txt">
    <h2>Game Informer, número 382</h2>
    <p class="updated">Edición digital: 29 de septiembre de 2026</p>
    <p>En la portada salen Jason y Lucia armados en un convertible rojo, con el dinero escondido en la puerta y Vice City al fondo.</p>
    <ul>
      <li>Reportaje de <strong>14 páginas</strong> con entrevistas a diseñadores de Rockstar.</li>
      <li><strong>12 capturas exclusivas</strong>: el downtown de noche, los pantanos de Grassrivers, los Cayos con tormenta y más.</li>
      <li>Lo más comentado: <strong>huracanes</strong>, clima por zonas, más de <strong>170 especies de animales</strong> y que es el mapa más grande que ha hecho Rockstar.</li>
      <li>Lo escribió Marcus Stewart, que se crio en el sur de Florida.</li>
    </ul>
    <p><strong>Cómo conseguirla:</strong> la versión digital está en la app de Game Informer. La impresa llega a los suscriptores; si no lo eres, toca buscarla de reventa.</p>
  </div>
</section>

<section class="revista">
  <figure><img src="img/revistas/dazed-gta-6.jpg" width="900" height="1067" loading="lazy" alt="Ejemplar físico de Dazed con Lucia Caminos y Jason Duval en la portada New Idols"><figcaption>Nuestro ejemplar de Dazed.</figcaption></figure>
  <div class="revista-txt">
    <h2>Dazed, otoño de 2026</h2>
    <p class="updated">Volumen VI · £7.99 en Reino Unido</p>
    <p>Portada <strong>"New Idols"</strong> con Lucia Caminos y Jason Duval frente a hoteles art déco de Vice City.</p>
    <ul>
      <li>Rockstar presenta a Jason como ex militar metido en el tráfico de droga, y a Lucia recién salida de prisión.</li>
      <li>Cuenta cómo el estudio lleva cerca de diez años investigando Miami y sale el "Leonida Man", la versión del juego del famoso "Florida Man".</li>
      <li>Más de 50 artistas callejeros reales pintaron los murales de Stockyard, el barrio inspirado en Wynwood.</li>
      <li>La música del juego bebe del Miami bass.</li>
    </ul>
    <p><strong>Cómo conseguirla:</strong> se vendió en tiendas y en la web de Dazed. Se agotó y luego volvió a haber ejemplares, así que vale la pena revisar antes de pagar precio de reventa.</p>
  </div>
</section>

<section class="revista">
  <figure><img src="img/revistas/troiscouleurs-gta-6.jpg" width="900" height="1273" loading="lazy" alt="Portada de TROISCOULEURS número 227 con Lucia y Jason abrazados frente a la bahía de Vice City"><figcaption>Portada: TROISCOULEURS / Rockstar Games.</figcaption></figure>
  <div class="revista-txt">
    <h2>TROISCOULEURS, número 227</h2>
    <p class="updated">Septiembre de 2026 · Francia · gratis</p>
    <p>La revista de cine de los cines mk2 de París le dio la portada a GTA 6 con una pregunta provocadora: <strong>"¿La mejor película del año?"</strong>. En la portada, Lucia y Jason abrazados frente a la bahía de Vice City.</p>
    <ul>
      <li>El periodista Étienne Rouillon vio unos <strong>30 minutos de juego en Rockstar North</strong> y a Rob Nelson jugando durante casi una hora.</li>
      <li><strong>Entrevista larga con Rob Nelson</strong>: el equipo visita los lugares reales antes de diseñar el mapa, y a veces una canción marca el tono de una zona. La pareja nació de lo que lograron con Arthur Morgan en RDR2: que te importen los dos personajes.</li>
      <li>Rockstar busca un estilo algo estilizado y no fotorrealista, para no caer en el "valle inquietante". Nelson describe los GTA como "cápsulas del tiempo" de su época.</li>
      <li>Según la revista, Vice City mide <strong>el doble que Los Santos</strong> y, sumando los pueblos de alrededor, las zonas urbanas son unas <strong>11 veces</strong> las de GTA 5.</li>
      <li>Trae también un especial sobre la relación entre GTA y el cine.</li>
    </ul>
    <p><strong>Cómo conseguirla:</strong> es gratis en los cines mk2 de Francia (100,000 ejemplares) y por suscripción en la tienda de mk2. La preview y la entrevista también están publicadas en su web.</p>
  </div>
</section>

<section class="revista">
  <figure><img src="img/revistas/love-gta-6.jpg" width="687" height="860" loading="lazy" alt="Portada de LOVE Magazine número 27 con Lucia y Jason y el lema America's Most Wanted"><figcaption>Portada: LOVE Magazine / Rockstar Games.</figcaption></figure>
  <div class="revista-txt">
    <h2>LOVE Magazine, número 27</h2>
    <p class="updated">5 de octubre de 2026</p>
    <p>Portada <strong>"America's Most Wanted"</strong> con Lucia y Jason. Se agotó en minutos y trae capturas nuevas y la entrevista más profunda sobre la historia:</p>
    <ul>
      <li>Lucia es de Liberty City, y Raul Bautista es el mentor que les enseña a dar golpes grandes.</li>
      <li>Ambrosia está inspirada en Clewiston y el lago Okeechobee.</li>
      <li>El sueño americano del juego es modesto: una casa para la familia y deudas pagadas.</li>
      <li>Hay sátira política con elecciones y anuncios de campaña, pero sin políticos reales.</li>
    </ul>
  </div>
</section>

{AD}


<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Qué revistas sacaron portada de GTA 6?</dt><dd>Edge (número 430), Game Informer (número 382), Dazed (otoño de 2026), TROISCOULEURS (número 227, Francia) y LOVE Magazine (número 27).</dd>
  <dt>¿Dónde leer gratis el reportaje de Edge sobre GTA 6?</dt><dd>Edge lo publicó completo y gratis en la web de GamesRadar+ el 29 de octubre de 2026, el mismo día que salió la revista impresa.</dd>
  <dt>¿Dónde se lee gratis la Game Informer de GTA 6?</dt><dd>La edición digital se puede leer en la app de Game Informer.</dd>
  <dt>¿Qué se sabe de GTA 6 por las revistas?</dt><dd>Todo lo que contaron está resumido en <a href="todo-lo-confirmado.html">Todo lo confirmado</a>.</dd>
</dl>
{AFF}"""

# ---------- Reseñas ----------
resenas = f"""
<span class="mile">Reseñas</span>
<h1>Reseñas de GTA 6: 99 en Metacritic</h1>
{UPD}
<p class="lede">Las reseñas de GTA VI salieron el <strong>18 de noviembre</strong>, un día antes del lanzamiento, y la nota media en Metacritic quedó en <strong>99 sobre 100</strong>. Es la nota más alta de la página, empatada con The Legend of Zelda: Ocarina of Time (1998).</p>
<div class="note"><strong>Ojo:</strong> la media de Metacritic puede moverse unas décimas mientras entran más reseñas. Por lo que se ha publicado, los medios analizaron la versión de PS5. Todavía no hay reseñas centradas en Xbox Series X|S.</div>

<h2>Las notas de cada medio</h2>
<div class="tbl"><table>
  <thead><tr><th>Medio</th><th>Nota</th></tr></thead>
  <tbody>
    <tr><td>IGN</td><td class="num">10/10</td></tr>
    <tr><td>GameSpot</td><td class="num">10/10</td></tr>
    <tr><td>Game Informer</td><td class="num">10/10</td></tr>
    <tr><td>Edge</td><td class="num">10/10</td></tr>
    <tr><td>Push Square</td><td class="num">10/10</td></tr>
    <tr><td>GAMINGbible</td><td class="num">10/10</td></tr>
    <tr><td>Eurogamer</td><td class="num">5/5</td></tr>
    <tr><td>GamesRadar+</td><td class="num">5/5</td></tr>
    <tr><td>VGC</td><td class="num">5/5</td></tr>
    <tr><td>The Guardian</td><td class="num">5/5</td></tr>
    <tr><td>Giant Bomb</td><td class="num">5/5</td></tr>
    <tr><td>TheSixthAxis</td><td class="num">9/10</td></tr>
    <tr><td>The New York Times</td><td class="num">Sin nota ("Critic's Pick")</td></tr>
  </tbody>
</table></div>
<p>Según GAMINGbible, las notas individuales recogidas en Metacritic van del 9 al 10. Ninguna de las grandes reseñas le pone menos de un 9.</p>

{AD}

<h2>Lo que más gusta</h2>
<ul>
  <li><strong>Jason y Lucia.</strong> Es lo más repetido. Edge dice que su relación está movida por el amor y no por el miedo, y The New York Times la describe como un juego sobre el amor y las relaciones de pareja.</li>
  <li><strong>El mundo abierto.</strong> Push Square lo llama el mundo abierto más profundo y denso desde Red Dead Redemption 2. GameSpot destaca el nivel de detalle de Leonida.</li>
  <li><strong>Todo mejora respecto a GTA V.</strong> GamesRadar+ dice que no hay una parte de la jugabilidad de la saga que no haya mejorado. VGC lo llama una obra maestra moderna en historia, jugabilidad, gráficos, música y tecnología.</li>
  <li><strong>Más parecido a Red Dead Redemption 2.</strong> Respec dice que se siente más como una secuela de Red Dead Redemption 2 que de GTA V.</li>
</ul>

<h2>Lo que se critica</h2>
<p>Las pegas son pocas y menores:</p>
<ul>
  <li><strong>Rendimiento:</strong> VGC habla de pequeños problemas de rendimiento que no estropean la experiencia.</li>
  <li><strong>Historia muy larga:</strong> TheSixthAxis dice que, en una historia tan larga, la necesidad de subir siempre la apuesta le quita algo de impacto.</li>
  <li><strong>Sin GTA Online todavía:</strong> el juego sale sin modo online nuevo. Rockstar no le ha puesto fecha.</li>
</ul>

<h2>¿Cuánto dura?</h2>
<p>Las reseñas no dan una duración oficial de la historia. Lo que sí cuentan los críticos son sus horas de juego: el de GAMINGbible pasó de las 70 horas y algunos medios hablan de 100 o más sin haber visto todo el mapa. La duración de 50 horas de historia que se reportó antes del lanzamiento sigue sin confirmar; la tienes en <a href="todo-lo-confirmado.html">todo lo confirmado</a>.</p>

<h2>Nominado a Juego del Año en The Game Awards</h2>
<p>Las nominaciones de The Game Awards 2026 se anunciaron el 17 de noviembre, antes de que el juego saliera, y GTA VI está entre los candidatos a <strong>Juego del Año</strong>. Según PC Gamer y Tom's Guide, suma <strong>8 nominaciones</strong> en total. La gala es el <strong>10 de diciembre</strong> en Los Ángeles, y el público puede votar hasta el 9 de diciembre.</p>

<dl class="faq">
  <dt>¿Qué nota tiene GTA 6 en Metacritic?</dt><dd>99 sobre 100, la más alta de la página, empatada con Ocarina of Time. La media puede variar un poco mientras se suman reseñas.</dd>
  <dt>¿Qué nota le dio IGN a GTA 6?</dt><dd>Un 10/10. GameSpot, Game Informer y Edge también le dieron un 10.</dd>
  <dt>¿Las reseñas hablan de la versión de Xbox?</dt><dd>Por ahora no. Los medios analizaron la versión de PS5. Cuando haya análisis de Xbox Series X|S, sobre todo de la Series S, lo añadimos aquí.</dd>
  <dt>¿Cuándo sale GTA 6?</dt><dd>El 19 de noviembre de 2026 en PS5 y Xbox Series X|S. Mira <a href="hora-de-salida-gta-6.html">a qué hora sale en tu país</a>.</dd>
</dl>
{AFF}"""
trofeos = f"""
<span class="mile">Guía</span>
<h1>Trofeos y logros de GTA 6: la lista completa de los 55</h1>
{UPD}
<p class="lede">GTA VI tiene <strong>55 trofeos</strong> en PS5: <strong>1 platino, 2 de oro, 6 de plata y 46 de bronce</strong>. En Xbox Series X|S son los mismos 55 logros y suman <strong>1.000 de Gamerscore</strong>. 28 están ocultos porque destripan la historia.</p>
<div class="note"><strong>Ojo:</strong> la lista viene de las guías de trofeos publicadas el 18 de noviembre, que coinciden en nombres, cantidad y grados. Rockstar no la publicó en su web. Dejamos los nombres originales en inglés, que son los que verás en la consola, y la condición traducida.</div>

<h2>Resumen rápido</h2>
<div class="tbl"><table>
  <thead><tr><th>Tipo</th><th>Cantidad</th></tr></thead>
  <tbody>
    <tr><td>Platino</td><td class="num">1</td></tr>
    <tr><td>Oro</td><td class="num">2</td></tr>
    <tr><td>Plata</td><td class="num">6</td></tr>
    <tr><td>Bronce</td><td class="num">46</td></tr>
    <tr><td>Ocultos (historia y secretos)</td><td class="num">28</td></tr>
  </tbody>
</table></div>

<h2>Los trofeos más difíciles</h2>
<ul>
  <li><strong>A Long Road (oro):</strong> llegar al 100% del juego. Es el más largo de todos.</li>
  <li><strong>You Gotta Know When to Get Off (oro):</strong> terminar la historia (la misión final).</li>
  <li><strong>Cunning Stunts (plata):</strong> 250 saltos de acrobacia repartidos por el mapa.</li>
  <li><strong>You WAiNKer! (plata):</strong> hacer WAiNK It en 100 lugares.</li>
  <li><strong>Maximum Withdrawal (plata):</strong> robar 5 cámaras acorazadas de bancos y escapar.</li>
</ul>

{AD}

<h2>Trofeos sin spoilers</h2>
<div class="tbl"><table>
  <thead><tr><th>Trofeo</th><th>Grado</th><th>Cómo se consigue</th></tr></thead>
  <tbody>
    <tr><td>Vice Got a Price!</td><td>Platino</td><td>Consigue todos los demás trofeos.</td></tr>
    <tr><td>A Long Road</td><td>Oro</td><td>Llega al 100% del juego.</td></tr>
    <tr><td>Cunning Stunts</td><td>Plata</td><td>Completa 250 acrobacias (saltos de acrobacia).</td></tr>
    <tr><td>The Shootist</td><td>Plata</td><td>Saca medalla de oro en todos los desafíos del campo de tiro.</td></tr>
    <tr><td>Strangers &amp; Freaks</td><td>Plata</td><td>Completa 8 cadenas de misiones de desconocidos por Leonida.</td></tr>
    <tr><td>Don't Touch My Deck</td><td>Plata</td><td>Completa 3 colecciones de cartas coleccionables.</td></tr>
    <tr><td>You WAiNKer!</td><td>Plata</td><td>Haz WAiNK It en 100 lugares.</td></tr>
    <tr><td>Maximum Withdrawal</td><td>Plata</td><td>Roba 5 cámaras acorazadas de bancos y escapa.</td></tr>
    <tr><td>Master of None</td><td>Bronce</td><td>Prueba cada tipo de actividad una vez.</td></tr>
    <tr><td>Top Fun</td><td>Bronce</td><td>Gana una carrera de drones Top Fun en cada ubicación.</td></tr>
    <tr><td>Earn Cash, Not Kudos</td><td>Bronce</td><td>Gana 20 carreras distintas.</td></tr>
    <tr><td>Baited My Tackle</td><td>Bronce</td><td>Gánale a Cal en un desafío de pesca.</td></tr>
    <tr><td>Stick Fiddler</td><td>Bronce</td><td>Completa un juego de arcade.</td></tr>
    <tr><td>Positive Mental Attitude</td><td>Bronce</td><td>Medita en todos los puntos de meditación de Leonida.</td></tr>
    <tr><td>One Last Thing</td><td>Bronce</td><td>Completa 50 desafíos.</td></tr>
    <tr><td>Hot Together</td><td>Bronce</td><td>Quítate un nivel de búsqueda de 4 estrellas junto a tu pareja.</td></tr>
    <tr><td>Retail Therapy</td><td>Bronce</td><td>Roba 3 tiendas seguidas con tu pareja sin perder el nivel de búsqueda.</td></tr>
    <tr><td>Whip It Good</td><td>Bronce</td><td>Descubre 100 vehículos.</td></tr>
    <tr><td>Gunslinger</td><td>Bronce</td><td>Elimina a 5 enemigos en un solo uso del Combat Focus.</td></tr>
    <tr><td>Sneakthief</td><td>Bronce</td><td>Roba una joyería sin que te detecten.</td></tr>
    <tr><td>A Classic Blitz Play</td><td>Bronce</td><td>Roba un camión blindado y escapa.</td></tr>
    <tr><td>The Goodtime State</td><td>Bronce</td><td>Explora todo Leonida.</td></tr>
    <tr><td>Pest Control</td><td>Bronce</td><td>Roba una operación ilegal de cada banda.</td></tr>
    <tr><td>Dime on the Dollar</td><td>Bronce</td><td>Gana 250.000 $ blanqueando billetes marcados con tus contactos.</td></tr>
    <tr><td>Treat Yo Self</td><td>Bronce</td><td>Gasta 100.000 $ en tiendas.</td></tr>
    <tr><td>Little Boxes</td><td>Bronce</td><td>Compra todas las propiedades de garaje.</td></tr>
    <tr><td>On the Spot</td><td>Bronce</td><td>Registra 10 vehículos en la app Scooter Bros.</td></tr>
  </tbody>
</table></div>

<h2>Trofeos ocultos de la historia (spoilers)</h2>
<p>Estos llevan nombres de capítulos y misiones. Si no quieres saber nada de la historia, sáltate esta sección.</p>
<details><summary>Mostrar los trofeos de la historia</summary>
<div class="tbl"><table>
  <thead><tr><th>Trofeo</th><th>Grado</th><th>Cómo se consigue</th></tr></thead>
  <tbody>
    <tr><td>You Gotta Know When to Get Off</td><td>Oro</td><td>Termina la historia (misión final).</td></tr>
    <tr><td>Just Like Paradise</td><td>Bronce</td><td>Completa "Gone Fishing".</td></tr>
    <tr><td>Paradise Lost</td><td>Bronce</td><td>Completa el capítulo 1.</td></tr>
    <tr><td>T**s Ass Drug Money</td><td>Bronce</td><td>Completa el capítulo 2.</td></tr>
    <tr><td>Vice City, Baby!</td><td>Bronce</td><td>Completa el capítulo 3.</td></tr>
    <tr><td>Top of the World, Ma</td><td>Bronce</td><td>Completa el capítulo 4.</td></tr>
    <tr><td>Trust</td><td>Bronce</td><td>Completa "Breakfast Run".</td></tr>
    <tr><td>Break the Bank</td><td>Bronce</td><td>Completa "The Cartel Heist".</td></tr>
    <tr><td>Family Matters</td><td>Bronce</td><td>Completa "Child's Play".</td></tr>
    <tr><td>DWNFALL</td><td>Bronce</td><td>Completa "Headliners".</td></tr>
    <tr><td>Hi-Jacked</td><td>Bronce</td><td>Completa "VCIA Takedown".</td></tr>
    <tr><td>Snow Storm</td><td>Bronce</td><td>Completa "Operation Savage Glory".</td></tr>
    <tr><td>Road to Rehabilitation</td><td>Bronce</td><td>Completa la última misión de Andy.</td></tr>
    <tr><td>This Was No Boat Accident</td><td>Bronce</td><td>Completa la última misión de Kenton.</td></tr>
    <tr><td>The Lone Rider</td><td>Bronce</td><td>Completa la última misión de Billy.</td></tr>
    <tr><td>Supply &amp; Demand</td><td>Bronce</td><td>Completa la última misión de Randy.</td></tr>
    <tr><td>Spin On This!</td><td>Bronce</td><td>Completa la última misión de Tyrone.</td></tr>
    <tr><td>Fair Game</td><td>Bronce</td><td>Caza un animal único para Bret.</td></tr>
  </tbody>
</table></div>
</details>

<h2>Trofeos ocultos secretos (spoilers)</h2>
<p>Estos tienen pistas en vez de instrucciones. Las guías todavía no explican cómo se sacan varios de ellos; los iremos completando cuando estén comprobados.</p>
<details><summary>Mostrar los trofeos secretos</summary>
<div class="tbl"><table>
  <thead><tr><th>Trofeo</th><th>Grado</th><th>Pista</th></tr></thead>
  <tbody>
    <tr><td>Catch Me If You Can</td><td>Bronce</td><td>Haz una "salida no programada" en el aeropuerto VCIA.</td></tr>
    <tr><td>Challenging Tank</td><td>Bronce</td><td>"Hace calor en estos Rhinos" (los tanques de la saga).</td></tr>
    <tr><td>In The Beginning...</td><td>Bronce</td><td>Tómate un cóctel con vistas en Ocean Beach.</td></tr>
    <tr><td>Capital Offense</td><td>Bronce</td><td>Sal rompiendo el escaparate de un concesionario, al estilo clásico.</td></tr>
    <tr><td>Let's Go Bowling</td><td>Bronce</td><td>Algo que pasa en la bolera de Kolt &amp; Associates.</td></tr>
    <tr><td>Personal Best</td><td>Bronce</td><td>"Una sociedad con atractivo para las masas."</td></tr>
    <tr><td>Actions Speak Louder</td><td>Bronce</td><td>"Decisiones tomadas (para bien o para mal)."</td></tr>
    <tr><td>Bad Luck, I Guess</td><td>Bronce</td><td>"A la segunda va la vencida."</td></tr>
    <tr><td>The Truth Is Out There</td><td>Bronce</td><td>"¿Qué demonios acaba de pasar?"</td></tr>
    <tr><td>Ten Pin</td><td>Bronce</td><td>Derriba a alguien con un ataque cuerpo a cuerpo desde un vehículo.</td></tr>
  </tbody>
</table></div>
</details>

{AD}

<h2>¿Hay trofeos que se pueden perder?</h2>
<p>Por ahora ninguna guía ha confirmado trofeos que se pierdan para siempre. Algunas avisan de que las cadenas de misiones de desconocidos podrían depender del avance de la historia, pero no está comprobado. Mientras tanto, lo prudente es:</p>
<ul>
  <li>Guardar a mano antes de las misiones grandes de la historia y de los golpes.</li>
  <li>Hacer las misiones de desconocidos en cuanto aparezcan en el mapa.</li>
  <li>Ir apuntando lo que llevas de los trofeos de "todos los lugares" (drones, meditación, WAiNK It, campo de tiro), que son los que más se olvidan.</li>
</ul>

<dl class="faq">
  <dt>¿Cuántos trofeos tiene GTA 6?</dt><dd>55: 1 platino, 2 de oro, 6 de plata y 46 de bronce. En Xbox son 55 logros que suman 1.000 de Gamerscore.</dd>
  <dt>¿Cómo se llama el platino de GTA 6?</dt><dd>"Vice Got a Price!". Se consigue al tener los otros 54 trofeos.</dd>
  <dt>¿Hay que llegar al 100% para el platino?</dt><dd>Sí. "A Long Road" pide el 100% del juego, así que sin el 100% no hay platino.</dd>
  <dt>¿Hay trofeos de GTA Online?</dt><dd>No. GTA VI salió sin modo online y los 55 trofeos son del modo historia.</dd>
  <dt>¿Cuánto se tarda en sacar el platino?</dt><dd>Todavía no hay una cifra fiable. Los críticos pasaron de 70 horas sin ver todo el mapa, así que cuenta con bastante más que eso.</dd>
</dl>
{AFF}"""


principiantes = f"""
<span class="mile">Guía</span>
<h1>Guía para empezar GTA 6: misiones del Capítulo 1, dinero y consejos</h1>
{UPD}
<p class="lede">Lo que conviene saber en tus primeras horas en Leonida: las <strong>22 misiones del Capítulo 1</strong> en orden, cómo <strong>no perder tu dinero</strong>, cómo moverte sin teletransporte, cómo quedarte con los autos que robas y las primeras formas de ganar plata. Sin spoilers de la trama.</p>
<div class="note"><strong>Ojo:</strong> todo lo de esta guía aparece en al menos dos de las guías publicadas tras el lanzamiento. Lo que solo decía una fuente lo dejamos fuera. Los nombres de misiones y apps van en inglés, que es como salen en el juego.</div>

<h2>Las misiones del Capítulo 1 en orden</h2>
<p>El Capítulo 1 tiene <strong>22 misiones de historia</strong>. Las guías coinciden en nombres y orden:</p>
<div class="tbl"><table>
  <thead><tr><th>#</th><th>Misión</th></tr></thead>
  <tbody>
    <tr><td class="num">1</td><td>Prologue</td></tr>
    <tr><td class="num">2</td><td>Gone Fishing</td></tr>
    <tr><td class="num">3</td><td>Gear Up</td></tr>
    <tr><td class="num">4</td><td>Just a Scratch</td></tr>
    <tr><td class="num">5</td><td>Lab Fees</td></tr>
    <tr><td class="num">6</td><td>Unwanted Attention</td></tr>
    <tr><td class="num">7</td><td>Pipework</td></tr>
    <tr><td class="num">8</td><td>Hey Arnold!</td></tr>
    <tr><td class="num">9</td><td>Island Dreams</td></tr>
    <tr><td class="num">10</td><td>Feng Shui</td></tr>
    <tr><td class="num">11</td><td>Coming Home</td></tr>
    <tr><td class="num">12</td><td>Buck Me</td></tr>
    <tr><td class="num">13</td><td>Clean Up After Donnie</td></tr>
    <tr><td class="num">14</td><td>Down To Earth</td></tr>
    <tr><td class="num">15</td><td>Clear Skies</td></tr>
    <tr><td class="num">16</td><td>Day Release</td></tr>
    <tr><td class="num">17</td><td>Swamped</td></tr>
    <tr><td class="num">18</td><td>Don Gone</td></tr>
    <tr><td class="num">19</td><td>Recalibration</td></tr>
    <tr><td class="num">20</td><td>Tourist Trap</td></tr>
    <tr><td class="num">21</td><td>Home Sweet Home</td></tr>
    <tr><td class="num">22</td><td>Discharge Time</td></tr>
  </tbody>
</table></div>
<p>El Capítulo 2 empieza con <strong>What's In The Bag?</strong> y <strong>Ambulance Chaser</strong>.</p>
<div class="note"><strong>Punto sin retorno:</strong> las guías avisan de que el Capítulo 1 tiene un punto sin retorno hacia el final. Si quieres explorar o hacer actividades de la zona inicial, hazlo antes de las últimas misiones del capítulo.</div>
{AD}

<h2>No pierdas tu dinero: guárdalo en el banco</h2>
<ul>
  <li><strong>El efectivo que llevas encima se pierde</strong> si te matan o te arrestan. Es el error más común de las primeras horas.</li>
  <li>En la misión <strong>Buck Me</strong> (la 12 del Capítulo 1) se desbloquea <strong>BuckMe</strong>, la app del banco en el teléfono. Desde ahí puedes buscar el cajero más cercano y depositar.</li>
  <li>Lo que está en la cuenta de BuckMe no se pierde al morir ni al ser arrestado. Pasa por un cajero cada vez que juntes una cantidad que te dolería perder.</li>
</ul>

<h2>Cómo moverte: no hay viaje rápido clásico</h2>
<p>GTA VI no tiene el viaje rápido de otros juegos. La alternativa es <strong>RydeMe</strong>, la app de viajes del teléfono: pides un auto y puedes ir sentado o <strong>saltarte el trayecto pagando 100 dólares</strong> extra.</p>

<h2>Quédate con los autos que robas</h2>
<p>Un auto robado no es tuyo para siempre. Para quedártelo, llévalo a un <strong>Pay 'n' Spray</strong> y regístralo como vehículo personal. Algunos autos de gama alta pueden pedir más avance en la historia antes de dejarte registrarlos.</p>

<h2>Usa el modo Focus antes de entrar</h2>
<p>Con el modo Focus activo, las <strong>puertas conectadas a la alarma se ven en rojo</strong>. Míralas antes de colarte en un edificio o de dar un golpe para no hacer saltar la alarma sin querer.</p>

<h2>Primeras formas de ganar dinero</h2>
<div class="tbl"><table>
  <thead><tr><th>Método</th><th>Qué saber</th></tr></thead>
  <tbody>
    <tr><td>Robar tiendas</td><td>La forma más directa al principio. Las tiendas pequeñas pagan poco, unos pocos miles como mucho, pero se pueden hacer desde el inicio.</td></tr>
    <tr><td>Vender a peristas</td><td>Los objetos robados se venden a peristas (fences). Cada uno paga distinto según el tipo de mercancía, así que compara antes de vender.</td></tr>
    <tr><td>Buscar tesoros bajo el agua</td><td>El buceo de tesoros con Kenton se presenta en el Capítulo 1 (misión Island Dreams) y las guías lo recomiendan como dinero fácil al empezar.</td></tr>
    <tr><td>Robar y vender autos</td><td>Los autos robados se pueden vender o registrar en un Pay 'n' Spray para quedártelos.</td></tr>
    <tr><td>Bancos</td><td>Son los golpes que más pagan, pero es mejor dejarlos para más adelante en la historia.</td></tr>
  </tbody>
</table></div>
<p>Y lo de siempre: deposita en BuckMe después de cada golpe.</p>

<h2>¿Y los trucos?</h2>
<p>GTA VI tiene trucos, pero <strong>no funcionan al empezar</strong>: la lista se desbloquea al terminar la historia, y cada truco pide además cumplir una condición. Entre ellos hay uno de <strong>250.000 dólares</strong>, que se desbloquea al acabar la historia de Jason y Lucia. Para tus primeras horas, olvídate de ellos. Cuando llegues, tienes <a href="trucos-gta-6.html">todos los códigos aquí</a>.</p>

<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Cuántas misiones tiene el Capítulo 1 de GTA 6?</dt><dd>22 misiones de historia, desde Prologue hasta Discharge Time.</dd>
  <dt>¿Se pierde el dinero al morir en GTA 6?</dt><dd>Sí, el efectivo que llevas encima. El dinero depositado en BuckMe está a salvo.</dd>
  <dt>¿Cuándo se desbloquea el banco BuckMe?</dt><dd>En la misión Buck Me, la número 12 del Capítulo 1.</dd>
  <dt>¿GTA 6 tiene viaje rápido?</dt><dd>No como en otros juegos. Con la app RydeMe puedes pedir un auto y pagar 100 dólares para saltarte el viaje.</dd>
  <dt>¿Cómo me quedo un auto robado?</dt><dd>Regístralo en un Pay 'n' Spray como vehículo personal.</dd>
  <dt>¿Se pueden usar trucos desde el principio?</dt><dd>No. Los trucos se desbloquean después de terminar la historia.</dd>
</dl>
<p>¿Vas a por el platino? Mira la <a href="trofeos-logros-gta-6.html">lista de los 55 trofeos</a>.</p>
{AFF}"""


trucos = f"""
<span class="mile">Guía</span>
<h1>Trucos de GTA 6: todos los códigos y cómo desbloquearlos</h1>
{UPD}
<p class="lede">GTA VI tiene <strong>61 trucos</strong>, pero no se pueden usar desde el principio: primero hay que <strong>terminar la historia</strong> y después cumplir el reto de cada truco. Aquí tienes cómo se meten, los <strong>18 códigos</strong> que ya se conocen y qué pide cada uno.</p>
<div class="note"><strong>Ojo:</strong> solo ponemos los códigos que coinciden en al menos cuatro guías publicadas tras el lanzamiento. Los demás todavía no se han descubierto, y aquí los marcamos como "sin descubrir". Los nombres de los trucos y vehículos van en inglés, que es como salen en el juego.</div>

<h2>Cómo se desbloquean</h2>
<ul>
  <li>Los trucos <strong>solo aparecen al terminar la historia principal</strong>. Al pasar los créditos se abre una pestaña nueva, <strong>Cheats</strong>, dentro del menú <strong>Progress</strong>.</li>
  <li>Cuatro trucos se desbloquean solo con acabar la historia: <strong>$250,000, Unlimited Focus, Attack Force y Cycle Weather</strong>.</li>
  <li>El resto pide un reto propio: hacer 100 entrenamientos, ganar medallas en los campos de tiro, escapar de la policía muchas veces, completar desafíos de cada categoría, etc. En el menú Progress se ve cuánto te falta.</li>
  <li>Si metes un código que aún no has desbloqueado, no pasa nada.</li>
</ul>

<h2>Cómo se meten los códigos</h2>
<ol>
  <li>Saca el teléfono con <strong>arriba en la cruceta</strong>.</li>
  <li>Con el teléfono fuera, mantén <strong>L1 y pulsa R1</strong> en PS5, o <strong>LB y RB</strong> en Xbox Series X|S.</li>
  <li>Sin soltar, mete la combinación con la cruceta. Los códigos son los mismos en las dos consolas.</li>
</ol>
<p>No hay trucos marcando números de teléfono como en GTA V. Y son solo para el modo historia.</p>

<div class="note"><strong>Antes de usar un truco, guarda la partida.</strong> Según las guías, al activar un truco <strong>no puedes guardar</strong> y se <strong>desactivan los trofeos y logros</strong> durante esa sesión. Haz un guardado manual antes y vuelve a cargarlo cuando termines. Eso también significa que el dinero del truco de $250,000 no se queda en tu partida.</div>
{AD}

<h2>Los códigos que ya se conocen</h2>
<p>A = arriba, B = abajo, I = izquierda, D = derecha, en la cruceta.</p>
<div class="tbl"><table>
  <thead><tr><th>Truco</th><th>Código</th><th>Cómo se desbloquea</th></tr></thead>
  <tbody>
    <tr><td>$250,000</td><td>A, D, B, I, A, I, B, D</td><td>Terminar la historia</td></tr>
    <tr><td>Unlimited Focus (Focus infinito)</td><td>B, A, A, B, A, B, A, B, A, D</td><td>Terminar la historia</td></tr>
    <tr><td>Attack Force</td><td>B, A, I, I, D, B, B, A, B</td><td>Terminar la historia</td></tr>
    <tr><td>Cycle Weather (cambiar el clima)</td><td>B, D, A, B, D, A, D</td><td>Terminar la historia</td></tr>
    <tr><td>Body Armor (chaleco)</td><td>B, A, I, A, A, A, A, A, B, B</td><td>Hacer 100 entrenamientos</td></tr>
    <tr><td>Raise Heat Level</td><td>I, B, D, B, A, B, A</td><td>Escapar 25 veces de un nivel de búsqueda de 3 estrellas</td></tr>
    <tr><td>Raise Wanted Level (subir búsqueda)</td><td>I, B, D, B, A, D, A</td><td>Escapar 50 veces de un nivel de búsqueda de 3 estrellas</td></tr>
    <tr><td>Max Ammo (munición al máximo)</td><td>B, A, D, B, I, I, A, A, B, I</td><td>25 medallas de bronce o mejor en los campos de tiro</td></tr>
    <tr><td>Infinite Ammo (munición infinita)</td><td>B, A, D, B, I, I, A, B, B, B</td><td>25 medallas de plata o mejor en los campos de tiro</td></tr>
    <tr><td>No Reload (sin recargar)</td><td>B, A, D, B, I, I, A, B, B, A</td><td>25 medallas de oro en los campos de tiro</td></tr>
    <tr><td>Exploding Balls</td><td>B, A, I, I, D, B, B, A, D</td><td>Dañar a 20 enemigos con explosivos</td></tr>
    <tr><td>Vehicle Force</td><td>B, A, I, I, D, B, I, A, B</td><td>Matar a 25 enemigos atropellándolos</td></tr>
    <tr><td>HVY Bulldozer</td><td>I, A, D, B, I, D, D, B</td><td>Descubrir la excavadora en el menú Progress</td></tr>
    <tr><td>MTL Pumper (camión de bomberos)</td><td>I, A, D, B, I, D, D, A</td><td>Descubrir el camión de bomberos en el menú Progress</td></tr>
    <tr><td>Maibatsu Boomazoom</td><td>I, A, D, B, I, I, A, I</td><td>Completar 5 desafíos de compras (Shopping)</td></tr>
    <tr><td>Filtro Cataclysm</td><td>B, B, A, D, D, A, I, I, D, D</td><td>Descubrir el Martha's Vamos en el menú Progress</td></tr>
    <tr><td>Filtro Dollhouse</td><td>B, B, A, D, D, A, I, I, B, D</td><td>Pasar 8 horas con tu pareja</td></tr>
    <tr><td>Filtro Faded Glory</td><td>B, B, A, D, D, A, I, I, I, D</td><td>Robar 50 tiendas con tu pareja</td></tr>
  </tbody>
</table></div>
<p>Ojo con los códigos que se parecen: Max Ammo, Infinite Ammo y No Reload solo cambian en los últimos botones, igual que los filtros. Mira bien el final antes de meterlos.</p>

<h2>Los que faltan por descubrir</h2>
<p>El resto de trucos ya se ve en la lista del juego con su reto, pero su código todavía no se conoce. Lo que pide cada grupo:</p>
<div class="tbl"><table>
  <thead><tr><th>Tipo</th><th>Trucos y reto</th></tr></thead>
  <tbody>
    <tr><td>Jugador</td><td>Drunk (gastar 2,500 dólares en alcohol), No Fall Damage (sobrevivir 20 caídas de 40 pies), Parachute (50 saltos en paracaídas o BASE desde 300 pies), Repair Vehicle (ganar 10 carreras en Gellhorn Raceway, Thrillbilly Mud Club y Boone Speedway), Unlimited Nitrous (50 saltos acrobáticos).</td></tr>
    <tr><td>Combate</td><td>All Explosive Weapons (lanzar 100 granadas), Exploding Bottles (lanzar 100 molotov), Explosive Shotgun (dañar a 100 enemigos con explosivos), Hauners H-AT (destruir 100 vehículos), Incendiary Ammo (quemar a 100 enemigos).</td></tr>
    <tr><td>Vehículos</td><td>La mayoría se consiguen completando 5 desafíos de una categoría o todos los de una categoría (Survival, Combat, Sports, Fitness, Criminal, Exploration, Vehicle, Shopping). El Hauners P-996 Lazer pide completar todos los desafíos, y el Inflatable Flamingo, destruir 50 flamencos de cocaína.</td></tr>
    <tr><td>Clima y hora</td><td>Move Time Forward (encontrar 10 relojes coleccionables) y Pause Time of Day (encontrar 20).</td></tr>
    <tr><td>Filtros</td><td>Golden Hour (4 horas de la mano con tu pareja), Bubblegum (las 24 cartas de Vice City Flamingos), Fisheye (pescar 100 peces), Fast Forward (meditar 50 veces), Dark Mirror (ganar 500,000 dólares vendiendo vehículos), Pixel Art (250,000 dólares vendiendo coleccionables), Hellscape (robar 100 vehículos de policía), Migraine (aguantar 6 minutos con 6 estrellas), entre otros.</td></tr>
  </tbody>
</table></div>
<p>Iremos sumando códigos a la tabla a medida que se confirmen.</p>

<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Cuántos trucos tiene GTA 6?</dt><dd>61, repartidos entre jugador, combate, vehículos, clima y hora, y filtros de pantalla.</dd>
  <dt>¿Cómo se ponen los trucos en GTA 6?</dt><dd>Saca el teléfono con arriba en la cruceta, mantén L1 y pulsa R1 (LB y RB en Xbox) y mete la combinación con la cruceta.</dd>
  <dt>¿Se pueden usar trucos desde el principio?</dt><dd>No. Se desbloquean al terminar la historia, y cada uno pide además cumplir su propio reto.</dd>
  <dt>¿Cuál es el truco de dinero de GTA 6?</dt><dd>$250,000: arriba, derecha, abajo, izquierda, arriba, izquierda, abajo, derecha. Se desbloquea al terminar la historia. Como no se puede guardar con trucos activos, ese dinero no se queda en tu partida.</dd>
  <dt>¿Los trucos desactivan los trofeos?</dt><dd>Sí, según las guías: durante la sesión en la que los usas no se ganan trofeos ni logros y no se puede guardar. Guarda antes y recarga después.</dd>
  <dt>¿Hay trucos con número de teléfono?</dt><dd>No. En GTA VI todos los trucos se meten con la cruceta.</dd>
</dl>
<p>¿Todavía no acabas la historia? Empieza por la <a href="guia-principiantes-gta-6.html">guía para empezar</a> y la <a href="trofeos-logros-gta-6.html">lista de trofeos</a>.</p>
{AFF}"""


robos = f"""
<span class="mile">Guía</span>
<h1>Robos y atracos de GTA 6: tiendas, bancos, cámaras acorazadas y golpes</h1>
{UPD}
<p class="lede">En GTA VI se puede robar casi cualquier negocio de Leonida: tiendas, casas de empeño, joyerías, prestamistas, bancos pequeños y las <strong>cámaras acorazadas</strong> de los bancos grandes, que dan hasta <strong>205,000 dólares</strong>. Aquí tienes cuándo se desbloquea cada tipo, cuánto pagan, cómo hacerlos sin que te pillen y los dos grandes golpes de la historia.</p>
<div class="note"><strong>Ojo:</strong> solo ponemos lo que coincide en varias guías publicadas tras el lanzamiento. Las cantidades son las que reportan los jugadores, no cifras de Rockstar, y pueden variar en tu partida. Los nombres de misiones y negocios van en inglés, como salen en el juego.</div>

<h2>Tipos de robo y cuándo se desbloquean</h2>
<div class="tbl"><table>
  <thead><tr><th>Tipo</th><th>Cuántos hay</th><th>Cuándo se desbloquea</th><th>Botín aproximado</th></tr></thead>
  <tbody>
    <tr><td>Atracos a tiendas (stick-ups)</td><td class="num">91</td><td>Desde el principio</td><td>Poco, unos pocos miles</td></tr>
    <tr><td>Casas de empeño (Smash 'n' Grab)</td><td class="num">15</td><td>Capítulo 2, tras la misión "Coffee Break"</td><td>1,000 a 12,000 dólares</td></tr>
    <tr><td>Joyerías (Smash 'n' Grab)</td><td class="num">20</td><td>Capítulo 3, tras "Yasmani's Jewelry Jobs"</td><td>Hasta 25,000 dólares</td></tr>
    <tr><td>Prestamistas (Payday Loans)</td><td class="num">7</td><td>Capítulo 3, tras "Credit Check"</td><td>Hasta 25,000 dólares</td></tr>
    <tr><td>Bancos pequeños</td><td class="num">14</td><td>Capítulo 3, tras "Credit Check"</td><td>5,000 a 45,000 dólares</td></tr>
    <tr><td>Cámaras acorazadas de bancos grandes</td><td class="num">8</td><td>Final del Capítulo 4, tras la misión opcional "That's Where The Money Is…"</td><td>65,000 a 205,000 dólares</td></tr>
    <tr><td>Escondites de pandillas (Illegal Operations)</td><td class="num">39</td><td>Se van abriendo con la historia</td><td>Efectivo y droga para vender</td></tr>
  </tbody>
</table></div>
<p>Cada negocio tiene un nivel de seguridad (bajo, medio o alto) que se ve antes de entrar. Para el 100% no hace falta robarlos todos: según las guías bastan 50 de los 91 atracos a tiendas.</p>
{AD}

<h2>Cómo hacer un robo paso a paso</h2>
<ol>
  <li><strong>Revisa el sitio antes.</strong> Mira en el mapa el nivel de seguridad y localiza entradas, cámaras y guardias.</li>
  <li><strong>Controla a la gente.</strong> Amenaza al personal y apunta a los guardias armados hasta que suelten el arma. Amenazar no te baja la reputación criminal; la violencia innecesaria, sí.</li>
  <li><strong>Desactiva la alarma.</strong> Es un panel blanco, casi siempre en la trastienda; el modo Focus lo resalta. Si rompes las vitrinas antes de apagarla, puede saltar.</li>
  <li><strong>Saca el botín.</strong> En los bancos pequeños hay dos objetivos, la caja y la caja fuerte, y hay que vaciar los dos.</li>
  <li><strong>Borra las grabaciones.</strong> Las cámaras te graban aunque la policía no llegue al momento, y ese video sirve para identificarte. Rompe las cámaras o destruye la grabación. En los sitios de seguridad alta el video se guarda en la nube y no se puede borrar después.</li>
  <li><strong>Escapa y cámbiate.</strong> Al salir, cambia de ropa o de vehículo para que no te reconozcan.</li>
</ol>

<h2>Cajas fuertes, botín y dónde venderlo</h2>
<ul>
  <li><strong>No te fíes de las listas de códigos.</strong> En la mayoría de tiendas y bancos la combinación de la caja fuerte cambia en cada partida, así que una lista de internet no te sirve. Si no tienes el código, puedes forzarla, pero parte del botín sale dañado.</li>
  <li><strong>Snap Gun:</strong> se consigue en el Capítulo 3 y abre cerraduras sin que salte la alarma, así que puedes entrar por la puerta de atrás.</li>
  <li><strong>Billetes marcados:</strong> el dinero de los bancos puede traer paquetes de tinta. El <strong>Dye Pack Jammer</strong>, que se consigue en la misión "Credit Check" del Capítulo 3, sirve para no perder ese dinero.</li>
  <li><strong>El botín no es dinero todavía.</strong> Las joyas y los objetos van en una bolsa que puedes guardar en el maletero, y se convierten en efectivo al venderlos a un comprador ("fence"). Si te atrapan, puedes perder la bolsa.</li>
  <li><strong>Yasmani</strong> compra joyas y billetes marcados.</li>
  <li>El efectivo que llevas encima se pierde si te arrestan, así que deposítalo pronto. Más detalles en la <a href="guia-principiantes-gta-6.html">guía para empezar</a>.</li>
</ul>

<h2>Cámaras acorazadas: el robo que más paga</h2>
<p>Los ocho bancos grandes son la mejor fuente de dinero fuera de la historia. Así funcionan:</p>
<ol>
  <li>Termina los trabajos previos de Yasmani, incluido robar dos Payday Loans, y la misión opcional "That's Where The Money Is…" al final del Capítulo 4.</li>
  <li>Yasmani te vende el soplo de cada cámara por <strong>10,000 dólares</strong>.</li>
  <li>Sigue al <strong>camión blindado</strong> hasta el banco. La cámara solo se abre mientras el guardia mete el dinero: ese es el momento de entrar. No se puede abrir con ganzúa ni con explosivos.</li>
  <li>Al robarla te cae <strong>4 estrellas de búsqueda</strong> de golpe. Lleva una moto rápida para la huida y cambia de vehículo en cuanto puedas.</li>
</ol>
<p>Las que más pagan, hasta <strong>205,000 dólares</strong> cada una según los jugadores, son <strong>Lombank Downtown</strong> y <strong>Lombank Ocean Beach</strong>. Robar cinco cámaras y escapar da el trofeo de plata <strong>Maximum Withdrawal</strong> (lista completa en <a href="trofeos-logros-gta-6.html">trofeos y logros</a>).</p>
{AD}

<h2>Robar en pareja</h2>
<ul>
  <li>Hacer robos juntos sube la relación entre Jason y Lucia.</li>
  <li>Uno puede vigilar a los rehenes mientras el otro vacía la caja, y en la huida uno maneja y el otro dispara.</li>
</ul>

<h2>Los dos grandes golpes de la historia</h2>
<div class="note"><strong>Spoilers leves:</strong> solo nombres de misiones y lugares, nada del argumento. Estos golpes <strong>no se pueden repetir</strong>, así que prepáralos bien.</div>
<p>Además de muchos trabajos pequeños, la historia tiene <strong>dos golpes grandes</strong>, los dos planeados con <strong>Raul Bautista</strong>, al que conoces en las misiones "Car Service", "First Impressions" y "Credit Check".</p>
<div class="tbl"><table>
  <thead><tr><th>Golpe</th><th>Capítulo</th><th>Objetivo</th><th>Preparación</th></tr></thead>
  <tbody>
    <tr><td><strong>The Cartel Heist</strong></td><td>3</td><td>Sinfrontera National Bank</td><td>Security Expert, Heist Planning, Safe Word (practicar con una caja fuerte) e Hidden Charges (poner explosivos en torres de telefonía)</td></tr>
    <tr><td><strong>VCIA Takedown</strong></td><td>4</td><td>Aeropuerto Internacional de Vice City</td><td>Fully Catered y Heist Plans in Place</td></tr>
  </tbody>
</table></div>
<ul>
  <li><strong>The Cartel Heist:</strong> con las tres torres listas tienes casi <strong>11 minutos</strong> para el golpe final. Los jugadores reportan unos <strong>120,000 dólares</strong> de botín, aunque hay quien habla de 150,000. Completarlo da el trofeo <strong>Break the Bank</strong>.</li>
  <li><strong>VCIA Takedown:</strong> completarlo da el trofeo <strong>Hi-Jacked</strong>. El botín todavía no está claro.</li>
</ul>

<h2>Preguntas frecuentes</h2>
<dl class="faq">
  <dt>¿Cuál es el robo que más dinero da en GTA 6?</dt><dd>Las cámaras acorazadas de los bancos grandes, sobre todo Lombank Downtown y Lombank Ocean Beach, con hasta 205,000 dólares cada una según los jugadores. Se desbloquean al final del Capítulo 4.</dd>
  <dt>¿Cuándo se pueden robar bancos en GTA 6?</dt><dd>Los bancos pequeños, en el Capítulo 3 tras la misión "Credit Check". Las cámaras acorazadas, al final del Capítulo 4 tras "That's Where The Money Is…".</dd>
  <dt>¿Cuántos golpes tiene GTA 6?</dt><dd>Dos golpes grandes en la historia, The Cartel Heist y VCIA Takedown, más muchos trabajos pequeños y cientos de robos libres por el mapa.</dd>
  <dt>¿Hay códigos fijos para las cajas fuertes?</dt><dd>En la mayoría de tiendas y bancos no: la combinación cambia en cada partida. Si no la tienes, puedes forzar la caja, aunque parte del botín se daña.</dd>
  <dt>¿Se pueden repetir los golpes?</dt><dd>No. Ni los golpes ni las misiones de la historia se pueden repetir, así que no hay forma de farmear sus botines.</dd>
  <dt>¿Cómo evito que la policía me reconozca después de un robo?</dt><dd>Rompe las cámaras o borra la grabación antes de salir, y al escapar cambia de ropa o de vehículo.</dd>
</dl>
<p>¿Buscas atajos? Mira los <a href="trucos-gta-6.html">trucos de GTA 6</a>, aunque solo funcionan al terminar la historia.</p>
{AFF}"""


pages = {
    "robos-atracos-gta-6.html": (robos, "Robos y atracos de GTA 6: bancos, cámaras acorazadas y golpes | Leonida Global 305", "Cómo robar tiendas, joyerías y bancos en GTA 6, cuándo se desbloquea cada robo, cuánto pagan las cámaras acorazadas y los dos grandes golpes de la historia.", True),
    "trucos-gta-6.html": (trucos, "Trucos de GTA 6: todos los códigos para PS5 y Xbox | Leonida Global 305", "Los 61 trucos de GTA 6: cómo se desbloquean, cómo meter los códigos en PS5 y Xbox y los 18 códigos conocidos, incluido el de 250,000 dólares.", True),
    "guia-principiantes-gta-6.html": (principiantes, "Guía para empezar GTA 6: misiones del Capítulo 1 y dinero | Leonida Global 305", "Las 22 misiones del Capítulo 1 de GTA 6 en orden, cómo no perder tu dinero con BuckMe, RydeMe, Pay 'n' Spray y las primeras formas de ganar dinero.", True),
    "trofeos-logros-gta-6.html": (trofeos, "Trofeos y logros de GTA 6: lista completa de los 55 | Leonida Global 305", "Los 55 trofeos y logros de GTA 6: platino, oros, platas y bronces, cómo se consigue cada uno y los ocultos de la historia.", True),
    "notas-resenas-gta-6.html": (resenas, "Reseñas de GTA 6: notas de IGN, GameSpot y Metacritic | Leonida Global 305", "GTA 6 tiene un 99 en Metacritic. Las notas de IGN, GameSpot, Game Informer, Edge, Eurogamer y más, lo que gusta y lo que critica la prensa.", True),
    "revistas-gta-6.html": (revistas, "Las revistas de GTA 6: Edge, Game Informer, Dazed y más | Leonida Global 305", "Las ediciones de Edge, Game Informer, Dazed, TROISCOULEURS y LOVE dedicadas a GTA 6: fotos de los ejemplares, qué trae cada una y cómo conseguirlas.", True),
    "hora-de-salida-gta-6.html": (hora, "¿A qué hora sale GTA 6? Hora de desbloqueo por país | Leonida Global 305", "A qué hora se desbloquea GTA 6 el 19 de noviembre en España, México, Argentina, Colombia, EE.UU. y más países, según la PlayStation Store.", True),
    "trailers-gta-6.html": (trailers, "Todos los tráilers de GTA 6 y el Extended Look | Leonida Global 305", "Mira los tres tráilers oficiales de GTA 6 y el Extended Look de 27 minutos, con lo que muestra cada uno.", True),
    "musica-radios-gta-6.html": (musica, "Radios, canciones y música de GTA 6: The Album y Original Score | Leonida Global 305", "Las radios confirmadas de GTA 6 con sus locutores y canciones, GTA VI: The Album y el Original Score de Justice: fechas, formatos y precios.", True),
    "mapa-miami-real.html": (mapa_real, "Mapa de Vice City en el Miami real | Leonida Global 305", "Mapa interactivo con los lugares reales de Miami y Florida que aparecen en GTA 6 y todo el marketing de Vice City en la ciudad.", True),
    "equipo-gta-6.html": (equipo, "Equipo para GTA 6: teles, monitores y SSD | Leonida Global 305", "Las mejores teles, monitores, SSD y accesorios para jugar GTA 6, con opciones económicas y de gama alta.", True),
    "leaks-cyberleek.html": (leaks, "Leaks de GTA 6 de CyberLeek | Leonida Global 305", "Cronología de los leaks de GTA 6 de CyberLeek, qué detalles confirmó Rockstar después y cómo terminó la filtración.", True),
    "todo-lo-confirmado.html": (conf, "GTA 6: todo lo confirmado | Leonida Global 305", "Todos los detalles de GTA 6 confirmados por Rockstar a IGN, Famitsu, Game Informer, Dazed, LOVE, Bloomberg y en el Extended Look.", True),
    "index.html": (index, "GTA 6: guías, fecha, mapa y tráilers | Leonida Global 305", "Guías de GTA 6: fecha, precio, mapa de Leonida, personajes, música y Vice City en el Miami real.", False),
    "fecha-precio-ediciones.html": (fecha, "GTA 6: fecha, precio y ediciones | Leonida Global 305", "GTA 6 sale el 19 de noviembre de 2026. Precio de la edición estándar y Ultimate, precarga y qué incluye cada una.", True),
    "mapa-leonida.html": (mapa, "Mapa de GTA 6: regiones de Leonida | Leonida Global 305", "Las seis regiones confirmadas del mapa de GTA 6 y su inspiración real en Florida.", True),
    "personajes.html": (pers, "Personajes de GTA 6 | Leonida Global 305", "Jason Duval, Lucia Caminos y todos los personajes confirmados de GTA 6.", True),
}
# Medios consultados por página: se muestran como mención, sin enlace.
CREDITOS = {
    "robos-atracos-gta-6.html": ["Respawndex", "Timesaver", "ViceCityHQ", "HappyGamer", "MetaForge"],
    "trucos-gta-6.html": ["VICE", "Red Bull", "Beebom", "SVG", "Gamer Tweak"],
    "guia-principiantes-gta-6.html": ["Push Square", "VGC", "Kotaku", "GTABase", "NoobFeed", "Beebom", "GTA BOOM"],
    "trofeos-logros-gta-6.html": ["PC Gamer", "CULTR", "TechWiser", "Of Zen and Computing"],
    "notas-resenas-gta-6.html": ["Metacritic", "PC Gamer", "GAMINGbible", "Forbes", "Tom's Guide", "ABC7"],
    "fecha-precio-ediciones.html": ["Rockstar Games", "Take-Two Interactive", "Gfinity", "tbreak", "SVG", "GTA Intel", "GamesBeat", "Insider Gaming", "GTA BOOM", "Digit", "Kotaku", "Notebookcheck", "RockstarINTEL", "Yahoo Finance", "Xbox Wire", "PlayStation Blog", "GamesRadar+", "Sensor Tower", "NewsCase"],
    "mapa-leonida.html": ["Rockstar Games", "LOVE", "Beebom", "All Things How"],
    "personajes.html": ["Rockstar Games", "TechRadar", "PC Gamer", "Dazed", "LOVE", "Associated Press", "Push Square"],
    "todo-lo-confirmado.html": ["IGN", "Famitsu", "Kinda Funny", "Game Informer", "Dazed", "LOVE", "Bloomberg (Jason Schreier)", "PC Gamer", "Kotaku", "Insider Gaming", "GTAVice.net", "iGrandTheftAuto", "Inven Global", "Edge", "GamesRadar+", "Beebom", "GTA BOOM", "Dexerto", "VICE", "TweakTown", "Yahoo Finance", "Forbes", "Xbox Wire", "PlayStation Blog", "VGC", "VideoGamer", "Gematsu", "The New York Times", "Notebookcheck", "Tech4Gamers", "2K", "Beebom", "ComicBook.com"],
    "leaks-cyberleek.html": ["Dexerto", "iGeeksBlog", "Tech Insider", "BBC"],
    "equipo-gta-6.html": ["RTINGS", "TechRadar", "GamesRadar", "Windows Central", "Turtle Beach", "PC Gamer", "PlayStation Blog", "Kotaku", "Insider Gaming", "Game Informer", "VGC"],
    "musica-radios-gta-6.html": ["Rockstar Games", "Forbes", "Kotaku", "Consequence", "G2A News", "Insider Gaming", "Stereogum", "VICE", "VGC", "Revolt", "Beebom", "VideoGamer", "NME", "Dexerto", "GamesRadar+"],
    "trailers-gta-6.html": ["Rockstar Games", "Insider Gaming", "Pure Xbox", "VICE", "Wikipedia", "VideoGamer"],
    "hora-de-salida-gta-6.html": ["PlayStation Store", "GTA BOOM", "Inven Global", "MP1st", "All Things How", "Kotaku", "Insider Gaming", "Xbox Wire", "YouTube", "Notebookcheck", "Streams Charts", "VICE", "tbreak", "VGTimes", "SourceVI"],
    "revistas-gta-6.html": ["Edge", "GamesRadar+", "Game Informer", "Dazed", "TROISCOULEURS", "mk2", "LOVE", "GTA Intel", "Beebom", "GTAVice.net"],
    "mapa-miami-real.html": ["GTA BOOM", "Miami New Times", "Kotaku", "VGC", "GamesRadar", "Portal Viciados y @samchrme", "GTAVice.net", "Beebom", "Dexerto", "Sole Retriever", "Condado de Miami-Dade", "WLRN", "RockstarINTEL", "Forbes"],
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
