# -*- coding: utf-8 -*-
"""
Seema · سيمة — static site builder.

    python3 src/build.py              -> dist/            (production: seema.qa)
    python3 src/build.py --artifact   -> dist-artifact/   (preview build)

English pages live at the root, Arabic pages in /ar/ with the same file names.
All copy lives in content.py. Components below are plain functions returning HTML.
"""
import html, json, os, re, shutil, sys
from PIL import Image

from content import (SITE, UI, NAV, FOOTER, SERVICES, PROCESS, PRINCIPLES, AUDIENCE,
                     PROJECTS, WORK_FILTERS, TOPICS, ARTICLES, L)
from content_v6 import SVC_V6, PROC_PHOTOS, PROC_WORDS
from editions import (initial, tear, rail, opener, collage, numeral, mk_browser, mk_phone, mk_identity,
                      mk_note, mk_dash, mk_post, mk_ticket, mk_chip)

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
ARTIFACT = "--artifact" in sys.argv
OUT = os.path.join(ROOT, "dist-artifact" if ARTIFACT else "dist")
HOME = "home.html" if ARTIFACT else "index.html"
FONTS = ("https://fonts.googleapis.com/css2?family=El+Messiri:wght@400;500;600;700"
         "&family=JetBrains+Mono:wght@400&family=Manrope:wght@200;300;400;500;600;700;800"
         "&family=Tajawal:wght@300;400;500;700&display=swap")

esc = html.escape
AR_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")


def num(n, lang, width=2):
    s = str(n).zfill(width)
    return s.translate(AR_DIGITS) if lang == "ar" else s


def other(lang):
    return "ar" if lang == "en" else "en"


# ------------------------------------------------------------------ assets
def svg_file(name):
    return open(os.path.join(SRC, "assets", "brand", name), encoding="utf-8").read()


def logo_svg(name, label, cls=""):
    """Inline a logo SVG: Indigo/Cloud paths take currentColor, Saffron points get class 'pts'."""
    s = svg_file(name)
    s = re.sub(r'\swidth="[\d.]+"\sheight="[\d.]+"', "", s, count=1)
    s = re.sub(r'fill="#(1B1847|F7F5F0|F4F2EC|F5F3EE)"', 'fill="currentColor"', s, flags=re.I)
    s = s.replace('fill="#E87722"', 'fill="#E87722" class="pts"')
    s = s.replace("<svg ", f'<svg role="img" aria-label="{esc(label)}" class="{cls}" ', 1)
    return s


def icon_svg(key):
    s = open(os.path.join(SRC, "assets", "icons", f"Seema_icon_{key}_indigo.svg"), encoding="utf-8").read()
    s = s.replace('stroke="#1B1847"', 'stroke="currentColor"')
    s = re.sub(r'\sheight="24"\swidth="24"', "", s)
    return s.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)


PT_PATH = ("M72 29 129-84Q134-92 129-97.5 124-103 117-101 72-92 26.5-83.5-19-75-66-67-68-66-71-64.5-74-63-75-61"
           "L-131 53Q-135 60-130.5 65.5-126 71-119 70-73 62-27.5 53 18 44 64 36 70 33 72 29Z")


def pt(cls=""):
    return f'<svg class="pt {cls}" viewBox="-136 -104 272 176" aria-hidden="true" focusable="false"><path d="{PT_PATH}"/></svg>'


ARR = ('<svg class="arr" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
       'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
GLOBE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
         'aria-hidden="true"><circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19M12 2.5c2.6 2.8 3.9 6 3.9 9.5S14.6 18.7 12 21.5M12 2.5C9.4 5.3 8.1 8.5 8.1 12s1.3 6.7 3.9 9.5"/></svg>')

ARR_LONG = ('<svg class="arr" viewBox="0 0 36 24" fill="none" stroke="currentColor" stroke-width="1.2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12h31M26 5l7 7-7 7"/></svg>')

IMG_DIMS = {}
for f in os.listdir(os.path.join(SRC, "assets", "img")):
    if f.endswith(".jpg"):
        with Image.open(os.path.join(SRC, "assets", "img", f)) as im:
            IMG_DIMS[f[:-4]] = im.size

ALT = {
    "sv-hero-dhow": L("A traditional dhow flying the Qatari flag, with the West Bay towers behind", "مركب تقليدي يرفع علم قطر، وتظهر أبراج الخليج الغربي خلفه"),
    "sv-consult": L("A Qatari professional reviewing a strategy document with phone and laptop", "مهني قطري يراجع وثيقة استراتيجية مع الهاتف والحاسوب"),
    "sv-brand": L("Arabic calligraphy on a contemporary building façade", "خط عربي على واجهة مبنى معاصر"),
    "sv-web": L("A developer in a hijab writing code on a laptop", "مطوّرة ترتدي الحجاب تكتب شيفرة على حاسوبها"),
    "sv-mobile": L("A man in a white ghutra on his phone in Doha", "رجل بالغترة البيضاء يتحدث على هاتفه في الدوحة"),
    "sv-systems": L("Reviewing reports on a phone and laptop at a meeting table", "مراجعة التقارير على الهاتف والحاسوب في اجتماع"),
    "sv-marketing": L("People walking through Msheireb Downtown Doha", "أشخاص يسيرون في مشيرب قلب الدوحة"),
    "sv-support": L("Network equipment and cabling in a server room", "معدات شبكات وكابلات في غرفة خوادم"),
    "sv-msheireb-office": L("Contemporary offices in Msheireb, Doha", "مكاتب معاصرة في مشيرب، الدوحة"),
    "sv-library": L("The Qatar National Library, Education City", "مكتبة قطر الوطنية، المدينة التعليمية"),
    "hero-souq-night": L("Souq Waqif lit up at night, Doha", "سوق واقف مضاءً ليلاً، الدوحة"),
    "svc-majlis": L("Men in ghutras gathered in conversation in a majlis", "رجال بالغتر يتحاورون في مجلس"),
    "svc-pattern": L("A golden Islamic geometric pattern", "زخرفة هندسية إسلامية ذهبية"),
    "svc-facade": L("A modern building with a geometric lattice façade", "مبنى حديث بواجهة من الزخارف الهندسية"),
    "svc-abaya-phone": L("A woman in an abaya using her phone among the city lights", "امرأة بالعباءة تستخدم هاتفها بين أضواء المدينة"),
    "svc-msheireb": L("Contemporary Qatari architecture in Msheireb, Doha", "عمارة قطرية معاصرة في مشيرب، الدوحة"),
    "svc-souq-stall": L("Shoppers at a lit stall in Souq Waqif", "متسوّقون أمام دكان مضاء في سوق واقف"),
    "svc-souq-lamps": L("Warm lamps along a passage in Souq Waqif", "مصابيح دافئة على امتداد ممر في سوق واقف"),
    "cs-majlis-coffee": L("Arabic coffee on a sadu rug in a majlis", "فنجان قهوة عربية على سجادة سدو في مجلس"),
    "cs-dallah-set": L("A brass dallah and coffee cups", "دلة نحاسية وفناجين قهوة"),
    "cs-qahwa": L("Arabic coffee poured into small cups", "قهوة عربية تُصب في فناجين صغيرة"),
    "cs-courtyard-water": L("A calm courtyard of arches and water", "فناء هادئ من الأقواس والماء"),
    "cs-courtyard": L("A traditional arcade with palm trees", "رواق تقليدي تحفّه أشجار النخيل"),
    "cs-dhows-fanar": L("Dhows on Doha Bay with the Fanar behind", "مراكب شراعية في خليج الدوحة ويظهر الفنار خلفها"),
    "cs-dhows-line": L("Traditional dhows moored in a row", "مراكب تقليدية راسية في صف"),
    "cs-mia-night": L("The Museum of Islamic Art at night", "متحف الفن الإسلامي ليلاً"),
    "cs-spreadsheet": L("A spreadsheet open on a laptop in an office", "جدول بيانات مفتوح على حاسوب في مكتب"),
    "cs-calligraphy": L("Hands writing Arabic calligraphy with a reed pen", "يدان تكتبان الخط العربي بقلم القصب"),
    "people-souq-square": L("A man in a white thobe crossing Souq Waqif square", "رجل بالثوب الأبيض يعبر ساحة سوق واقف"),
    "qa-ghutra": L("A man adjusting a white ghutra", "رجل يعدّل غترته البيضاء"),
    "qa-katara-towers": L("The pigeon towers of Katara Cultural Village", "أبراج الحمام في الحي الثقافي كتارا"),
    "qa-mia-arches": L("The Museum of Islamic Art, Doha", "متحف الفن الإسلامي، الدوحة"),
    "hero-lattice-figure": L("A man standing in the half-light of a lattice window", "رجل يقف في الضوء الخافت أمام نافذة مشربية"),
    "arches-shadow-walk": L("A figure walking through long shadows cast by arches", "شخص يسير بين ظلال طويلة ترسمها الأقواس"),
    "lattice-arch": L("Sunlight through a geometric lattice arch", "ضوء الشمس عبر قوس من الزخارف الهندسية"),
    "lattice-dark": L("A lattice window glowing in a dark hall", "نافذة مشربية مضيئة في قاعة معتمة"),
    "lattice-gold": L("Golden light through a carved lattice screen", "ضوء ذهبي عبر مشربية منحوتة"),
    "hand-shadow": L("The shadow of a hand on a warm, sunlit wall", "ظل يد على جدار دافئ يغمره الضوء"),
    "corridor-glow": L("A corridor of arches lit with warm light", "ممر من الأقواس يضيئه نور دافئ"),
    "stone-gold": L("Close-up of golden stone", "لقطة قريبة لحجر ذهبي"),
    "columns-gold": L("Stone columns in raking light", "أعمدة حجرية في ضوء مائل"),
    "fort-arches": L("A traditional Gulf interior with arched windows and a timber ceiling", "مجلس خليجي تقليدي بنوافذ مقوّسة وسقف خشبي"),
    "edu-city-oval": L("Contemporary architecture in Education City, Doha", "عمارة معاصرة في المدينة التعليمية، الدوحة"),
    "mia-window": L("A tall glass wall looking out over the water in Doha", "واجهة زجاجية شاهقة تطل على البحر في الدوحة"),
    "nmoq-interior": L("Interlocking discs inside the National Museum of Qatar", "الأقراص المتشابكة داخل متحف قطر الوطني"),
    "portrait-man-dark": L("Portrait of a man in low, warm light", "صورة لرجل في إضاءة خافتة دافئة"),
    "portrait-man-indigo": L("Portrait of a bearded man in deep shadow", "صورة لرجل ملتحٍ في ظل عميق"),
    "portrait-profile": L("A man in profile against a dark background", "رجل من الجانب على خلفية داكنة"),
    "portrait-woman": L("Portrait of a woman wearing a white headscarf", "صورة لامرأة ترتدي غطاء رأس أبيض"),
    "portrait-woman-dark": L("Portrait of a woman in a patterned headscarf", "صورة لامرأة بغطاء رأس مزخرف"),
    "pen-ink": L("A dip pen writing in ink", "ريشة تكتب بالحبر"),
    "ink-pen-minimal": L("An ink bottle and dip pen on a pale surface", "محبرة وريشة على سطح فاتح"),
    "interior-curve": L("A curved interior with warm lighting", "فضاء داخلي منحنٍ بإضاءة دافئة"),
    "palm-shutter": L("Palm shadows on a sunlit wall beside a wooden shutter", "ظلال النخيل على جدار مشمس بجوار نافذة خشبية"),
    "lattice-dome": L("A lattice dome seen from below", "قبة مزخرفة من الأسفل"),
    "dallah-brass": L("Brass dallah coffee pots in low light", "دلال قهوة نحاسية في ضوء خافت"),
    "concrete-light": L("Light falling across a concrete wall", "ضوء يسقط على جدار خرساني"),
    "linen": L("Folds of undyed linen", "طيّات من الكتان الطبيعي"),
    "airport-arch": L("A vast arched hall in Doha", "قاعة مقوّسة واسعة في الدوحة"),
    "lounge-dark": L("A quiet, dark hall with a wall of light", "قاعة هادئة معتمة تقابلها واجهة من الضوء"),
}


