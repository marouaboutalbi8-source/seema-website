# -*- coding: utf-8 -*-
"""
v6 "Editions" components, after the Shopify Editions Winter '26 page:
a chapter rail, full-screen chapter openers with a giant word, torn-paper edges
between photo scenes and paper sections, and floating mock-ups over the photos.
"""
import html
import random

from content import L

esc = html.escape
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
AR_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")


def numeral(i, lang):
    return ROMAN[i] if lang == "en" else str(i + 1).translate(AR_DIGITS)


# ------------------------------------------------------------------ torn paper
def _edge(seed, w=1600, base=58):
    rnd = random.Random(seed)
    pts, y, x = [], base, 0.0
    while x < w:
        y += rnd.uniform(-7, 7) + (base - y) * 0.12
        if rnd.random() < 0.06:
            y += rnd.choice([-1, 1]) * rnd.uniform(10, 22)   # a deeper rip
        y = max(14, min(86, y))
        pts.append((x, y))
        x += rnd.uniform(5, 19)
    pts.append((w, y))
    return pts


def _fibres(pts, seed):
    rnd = random.Random(seed * 7 + 1)
    return [(x, y - rnd.uniform(1.5, 7.5)) for x, y in pts]


def tear(seed, where="top"):
    """An SVG strip of torn paper. 'top' sits above a paper section, 'bot' below it."""
    pts = _edge(seed)
    fib = _fibres(pts, seed)
    main = "M0 100 " + " ".join(f"L{x:.0f} {y:.1f}" for x, y in pts) + " L1600 100Z"
    lite = "M0 100 " + " ".join(f"L{x:.0f} {y:.1f}" for x, y in fib) + " L1600 100Z"
    return (f'<div class="tear tear-{where}" aria-hidden="true"><svg viewBox="0 0 1600 100" preserveAspectRatio="none">'
            f'<path class="fib" d="{lite}"/><path class="pap" d="{main}"/></svg></div>')


# ------------------------------------------------------------------ chapter rail
def rail(p, items):
    """items: [(chapter_id, L(label))]. A fixed index that lights up as you scroll."""
    lis = "".join(f'<li><a href="#{cid}" data-rail="{cid}"><span class="rl">{esc(p.t(lbl))}</span>'
                  f'<span class="rn">{numeral(i, p.lang)}</span></a></li>' for i, (cid, lbl) in enumerate(items))
    lab = p.t(L("Chapters", "الفصول"))
    return f'<nav class="rail" aria-label="{lab}"><ol>{lis}</ol></nav>'


# ------------------------------------------------------------------ mock-ups
BRAND = L("Your brand", "علامتك")


def _img(p, name):
    return f'<img src="{p.asset("img/" + name + "-sm.jpg")}" alt="" loading="lazy" decoding="async">'


def mk_browser(p, photo):
    t = p.t
    return f"""<div class="mk-browser">
  <div class="mk-bar"><i></i><i></i><i></i><span dir="ltr">yourbrand.qa</span></div>
  <div class="mk-site">
    <div class="mk-nav"><b>{esc(t(BRAND))}</b><span></span><span></span><span></span></div>
    <div class="mk-hero">{_img(p, photo)}<div><p class="mk-h">{esc(t(L("Welcome, properly.", "أهلاً، كما يليق.")))}</p><span class="mk-btn">{esc(t(L("Book a visit", "احجز زيارة")))}</span></div></div>
    <div class="mk-cols"><span></span><span></span><span></span></div>
  </div>
</div>"""


def mk_phone(p, photo):
    t = p.t
    return f"""<div class="mk-phone"><div class="mk-scr">
  <div class="mk-st"><span dir="ltr">9:41</span><i></i></div>
  <p class="mk-ttl">{esc(t(L("Good evening", "مساء الخير")))}</p>
  <div class="mk-pic">{_img(p, photo)}</div>
  <div class="mk-row"><span></span><b>{esc(t(L("Your booking", "حجزك")))}</b><em>{esc(t(L("Confirmed", "مؤكد")))}</em></div>
  <div class="mk-row"><span></span><b>{esc(t(L("Pay with one tap", "ادفع بلمسة")))}</b><em class="g"></em></div>
  <div class="mk-tab"><i></i><i></i><i></i><i></i></div>
</div></div>"""


def mk_identity(p):
    t = p.t
    return f"""<div class="mk-id">
  <div class="mk-card"><span class="mk-mono">{'A' if p.lang == 'en' else 'ع'}</span><div><b>{esc(t(BRAND))}</b><em>{esc(p.o(BRAND))}</em></div></div>
  <div class="mk-sw"><i style="background:#1B1847"></i><i style="background:#F7F5F0"></i><i style="background:#5F5B80"></i><i style="background:#EEEBF3"></i><i class="pt-sw"></i></div>
  <p class="mk-type"><span class="la">Aa</span><span class="ar" lang="ar">أب</span><em>{esc(t(L("Type in two scripts", "خط بلغتين")))}</em></p>
</div>"""


