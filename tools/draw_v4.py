#!/usr/bin/env python3
"""Front page for Saturday 21 November 2026, built from the day's verified digest.

Every illustration here is an original vector drawing made with Pillow.
The layout carries 35 dated stories, region counts, a location map, a wire
list, and a date check that separates 21 November reporting from earlier news.
"""
from PIL import Image, ImageDraw, ImageFont

F = "C:/Windows/Fonts/"
def font(name, size):
    return ImageFont.truetype(F + name, size)

INK = (24, 28, 36)
PAPER = (253, 251, 246)
RED = (163, 28, 32)
RED_D = (133, 21, 25)
TEAL = (22, 96, 108)
GOLD = (170, 116, 12)
PURPLE = (84, 60, 124)
GREEN = (40, 110, 72)
NAVY = (34, 46, 70)
GREY = (94, 100, 112)
FAINT = (226, 222, 213)
WHITE = (255, 255, 255)
NIGHT = (34, 45, 74)

SERIF = font("georgia.ttf", 62)
SERIF_SM = font("georgia.ttf", 22)
SERIF_IT = font("georgiai.ttf", 19)
SMALLB = font("arialbd.ttf", 13)
MICRO = font("arial.ttf", 11)
MICROB = font("arialbd.ttf", 11)
HEAD = font("arialbd.ttf", 19)
CARDHEAD = font("arialbd.ttf", 13)
BODY = font("arial.ttf", 12.5)
TAGF = font("arialbd.ttf", 10.5)
BADGE = font("arialbd.ttf", 9)
WIREF = font("arial.ttf", 10.5)

im = Image.new("RGB", (1024, 1024), PAPER)
d = ImageDraw.Draw(im)

def textw(s, fnt):
    return d.textlength(s, font=fnt)