def qalam_clip():
    """The Saffron Point's own outline, normalised for clipPathUnits=objectBoundingBox."""
    toks = re.findall(r"[MQLZ]|-?\d+(?:\.\d+)?", PT_PATH)
    out, nums = [], []
    for tk in toks:
        if tk in "MQLZ":
            out.append(tk)
        else:
            nums.append(float(tk))
            if len(nums) == 2:
                out.append(f"{(nums[0] + 136) / 272:.4f} {(nums[1] + 104) / 176:.4f}")
                nums = []
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>'
            f'<clipPath id="qalam" clipPathUnits="objectBoundingBox"><path d="{" ".join(out)}"/></clipPath></defs></svg>')


QALAM = qalam_clip()


class Page:
    def __init__(self, lang, file, key):
        self.lang, self.file, self.key = lang, file, key
        self.P = "../" if lang == "ar" else ""
        self.ol = "ar" if lang == "en" else "en"

    def t(self, d):
        return d[self.lang] if isinstance(d, dict) else d

    def o(self, d):
        return d[self.ol]

    def href(self, file):
        return HOME if file == "index.html" else file

    def alt_href(self):
        f = self.href(self.file)
        return ("ar/" + f) if self.lang == "en" else ("../" + f)

    def asset(self, path):
        return self.P + "assets/" + path

    def img(self, name, sizes="100vw", eager=False):
        w, h = IMG_DIMS[name]
        sw, _ = IMG_DIMS[name + "-sm"]
        a = self.t(ALT.get(name, L("", "")))
        load = 'fetchpriority="high"' if eager else 'loading="lazy"'
        return (f'<img src="{self.asset("img/" + name + ".jpg")}" srcset="{self.asset("img/" + name + "-sm.jpg")} {sw}w, '
                f'{self.asset("img/" + name + ".jpg")} {w}w" sizes="{sizes}" width="{w}" height="{h}" alt="{esc(a)}" {load} decoding="async">')


# ------------------------------------------------------------------ small components
def lines(*parts):
    return "".join(f'<span class="ln"><span>{x}</span></span>' for x in parts)


def words(text):
    return " ".join(f'<span class="w">{w}</span>' for w in text.split(" "))


def btn(text, href, cls=""):
    return f'<a class="btn {cls}" href="{href}">{pt()}<span>{esc(text)}</span></a>'


def lnk(text, href):
    return f'<a class="lnk" href="{href}"><span>{esc(text)}</span>{ARR_LONG}</a>'


def kick(p, idx, en, ar):
    return f'<p class="kick"><span class="idx">{idx}</span><span class="cap">{esc(en if p.lang == "en" else ar)}</span></p>'


def head(p, title, desc, og):
    lang, dirn, f = p.lang, ("rtl" if p.lang == "ar" else "ltr"), p.file
    en_url = SITE["domain"] + "/" + ("" if f == "index.html" else f)
    ar_url = SITE["domain"] + "/ar/" + ("" if f == "index.html" else f)
    canon = en_url if lang == "en" else ar_url
    full = title if p.key == "home" else f"{title} · {p.t(UI['home_title_suffix'])}"
    return f"""<!doctype html>
<html lang="{lang}" dir="{dirn}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ar" href="{ar_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Seema · سيمة">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE['domain']}/assets/img/{og}.jpg">
<meta property="og:locale" content="{'ar_QA' if lang == 'ar' else 'en_QA'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B1847">
<link rel="icon" href="{p.asset('brand/fav/favicon.ico')}" sizes="any">
<link rel="icon" href="{p.asset('brand/Seema_mark_inktile.svg')}" type="image/svg+xml">
<link rel="icon" href="{p.asset('brand/fav/favicon-32.png')}" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{p.asset('brand/fav/apple-touch-icon.png')}">
<link rel="manifest" href="{p.asset('site.webmanifest')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{p.asset('css/seema.css')}">
<script>document.documentElement.classList.add('js');if('scrollRestoration' in history)history.scrollRestoration='manual';</script>
</head>
<body>
"""


def header(p):
    t = p.t
    nav = []
    for key, label in NAV:
        f = p.href("index.html" if key == "home" else key + ".html")
        cur = ' aria-current="page"' if key == p.key else ""
        nav.append(f'<a href="{f}"{cur}>{pt() if key == p.key else ""}{esc(t(label))}</a>')
    mitems = "".join(
        f'<li><a href="{p.href("index.html" if k == "home" else k + ".html")}"{" aria-current=\"page\"" if k == p.key else ""}>'
        f'<span class="idx">{num(i + 1, p.lang)}</span><span>{esc(t(lab))}</span></a></li>' for i, (k, lab) in enumerate(NAV))
    ol = p.ol
    lang = (f'<a class="lang" href="{p.alt_href()}" hreflang="{ol}" lang="{ol}" aria-label="{esc(t(UI["lang_label"]))}">'
            f'<span class="bi-{ol}">{esc(t(UI["lang_other"]))}</span></a>')
    return f"""{QALAM}<a class="skip" href="#main">{esc(t(UI['skip']))}</a>
<header class="hd">
  <div class="wrap">
    <a class="brand" href="{p.href('index.html')}" aria-label="Seema · سيمة">{logo_svg("Seema_horiz_bone.svg", "Seema · سيمة")}</a>
    <nav class="nav" aria-label="{'Main' if p.lang == 'en' else 'القائمة الرئيسية'}">{''.join(nav)}</nav>
    <div class="hd-act">{lang}{btn(t(UI['start']), p.href('contact.html'))}
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu"><span>{esc(t(UI['menu']))}</span><i aria-hidden="true"></i></button>
    </div>
  </div>
</header>
<div class="menu" id="menu" aria-hidden="true" role="dialog" aria-modal="true" aria-label="{esc(t(UI['menu']))}">
  <div class="menu-top"><span class="brand">{logo_svg("Seema_horiz_bone.svg", "Seema · سيمة")}</span>
    <button class="menu-btn menu-close" type="button" style="display:inline-flex" aria-label="{esc(t(UI['close']))}"><span>{esc(t(L('Close', 'إغلاق')))}</span></button></div>
  <nav aria-label="{esc(t(UI['menu']))}"><ul>{mitems}</ul></nav>
  <div class="menu-foot">{btn(t(UI['start']), p.href('contact.html'))}{lang}
    <p class="cap">{SITE['email']} · {esc(t(SITE['city']))}</p></div>
</div>
"""


def cta(p):
    t = p.t
    return f"""
<section class="sec dark cta" data-tone="dark" aria-labelledby="cta-h">
  <div class="wrap">
    {kick(p, "—", "Start a project", "ابدأ مشروعك")}
    <h2 class="t-hero mt3 lines" id="cta-h">{lines(*t(L(["Let’s find", "your point" + pt()], ["لنجد", "نقطتك" + pt()])))}</h2>
    <div class="cta-row">
      <p class="mail" dir="ltr">{SITE['email']}</p>
      <div class="acts">{btn(t(UI['start']), p.href('contact.html'), 'btn--solid')}<button class="copy-btn" type="button" data-copy="{SITE['email']}" data-done="{esc(t(UI['copied']))}">{esc(t(L('Copy email', 'نسخ البريد')))}</button></div>
    </div>
  </div>
</section>"""


def footer(p):
    t = p.t
    ol = p.ol
    studio = "".join(f'<a href="{p.href("index.html" if k == "home" else k + ".html")}">{esc(t(lab))}</a>' for k, lab in NAV)
    svcs = "".join(f'<a href="{p.href("service-" + s["id"] + ".html")}">{esc(t(s["name"]))}</a>' for s in SERVICES)
    return f"""
<footer class="ft dark2" data-tone="dark">
  <div class="wrap">
    <div class="ft-top">
      <div class="ft-tag"><p class="t-m">{esc(t(SITE['tagline']))}</p><p class="voice" lang="{ol}">{esc(p.o(SITE['tagline']))}</p></div>
      <div class="ft-col"><p class="cap">{esc(t(FOOTER['studio']))}</p>{studio}</div>
      <div class="ft-col"><p class="cap">{esc(t(FOOTER['services']))}</p>{svcs}</div>
      <div class="ft-col"><p class="cap">{esc(t(FOOTER['contact']))}</p><span dir="ltr">{SITE['email']}</span><span>{SITE['web']}</span><span>{esc(t(SITE['city']))}</span>
        <a class="lang" href="{p.alt_href()}" hreflang="{ol}" lang="{ol}"><span class="bi-{ol}">{esc(t(UI['lang_other']))}</span></a></div>
    </div>
    <div class="ft-mark" aria-hidden="true"><span class="lat">{logo_svg("Seema_lat_bone.svg", "SEEMA")}</span><span class="ar">{logo_svg("Seema_ar_bone.svg", "سيمة")}</span></div>
    <div class="ft-bottom">
      <span>{esc(SITE['registered']['en'])}</span><span class="bi-ar" lang="ar">{esc(SITE['registered']['ar'])}</span>
      <span>{esc(t(FOOTER['rights']))}</span>
    </div>
    <p class="ft-bottom" style="border:0;padding-top:.6rem">{esc(t(FOOTER['photo']))}</p>
  </div>
</footer>
<script src="{p.asset('js/seema.js')}" defer></script>
</body>
</html>
"""


def page(p, title, desc, body, og="hero-souq-night", with_cta=True):
    return head(p, title, desc, og) + header(p) + f'<main id="main">{body}{cta(p) if with_cta else ""}</main>' + footer(p)