def mk_note(p):
    if p.lang == "en":
        body = 'For <u>[audience]</u> who <u>[need]</u>, we are the only <u>[category]</u> that <u>[difference]</u>.'
    else:
        body = 'لـ<u>[الجمهور]</u> الذين <u>[الحاجة]</u>، نحن الوحيدون في <u>[الفئة]</u> الذين <u>[الفرق]</u>.'
    t = p.t
    return f"""<div class="mk-note">
  <span class="mk-lbl">{esc(t(L("Positioning · draft 3", "التموضع · المسودة ٣")))}</span>
  <p>{body}</p>
  <div class="mk-sig"><i></i><span>{esc(t(L("Agreed by leadership", "اتفقت عليه القيادة")))}</span></div>
</div>"""


def mk_dash(p):
    t = p.t
    bars = "".join(f'<i style="--h:{h}%"></i>' for h in (38, 52, 44, 61, 58, 72, 66, 79, 74, 88, 83, 92))
    kp = [(L("Orders", "الطلبات"), "128"), (L("Low stock", "مخزون منخفض"), "3"), (L("Invoices", "الفواتير"), "42")]
    kpis = "".join(f'<div><em>{esc(t(a))}</em><b>{b if p.lang == "en" else b.translate(AR_DIGITS)}</b></div>' for a, b in kp)
    return f"""<div class="mk-dash">
  <div class="mk-dh"><b>{esc(t(L("Operations · Today", "العمليات · اليوم")))}</b><span>{esc(t(L("Live", "مباشر")))}</span></div>
  <div class="mk-kpis">{kpis}</div>
  <div class="mk-bars">{bars}</div>
</div>"""


def mk_post(p, photo):
    t = p.t
    return f"""<div class="mk-post">
  <div class="mk-ph"><i></i><b>{esc(t(BRAND))}</b><span>{esc(t(L("Sponsored", "مُموَّل")))}</span></div>
  <div class="mk-pic">{_img(p, photo)}</div>
  <div class="mk-act"><i></i><i></i><i></i></div>
  <p>{esc(t(L("Ramadan evenings, reserved for you.", "أمسيات رمضان، محجوزة لك.")))}</p>
</div>"""


def mk_ticket(p):
    t = p.t
    steps = [L("Reported", "أُبلغ عنه"), L("Assigned", "أُسند"), L("Fixed", "حُلّ")]
    times = ["09:12", "09:14", "10:02"]
    lis = "".join(f'<li><i></i><span>{esc(t(a))}</span><em dir="ltr">{b}</em></li>' for a, b in zip(steps, times))
    return f"""<div class="mk-tk">
  <div class="mk-tkh"><span dir="ltr">#2048</span><em>{esc(t(L("Resolved", "تم الحل")))}</em></div>
  <p>{esc(t(L("Email not syncing on new laptops", "البريد لا يتزامن على الأجهزة الجديدة")))}</p>
  <ol>{lis}</ol>
</div>"""


def mk_chip(p, text, pt_svg):
    return f'<div class="mk-chip">{pt_svg}<span>{esc(p.t(text))}</span></div>'


def collage(items):
    """items: [(html, start%, top%, width, depth, rotate_deg)]"""
    out = []
    for h, x, y, w, d, r in items:
        out.append(f'<div class="mk" data-depth="{d}" style="inset-inline-start:{x}%;top:{y}%;--w:{w};--r:{r}deg">{h}</div>')
    return f'<div class="collage" aria-hidden="true">{"".join(out)}</div>'


# ------------------------------------------------------------------ chapter opener
def initial(text, lang):
    if lang != "en" or not text:
        return esc(text)
    return f'<span class="ini">{esc(text[0])}</span>{esc(text[1:])}'


def opener(p, cid, i, photo_html, word, sub, other_word, extra="", collage_html="", heading_id=None):
    hid = heading_id or (cid + "-h")
    return f"""
<section class="opener" id="{cid}" data-chapter="{cid}" data-tone="dark" aria-labelledby="{hid}">
  <div class="op-stage">
    <div class="op-bg">{photo_html}</div>
    <div class="op-type">
      <div class="op-top"><span class="cap">{numeral(i, p.lang)}</span><span class="voice" lang="{p.ol}">{esc(other_word)}</span></div>
      <h2 class="op-word" id="{hid}">{esc(word)}</h2>
      <div class="op-foot"><p class="op-sub">{initial(sub, p.lang)}</p>{extra}</div>
    </div>
    {collage_html}
  </div>
</section>"""