def wrap(s, fnt, maxw):
    lines, cur = [], ""
    for w in s.split():
        t = (cur + " " + w).strip()
        if textw(t, fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def lines(s, fnt, x, y, maxw, n, fill, lh=None, size=None):
    lh = lh or (size or (fnt.size + 3))
    for i, ln in enumerate(wrap(s, fnt, maxw)[:n]):
        d.text((x, y + i * lh), ln, font=fnt, fill=fill)
    return y + len(wrap(s, fnt, maxw)[:n]) * lh

def clip(s, fnt, maxw):
    out = s
    while out and textw(out + "…", fnt) > maxw:
        out = out[:-1]
    return out + "…"

# ---------------- masthead ----------------
d.rectangle([0, 0, 1024, 26], fill=NAVY)
d.text((18, 6), "THE WORLD IN ONE DAY", font=font("arialbd.ttf", 14), fill=WHITE)
d.text((1006, 6), "35 STORIES  ·  7 REGIONS  ·  EVERY ONE DATED SATURDAY 21 NOVEMBER 2026",
       font=font("arial.ttf", 12), fill=(214, 224, 236), anchor="ra")
d.text((512, 32), "Saturday 21 November 2026", font=SERIF, fill=INK, anchor="ma")
d.text((512, 104), "COP31 talks run into overtime  ·  missiles over Riyadh  ·  a quake shakes Peru",
       font=SERIF_IT, fill=GREY, anchor="ma")
d.line([18, 132, 1006, 132], fill=RED, width=3)

# ---------------- lead statistics ----------------
STATS = [
    ("DAY 13", "day of COP31 — meant to close on day 12", RED),
    ("3", "missiles shot down over Riyadh", RED),
    ("6.7", "magnitude of the Peru quake", RED),
    ("146", "people safe after the Davao landing", RED),
    ("$58,983", "bitcoin early Saturday, down 3.9% in a day", TEAL),
    ("124*", "K L Rahul's score at tea in Wellington", TEAL),
]
CW = 988 / 6
for i, (big, cap, col) in enumerate(STATS):
    x = 18 + i * CW
    d.text((x + 8, 140), big, font=font("georgia.ttf", 29), fill=col)
    lines(cap, font("arial.ttf", 11.5), x + 8, 174, CW - 18, 2, GREY, 14)
    if i:
        d.line([x, 142, x, 202], fill=FAINT, width=2)
d.line([18, 206, 1006, 206], fill=FAINT, width=2)

# ---------------- region bar ----------------
REGIONS = [("EUROPE  4", NAVY, 118), ("ASIA  10", RED, 128),
           ("MIDDLE EAST  5", GOLD, 152), ("AFRICA  1", GREEN, 108),
           ("AMERICAS  11", PURPLE, 140), ("OCEANIA  3", TEAL, 124),
           ("GLOBAL  1", GREY, 106)]
x = 18
for label, col, width in REGIONS:
    d.rectangle([x, 212, x + width, 232], fill=col)
    d.text((x + width / 2, 216), label, font=TAGF, fill=WHITE, anchor="ma")
    x += width + 4

# ---------------- illustration helpers ----------------
def label_bar(x, y, w, label, col=RED):
    d.rectangle([x, y, x + w, y + 22], fill=col)
    d.text((x + 7, y + 5), label, font=TAGF, fill=WHITE)

def night_city(x, y, w, h, flare=True):
    d.rectangle([x, y, x + w, y + h], fill=NIGHT)
    for i in range(7):
        bw = 22 + (i * 7) % 16
        bx = x + 8 + i * (w - 20) / 7
        bh = 24 + (i * 13) % 34
        d.rectangle([bx, y + h - bh, bx + bw, y + h], fill=(20, 28, 49))
        for r in range(3):
            for c in range(2):
                if (i + r + c) % 3:
                    d.rectangle([bx + 5 + c * 9, y + h - bh + 6 + r * 9,
                                 bx + 9 + c * 9, y + h - bh + 10 + r * 9], fill=(244, 202, 96))
    if flare:
        import math
        for a in range(20, 161, 10):
            t = math.radians(a)
            d.line([x + w / 2 + 40 * math.cos(t), y + h - 12 - 40 * math.sin(t),
                    x + w / 2 + 82 * math.cos(t), y + h - 12 - 82 * math.sin(t)],
                   fill=(250, 214, 130), width=2)
        d.ellipse([x + w / 2 + 76, y + h - 90, x + w / 2 + 96, y + h - 70], fill=(255, 236, 170))

def cop_globe(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 236))
    d.ellipse([x + 18, y + 14, x + 108, y + 94], fill=(112, 174, 200), outline=TEAL, width=2)
    d.ellipse([x + 40, y + 28, x + 60, y + 46], fill=GREEN)
    d.ellipse([x + 66, y + 50, x + 88, y + 70], fill=GREEN)
    d.ellipse([x + 26, y + 56, x + 40, y + 66], fill=GREEN)
    d.rectangle([x + 128, y + 20, x + 140, y + 84], fill=WHITE, outline=RED, width=2)
    d.ellipse([x + 122, y + 56, x + 146, y + 76], fill=RED)
    d.ellipse([x + 164, y + 20, x + 214, y + 70], fill=WHITE, outline=NAVY, width=2)
    d.line([x + 189, y + 45, x + 189, y + 27], fill=NAVY, width=2)
    d.line([x + 189, y + 45, x + 202, y + 51], fill=NAVY, width=2)
    d.text((x + 140, y + 2), "+1.5C", font=BADGE, fill=RED)
    d.text((x + 176, y + 74), "DAY 13", font=BADGE, fill=NAVY)