def steps(p, tone="light", idx="04", chapter=None, top="", bot=""):
    t = p.t
    n = len(PROCESS)
    bgs = "".join(f'<div class="proc-bg{" is-on" if k == 0 else ""}" data-k="{k}">{p.img(PROC_PHOTOS[k], "100vw")}</div>' for k in range(n))
    words_ = "".join(f'<span class="proc-word{" is-on" if k == 0 else ""}" data-k="{k}" aria-hidden="true">{esc(t(PROC_WORDS[k]))}</span>' for k in range(n))
    items = "".join(f'<li class="proc-it{" is-on" if k == 0 else ""}" data-k="{k}"><i class="bar"><b></b></i><span class="n">{num(k + 1, "en")}</span>'
                    f'<h3>{esc(t(a))}</h3><p>{esc(t(b))}</p></li>' for k, (a, b) in enumerate(PROCESS))
    return f"""
<section class="proc"{f' id="{chapter}" data-chapter="{chapter}"' if chapter else ''} data-tone="dark" aria-labelledby="how-h" style="--n:{n}">
  <div class="proc-stage">
    {bgs}
    <div class="proc-type wrap">
      <div class="proc-head">
        {kick(p, idx, "Approach", "منهجنا")}
        <h2 class="proc-title" id="how-h">{esc(t(L("From the first conversation to a mark that lasts.", "من الحديث الأول إلى علامة تبقى.")))}</h2>
        <p class="proc-count idx" aria-hidden="true"><span class="cur">01</span> / {num(n, "en")}</p>
      </div>
      <div class="proc-words">{words_}</div>
      <ol class="proc-list">{items}</ol>
    </div>
  </div>
</section>"""


def placeholder_note(p):
    return f'<p class="note-ph">{pt()}<span>{esc(p.t(L("Placeholder projects: they show how Seema case studies will be presented and will be replaced with real, client-approved work.", "مشاريع توضيحية تبيّن طريقة عرض دراسات الحالة، وستُستبدل بأعمال حقيقية بعد موافقة العملاء.")))}</span></p>'


# ------------------------------------------------------------------ HOME
def home(p):
    t = p.t
    ol = p.ol
    if p.lang == "en":
        w1, w2 = "Every brand", f'has its <span class="em">seema</span>{pt()}'
    else:
        w1, w2 = "لكل علامة", f'<span class="em">سمتها</span>{pt()}'
    rows = "".join(f"""<li><a class="svc-row" href="{p.href('service-' + s['id'] + '.html')}" data-peek="{s['id']}">
  <span class="idx">{num(i + 1, "en")}</span><span class="nm">{esc(t(s['name']))}</span>
  <span class="meta"><span class="cap">{esc(t(s['outcome']))}</span><span class="oth bi-{ol}" lang="{ol}">{esc(p.o(s['name']))}</span></span>
</a></li>""" for i, s in enumerate(SERVICES))
    peeks = "".join(f'<img data-id="{s["id"]}" src="{p.asset("img/" + s["peek"] + "-sm.jpg")}" alt="" loading="lazy">' for s in SERVICES)
    cards = "".join(f"""<article class="card" data-tone="dark">
  <div class="ph">{p.img(pr['cover'], '100vw')}</div>
  <a class="cin wrap" href="{p.href('case-' + pr['slug'] + '.html')}" data-cursor="{esc(t(L('View', 'شاهد')))}">
    <div class="top"><span class="idx">{num(i + 1, 'en')} / {num(len(PROJECTS[:4]), 'en')}</span><span class="cap tag">{esc(t(UI['placeholder']))}</span></div>
    <span></span>
    <div class="bottom">
      <h3 class="t-xl">{esc(t(pr['title']))}</h3>
      <div class="aside"><span class="cap">{esc(t(pr['sector']))}</span><span>{esc(t(pr['services']))}</span><span class="lnk"><span>{esc(t(UI['view_case']))}</span>{ARR_LONG}</span></div>
    </div>
  </a>
</article>""" for i, pr in enumerate(PROJECTS[:4]))
    topics = dict(TOPICS)
    arts = [a for a in ARTICLES if a.get("slug")]
    ins = "".join(f"""<a class="ins rv" href="{p.href('insight-' + a['slug'] + '.html')}" data-cursor="{esc(t(UI['read']))}">
  <div class="ph">{p.img(a['photo'], '(max-width: 820px) 30vw, 16vw')}</div>
  <div><h3>{esc(t(a['title']))}</h3><p class="dek">{esc(t(a['dek']))}</p></div>
  <div class="meta"><span class="cap">{esc(t(topics[a['topic']]))}</span><span class="idx">{num(a['minutes'], p.lang, 1)} {esc(t(UI['min']))}</span></div>
</a>""" for a in arts)
    svc_opener = opener(
        p, "services", 1, p.img('svc-majlis', '100vw'),
        t(L("Services", "خدماتنا")), t(L("Seven disciplines, one point of view, from the first question to the systems that keep you running.", "سبع خدمات ورؤية واحدة، من السؤال الأول حتى الأنظمة التي تُبقي عملك مستمراً.")),
        p.o(L("Services", "خدماتنا")), heading_id="svc-op-h",
        collage_html=collage([
            (mk_browser(p, 'cs-majlis-coffee'), 47, 39, "28vw", 1.0, -2),
            (mk_phone(p, 'cs-qahwa'), 80, 42, "11vw", 1.5, 3),
            (mk_identity(p), 64, 64, "15vw", .7, -4),
            (mk_chip(p, L("Find the point", "اعثر على النقطة"), pt()), 50, 88, "auto", 1.2, 0),
        ]))
    work_opener = opener(
        p, "work", 3, p.img('svc-souq-lamps', '100vw'),
        t(L("Work", "أعمالنا")), t(L("Work that makes the difference, for hospitality, health, trade and culture.", "أعمال تصنع الفرق، في الضيافة والصحة والتجارة والثقافة.")),
        p.o(L("Work", "أعمالنا")), heading_id="work-h",
        extra=f'<div class="op-aside">{placeholder_note(p)}{lnk(t(UI["all_work"]), p.href("work.html"))}</div>')
    home_rail = rail(p, [("studio", L("Studio", "الاستوديو")), ("services", L("Services", "الخدمات")), ("belief", L("Belief", "فلسفتنا")),
                         ("work", L("Work", "الأعمال")), ("approach", L("Approach", "المنهج")), ("insights", L("Insights", "رؤى"))])
    manifesto = t(L("We help ambitious businesses in Qatar and the Gulf find what makes them different, then make it impossible to miss: in strategy, in identity and online.",
                    "نساعد الشركات الطموحة في قطر والخليج على اكتشاف ما يميّزها، ثم نجعل هذا التميّز واضحاً لا يمكن تجاهله: في الاستراتيجية، وفي الهوية، وفي الحضور الرقمي."))
    body = home_rail + f"""
<section class="hero" data-tone="dark" aria-labelledby="hero-h">
  <div class="hero-stage">
    <div class="hero-win">{p.img('hero-souq-night', '100vw', eager=True)}</div>
    <div class="hero-type">
      <div class="hero-top"><span class="cap">{esc(t(SITE['city']))}</span><span class="cap">{esc(t(L("Strategy · Identity · Digital", "استراتيجية · هوية · حلول رقمية")))}</span><span class="cap">{esc(t(L("Est. 2026", "تأسست ٢٠٢٦")))}</span></div>
      <h1 class="hero-words t-hero" id="hero-h"><span class="w1">{lines(w1)}</span><span class="w2">{lines(w2)}</span></h1>
      <div class="hero-foot">
        <p class="lead">{esc(t(L("A Doha consultancy for strategy, identity and digital, for businesses that intend to lead.", "شركة استشارات في الدوحة للاستراتيجية والهوية والحلول الرقمية، للأعمال التي تنوي أن تقود.")))}</p>
        <p class="voice" lang="{ol}">{esc(p.o(SITE['tagline']).rstrip('.'))}</p>
        <p class="scroll"><span class="cap">{esc(t(L("Scroll", "مرّر")))}</span><i aria-hidden="true"></i></p>
      </div>
    </div>
    <div class="hero-after" aria-hidden="true"><div class="wrap">
      <p class="t-l">{esc(t(L("Strategy, identity and digital, built around the one thing that makes you different.", "استراتيجية وهوية وحلول رقمية، تُبنى حول الشيء الوحيد الذي يميّزك.")))}</p>
      <p class="cap">{esc(t(SITE['tagline']).rstrip('.'))}</p>
    </div></div>
  </div>
</section>

<section class="sec light manifesto" id="studio" data-chapter="studio" data-tone="light" aria-label="{esc(t(L('Who we are', 'من نحن')))}">
  <div class="wrap g12">
    <div class="side"><span class="idx">01</span><span class="cap">{esc(t(L("Who we are", "من نحن")))}</span></div>
    <p class="text t-l words">{words(esc(manifesto))}</p>
    <div class="manifesto-media">
      <figure class="ph reveal-img">{p.img('qa-ghutra', '(max-width: 820px) 50vw, 28vw')}</figure>
      <figure class="ph reveal-img" data-delay="150">{p.img('cs-qahwa', '(max-width: 820px) 50vw, 24vw')}</figure>
      <div class="note rv"><p class="lead">{esc(t(L("Senior people, working in Arabic and English, from the first question to the systems that keep a business running.", "فريق من ذوي الخبرة، يعمل بالعربية والإنجليزية، من السؤال الأول حتى الأنظمة التي تُبقي العمل مستمراً.")))}</p>{lnk(t(L("About Seema", "عن سيمة")), p.href('about.html'))}</div>
    </div>
  </div>
</section>

{svc_opener}
<section class="sec light" data-chapter="services" data-tone="light" aria-labelledby="svc-h"><div class="wrap">
    <div class="sec-head">
      {kick(p, "02", "Capabilities", "خدماتنا")}
      <h2 class="t-xl lines" id="svc-h">{lines(*t(L(["Seven disciplines.", "One point of view."], ["سبع خدمات.", "ورؤية واحدة."])))}</h2>
      <div class="aside"><p class="body">{esc(t(L("Three core practices and four supporting services. Each has a clear outcome, so you buy a result, not a list of deliverables.", "ثلاث ممارسات أساسية وأربع خدمات داعمة. لكل منها نتيجة واضحة، فتشتري نتيجة لا قائمة مخرجات.")))}</p>{lnk(t(L("All services", "كل الخدمات")), p.href('services.html'))}</div>
    </div>
    <ul class="svc-list">{rows}</ul>
  </div>
  <div class="svc-peek qw" aria-hidden="true">{peeks}</div>
</section>

<section class="break" id="belief" data-chapter="belief" data-tone="dark" aria-labelledby="bel-h">
  <div class="ph par">{p.img('corridor-glow', '100vw')}</div>
  <div class="wrap">
    <h2 class="t-giant lines" id="bel-h">{lines(*t(L(["Define,", "don’t decorate."], ["نُعرِّف،", "لا نُزخرِف."])))}</h2>
    <div class="side"><p class="voice" lang="{ol}">{esc(p.o(L("Define, don’t decorate.", "نُعرِّف، لا نُزخرِف.")))}</p><p>{esc(t(L("Our philosophy. Every choice we make has to earn its place.", "فلسفتنا: كل قرار نتخذه يجب أن يستحق مكانه.")))}</p></div>
  </div>
</section>

{work_opener}
<section class="dark" data-chapter="work" data-tone="dark" aria-label="{esc(t(L('Selected work', 'أعمال مختارة')))}">
  <div class="stack-cards">{cards}</div>
</section>

<section class="bloom" data-tone="dark" aria-labelledby="bloom-h">
  <div class="bloom-stage">
    <div class="bloom-field"></div>
    {pt('bloom-pt')}
    <p class="bloom-pre cap" aria-hidden="true">{esc(t(L("One point changes everything", "نقطة واحدة تغيّر كل شيء")))}</p>
    <div class="bloom-copy"><h2 class="t-giant" id="bloom-h">{esc(t(SITE['tagline']))}</h2><p class="voice" lang="{ol}">{esc(p.o(SITE['tagline']))}</p></div>
  </div>
</section>

{steps(p, 'light', '04', chapter='approach')}

<section class="sec dark2" id="insights" data-chapter="insights" data-tone="dark" aria-labelledby="ins-h">
  <div class="wrap">
    <div class="sec-head">
      {kick(p, "05", "Insights", "رؤى")}
      <h2 class="t-xl lines" id="ins-h">{lines(*t(L(["Notes from", "the studio."], ["ملاحظات", "من الاستوديو."])))}</h2>
      <div class="aside">{lnk(t(UI['all_insights']), p.href('insights.html'))}</div>
    </div>
    <div class="ins-list">{ins}</div>
  </div>
</section>
"""
    ld = {"@context": "https://schema.org", "@type": "Organization", "name": "Seema", "alternateName": "سيمة",
          "legalName": SITE["registered"]["en"], "url": SITE["domain"], "email": SITE["email"],
          "logo": SITE["domain"] + "/assets/brand/Seema_mark_inktile.svg", "foundingDate": SITE["founded"],
          "slogan": SITE["tagline"][p.lang], "address": {"@type": "PostalAddress", "addressLocality": "Doha", "addressCountry": "QA"},
          "areaServed": ["QA", "SA", "AE", "KW", "BH", "OM"]}
    body += f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    title = t(L("Seema · سيمة — The mark that makes the difference", "سيمة · Seema — العلامة التي تصنع الفرق"))
    desc = t(L("Seema is a Doha consultancy for brand strategy, identity, websites, apps and business systems, serving ambitious businesses in Qatar and the GCC.",
               "سيمة شركة استشارات في الدوحة متخصصة في استراتيجية العلامة والهوية والمواقع والتطبيقات وأنظمة الأعمال، تخدم الشركات الطموحة في قطر والخليج."))
    return page(p, title, desc, body)


