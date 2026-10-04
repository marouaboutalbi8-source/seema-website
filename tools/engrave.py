# -*- coding: utf-8 -*-
"""Turn a photograph into a line engraving: Cloud lines on Indigo.
    python3 tools/engrave.py hero-souq-night
writes src/assets/img/<name>-engrave.jpg (+ -sm)."""
import os, sys
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "..", "src", "assets", "img")
INDIGO = np.array([27, 24, 71], float) / 255
CLOUD = np.array([247, 245, 240], float) / 255


def blur(a, r):
    return np.asarray(Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r)), float) / 255


def engrave(name, period=5.2):
    im = Image.open(os.path.join(IMG, name + ".jpg")).convert("L")
    L = np.asarray(im, float) / 255
    lo, hi = np.percentile(L, 2), np.percentile(L, 99.5)
    L = np.clip((L - lo) / (hi - lo), 0, 1)
    Ls = blur(L, 2.2)
    h, w = L.shape
    y, x = np.mgrid[0:h, 0:w].astype(float)
    # contour-following warp: lines bend with the large-scale tone
    warp = blur(L, 18) * 9.0
    def hatch(angle, per, thick, gain):
        a = np.deg2rad(angle)
        ph = (x * np.sin(a) + y * np.cos(a) + warp * per) / per
        d = np.abs(ph - np.round(ph)) * 2          # 0 at line centre .. 1 between lines
        t = np.clip(thick, 0, 1)
        return np.clip((t - d) / 0.18 + 0.5, 0, 1) * gain
    tone = np.clip((Ls - .07) / .93, 0, 1) ** 0.9
    ink = hatch(-14, period, tone * 0.95, 1.0)
    ink = np.maximum(ink, hatch(58, period * 1.15, np.clip((tone - .45) / .55, 0, 1) * .8, .85))
    ink = np.maximum(ink, hatch(-74, period * 1.3, np.clip((tone - .75) / .25, 0, 1) * .7, .7))
    # contours
    gx = np.zeros_like(Ls); gy = np.zeros_like(Ls)
    gx[:, 1:-1] = Ls[:, 2:] - Ls[:, :-2]; gy[1:-1] = Ls[2:] - Ls[:-2]
    edge = np.clip((np.hypot(gx, gy) - .045) * 7, 0, 1)
    ink = np.maximum(ink * .82, edge * .7)
    ink = blur(ink, .6)
    rgb = INDIGO[None, None] * (1 - ink[..., None]) + CLOUD[None, None] * ink[..., None]
    out = Image.fromarray((rgb * 255).astype(np.uint8))
    out.save(os.path.join(IMG, name + "-engrave.jpg"), quality=84, optimize=True, progressive=True)
    sm = out.resize((1000, round(1000 * h / w)), Image.LANCZOS)
    sm.save(os.path.join(IMG, name + "-engrave-sm.jpg"), quality=82, optimize=True, progressive=True)
    print(name, out.size)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        engrave(n)
