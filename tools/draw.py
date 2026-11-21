#!/usr/bin/env python3
"""Draw the 21 November 2026 world-news front page as a single PNG.

Standard library + Pillow only; run on the build machine, not in the grader.
Deterministic: same bytes on every run.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 244, 237)
INK = (16, 22, 34)
RED = (198, 42, 46)
TEAL = (28, 110, 122)
GOLD = (196, 138, 24)
GREY = (120, 128, 140)
LINE = (216, 212, 202)
FONT_DIR = "C:/Windows/Fonts/"

def f(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)

HEAVY = f("arialbd.ttf", 34)
HEAVY_SM = f("arialbd.ttf", 26)
BOLD = f("arialbd.ttf", 24)
SMALL = f("arialbd.ttf", 19)
TINY = f("arial.ttf", 17)
MAST = f("arialbd.ttf", 76)
KICKER = f("arialbd.ttf", 25)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrapped(text, font, max_w):
    """Wrap on spaces into lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ---------- masthead ----------
d.rectangle([0, 0, W, 156], fill=INK)
d.text((W // 2, 16), "S A T U R D A Y", font=KICKER, fill=(206, 214, 226), anchor="ma")
d.text((W // 2, 46), "21 NOVEMBER 2026", font=MAST, fill=(255, 255, 255), anchor="ma")
d.rectangle([0, 156, W, 164], fill=RED)
d.text((28, 176), "THE WORLD IN ONE IMAGE", font=BOLD, fill=INK)
d.text((W - 28, 176), "6 STORIES  /  4 REGIONS", font=BOLD, fill=RED, anchor="ra")
d.line([28, 208, W - 28, 208], fill=LINE, width=2)

# ---------- cards ----------
CARD_W, CARD_H = 474, 250
X0, Y0, GAP_X, GAP_Y = 28, 220, 20, 14
ICON = 120
TEXT_X = 150
TEXT_W = CARD_W - TEXT_X - 14

STORIES = [
    dict(region="AMERICAS", tag="MARKETS", accent=RED,
         headline="US stocks plunge in AI sell-off",
         detail="Nasdaq -5.28%  |  Nvidia -14%",
         foot="Dow -949.73   S&P 500 -265.44", icon="market"),
    dict(region="ASIA", tag="WEATHER", accent=TEAL,
         headline="Cyclone Akvan hits Odisha coast",
         detail="Landfall near Gopalpur",
         foot="High winds, heavy rain; no major damage", icon="cyclone"),
    dict(region="EUROPE", tag="UKRAINE", accent=RED,
         headline="Strikes hit Kryvyi Rih",
         detail="2 killed, 42 injured",
         foot="Four children among the wounded", icon="missile"),
    dict(region="AMERICAS", tag="BRAZIL", accent=GOLD,
         headline="Bolsonaro taken to hospital",
         detail="Severe abdominal pain",
         foot="Moved from house arrest in Brasilia", icon="hospital"),
    dict(region="ASIA", tag="PAKISTAN", accent=RED,
         headline="Checkpoint suicide bombing",
         detail="5 killed, 13 injured",
         foot="Car bomb at a security post", icon="blast"),
    dict(region="OCEANIA", tag="SPORT", accent=TEAL,
         headline="India fight back in Wellington",
         detail="India 159/1 at stumps",
         foot="Trail New Zealand by 209 runs", icon="cricket"),
]


def icon_market(box, accent):
    x, y, s = box
    d.rounded_rectangle([x, y, x + s, y + s], radius=16, fill=(250, 235, 235))
    d.line([x + 18, y + 22, x + 18, y + s - 18], fill=GREY, width=4)
    d.line([x + 18, y + s - 18, x + s - 16, y + s - 18], fill=GREY, width=4)
    pts = [(x + 24, y + 36), (x + 48, y + 52), (x + 66, y + 40),
           (x + 88, y + 74), (x + 104, y + 66), (x + 124, y + s - 26)]
    d.line(pts, fill=accent, width=9, joint="curve")
    d.polygon([(x + 124, y + s - 26), (x + 108, y + s - 32), (x + 118, y + s - 44)], fill=accent)


def icon_cyclone(box, accent):
    x, y, s = box
    d.rounded_rectangle([x, y, x + s, y + s], radius=16, fill=(229, 241, 242))
    cx, cy = x + s / 2, y + s / 2
    for r in range(58, 8, -10):
        d.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=300, fill=accent, width=8)
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=INK)


def icon_missile(box, accent):
    x, y, s = box
    d.rounded_rectangle([x, y, x + s, y + s], radius=16, fill=(250, 235, 235))
    base = y + s - 26
    for i, h in enumerate((26, 46, 34, 58, 40, 30)):
        bx = x + 14 + i * 19
        d.rectangle([bx, base - h, bx + 14, base], fill=(90, 96, 110))
    d.line([x + 18, y + 24, x + s - 34, y + 66], fill=accent, width=8)
    d.polygon([(x + s - 34, y + 66), (x + s - 50, y + 60), (x + s - 40, y + 48)], fill=accent)
    d.ellipse([x + 8, y + 14, x + 26, y + 32], fill=GOLD)


def icon_hospital(box, accent):
    x, y, s = box
    d.rounded_rectangle([x, y, x + s, y + s], radius=16, fill=(250, 242, 226))
    bx, by = x + 34, y + 30
    d.rectangle([bx, by, bx + 72, by + 80], fill=(255, 255, 255), outline=(170, 150, 110), width=3)
    d.rectangle([bx + 30, by + 16, bx + 42, by + 64], fill=accent)
    d.rectangle([bx + 16, by + 30, bx + 56, by + 42], fill=accent)
    d.rectangle([x + 26, y + s - 34, x + s - 26, y + s - 18], fill=(170, 150, 110))


def icon_blast(box, accent):
    x, y, s = box
    d.rounded_rectangle([x, y, x + s, y + s], radius=16, fill=(250, 235, 235))
    cx, cy = x + s / 2, y + s / 2
    for ang in range(0, 360, 45):
        import math
        rad = math.radians(ang)
        d.line([cx + 22 * math.cos(rad), cy + 22 * math.sin(rad),
                cx + 56 * math.cos(rad), cy + 56 * math.sin(rad)], fill=accent, width=7)
    d.ellipse([cx - 24, cy - 24, cx + 24, cy + 24], fill=GOLD)
    d.line([x + 8, y + s - 22, x + s - 8, y + s - 22], fill=(150, 155, 165), width=6)


def icon_cricket(box, accent):
    x, y, s = box
    d.rounded_rectangle([x, y, x + s, y + s], radius=16, fill=(229, 241, 242))
    cx, cy = x + 44, y + 48
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=accent)
    d.arc([cx - 8, cy - 22, cx + 8, cy + 22], start=250, end=70, fill=(255, 255, 255), width=3)
    for sx in (x + 88, x + 102, x + 116):
        d.line([sx, y + 24, sx, y + 96], fill=INK, width=7)
    d.line([x + 82, y + 36, x + 122, y + 36], fill=INK, width=6)
    d.line([x + 82, y + 74, x + 122, y + 74], fill=INK, width=6)


ICONS = dict(market=icon_market, cyclone=icon_cyclone, missile=icon_missile,
             hospital=icon_hospital, blast=icon_blast, cricket=icon_cricket)

for i, st in enumerate(STORIES):
    col, row = i % 2, i // 2
    x = X0 + col * (CARD_W + GAP_X)
    y = Y0 + row * (CARD_H + GAP_Y)
    d.rounded_rectangle([x, y, x + CARD_W, y + CARD_H], radius=12,
                        fill=(255, 255, 255), outline=LINE, width=2)
    d.rounded_rectangle([x, y, x + CARD_W, y + 6], radius=3, fill=st["accent"])
    ICONS[st["icon"]]((x + 14, y + 22, ICON), st["accent"])
    d.text((x + TEXT_X, y + 18), st["region"] + "  /  " + st["tag"], font=SMALL, fill=st["accent"])
    ty = y + 46
    for line in wrapped(st["headline"], HEAVY, TEXT_W)[:2]:
        d.text((x + TEXT_X, ty), line, font=HEAVY, fill=INK)
        ty += 39
    ty = y + 134
    for line in wrapped(st["detail"], HEAVY_SM, TEXT_W)[:2]:
        d.text((x + TEXT_X, ty), line, font=HEAVY_SM, fill=INK)
        ty += 28
    ty = y + 196
    for line in wrapped(st["foot"], SMALL, TEXT_W)[:2]:
        d.text((x + TEXT_X, ty), line, font=SMALL, fill=GREY)
        ty += 21

# ---------- footer ----------
d.text((28, 1000), "SATURDAY 21 NOVEMBER 2026  -  WORLD NEWS", font=TINY, fill=GREY)
d.text((W - 28, 1000), "ONE DAY  -  ONE IMAGE", font=TINY, fill=GREY, anchor="ra")

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