# ------------------------------------------------------------------ ABOUT
def about(p):
    t = p.t
    ol = p.ol
    pr = "".join(f'<div class="principle rv" data-delay="{(i % 2) * 120}"><span class="idx">{num(i + 1, "en")}</span><div><h3>{esc(t(a))}</h3><p>{esc(t(b))}</p></div></div>'
                 for i, (a, b) in enumerate(PRINCIPLES))
    aud = "".join(f'<div class="rv" data-delay="{i * 90}"><span class="idx c3">{num(i + 1, "en")}</span><h3>{esc(t(a))}</h3><p>{esc(t(b))}</p></div>' for i, (a, b) in enumerate(AUDIENCE))
    pvp = [(L("Purpose", "الغاية"), L("To give ambitious businesses a brand that means something, and can prove it works.", "أن نمنح الشركات الطموحة علامة لها معنى، وتثبت أنها تعمل.")),
           (L("Vision", "الرؤية"), L("A region where the strongest brands are built here, on their own terms.", "منطقة تُبنى فيها أقوى العلامات هنا، وبشروطها الخاصة.")),
           (L("Promise", "الوعد"), L("Every client leaves with a mark that is clearly, only theirs.", "أن يخرج كل عميل بعلامة واضحة، له وحده."))]
    triad = "".join(f'<div class="rv" data-delay="{i * 110}"><span class="cap">{esc(t(a))}</span><p class="t-m">{esc(t(b))}</p></div>' for i, (a, b) in enumerate(pvp))
    statement = t(L("Seema is a consultancy for strategy, identity and digital, based in Doha and working across the Gulf.",
                    "سيمة شركة استشارات في الاستراتيجية والهوية والحلول الرقمية، مقرّها الدوحة وتعمل في أنحاء الخليج."))
    body = f"""
<section class="split-hero dark" data-tone="dark" aria-labelledby="ab-h">
  <div class="qwin qw">{p.img('fort-arches', '(max-width: 820px) 100vw, 64vw', eager=True)}</div>
  <div class="wrap">
    {kick(p, "00", "About Seema", "عن سيمة")}
    <h1 class="t-giant" id="ab-h">{lines(*t(L(["Made to be", "unmistakable" + pt()], ["صُنعت", "لتكون مميّزة" + pt()])))}</h1>
    <div class="row"><p class="lead">{esc(t(L("We work closely with ambitious businesses across Qatar and the Gulf, from the first strategic question to the systems that keep them running.", "نعمل عن قرب مع الشركات الطموحة في قطر والخليج، من السؤال الاستراتيجي الأول حتى الأنظمة التي تُبقي أعمالها مستمرة.")))}</p>
      <p class="voice" lang="{ol}">{esc(p.o(L("About Seema", "عن سيمة")))}</p></div>
  </div>
</section>

<section class="sec light about-intro" data-tone="light">
  <div class="wrap g12">
    <p class="t-l words" style="grid-column:1/span 10">{words(esc(statement))}</p>
    <div class="cols">
      <p>{esc(t(L("We bring together the thinking of a management consultancy and the craft of a design studio. That means we can define a position, give it a form and build the platforms that carry it, without handing the idea between agencies.", "نجمع بين تفكير الاستشارات الإدارية وحرفية استوديو التصميم. لذلك نستطيع أن نحدّد التموضع، ونمنحه شكلاً، ونبني المنصات التي تحمله، دون أن تتنقّل الفكرة بين الوكالات.")))}</p>
      <p>{esc(t(L("Our work is organised in three practices, consultations, branding and website development, supported by mobile apps, business applications, digital marketing and IT support.", "ينتظم عملنا في ثلاث ممارسات: الاستشارات، والهوية التجارية، وتطوير المواقع، تدعمها تطبيقات الجوال، وتطبيقات الأعمال، والتسويق الرقمي، والدعم الفني.")))}</p>
    </div>
  </div>
</section>

<section class="sec dark" data-tone="dark" aria-labelledby="pr-h">
  <div class="wrap">
    <div class="sec-head">
      {kick(p, "01", "How we work with you", "كيف نعمل معك")}
      <h2 class="t-xl lines" id="pr-h">{lines(*t(L(["Four commitments.", "Every engagement."], ["أربعة التزامات.", "في كل مشروع."])))}</h2>
    </div>
    <div class="principles">{pr}</div>
  </div>
</section>

<section class="sec dark" data-tone="dark" style="padding-top:0" aria-label="{esc(t(L('Doha', 'الدوحة')))}">
  <div class="wrap diptych">
    <figure><div class="ph reveal-img" style="aspect-ratio:4/3">{p.img('edu-city-oval', '(max-width: 820px) 100vw, 56vw')}</div><figcaption class="cap">{esc(t(L("Doha · Education City", "الدوحة · المدينة التعليمية")))}</figcaption></figure>
    <figure><div class="ph reveal-img" data-delay="150" style="aspect-ratio:4/5">{p.img('cs-mia-night', '(max-width: 820px) 100vw, 40vw')}</div><figcaption class="cap">{esc(t(L("Where we work", "حيث نعمل")))}</figcaption></figure>
  </div>
</section>

<section class="sec dark2 belief" data-tone="dark" aria-labelledby="bl-h">
  <div class="wrap">
    {kick(p, "02", "What we believe", "ما نؤمن به")}
    <h2 class="t-giant mt3 lines" id="bl-h">{lines(*t(L(["Define,", "don’t decorate."], ["نُعرِّف،", "لا نُزخرِف."])))}</h2>
    <div class="triad">{triad}</div>
  </div>
</section>

<section class="sec light" data-tone="light" aria-labelledby="au-h">
  <div class="wrap">
    <div class="sec-head">
      {kick(p, "03", "Who we work with", "مع من نعمل")}
      <h2 class="t-xl lines" id="au-h">{lines(*t(L(["Ambitious businesses,", "at every stage."], ["شركات طموحة،", "في كل مرحلة."])))}</h2>
    </div>
    <div class="audience">{aud}</div>
  </div>
</section>

{steps(p, 'dark2', '04')}
"""
    desc = t(L("Seema is a Doha consultancy for strategy, identity and digital, working with ambitious businesses across Qatar and the Gulf.",
               "سيمة شركة استشارات في الدوحة للاستراتيجية والهوية والحلول الرقمية، تعمل مع الشركات الطموحة في قطر والخليج."))
    return page(p, t(L("About", "من نحن")), desc, body, og="fort-arches")


# ------------------------------------------------------------------ SERVICES
SHORT = {
    "consultations": L("Consulting", "الاستشارات"), "branding": L("Branding", "الهوية"),
    "websites": L("Websites", "المواقع"), "mobile": L("Apps", "التطبيقات"),
    "business-apps": L("Systems", "الأنظمة"), "marketing": L("Marketing", "التسويق"),
    "support": L("Support", "الدعم"),
}
SVC_COLLAGE = {
    "consultations": lambda p, s: [(mk_note(p), 56, 37, "25vw", 1.0, -2),
                                   (mk_chip(p, L("What makes us different?", "ما الذي يميّزنا؟"), pt()), 68, 82, "auto", 1.4, 0)],
    "branding": lambda p, s: [(mk_identity(p), 60, 35, "20vw", 1.0, 3),
                              (mk_chip(p, L("Make it unmistakable", "اجعلها لا تلتبس"), pt()), 52, 84, "auto", 1.4, 0)],
    "websites": lambda p, s: [(mk_browser(p, s["photo2"]), 52, 37, "30vw", 1.0, -2),
                              (mk_chip(p, L("Arabic first, not mirrored", "العربية أولاً، لا معكوسة"), pt()), 62, 86, "auto", 1.4, 0)],
    "mobile": lambda p, s: [(mk_phone(p, s["photo2"]), 60, 31, "12vw", 1.0, -3),
                            (mk_phone(p, "cs-majlis-coffee"), 77, 40, "10.5vw", 1.5, 4),
                            (mk_chip(p, L("Book in two taps", "احجز بلمستين"), pt()), 48, 84, "auto", 1.3, 0)],
    "business-apps": lambda p, s: [(mk_dash(p), 54, 37, "28vw", 1.0, -2),
                                   (mk_chip(p, L("One system, not twelve spreadsheets", "نظام واحد، لا اثنا عشر جدولاً"), pt()), 58, 86, "auto", 1.4, 0)],
    "marketing": lambda p, s: [(mk_post(p, s["photo2"]), 62, 31, "16vw", 1.0, 3),
                               (mk_chip(p, L("Reach the people who matter", "اصل إلى من يهمّك"), pt()), 46, 84, "auto", 1.4, 0)],
    "support": lambda p, s: [(mk_ticket(p), 57, 38, "24vw", 1.0, -2),
                             (mk_chip(p, L("Fixed before you notice", "يُحل قبل أن تلاحظ"), pt()), 64, 84, "auto", 1.4, 0)],
}