def quake_scene(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 235, 242))
    d.line([x + 8, y + 34, x + w - 8, y + 34], fill=RED, width=2)
    import math
    pts = []
    for i in range(int(w - 20)):
        px = x + 10 + i
        amp = 16 if 40 < i < 120 else 2
        py = y + 34 + amp * math.sin(i / 4.5) * (1 if (i // 17) % 2 else -1)
        pts.append((px, py))
    d.line(pts, fill=RED, width=2)
    for i, bx in enumerate((20, 78, 142, 206)):
        bw = 42
        d.rectangle([x + bx, y + h - 40, x + bx + bw, y + h - 12], fill=(224, 156, 108))
        d.polygon([(x + bx - 4, y + h - 40), (x + bx + bw / 2, y + h - 58),
                   (x + bx + bw + 4, y + h - 40)], fill=(168, 68, 56))
    d.text((x + 8, y + 4), "6.7", font=font("arialbd.ttf", 18), fill=RED)
    d.text((x + w - 74, y + 5), "00:09 UTC", font=BADGE, fill=NAVY)
    d.text((x + w - 96, y + h - 70), "108 KM DEEP", font=BADGE, fill=NAVY)

def icon_small(kind, x, y):
    """Small original pictograms for the ten card grid."""
    if kind == "bridge":
        d.line([x, y + 18, x + 60, y + 18], fill=NAVY, width=3)
        d.line([x + 10, y + 18, x + 10, y + 6], fill=NAVY, width=2)
        d.line([x + 50, y + 18, x + 50, y + 6], fill=NAVY, width=2)
        d.line([x, y + 7, x + 60, y + 7], fill=NAVY, width=2)
        d.line([x + 28, y + 18, x + 34, y + 2], fill=RED, width=3)
    elif kind == "drone":
        d.line([x + 6, y + 10, x + 54, y + 10], fill=NAVY, width=3)
        d.ellipse([x + 26, y + 6, x + 36, y + 14], fill=NAVY)
        for cx in (x + 10, x + 50):
            d.ellipse([cx - 8, y + 2, cx + 8, y + 8], outline=NAVY, width=2)
        d.line([x + 58, y + 2, x + 42, y + 16], fill=RED, width=3)
    elif kind == "atom":
        d.ellipse([x + 18, y + 2, x + 46, y + 22], outline=TEAL, width=2)
        d.ellipse([x + 8, y + 10, x + 56, y + 18], outline=RED, width=2)
        d.ellipse([x + 28, y + 14, x + 36, y + 22], fill=NAVY)
    elif kind == "tax":
        d.rectangle([x + 6, y + 6, x + 34, y + 26], fill=(230, 226, 214), outline=NAVY)
        d.line([x + 40, y + 6, x + 58, y + 24], fill=RED, width=4)
        d.line([x + 58, y + 6, x + 40, y + 24], fill=RED, width=4)
        d.text((x + 9, y + 8), "%", font=BADGE, fill=NAVY)
    elif kind == "flags":
        d.rectangle([x + 6, y + 6, x + 30, y + 24], fill=RED)
        d.ellipse([x + 12, y + 10, x + 18, y + 16], fill=GOLD)
        d.rectangle([x + 34, y + 6, x + 58, y + 24], fill=WHITE, outline=NAVY)
        d.ellipse([x + 42, y + 10, x + 52, y + 20], fill=RED)
    elif kind == "plane":
        d.polygon([(x + 2, y + 16), (x + 54, y + 8), (x + 60, y + 14),
                   (x + 26, y + 20), (x + 18, y + 28), (x + 12, y + 26),
                   (x + 14, y + 19)], fill=NAVY)
        d.line([x + 40, y + 18, x + 52, y + 2], fill=GREEN, width=3)
    elif kind == "ai":
        for i in range(4):
            d.ellipse([x + 8 + i * 13, y + 8 + (i % 2) * 7,
                       x + 16 + i * 13, y + 16 + (i % 2) * 7], fill=PURPLE)
        d.line([x + 12, y + 13, x + 55, y + 13], fill=PURPLE, width=2)
    elif kind == "bitcoin":
        d.ellipse([x + 16, y + 2, x + 44, y + 28], fill=GOLD)
        d.text((x + 23, y + 7), "B", font=font("arialbd.ttf", 16), fill=WHITE)
        d.line([x + 48, y + 22, x + 58, y + 12, x + 64, y + 16], fill=RED, width=3)
    elif kind == "car":
        d.rectangle([x + 4, y + 12, x + 54, y + 24], fill=RED)
        d.polygon([(x + 16, y + 12), (x + 24, y + 4), (x + 42, y + 4),
                   (x + 48, y + 12)], fill=RED)
        for cx in (x + 14, x + 44):
            d.ellipse([cx - 5, y + 21, cx + 5, y + 31], fill=NAVY)
        d.rectangle([x + 56, y + 4, x + 62, y + 24], fill=NAVY)
    elif kind == "cricket":
        d.ellipse([x + 6, y + 4, x + 26, y + 24], fill=RED)
        d.arc([x + 10, y + 6, x + 22, y + 22], start=250, end=70, fill=WHITE, width=2)
        for sx in (x + 36, x + 44, x + 52):
            d.line([sx, y + 2, sx, y + 26], fill=NAVY, width=3)
        d.line([x + 32, y + 9, x + 56, y + 9], fill=NAVY, width=2)

# ---------------- three lead stories ----------------
LEADS = [
    (1, "Riyadh · Jizan", "WAR", "SAUDI: MISSILES", "night",
     "Three missiles down over the capital",
     "Saudi defences destroyed three ballistic missiles aimed at Riyadh before dawn, the third night running. No damage or casualties. (Reuters, AFP)",
     "OFFICIAL", RED),
    (2, "Antalya · Türkiye", "CLIMATE", "COP31 IN OVERTIME", "cop",
     "Climate talks miss their deadline",
     "Nearly 200 countries missed Friday's 6pm close. A draft with no fossil-fuel mention split the summit; a third text is due Saturday. (AP, AFP)",
     "CONFIRMED", TEAL),
    (3, "Junín · Peru", "EARTHQUAKE", "QUAKE IN PERU", "quake",
     "Deep 6.7 quake rattles central Peru",
     "The quake struck 108 km beneath the Andes and was felt in Lima. Peru's institute reported no deaths, damage or tsunami risk. (USGS, IGP)",
     "RISK", GOLD),
]
LW = (988 - 24) / 3
for i, (num, place, section, tag, art, head, body, badge, col) in enumerate(LEADS):
    x = 18 + i * (LW + 12)
    y = 240
    d.rectangle([x, y, x + LW, y + 194], fill=WHITE, outline=FAINT, width=2)
    iy, ih = y + 3, 80
    if art == "night":
        night_city(x + 3, iy, LW - 6, ih)
    elif art == "cop":
        cop_globe(x + 3, iy, LW - 6, ih)
    else:
        quake_scene(x + 3, iy, LW - 6, ih)
    label_bar(x + 3, iy + ih - 22, LW - 6, tag, col)
    bw = textw(badge, BADGE) + 12
    d.rounded_rectangle([x + LW - bw - 12, iy + 5, x + LW - 12, iy + 21], radius=5,
                        fill=(245, 242, 233), outline=col, width=1)
    d.text((x + LW - bw / 2 - 12, iy + 8), badge, font=BADGE, fill=col, anchor="ma")
    d.text((x + 10, y + 88), f"{num} · {place} · {section}", font=TAGF, fill=col)
    ty = y + 105
    for ln in wrap(head, HEAD, LW - 20)[:2]:
        d.text((x + 9, ty), ln, font=HEAD, fill=INK)
        ty += 21
    lines(body, BODY, x + 9, y + 150, LW - 20, 3, GREY, 13)

# ---------------- ten smaller stories ----------------
CARDS = [
    (4, "KYIV WARNING", "bridge", "Crimea bridge 'will not stay'", "Warns of more double-tap strikes.", "NBC", "REPORTED", RED),
    (5, "HORMUZ: DRONE", "drone", "Iran says it downed US drone", "No confirmation from Washington.", "IRIB", "REPORTED", RED),
    (6, "IRAN: URANIUM", "atom", "Iran: uranium stays in country", "Minister sees a 'fair solution'.", "ToI", "OFFICIAL", TEAL),
    (7, "TRUMP: AI TAX", "tax", "Trump vows tax on data centres", "'Tremendous' penalty, no details.", "ABC", "REPORTED", GOLD),
    (8, "CHINA–JAPAN", "flags", "China chides Japan on Taiwan", "Tokyo: stance unchanged.", "Ministry · AFP", "OFFICIAL", RED),
    (9, "DAVAO: 146 SAFE", "plane", "Jet lands after engine fire alert", "767 diverts after midnight.", "Airline · AP", "OFFICIAL", GREEN),
    (10, "CANBERRA: AI", "ai", "Australia, China agree AI talks", "Albanese ends an 11-day trip.", "ABC", "OFFICIAL", PURPLE),
    (11, "BITCOIN $58,983", "bitcoin", "Bitcoin slips below $59,000", "Down 3.9%; ether $1,625.", "CoinGecko", "CONFIRMED", GOLD),
    (12, "RUSSELL P1", "car", "Russell fastest in Vegas practice", "1:34.041 in a damp session.", "Formula 1", "OFFICIAL", RED),
    (13, "RAHUL 124*", "cricket", "Rahul century puts India on top", "India 344/2 at tea vs 368.", "AP", "OFFICIAL", TEAL),
]
CW2 = (988 - 4 * 10) / 5
for i, (num, tag, art, head, body, src, badge, col) in enumerate(CARDS):
    row, colidx = divmod(i, 5)
    x = 18 + colidx * (CW2 + 10)
    y = 442 + row * 98
    d.rectangle([x, y, x + CW2, y + 92], fill=WHITE, outline=FAINT, width=2)
    d.rectangle([x, y, x + CW2, y + 18], fill=(242, 239, 231))
    d.text((x + 6, y + 3), tag, font=TAGF, fill=col)
    icon_small(art, x + 6, y + 22)
    lines(head, CARDHEAD, x + 72, y + 23, CW2 - 78, 2, INK, 15)
    lines(body, font("arial.ttf", 10), x + 72, y + 55, CW2 - 78, 2, GREY, 11)
    d.text((x + 6, y + 78), f"({src})", font=font("arial.ttf", 9.5), fill=GREY)
    bw = textw(badge, BADGE) + 8
    d.rectangle([x + CW2 - bw - 5, y + 76, x + CW2 - 5, y + 88], fill=col)
    d.text((x + CW2 - bw / 2 - 5, y + 78), badge, font=BADGE, fill=WHITE, anchor="ma")

# ---------------- where it happened ----------------
d.text((18, 644), "WHERE IT HAPPENED — STORIES 1–13", font=SMALLB, fill=INK)
d.line([18, 661, 446, 661], fill=INK, width=2)
mx, my, mw, mh = 18, 666, 428, 226
d.rectangle([mx, my, mx + mw, my + mh], fill=(236, 233, 223), outline=FAINT)

def poly(points, fillc, outc=(170, 166, 154)):
    d.polygon([(mx + px * mw, my + py * mh) for px, py in points], fill=fillc, outline=outc)

LAND = (206, 202, 187)
# rough continent silhouettes, enough to read as a world map at this size
poly([(0.07, 0.16), (0.16, 0.10), (0.26, 0.12), (0.30, 0.20), (0.26, 0.30),
      (0.21, 0.32), (0.19, 0.42), (0.15, 0.38), (0.13, 0.27), (0.07, 0.24)], LAND)
poly([(0.21, 0.44), (0.28, 0.42), (0.31, 0.52), (0.29, 0.66), (0.26, 0.78),
      (0.23, 0.86), (0.20, 0.74), (0.20, 0.58)], LAND)
poly([(0.44, 0.20), (0.49, 0.16), (0.52, 0.22), (0.50, 0.30), (0.46, 0.32),
      (0.43, 0.27)], LAND)
poly([(0.45, 0.34), (0.54, 0.32), (0.57, 0.42), (0.53, 0.58), (0.49, 0.68),
      (0.46, 0.56), (0.44, 0.44)], LAND)
poly([(0.53, 0.18), (0.70, 0.12), (0.86, 0.16), (0.92, 0.26), (0.86, 0.38),
      (0.74, 0.40), (0.68, 0.34), (0.58, 0.36), (0.54, 0.28)], LAND)
poly([(0.80, 0.68), (0.88, 0.64), (0.92, 0.72), (0.88, 0.82), (0.81, 0.80)], LAND)

GEO = [(1,36.9,30.7),(2,24.7,46.7),(3,-11.2,-76.0),(4,50.5,30.5),(5,26.6,56.3),
       (6,35.7,51.4),(7,38.9,-77.0),(8,39.9,116.4),(9,7.2,125.5),(10,-35.3,149.1),
       (12,36.2,-115.1),(13,-41.3,174.8)]
for n, lat, lon in GEO:
    gx = mx + (lon + 180) / 360 * mw
    gy = my + (90 - lat) / 180 * mh * 0.92 + 8
    r = 9
    d.ellipse([gx - r, gy - r, gx + r, gy + r], fill=RED, outline=WHITE, width=2)
    d.text((gx, gy + 0.5), str(n), font=font("arialbd.ttf", 10), fill=WHITE, anchor="mm")
d.text((22, my + mh - 16), "Each number is a story on this page.", font=font("arial.ttf", 10), fill=GREY)

# ---------------- wire list ----------------
wx = 458
d.text((wx, 644), "ALSO ON SATURDAY 21 NOVEMBER 2026 — 22 MORE STORIES", font=SMALLB, fill=INK)
d.line([wx, 661, 1006, 661], fill=INK, width=2)
WIRE = [
    "14 Kryvyi Rih double strike kills 2, injures 42 (Kyiv Ind.)",
    "15 Cameroon: region chief Babseko expelled over a plot (Al Jazeera)",
    "16 Antalya: EU warn COP31 risks a 'total failure' (AP)",
    "17 Panama threatens to block the climate text (Al Jazeera)",
    "18 Indonesia's PLN signs six clean-power deals (Antara)",
    "19 Yemen: Houthis threaten Jeddah, Red Sea ports (Al Jazeera)",
    "20 Washington: Vance says Iran strikes were Trump's decision (Reuters)",
    "21 Lawmakers threaten SpaceX's federal funding (CNN)",
    "22 Texas: execution of a man of 70 takes 63 minutes (ABC)",
    "23 Jury convicts man of starting Palisades fire (ABC)",
    "24 Judge approves $7.25bn Roundup settlement (AFP)",
    "25 Canada rests defence in youth climate trial (AFP)",
    "26 Hong Kong: strong quake kills four (AP)",
    "27 Freight train derails near Seoul; no one hurt (Kyodo)",
    "28 Taipei: budget and NT$10,000 cash payout passed",
    "29 Bangkok: six-point plan on arsenic in two rivers (The Nation)",
    "30 Pakistan minister joins SCO forum in India (Dawn)",
    "31 Rain alert as cyclone remnants move inland (IMD)",
    "32 Rights groups urge sanctions after Myanmar ruling (AP)",
    "33 Portugal: Lisbon port authority tax cuts to 15 states",
    "34 Cummins keeps the Australian captaincy (ABC)",
    "35 Verstappen sent to stewards after Las Vegas contact (Autosport)",
]
for i, s in enumerate(WIRE):
    col, row = divmod(i, 11)
    d.text((wx + col * 276, 666 + row * 20.2), clip(s, WIREF, 272), font=WIREF, fill=INK)

# ---------------- date check ----------------
d.rectangle([18, 900, 1006, 958], fill=(250, 246, 236), outline=RED, width=2)
d.rectangle([18, 900, 150, 922], fill=RED)
d.text((84, 904), "DATE CHECK", font=TAGF, fill=WHITE, anchor="ma")
d.text((160, 904), "Left out as FRIDAY 20 NOVEMBER news: Wall Street's rout, the Kryvyi Rih barrage, the missile in Poland,",
       font=font("arial.ttf", 10.5), fill=INK)
d.text((160, 918), "Cyclone Akvan's landfall, the UK–EU deal. Older still: Voyager 1's flight-day (18 Nov). Not confirmed when drawn,",
       font=font("arial.ttf", 10.5), fill=INK)
d.text((160, 932), "so not shown: BepiColombo at Mercury and a final COP31 text. Every story above was reported on 21 November.",
       font=font("arial.ttf", 10.5), fill=INK)
d.text((24, 944), "Sources beside each story  ·  original drawings  ·  CONFIRMED = 2+ outlets  ·  OFFICIAL = on the record  ·  REPORTED = one side's account",
       font=font("arial.ttf", 9), fill=GREY)

d.text((18, 966), "Every story here happened, or was first reported, on Saturday 21 November 2026.",
       font=font("arial.ttf", 10), fill=GREY)
d.text((1006, 966), "21 NOV 2026  ·  ONE DAY, ONE IMAGE", font=font("arial.ttf", 10), fill=GREY, anchor="ra")

im.save("entry.png", optimize=True)
print("wrote entry.png v4", im.size)
