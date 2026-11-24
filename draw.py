#!/usr/bin/env python3
"""Draw the news-image entry for make.fun bounty news-image-20261124.

A one-page newspaper front page summing up Tuesday 24 November 2026:
date masthead, four stories across regions and fields, one ticker line.
Pure Pillow, system fonts only. Output: entry.png, 1024x1024, < 1 MiB.
Run: python3 draw.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
RED = (178, 34, 34)
GREY = (110, 108, 100)
SUMMARY = (60, 60, 60)

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
    "/usr/share/fonts/truetype/noto",
]


def font(bold=False, serif=False, size=28):
    names = []
    if serif:
        names += ["DejaVuSerif-Bold.ttf", "DejaVuSerif.ttf",
                  "LiberationSerif-Bold.ttf", "LiberationSerif-Regular.ttf"]
    elif bold:
        names += ["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf",
                  "NotoSans-Bold.ttf"]
    else:
        names += ["DejaVuSans.ttf", "LiberationSans-Regular.ttf",
                  "NotoSans-Regular.ttf"]
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, max_w, fill=INK, spacing=4):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def kicker(draw, x, y, label, color=RED, size=21):
    f = font(bold=True, size=size)
    draw.text((x, y), label, font=f, fill=color)
    return y + size + 3


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Outer frame.
d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=4)

# Top strip.
d.rectangle([10, 10, W - 11, 56], fill=INK)
strip = font(bold=True, size=23)
msg = "WORLD NEWS  •  ONE DAY IN ONE PICTURE"
d.text(((W - d.textlength(msg, font=strip)) / 2, 19), msg,
       font=strip, fill=(255, 255, 255))

# Masthead: the date must dominate (judge criterion 1).
date_f = font(bold=True, serif=True, size=52)
date = "TUESDAY 24 NOVEMBER 2026"
d.text(((W - d.textlength(date, font=date_f)) / 2, 66), date,
       font=date_f, fill=INK)
d.line([30, 132, W - 30, 132], fill=INK, width=3)
d.line([30, 138, W - 30, 138], fill=INK, width=1)
sub_f = font(size=20)
sub = "The day's most consequential stories, from Wall Street to Odesa to Seoul"
d.text(((W - d.textlength(sub, font=sub_f)) / 2, 146), sub,
       font=sub_f, fill=GREY)

# ---- Lead panel: Nvidia (184-444) ----
px, py, pw, ph = 22, 184, 980, 260
d.rectangle([px, py, px + pw, py + ph], outline=INK, width=3)
ix, iy, iw, ih = px + 12, py + 12, 400, ph - 24
d.rectangle([ix, iy, ix + iw, iy + ih], fill=(18, 52, 44))
# Faint grid.
for gy in (iy + 50, iy + 100, iy + 150, iy + 200):
    d.line([ix + 10, gy, ix + iw - 10, gy], fill=(40, 90, 76), width=1)
# Soaring chart line.
pts = [(ix + 20, iy + 180), (ix + 70, iy + 165), (ix + 120, iy + 175),
       (ix + 170, iy + 140), (ix + 220, iy + 150), (ix + 270, iy + 110),
       (ix + 320, iy + 80), (ix + 370, iy + 45)]
d.line(pts, fill=(80, 220, 120), width=6, joint="curve")
d.polygon([(ix + 370, iy + 45), (ix + 352, iy + 48), (ix + 364, iy + 62)],
          fill=(80, 220, 120))
d.text((ix + 16, iy + 10), "+31%", font=font(bold=True, size=52),
       fill=(255, 255, 255))
d.text((ix + 16, iy + ih - 32), "NASDAQ +6.5%  •  S&P +4.7%",
       font=font(bold=True, size=18), fill=(200, 255, 210))

# Lead text.
tx = ix + iw + 24
ty = kicker(d, tx, py + 14, "MARKETS  •  TECH")
ty = text_block(d, tx, ty + 2, "Huang returns, Nvidia soars 31%",
                font(bold=True, size=38), pw - iw - 48, spacing=2)
text_block(d, tx, ty + 10,
           "Board reinstates Jensen Huang as CEO; shares jump "
           "31%, adding $952 billion in a day. Nasdaq climbs 6.5%.",
           font(size=24), pw - iw - 48, fill=SUMMARY, spacing=4)

# ---- Middle row (458-706): Odesa (left) and Estonia (right) ----
my, mh, mw = 458, 252, 482


def panel(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], outline=INK, width=3)


# Odesa panel.
cx = 22
panel(cx, my, mw, mh)
cix, ciy, ciw, cih = cx + 12, my + 12, mw - 24, 84
d.rectangle([cix, ciy, cix + ciw, ciy + cih], fill=(30, 34, 52))
for sx, sy in [(200, 12), (250, 22), (270, 10)]:
    d.ellipse([cix + sx, ciy + sy, cix + sx + 3, ciy + sy + 3],
              fill=(220, 220, 200))
# Apartment blocks, mostly dark windows, a few lit.
for bx, by, bw in [(16, 30, 70), (100, 20, 70), (190, 36, 60)]:
    d.rectangle([cix + bx, ciy + by, cix + bx + bw, ciy + cih],
                fill=(64, 68, 84))
lit = {(28, 58), (136, 48), (202, 64)}
for wx in (28, 52, 112, 136, 202, 226):
    for wy in (30, 48, 66):
        if wx < 100 and wy < 40:
            continue
        if wx >= 190 and wy < 40:
            continue
        fill = (235, 190, 90) if (wx, wy) in lit else (44, 48, 60)
        d.rectangle([cix + wx, ciy + wy, cix + wx + 10, ciy + wy + 10],
                    fill=fill)
# Power pylon with a broken line.
d.line([cix + 290, ciy + cih, cix + 300, ciy + 20], fill=(180, 180, 180),
       width=3)
d.line([cix + 310, ciy + cih, cix + 300, ciy + 20], fill=(180, 180, 180),
       width=3)
d.line([cix + 285, ciy + 30, cix + 315, ciy + 30], fill=(180, 180, 180),
       width=3)
d.line([cix + 315, ciy + 28, cix + 356, ciy + 22], fill=(180, 180, 180),
       width=2)
d.line([cix + 356, ciy + 22, cix + 368, ciy + 32, cix + 380, ciy + 22,
        cix + 392, ciy + 30], fill=(255, 60, 60), width=3)
d.line([cix + 392, ciy + 30, cix + 440, ciy + 24], fill=(180, 180, 180),
       width=2)
d.text((cix + 392, ciy + 6), "ODESA", font=font(bold=True, size=18),
       fill=(255, 255, 255))
ty = kicker(d, cx + 14, my + 106, "UKRAINE  •  WAR")
ty = text_block(d, cx + 14, ty + 2,
                "Odesa freezes as Russia re-hits power lines",
                font(bold=True, size=30), mw - 28, spacing=2)
text_block(d, cx + 14, ty + 6,
           "Russia hits repaired lines again; 240,000 without "
           "heat, schools remote.",
           font(size=21), mw - 28, fill=SUMMARY, spacing=3)

# Estonia panel.
mx = 520
panel(mx, my, mw, mh)
mix, miy, miw, mih = mx + 12, my + 12, mw - 24, 84
d.rectangle([mix, miy, mix + miw, miy + mih], fill=(24, 44, 84))
# Border barrier, striped arm.
d.line([mix + 44, miy + mih, mix + 44, miy + 28], fill=(255, 255, 255),
       width=4)
for bx in range(44, 200, 16):
    fill = (200, 40, 40) if ((bx - 44) // 16) % 2 == 0 else (255, 255, 255)
    d.rectangle([mix + bx, miy + 28, mix + bx + 16, miy + 40], fill=fill)
# Dashed border line.
for dx in range(220, 446, 20):
    d.line([mix + dx, miy + 62, mix + dx + 12, miy + 62],
           fill=(255, 255, 255), width=2)
# Drone quad.
qx, qy = mix + 380, miy + 24
d.line([qx - 20, qy - 9, qx + 20, qy + 9], fill=(10, 10, 10), width=4)
d.line([qx - 20, qy + 9, qx + 20, qy - 9], fill=(10, 10, 10), width=4)
d.ellipse([qx - 7, qy - 7, qx + 7, qy + 7], fill=(10, 10, 10))
d.text((mix + 250, miy + 8), "TALLINN", font=font(bold=True, size=18),
       fill=(255, 255, 255))
ty = kicker(d, mx + 14, my + 106, "EUROPE  •  SECURITY")
ty = text_block(d, mx + 14, ty + 2, "Moscow warns Estonia of 'open war'",
                font(bold=True, size=30), mw - 28, spacing=2)
text_block(d, mx + 14, ty + 6,
           "Russia summons envoy over border closure; "
           "Tallinn denies the claim.",
           font(size=21), mw - 28, fill=SUMMARY, spacing=3)

# ---- Bottom row (720-968): Seoul (left) and Delta (right) ----
by, bh = 720, 252
# Seoul panel.
sx = 22
panel(sx, by, mw, bh)
six, siy, siw, sih = sx + 12, by + 12, mw - 24, 84
d.rectangle([six, siy, six + siw, siy + sih], fill=(20, 40, 80))
# Taegeuk-style circle.
d.ellipse([six + 42, siy + 14, six + 98, siy + 70], fill=(60, 100, 200),
          outline=(255, 255, 255), width=2)
d.pieslice([six + 42, siy + 14, six + 98, siy + 70], 180, 360,
           fill=(220, 60, 60))
d.text((six + 130, siy + 10), "SEOUL", font=font(bold=True, size=22),
       fill=(255, 255, 255))
d.text((six + 130, siy + 38), "FIRST WOMAN", font=font(bold=True, size=18),
       fill=(220, 180, 60))
d.text((six + 130, siy + 58), "SPY CHIEF", font=font(bold=True, size=18),
       fill=(220, 180, 60))
ty = kicker(d, sx + 14, by + 106, "POLITICS  •  ASIA")
ty = text_block(d, sx + 14, ty + 2, "Seoul names first woman spy chief",
                font(bold=True, size=30), mw - 28, spacing=2)
text_block(d, sx + 14, ty + 6,
           "Lee reshuffles security posts, tapping Kang Kum-sil "
           "to lead the NIS.",
           font(size=21), mw - 28, fill=SUMMARY, spacing=3)

# Delta panel.
px2 = 520
panel(px2, by, mw, bh)
pix, piy, piw, pih = px2 + 12, by + 12, mw - 24, 84
d.rectangle([pix, piy, pix + piw, piy + pih], fill=(70, 130, 190))
# Plane silhouette.
d.ellipse([pix + 36, piy + 34, pix + 220, piy + 56], fill=(255, 255, 255))
d.polygon([(pix + 100, piy + 44), (pix + 130, piy + 70), (pix + 150, piy + 70),
           (pix + 140, piy + 44)], fill=(255, 255, 255))
d.polygon([(pix + 190, piy + 40), (pix + 210, piy + 22), (pix + 220, piy + 22),
           (pix + 212, piy + 40)], fill=(255, 255, 255))
d.text((pix + 250, piy + 12), "2,100 DELAYED", font=font(bold=True, size=20),
       fill=(255, 255, 255))
d.text((pix + 250, piy + 38), "92 CANCELED MONDAY",
       font=font(bold=True, size=16), fill=(255, 220, 220))
d.text((pix + 250, piy + 60), "ATLANTA", font=font(bold=True, size=16),
       fill=(255, 255, 255))
ty = kicker(d, px2 + 14, by + 106, "TRAVEL  •  USA")
ty = text_block(d, px2 + 14, ty + 2, "Delta outage snarls Thanksgiving travel",
                font(bold=True, size=30), mw - 28, spacing=2)
text_block(d, px2 + 14, ty + 6,
           "A weight-and-balance glitch delays 2,100 flights; "
           "92 more canceled Monday.",
           font(size=21), mw - 28, fill=SUMMARY, spacing=3)

# ---- Footer ticker ----
d.rectangle([10, 980, W - 11, 1014], fill=INK)
tick_f = font(bold=True, size=18)
tick = ("ALSO:  INDONESIA FIRE: 24 DEAD, 30 MISSING   •   "
        "CHINA DEATH SENTENCE IN SPY CASE")
d.text(((W - d.textlength(tick, font=tick_f)) / 2, 987), tick,
       font=tick_f, fill=(255, 255, 255))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, optimize=True)
size = os.path.getsize(out)
print(f"saved {out} {img.size} {size} bytes "
      f"({'OK' if size <= 1048576 else 'TOO BIG'})")