FEAT_MOCKS = {   # (kind, width as % of a wide card, rotation)
    "consultations": [("note", 44, -2), ("browser", 58, 2)],
    "branding": [("identity", 38, 3), ("post", 30, -3)],
    "websites": [("browser", 62, -2), ("phone", 20, 3)],
    "mobile": [("phone", 21, -3), ("phone2", 21, 3)],
    "business-apps": [("dash", 56, -2), ("phone", 20, 3)],
    "marketing": [("post", 30, -3), ("dash", 54, 2)],
    "support": [("ticket", 44, -2), ("phone", 20, 3)],
}


def feat_mock(p, s, k):
    kind, w, r = FEAT_MOCKS[s["id"]][k]
    other = SERVICES[(SERVICES.index(s) + 3) % len(SERVICES)]["photo2"]
    html_ = {"note": lambda: mk_note(p), "browser": lambda: mk_browser(p, s["photo"]), "identity": lambda: mk_identity(p),
             "post": lambda: mk_post(p, s["photo"]), "phone": lambda: mk_phone(p, s["photo2"]), "phone2": lambda: mk_phone(p, other),
             "dash": lambda: mk_dash(p), "ticket": lambda: mk_ticket(p)}[kind]()
    return f'<div class="feat-mk mk-{kind}-w" aria-hidden="true" style="--w:{w}%;--r:{r}deg">{html_}</div>'


def svc_feats(p, i, s):
    """Shopify-style featured cards (photo + product screen + prompt) and the dense deliverables list."""
    t = p.t
    v = SVC_V6[s["id"]]
    names = t(s["scope"])
    feats = ""
    for k, (si, photo, prompt) in enumerate(v["feat"]):
        feats += f"""<article class="feat{' wide' if (k + i) % 2 == 0 else ''} rv" data-delay="{k * 120}">
  <div class="feat-ph">{p.img(photo, '(max-width: 820px) 100vw, 50vw')}{feat_mock(p, s, k)}<div class="feat-ui">{mk_chip(p, prompt, pt())}</div></div>
  <h3>{esc(names[si])}</h3><p>{esc(t(v['desc'][si]))}</p>
  <a class="lnk" href="{p.href('contact.html')}"><span>{esc(t(L("Discuss this", "ناقش هذا")))}</span>{ARR_LONG}</a>
</article>"""
    dense = "".join(f'<div class="dl-it"><b>{esc(nm)}</b><p>{esc(t(v["desc"][k]))}</p></div>' for k, nm in enumerate(names))
    return feats, dense


SD_MOCKS = {   # the product screen laid over the "What we do" photograph: (kind, width % of the photo)
    "consultations": ("note", 52), "branding": ("identity", 48), "websites": ("browser", 70), "mobile": ("phone", 23),
    "business-apps": ("dash", 66), "marketing": ("post", 36), "support": ("ticket", 52),
}


def sd_mock(p, s):
    kind, w = SD_MOCKS[s["id"]]
    html_ = {"note": lambda: mk_note(p), "browser": lambda: mk_browser(p, s["photo"]), "identity": lambda: mk_identity(p),
             "post": lambda: mk_post(p, s["photo"]), "phone": lambda: mk_phone(p, s["photo"]), "dash": lambda: mk_dash(p),
             "ticket": lambda: mk_ticket(p)}[kind]()
    return f'<div class="sd-mk sd-{kind}" aria-hidden="true" style="--w:{w}%">{html_}</div>'


def cloud(p):
    import random
    rnd = random.Random(7)
    items = []
    for s in SERVICES:
        for nm in p.t(s["scope"]):
            items.append((nm, s["id"]))
    rnd.shuffle(items)
    out = ""
    for nm, sid in items:
        sz = rnd.choice([1, 1, 1, 2, 2, 3])
        d = round(rnd.uniform(.4, 1.6), 2)
        dy = rnd.randint(-30, 30)
        label = ("/" + nm.lower().replace(" ", "-")) if p.lang == "en" else nm
        out += f'<a class="cw s{sz}" href="#{sid}" data-depth="{d}" style="--dy:{dy}px">{esc(label)}</a>'
    return f"""
<section class="sec light cloud-sec" data-tone="light" aria-labelledby="cl-h">
  <div class="wrap">
    <div class="cl-head">
      {kick(p, "—", "Everything we deliver", "كل ما نقدّمه")}
      <h2 class="pc-title" id="cl-h">{initial(p.t(L("Every deliverable, one point of view", "كل مُخرَج، ورؤية واحدة")), p.lang)}</h2>
    </div>
    <div class="cloud">{out}</div>
  </div>
</section>"""


def services(p):
    t = p.t
    ol = p.ol

    def card(i, s):
        return f"""<a class="svc-card rv" data-delay="{(i % 3) * 90}" href="{p.href('service-' + s['id'] + '.html')}" data-cursor="{esc(t(L('Open', 'افتح')))}">
  <div class="ph">{p.img(s['photo'], '(max-width: 820px) 100vw, 30vw')}</div>
  <div class="meta"><span class="idx">{num(i + 1, 'en')}</span><span class="voice" lang="{ol}">{esc(p.o(s['name']))}</span></div>
  <h3>{esc(t(s['name']))}</h3>
  <p>{esc(t(s['outcome']))}</p>
  <span class="lnk"><span>{esc(t(UI['services_link']))}</span>{ARR_LONG}</span>
</a>"""
    def chapter(i, s):
        sc = SVC_COLLAGE[s["id"]](p, s)
        scope = "".join(f'<li><span class="idx">{num(k + 1, "en")}</span><b>{esc(x)}</b></li>' for k, x in enumerate(t(s["scope"])))
        res = "".join(f"<li>{esc(x)}</li>" for x in t(s["results"]))
        op = opener(p, s["id"], i, p.img(s["photo"], "100vw"), t(SHORT[s["id"]]), t(s["outcome"]), p.o(s["name"]),
                    heading_id=s["id"] + "-h", collage_html=collage(sc))
        v = SVC_V6[s["id"]]
        feats, dense = svc_feats(p, i, s)
        res = "".join(f'<li><span class="idx">{num(k + 1, "en")}</span><p>{esc(x)}</p></li>' for k, x in enumerate(t(s["results"])))
        return op + f"""
<section class="sec light paper-chap" data-chapter="{s['id']}" data-tone="light" aria-label="{esc(t(s['name']))}">
  <div class="wrap">
    <div class="pc-head">
      <p class="kick"><span class="idx">{num(i + 1, 'en')} / 07</span><span class="cap">{esc(t(s['name']))}</span><span class="cap c3">{esc(t(L("Practice", "ممارسة")) if s["group"] == "practice" else t(L("Service", "خدمة")))}</span></p>
      <h3 class="pc-title">{initial(t(v['head']), p.lang)}</h3>
      <p class="lead">{esc(t(s['value']))}</p>
    </div>
    <div class="feats">{feats}</div>
    <div class="dense">
      <p class="cap c3">{esc(t(L("What’s included", "ما تشمله")))}</p>
      <div class="dl">{dense}</div>
    </div>
    <div class="changes">
      <p class="cap c3">{esc(t(L("What it changes", "ما الذي تغيّره")))}</p>
      <ol>{res}</ol>
    </div>
    <div class="pc-foot">{lnk(t(UI['services_link']), p.href('service-' + s['id'] + '.html'))}{btn(t(L("Discuss this service", "ناقش هذه الخدمة")), p.href('contact.html'), 'btn--solid')}</div>
  </div>
</section>"""
    chapters = "".join(chapter(i, s) for i, s in enumerate(SERVICES))
    svc_rail = rail(p, [(s["id"], SHORT[s["id"]]) for s in SERVICES])
    body = svc_rail + f"""
<section class="split-hero dark" data-tone="dark" aria-labelledby="sv-h">
  <div class="qwin qw">{p.img('sv-hero-dhow', '(max-width: 820px) 100vw, 55vw', eager=True)}</div>
  <div class="wrap">
    {kick(p, "00", "Services", "خدماتنا")}
    <h1 class="t-giant" id="sv-h">{lines(*t(L(["Seven", "disciplines" + pt()], ["سبع", "خدمات" + pt()])))}</h1>
    <div class="row"><p class="lead">{esc(t(L("Rooted in Doha, built for what comes next. From the first strategic question to the systems that keep a business running, each service has one clear outcome.", "جذورنا في الدوحة، وعملنا لما هو قادم. من السؤال الاستراتيجي الأول حتى الأنظمة التي تُبقي العمل مستمراً، لكل خدمة نتيجة واحدة واضحة.")))}</p>
      <p class="voice" lang="{ol}">{esc(p.o(L("Services", "خدماتنا")))}</p></div>
  </div>
</section>
{chapters}
{cloud(p)}
{steps(p, 'dark2', '08')}
"""
    desc = t(L("Consultations, branding, website development, mobile apps, business applications, digital marketing and IT support from Seema in Doha.",
               "الاستشارات والهوية التجارية وتطوير المواقع وتطبيقات الجوال وتطبيقات الأعمال والتسويق الرقمي والدعم الفني من سيمة في الدوحة."))
    return page(p, t(L("Services", "خدماتنا")), desc, body, og="sv-hero-dhow")


def service_page(p, i, s):
    t = p.t
    ol = p.ol
    scope = "".join(f"<li>{esc(x)}</li>" for x in t(s["scope"]))
    res = "".join(f"<li>{esc(x)}</li>" for x in t(s["results"]))
    others = "".join(f"""<li><a class="svc-row" href="{p.href('service-' + o['id'] + '.html')}" data-peek="{o['id']}">
  <span class="idx">{num(k + 1, "en")}</span><span class="nm">{esc(t(o['name']))}</span>
  <span class="meta"><span class="cap">{esc(t(o['outcome']))}</span><span class="oth bi-{ol}" lang="{ol}">{esc(p.o(o['name']))}</span></span>
</a></li>""" for k, o in enumerate(SERVICES) if o["id"] != s["id"])
    peeks = "".join(f'<img data-id="{o["id"]}" src="{p.asset("img/" + o["peek"] + "-sm.jpg")}" alt="" loading="lazy">' for o in SERVICES)
    grp = t(L("Practice", "ممارسة")) if s["group"] == "practice" else t(L("Service", "خدمة"))
    nxt = SERVICES[(i + 1) % len(SERVICES)]
    sf = svc_feats(p, i, s)
    body = f"""
<section class="split-hero dark svc-hero" data-tone="dark" aria-labelledby="s-h">
  <div class="qwin qw">{p.img(s['photo'], '(max-width: 820px) 100vw, 55vw', eager=True)}</div>
  <div class="wrap">
    <p class="kick"><span class="idx">{num(i + 1, 'en')} / 07</span><a class="cap" href="{p.href('services.html')}">{esc(t(L("Services", "خدماتنا")))}</a><span class="cap c3">{esc(grp)}</span></p>
    <h1 class="t-giant" id="s-h">{lines(esc(t(s['name'])) + pt())}</h1>
    <div class="row"><p class="lead">{esc(t(s['outcome']))}</p><p class="voice" lang="{ol}">{esc(p.o(s['name']))}</p></div>
  </div>
</section>
<section class="sec light" data-tone="light"><div class="wrap svc-detail">
    <div class="sd-copy">
      {kick(p, "01", "What we do", "ما نقدّمه")}
      <p class="t-l">{esc(t(s['value']))}</p>
      <div class="lists">
        <div><span class="cap">{esc(t(L("What’s included", "ما تشمله")))}</span><ul>{scope}</ul></div>
        <div><span class="cap">{esc(t(L("What it changes", "ما الذي تغيّره")))}</span><ul>{res}</ul></div>
      </div>
      <div class="acts">{btn(t(L("Discuss this service", "ناقش هذه الخدمة")), p.href('contact.html'), 'btn--solid')}</div>
    </div>
    <figure class="sd-media"><div class="ph reveal-img">{p.img(s['photo2'], '(max-width: 820px) 100vw, 40vw')}</div>{sd_mock(p, s)}</figure>
  </div>
</section>
<section class="sec light paper-chap practice" data-tone="light" aria-labelledby="ip-h">
  <div class="wrap">
    <div class="pc-head">
      {kick(p, "02", "In practice", "على أرض الواقع")}
      <h2 class="pc-title" id="ip-h">{initial(t(SVC_V6[s['id']]['head']), p.lang)}</h2>
    </div>
    <div class="feats">{sf[0]}</div>
    <div class="dense">
      <p class="cap c3">{esc(t(L("Every deliverable", "كل المخرجات")))}</p>
      <div class="dl">{sf[1]}</div>
    </div>
  </div>
</section>
{steps(p, 'dark2', '03')}
<section class="sec dark" data-tone="dark" aria-labelledby="ot-h">
  <div class="wrap">
    <div class="sec-head">{kick(p, "04", "Other services", "خدمات أخرى")}
      <h2 class="t-xl" id="ot-h">{esc(t(L("Explore the rest of what we do.", "تعرّف على بقية خدماتنا.")))}</h2>
      <div class="aside">{lnk(t(L("Next", "التالي")) + ": " + t(nxt['name']), p.href('service-' + nxt['id'] + '.html'))}</div></div>
    <ul class="svc-list">{others}</ul>
  </div>
  <div class="svc-peek qw" aria-hidden="true">{peeks}</div>
</section>
"""
    return page(p, t(s["name"]), t(s["outcome"]) + " " + t(s["value"]), body, og=s["photo"])


def work(p):
    t = p.t
    ol = p.ol
    filt = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{esc(t(v))}</button>' for k, v in WORK_FILTERS)
    items = "".join(f"""<article class="wi" data-tags="{' '.join(pr['tags'])}">
  <a class="ph reveal-img" href="{p.href('case-' + pr['slug'] + '.html')}" tabindex="-1" aria-hidden="true" data-cursor="{esc(t(L('View', 'شاهد')))}">{p.img(pr['cover'], '(max-width: 820px) 100vw, 64vw', eager=(i == 0))}</a>
  <div class="txt rv">
    <p class="flexb"><span class="idx c3">{num(i + 1, 'en')}</span><span class="cap tag c3">{esc(t(UI['placeholder']))}</span></p>
    <h2 class="t-l"><a href="{p.href('case-' + pr['slug'] + '.html')}">{esc(t(pr['title']))}</a></h2>
    <p>{esc(t(pr['challenge']))}</p>
    <p class="cap c3">{esc(t(pr['sector']))} · {esc(t(pr['services']))}</p>
    {lnk(t(UI['view_case']), p.href('case-' + pr['slug'] + '.html'))}
  </div>
</article>""" for i, pr in enumerate(PROJECTS))
    body = f"""
<section class="ph-hero light" data-tone="light" aria-labelledby="wk-h">
  <div class="wrap">
    <div class="kick"><span class="cap">{esc(t(L("Work", "أعمالنا")))}</span><span class="cap">{num(len(PROJECTS), 'en')} {esc(t(L("case studies", "دراسات حالة")))}</span></div>
    <div class="g12">
      <h1 class="t-hero" id="wk-h">{lines(*t(L(["Selected", "work" + pt()], ["أعمال", "مختارة" + pt()])))}</h1>
      <p class="lead">{esc(t(L("Every project starts with one question: what makes this business different? Each case study follows that answer from the first brief to the final result.", "كل مشروع يبدأ بسؤال واحد: ما الذي يميّز هذا العمل؟ وتتبع كل دراسة حالة الإجابة من الموجز الأول حتى النتيجة النهائية.")))}</p>
      <div class="aside" style="text-align:start">{placeholder_note(p)}</div>
    </div>
  </div>
</section>
<section class="sec light" data-tone="light" style="padding-top:0" aria-label="{esc(t(L('Projects', 'المشاريع')))}">
  <div class="wrap">
    <div class="filters" role="group" aria-label="{esc(t(L('Filter by discipline', 'تصفية حسب التخصص')))}" data-filter-group="#wl" data-live="#wl-count">{filt}</div>
    <p id="wl-count" class="sr-only" aria-live="polite" data-tpl="{esc(t(L('{n} projects shown', 'عدد المشاريع المعروضة: {n}')))}"></p>
    <div class="wl" id="wl">{items}</div>
  </div>
</section>
"""
    desc = t(L("Seema case studies in brand strategy, identity, websites, apps and business systems for ambitious businesses in Qatar and the GCC.",
               "دراسات حالة سيمة في استراتيجية العلامة والهوية والمواقع والتطبيقات وأنظمة الأعمال للشركات الطموحة في قطر والخليج."))
    return page(p, t(L("Work", "أعمالنا")), desc, body, og="cs-majlis-coffee")


def case(p, i, pr):
    t = p.t
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    meta = [(L("Client", "العميل"), pr["client"]), (L("Sector", "القطاع"), pr["sector"]), (L("Services", "الخدمات"), pr["services"]),
            (L("Year", "السنة"), pr["year"]), (L("Location", "الموقع"), pr["place"])]
    meta_html = "".join(f'<div><dt class="cap">{esc(t(a))}</dt><dd>{esc(t(b))}</dd></div>' for a, b in meta)
    steps_html = "".join(f'<li class="rv" data-delay="{j * 90}"><span class="idx">{num(j + 1, "en")}</span><p>{esc(x)}</p></li>' for j, x in enumerate(t(pr['approach'])))
    gal = "".join(f'<figure class="ph reveal-img" data-delay="{j * 120}">{p.img(g, "(max-width: 820px) 100vw, 70vw")}</figure>' for j, g in enumerate(pr["gallery"]))
    metrics = "".join(f'<div class="metric rv" data-delay="{j * 100}"><span class="v" aria-hidden="true">—</span><p class="cap">{esc(m)}</p><p>{esc(t(L("To be published once measured and approved by the client.", "يُنشر بعد قياسه وموافقة العميل.")))}</p></div>' for j, m in enumerate(t(pr['measures'])))
    body = f"""
<article>
<section class="cs-cover" data-tone="dark" aria-labelledby="cs-h">
  <div class="ph">{p.img(pr['cover'], '100vw', eager=True)}</div>
  <div class="wrap">
    <p class="kick"><a class="cap" href="{p.href('work.html')}">{esc(t(NAV[3][1]))}</a><span class="cap tag">{esc(t(UI['placeholder']))} · {esc(t(L("Case study", "دراسة حالة")))} {num(i + 1, 'en')}</span></p>
    <h1 class="t-xl" id="cs-h">{esc(t(pr['title']))}</h1>
    <dl class="cs-meta">{meta_html}</dl>
  </div>
</section>
<section class="sec light" data-tone="light">
  <div class="wrap cs-sec"><p class="cap">{esc(t(L("The challenge", "التحدّي")))}</p><div class="bd"><p class="t-l">{esc(t(pr['challenge']))}</p>
    <p class="note-ph">{pt()}<span>{esc(t(L("Illustrative case study. The structure is final; client, story and images will be replaced with a real project.", "دراسة حالة توضيحية. البنية نهائية، أما العميل والقصة والصور فستُستبدل بمشروع حقيقي.")))}</span></p></div></div>
</section>
<section class="dark2" data-tone="dark">
  <div class="wrap cs-idea"><p class="cap">{esc(t(L("The idea", "الفكرة")))}</p>{pt('pt-lg')}<p class="t-giant">{esc(t(pr['point']))}</p></div>
</section>
<section class="sec light" data-tone="light">
  <div class="wrap cs-sec"><p class="cap">{esc(t(L("Approach", "المنهج")))}</p><div class="bd"><ol class="cs-steps">{steps_html}</ol></div></div>
  <div class="wrap cs-sec mt3"><p class="cap">{esc(t(L("Solution", "الحل")))}</p><div class="bd"><p class="t-m" style="max-width:34ch">{esc(t(pr['solution']))}</p></div></div>
  <div class="wrap mt3"><div class="cs-gal">{gal}</div></div>
</section>
<section class="sec dark" data-tone="dark">
  <div class="wrap cs-sec"><p class="cap">{esc(t(L("Outcomes", "النتائج")))}</p>
    <div class="bd"><p class="t-l">{esc(t(L("How success is measured.", "كيف يُقاس النجاح.")))}</p><div class="metrics">{metrics}</div></div></div>
</section>
<a class="next" href="{p.href('case-' + nxt['slug'] + '.html')}" data-tone="dark" data-cursor="{esc(t(L('Next', 'التالي')))}">
  <div class="ph">{p.img(nxt['cover'], '100vw')}</div>
  <div class="wrap"><span class="cap">{esc(t(L("Next case study", "دراسة الحالة التالية")))}</span><p class="t-xl">{esc(t(nxt['title']))}</p><span class="lnk"><span>{esc(t(UI['view_case']))}</span>{ARR_LONG}</span></div>
</a>
</article>
"""
    return page(p, t(pr["title"]), t(pr["challenge"]), body, og=pr["cover"])


# ------------------------------------------------------------------ INSIGHTS
def insights(p):
    t = p.t
    ol = p.ol
    topics = dict(TOPICS)
    arts = [a for a in ARTICLES if a.get("slug")]
    feat = arts[0]
    filt = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{esc(t(v))}</button>' for k, v in TOPICS)
    rows = []
    for a in ARTICLES[1:]:
        if a.get("slug"):
            rows.append(f"""<a class="ins" href="{p.href('insight-' + a['slug'] + '.html')}" data-tags="{a['topic']}" data-cursor="{esc(t(UI['read']))}">
  <div class="ph">{p.img(a['photo'], '(max-width: 820px) 30vw, 16vw')}</div>
  <div><h3>{esc(t(a['title']))}</h3><p class="dek">{esc(t(a['dek']))}</p></div>
  <div class="meta"><span class="cap">{esc(t(topics[a['topic']]))}</span><span class="idx">{num(a['minutes'], p.lang, 1)} {esc(t(UI['min']))}</span></div></a>""")
        else:
            rows.append(f"""<div class="ins soon" data-tags="{a['topic']}"><div class="ph ph-soon" aria-hidden="true">{pt()}</div>
  <div><h3>{esc(t(a['title']))}</h3><p class="dek">{esc(t(a['dek']))}</p></div>
  <div class="meta"><span class="cap">{esc(t(topics[a['topic']]))}</span><span class="cap">{esc(t(UI['soon']))}</span></div></div>""")
    body = f"""
<section class="ph-hero light" data-tone="light" aria-labelledby="in-h">
  <div class="wrap">
    <div class="kick"><span class="cap">{esc(t(L("Notes from the studio", "ملاحظات من الاستوديو")))}</span><span class="cap">{esc(t(SITE['city']))} · {esc(t(L("September 2026", "سبتمبر ٢٠٢٦")))}</span></div>
    <div class="g12">
      <h1 class="t-hero" id="in-h">{lines(t(L("Insights", "رؤى")) + pt())}</h1>
      <p class="lead">{esc(t(L("Practical thinking on brand strategy, digital transformation, website design and business technology, for leaders in Qatar and the Gulf.", "أفكار عملية في استراتيجية العلامة والتحوّل الرقمي وتصميم المواقع وتقنية الأعمال، لقادة الأعمال في قطر والخليج.")))}</p>
      <p class="aside voice" lang="{ol}">{esc(p.o(L("Insights", "رؤى")))}</p>
    </div>
  </div>
</section>
<section class="light" data-tone="light" aria-label="{esc(t(L('Featured', 'مقال مختار')))}">
  <a class="wrap feature" href="{p.href('insight-' + feat['slug'] + '.html')}" data-cursor="{esc(t(UI['read']))}">
    <div class="ph">{p.img(feat['photo'], '(max-width: 820px) 100vw, 56vw', eager=True)}</div>
    <div class="ft-txt"><span class="cap c3">{esc(t(L("Featured", "مقال مختار")))} · {esc(t(topics[feat['topic']]))}</span>
      <h2 class="t-l">{esc(t(feat['title']))}</h2><p>{esc(t(feat['dek']))}</p><span class="lnk"><span>{esc(t(UI['read']))}</span>{ARR_LONG}</span></div>
  </a>
</section>
<section class="sec light" data-tone="light" aria-labelledby="ix-h">
  <div class="wrap">
    <h2 class="sr-only" id="ix-h">{esc(t(L("All insights", "كل المقالات")))}</h2>
    <div class="filters" role="group" aria-label="{esc(t(L('Filter by topic', 'تصفية حسب الموضوع')))}" data-filter-group="#ix" data-live="#ix-count">{filt}</div>
    <p id="ix-count" class="sr-only" aria-live="polite" data-tpl="{esc(t(L('{n} articles shown', 'عدد المقالات المعروضة: {n}')))}"></p>
    <div class="ins-list" id="ix" style="border-top:0">{''.join(rows)}</div>
  </div>
</section>
"""
    desc = t(L("Articles and practical advice on brand strategy, digital transformation, website design and business technology from Seema in Doha.",
               "مقالات ونصائح عملية في استراتيجية العلامة والتحوّل الرقمي وتصميم المواقع وتقنية الأعمال من سيمة في الدوحة."))
    return page(p, t(L("Insights", "رؤى")), desc, body, og="ink-pen-minimal")


def article(p, a):
    t = p.t
    topics = dict(TOPICS)
    rel = [x for x in ARTICLES if x.get("slug") and x["slug"] != a["slug"]][:2]
    rel_html = "".join(f"""<a href="{p.href('insight-' + r['slug'] + '.html')}" class="rv" data-cursor="{esc(t(UI['read']))}"><div class="ph">{p.img(r['photo'], '(max-width: 820px) 100vw, 45vw')}</div>
  <span class="cap c3">{esc(t(topics[r['topic']]))} · {num(r['minutes'], p.lang, 1)} {esc(t(UI['min']))}</span><h3>{esc(t(r['title']))}</h3></a>""" for r in rel)
    url = SITE["domain"] + ("/ar/" if p.lang == "ar" else "/") + "insight-" + a["slug"] + ".html"
    body = f"""
<article>
<header class="art-head light" data-tone="light">
  <div class="wrap">
    <p class="kick"><a class="cap" href="{p.href('insights.html')}">{esc(t(NAV[4][1]))}</a><span class="cap c3">{esc(t(topics[a['topic']]))}</span></p>
    <h1 class="t-xl">{esc(t(a['title']))}</h1>
    <p class="lead">{esc(t(a['dek']))}</p>
  </div>
</header>
<div class="light" data-tone="light"><div class="wrap"><figure class="ph art-cover">{p.img(a['photo'], '100vw', eager=True)}</figure></div></div>
<section class="sec light" data-tone="light">
  <div class="wrap art">
    <aside>
      <dl>
        <div><dt class="cap">{esc(t(L("Written by", "بقلم")))}</dt><dd>{esc(t(L("Seema studio", "فريق سيمة")))}</dd></div>
        <div><dt class="cap">{esc(t(L("Published", "تاريخ النشر")))}</dt><dd>{esc(t(a['date']))}</dd></div>
        <div><dt class="cap">{esc(t(L("Reading time", "مدة القراءة")))}</dt><dd>{num(a['minutes'], p.lang, 1)} {esc(t(UI['min']))}</dd></div>
      </dl>
      <button class="copy-btn" type="button" data-copy="{url}" data-done="{esc(t(UI['copied']))}">{esc(t(L("Copy link", "نسخ الرابط")))}</button>
    </aside>
    <div class="prose">{a['body'][p.lang]}</div>
  </div>
</section>
<section class="sec dark2" data-tone="dark" aria-labelledby="rel-h">
  <div class="wrap">
    <div class="flexb" style="margin-block-end:clamp(2.5rem,5vw,4rem)"><h2 class="t-l" id="rel-h">{esc(t(L("Keep reading", "تابع القراءة")))}</h2>{lnk(t(UI['all_insights']), p.href('insights.html'))}</div>
    <div class="rel">{rel_html}</div>
  </div>
</section>
</article>
"""
    return page(p, t(a["title"]), t(a["dek"]), body, og=a["photo"])


# ------------------------------------------------------------------ CONTACT
def contact(p):
    t = p.t
    chips = "".join(f'<label class="chip"><input type="checkbox" name="services" value="{esc(s["name"]["en"])}"><span>{esc(t(s["name"]))}</span></label>' for s in SERVICES)
    budgets = [L("Not sure yet", "لم أحدّد بعد"), L("Under QAR 50,000", "أقل من ٥٠٬٠٠٠ ريال"), L("QAR 50,000 – 150,000", "٥٠٬٠٠٠ – ١٥٠٬٠٠٠ ريال"),
               L("QAR 150,000 – 500,000", "١٥٠٬٠٠٠ – ٥٠٠٬٠٠٠ ريال"), L("Over QAR 500,000", "أكثر من ٥٠٠٬٠٠٠ ريال")]
    times = [L("Flexible", "مرن"), L("Within a month", "خلال شهر"), L("1–3 months", "من شهر إلى ثلاثة أشهر"), L("3–6 months", "من ثلاثة إلى ستة أشهر"), L("Later this year", "لاحقاً هذا العام")]
    opt = lambda xs: "".join(f'<option value="{esc(x["en"])}">{esc(t(x))}</option>' for x in xs)
    langs = [L("English", "الإنجليزية"), L("Arabic", "العربية"), L("Both", "كلتاهما")]
    lang_chips = "".join(f'<label class="chip"><input type="radio" name="lang" value="{x["en"]}"{" checked" if j == (0 if p.lang == "en" else 1) else ""}><span>{esc(t(x))}</span></label>' for j, x in enumerate(langs))
    msgs = {"required": t(L("Please fill in this field.", "يُرجى تعبئة هذا الحقل.")),
            "email": t(L("Enter an email address like name@company.com.", "أدخل بريداً إلكترونياً بصيغة name@company.com.")),
            "short": t(L("Tell us a little more, at least 20 characters.", "أخبرنا بالمزيد، ٢٠ حرفاً على الأقل.")),
            "subject": t(L("Project enquiry", "استفسار عن مشروع")),
            "l_name": t(L("Name", "الاسم")), "l_company": t(L("Company", "الشركة")), "l_email": t(L("Email", "البريد")),
            "l_phone": t(L("Phone", "الهاتف")), "l_services": t(L("Services", "الخدمات")), "l_budget": t(L("Budget", "الميزانية")),
            "l_timeline": t(L("Timeline", "الإطار الزمني")), "l_lang": t(L("Preferred language", "اللغة المفضّلة"))}

    def field(id_, label, typ="text", req=False, auto="", optional=False, dirn=""):
        o = f' <span class="opt">({esc(t(L("optional", "اختياري")))})</span>' if optional else ""
        return (f'<div class="fld"><label for="{id_}">{esc(label)}{o}</label>'
                f'<input class="inp" id="{id_}" name="{id_}" type="{typ}"{" required aria-required=\"true\"" if req else ""}'
                f'{f" autocomplete=\"{auto}\"" if auto else ""}{f" dir=\"{dirn}\"" if dirn else ""} aria-describedby="{id_}-err">'
                f'<p class="err" id="{id_}-err" aria-live="polite"></p></div>')
    nsteps = [(L("We read and reply", "نقرأ ونردّ"), L("A senior member of the team reads every enquiry and replies personally, in the language you choose.", "يقرأ أحد كبار أعضاء الفريق كل استفسار ويردّ عليه شخصياً، باللغة التي تختارها.")),
              (L("A first conversation", "حديث أول"), L("A call, or a coffee in Doha, to understand the business, the goal and the constraints.", "مكالمة، أو فنجان قهوة في الدوحة، لفهم العمل والهدف والقيود.")),
              (L("A clear proposal", "عرض واضح"), L("A written scope with outcomes, timeline and fees. No obligation.", "نطاق عمل مكتوب يتضمّن النتائج والإطار الزمني والأتعاب، دون أي التزام."))]
    ns = "".join(f'<li class="step rv" data-delay="{i * 110}"><span class="n">{num(i + 1, "en")}</span><h3>{esc(t(a))}</h3><p>{esc(t(b))}</p></li>' for i, (a, b) in enumerate(nsteps))
    faqs = [(L("Do you work outside Qatar?", "هل تعملون خارج قطر؟"), L("Yes. We are based in Doha and work with businesses across the GCC.", "نعم. مقرّنا في الدوحة ونعمل مع الشركات في دول الخليج كلها.")),
            (L("Do you work in Arabic and English?", "هل تعملون بالعربية والإنجليزية؟"), L("Always. Both languages carry equal weight in everything we write, design and build.", "دائماً. للغتين الوزن نفسه في كل ما نكتبه ونصمّمه ونبنيه.")),
            (L("Can we start with one service?", "هل يمكن أن نبدأ بخدمة واحدة؟"), L("Yes. Each service can be engaged on its own, and many engagements begin with a consultation.", "نعم. يمكن التعاقد على كل خدمة بمفردها، وكثير من المشاريع تبدأ باستشارة.")),
            (L("Do you support what you build after launch?", "هل تدعمون ما تبنونه بعد الإطلاق؟"), L("Yes. Our IT help desk and support service covers maintenance, monitoring and user support.", "نعم. تشمل خدمة الدعم الفني لدينا الصيانة والمراقبة ودعم المستخدمين."))]
    faq = "".join(f'<details><summary>{esc(t(q))}</summary><p>{esc(t(a))}</p></details>' for q, a in faqs)
    body = f"""
<section class="contact" data-tone="dark" aria-labelledby="ct-h">
  <div class="left dark">
    <div class="bgph">{p.img('palm-shutter', '(max-width: 1180px) 100vw, 42vw', eager=True)}</div>
    <p class="cap c2">{esc(t(L("Contact", "تواصل معنا")))}</p>
    <h1 class="t-giant" id="ct-h" style="align-self:center">{lines(*t(L(["Let’s", "talk" + pt()], ["لنتحدّث" + pt()])))}</h1>
    <dl>
      <div><dt class="cap">{esc(t(L("Email", "البريد الإلكتروني")))}</dt><dd><span dir="ltr">{SITE['email']}</span><button class="copy-btn" type="button" data-copy="{SITE['email']}" data-done="{esc(t(UI['copied']))}">{esc(t(UI['copy']))}</button></dd></div>
      <div><dt class="cap">{esc(t(L("Studio", "الاستوديو")))}</dt><dd>{esc(t(SITE['city']))}</dd></div>
      <div><dt class="cap">{esc(t(L("Web", "الموقع")))}</dt><dd>{SITE['web']}</dd></div>
    </dl>
  </div>
  <div class="right light">
    <form class="form" id="enquiry" novalidate data-endpoint="" data-msgs='{esc(json.dumps(msgs, ensure_ascii=False))}' aria-labelledby="form-h">
      <p class="lead c2" id="form-h">{esc(t(L("Tell us about the business and what you want to change. The more we know, the better our first conversation will be.", "أخبرنا عن عملك وما تريد تغييره. كلما عرفنا أكثر، كان حديثنا الأول أفضل.")))}</p>
      <fieldset class="fs"><legend><span class="idx">01</span><span class="t-m">{esc(t(L("About you", "عنك")))}</span></legend>
        <div class="row2">{field('name', t(L('Full name', 'الاسم الكامل')), req=True, auto='name')}{field('company', t(L('Company', 'الشركة')), auto='organization', optional=True)}</div>
        <div class="row2">{field('email', t(L('Work email', 'البريد الإلكتروني')), 'email', req=True, auto='email', dirn='ltr')}{field('phone', t(L('Phone', 'رقم الهاتف')), 'tel', auto='tel', optional=True, dirn='ltr')}</div>
      </fieldset>
      <fieldset class="fs"><legend><span class="idx">02</span><span class="t-m">{esc(t(L("What you need", "ما تحتاجه")))}</span></legend>
        <div class="fld"><span class="fl" id="svc-lbl">{esc(t(L("Services", "الخدمات")))} <span class="opt">({esc(t(L("choose any", "اختر ما يناسبك")))})</span></span><div class="chips" role="group" aria-labelledby="svc-lbl">{chips}</div></div>
        <div class="row2">
          <div class="fld"><label for="budget">{esc(t(L("Budget range", "نطاق الميزانية")))}</label><select class="inp" id="budget" name="budget">{opt(budgets)}</select></div>
          <div class="fld"><label for="timeline">{esc(t(L("Start", "موعد البدء")))}</label><select class="inp" id="timeline" name="timeline">{opt(times)}</select></div>
        </div>
      </fieldset>
      <fieldset class="fs"><legend><span class="idx">03</span><span class="t-m">{esc(t(L("The project", "المشروع")))}</span></legend>
        <div class="fld"><label for="message">{esc(t(L("What would you like to change?", "ما الذي تودّ تغييره؟")))}</label>
          <textarea class="inp" id="message" name="message" required aria-required="true" aria-describedby="message-err" placeholder="{esc(t(L('Where the business is today, and what you want it to be known for.', 'أين يقف عملك اليوم، وبماذا تريد أن يُعرف.')))}"></textarea>
          <p class="err" id="message-err" aria-live="polite"></p></div>
        <div class="fld"><span class="fl" id="lang-lbl">{esc(t(L("Reply in", "لغة الرد")))}</span><div class="chips" role="radiogroup" aria-labelledby="lang-lbl">{lang_chips}</div></div>
      </fieldset>
      <div class="form-foot"><button class="btn btn--solid" type="submit">{pt()}<span>{esc(t(L("Send enquiry", "أرسل الاستفسار")))}</span></button>
        <p>{esc(t(L("We use your details only to reply to this enquiry.", "نستخدم بياناتك للرد على هذا الاستفسار فقط.")))}</p></div>
      <div class="form-status" id="enquiry-status" tabindex="-1" hidden role="status">
        <div data-ready style="display:grid;gap:1rem">
          <p class="t-m">{esc(t(L("Your enquiry is ready.", "استفسارك جاهز.")))}</p>
          <p class="c2">{esc(t(L("This site is not yet connected to a mail service, so nothing has been sent. Copy the summary below and send it to hello@seema.qa, or open it in your email app.", "هذا الموقع غير مرتبط بخدمة بريد بعد، لذلك لم يُرسل شيء. انسخ الملخّص أدناه وأرسله إلى hello@seema.qa، أو افتحه في تطبيق البريد.")))}</p>
          <pre id="enquiry-summary"></pre>
          <div class="row"><button class="btn" type="button" data-copy="#enquiry-summary" data-done="{esc(t(UI['copied']))}">{pt()}<span>{esc(t(L("Copy summary", "انسخ الملخّص")))}</span></button>
            <a class="lnk" id="enquiry-mail" href="mailto:{SITE['email']}"><span>{esc(t(L("Open in email app", "افتح في تطبيق البريد")))}</span>{ARR_LONG}</a></div>
        </div>
        <div data-sent hidden><p class="t-m">{esc(t(L("Thank you. Your enquiry has been sent.", "شكراً لك. تم إرسال استفسارك.")))}</p></div>
      </div>
    </form>
  </div>
</section>
<section class="sec dark" data-tone="dark" aria-labelledby="nx-h">
  <div class="wrap">
    <div class="sec-head">{kick(p, "—", "What happens next", "ما الذي يحدث بعد ذلك")}
      <h2 class="t-xl lines" id="nx-h">{lines(*t(L(["Three steps", "to a clear proposal."], ["ثلاث خطوات", "إلى عرض واضح."])))}</h2></div>
    <ol class="steps" style="grid-template-columns:repeat(3,minmax(0,1fr))">{ns}</ol>
    <div class="faq mt3">{faq}</div>
  </div>
</section>
"""
    desc = t(L("Start a project with Seema. Email hello@seema.qa or send an enquiry. Based in Doha, Qatar, serving the GCC.",
               "ابدأ مشروعك مع سيمة. راسلنا على hello@seema.qa أو أرسل استفساراً. مقرّنا في الدوحة، قطر، ونخدم دول الخليج."))
    return page(p, t(L("Contact", "تواصل معنا")), desc, body, og="palm-shutter", with_cta=False)


# ------------------------------------------------------------------ build
def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(SRC, "assets"), os.path.join(OUT, "assets"))
    pages = []
    for lang in ("en", "ar"):
        base = OUT if lang == "en" else os.path.join(OUT, "ar")

        def emit(file, key, fn, *a):
            p = Page(lang, file, key)
            out = fn(p, *a)
            write(os.path.join(base, p.href(file)), out)
            pages.append((lang, file))
            return out
        home_html = emit("index.html", "home", home)
        emit("about.html", "about", about)
        emit("services.html", "services", services)
        for i, s in enumerate(SERVICES):
            emit(f"service-{s['id']}.html", "services", service_page, i, s)
        emit("work.html", "work", work)
        for i, pr in enumerate(PROJECTS):
            emit(f"case-{pr['slug']}.html", "work", case, i, pr)
        emit("insights.html", "insights", insights)
        for a in ARTICLES:
            if a.get("slug"):
                emit(f"insight-{a['slug']}.html", "insights", article, a)
        emit("contact.html", "contact", contact)
        if ARTIFACT and lang == "en":
            m = re.match(r"(?s)<!doctype html>\s*<html[^>]*>\s*<head>(.*?)</head>\s*<body[^>]*>(.*)</body>\s*</html>\s*$", home_html)
            head_inner, body_inner = m.group(1), m.group(2)
            head_inner = re.sub(r'<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', "", head_inner)
            head_inner = re.sub(r"<title>.*?</title>", "<title>Seema · سيمة</title>", head_inner)
            boot = "<script>(function(d){d.lang='en';d.dir='ltr';d.classList.add('js');})(document.documentElement)</script>"
            write(os.path.join(ROOT, "dist-artifact", "_entry.html"), head_inner + boot + body_inner)
    if not ARTIFACT:
        urls = "".join(f"<url><loc>{SITE['domain']}/{'ar/' if l == 'ar' else ''}{'' if f == 'index.html' else f}</loc></url>" for l, f in pages)
        write(os.path.join(OUT, "sitemap.xml"), f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
        write(os.path.join(OUT, "robots.txt"), f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n")
    print(f"Built {len(pages)} pages -> {OUT}")


if __name__ == "__main__":
    build()
