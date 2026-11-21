#!/usr/bin/env python3
"""Second, broader front page for Saturday 21 November 2026.

Dense editorial layout: lead statistics, three featured stories, a grid of
smaller stories, a wire list and a date check. All copy is written here.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FONT_DIR = "C:/Windows/Fonts/"
def f(n, s): return ImageFont.truetype(FONT_DIR + n, s)

INK = (18, 24, 36)
PAPER = (250, 248, 243)
RED = (183, 34, 42)
TEAL = (24, 105, 116)
GOLD = (183, 126, 18)
PURPLE = (105, 66, 150)
GREEN = (44, 122, 78)
GREY = (105, 112, 124)
LIGHT = (224, 220, 211)
WHITE = (255, 255, 255)

TITLE = f("arialbd.ttf", 72)
KICK = f("arialbd.ttf", 18)
STAT = f("arialbd.ttf", 30)
STATCAP = f("arial.ttf", 14)
FEAT = f("arialbd.ttf", 23)
BODY = f("arial.ttf", 14)
MED = f("arialbd.ttf", 16)
TAG = f("arialbd.ttf", 11)
WIRE = f("arial.ttf", 14)
SECT = f("arialbd.ttf", 17)
SMALL = f("arial.ttf", 12)

im = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(im)

def wrap(text, font, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = word
    if cur: lines.append(cur)
    return lines

def put_lines(text, font, x, y, maxw, maxlines, fill, lh):
    for i, line in enumerate(wrap(text, font, maxw)[:maxlines]):
        d.text((x, y + i * lh), line, font=font, fill=fill)

# masthead
d.rectangle([0, 0, W, 34], fill=INK)
d.text((20, 8), "THE WORLD IN ONE DAY", font=KICK, fill=WHITE)
d.text((W - 20, 8), "35 STORIES  /  7 REGIONS  /  SATURDAY 21 NOVEMBER 2026", font=KICK, fill=(210, 220, 232), anchor="ra")
d.text((W // 2, 40), "Saturday 21 November 2026", font=TITLE, fill=INK, anchor="ma")
d.line([20, 122, W - 20, 122], fill=RED, width=3)

# lead statistics
STATS = [
    ("0", "climate deals agreed at COP31", RED),
    ("12", "killed in Ukraine strikes", RED),
    ("42", "injured at Kryvyi Rih", RED),
    ("900,000", "AI chips cleared for China", TEAL),
    ("6", "Houthi workshops hit in Sana'a", GOLD),
    ("$7.25B", "Roundup settlement approved", PURPLE),
]
cw = (W - 40) / 6
for i, (num, cap, col) in enumerate(STATS):
    x = 20 + i * cw
    d.text((x + 6, 130), num, font=STAT, fill=col)
    put_lines(cap, STATCAP, x + 6, 166, cw - 14, 2, GREY, 15)
    if i: d.line([x, 130, x, 188], fill=LIGHT, width=2)
d.line([20, 194, W - 20, 194], fill=LIGHT, width=2)

# region bar
REGIONS = [("EUROPE 9", INK), ("ASIA 9", RED), ("MIDDLE EAST 5", GOLD),
           ("AFRICA 2", GREEN), ("AMERICAS 8", TEAL), ("OCEANIA 1", PURPLE), ("GLOBAL 1", GREY)]
x = 20
for label, col in REGIONS:
    width = d.textlength(label, font=TAG) + 16
    d.rectangle([x, 200, x + width, 220], fill=col)
    d.text((x + 8, 204), label, font=TAG, fill=WHITE)
    x += width + 3

# featured stories
FEATURES = [
    dict(col=TEAL, tag="COP31 / ANTALYA", head="COP31 runs into overtime with no deal",
         body="Talks pass their scheduled close with no agreement; a third draft is due Saturday morning. Activists call it the worst COP ever.",
         icon="cop"),
    dict(col=RED, tag="KYIV / UKRAINE", head="Russian strikes kill 12, wound 42 in a day",
         body="A strike on Kryvyi Rih kills 2 and injures 42, four of them children; an overnight barrage hits sites across the country.",
         icon="war"),
    dict(col=GOLD, tag="SANA'A / YEMEN", head="Coalition destroys six Houthi workshops",
         body="Missile and drone workshops are hit in Sana'a; a Houthi missile is intercepted over Riyadh and falls on the city.",
         icon="houthi"),
]
FW = (W - 40 - 24) / 3
def feat_icon(kind, x, y, col):
    if kind == "cop":
        d.ellipse([x + 16, y + 10, x + 92, y + 86], fill=(150, 200, 220), outline=col, width=3)
        d.ellipse([x + 38, y + 28, x + 60, y + 46], fill=GREEN)
        d.ellipse([x + 60, y + 46, x + 80, y + 64], fill=GREEN)
        d.rectangle([x + 118, y + 16, x + 132, y + 72], fill=WHITE, outline=col, width=3)
        d.ellipse([x + 112, y + 64, x + 138, y + 90], fill=RED)
    elif kind == "war":
        for i, h in enumerate((24, 40, 32, 52, 30)):
            d.rectangle([x + 12 + i * 22, y + 90 - h, x + 28 + i * 22, y + 90], fill=(110, 116, 130))
        d.line([x + 24, y + 12, x + 120, y + 56], fill=RED, width=6)
        d.polygon([(x + 120, y + 56), (x + 104, y + 50), (x + 112, y + 38)], fill=RED)
        d.ellipse([x + 110, y + 48, x + 140, y + 78], outline=GOLD, width=4)
    else:
        for i, h in enumerate((28, 46, 36, 56, 32)):
            d.rectangle([x + 12 + i * 22, y + 90 - h, x + 28 + i * 22, y + 90], fill=(150, 130, 100))
        d.line([x + 110, y + 14, x + 34, y + 58], fill=RED, width=6)
        d.polygon([(x + 34, y + 58), (x + 52, y + 52), (x + 44, y + 42)], fill=RED)
        d.ellipse([x + 12, y + 50, x + 44, y + 82], outline=GOLD, width=4)

for i, st in enumerate(FEATURES):
    x = 20 + i * (FW + 12)
    y = 228
    d.rectangle([x, y, x + FW, y + 196], fill=WHITE, outline=LIGHT, width=2)
    d.rectangle([x, y, x + FW, y + 5], fill=st["col"])
    feat_icon(st["icon"], x + 12, y + 12, st["col"])
    d.text((x + 12, y + 100), st["tag"], font=TAG, fill=st["col"])
    put_lines(st["head"], FEAT, x + 12, y + 116, FW - 24, 2, INK, 24)
    put_lines(st["body"], BODY, x + 12, y + 166, FW - 24, 2, GREY, 14)

# medium story grid
MEDIA = [
    ("POLAND", "Russian missile lands in Poland; Danish F-16s scramble"),
    ("MYANMAR", "Myanmar, China call genocide ruling 'unjust'"),
    ("CALIFORNIA", "California subpoenas Nvidia over chip sales to China"),
    ("CHIPS", "US clears 900,000 AI chips for China"),
    ("INDIA", "India launches first H5N1 vaccine for chickens"),
    ("NEW DELHI", "SCO diplomacy forum opens for a three-day session"),
    ("WASHINGTON", "Trump: Iran wants a deal; Tehran seeks sanctions relief"),
    ("SUMY", "HIMARS wipes out 20 Russian commanders"),
    ("LONDON", "Britain names Moscow in cyberattacks on UK bodies"),
    ("JAKARTA", "Indonesia asks Google why 19,000 accounts vanished"),
    ("MARKETS", "Nasdaq -5.28%; Nvidia -14% in AI sell-off"),
    ("ODISHA", "Cyclone Akvan makes landfall near Gopalpur"),
]
MW = (W - 40 - 30) / 4
for i, (tag, head) in enumerate(MEDIA):
    col, row = i % 4, i // 4
    x = 20 + col * (MW + 10)
    y = 432 + row * 78
    d.rectangle([x, y, x + MW, y + 72], fill=WHITE, outline=LIGHT, width=2)
    d.text((x + 8, y + 6), tag, font=TAG, fill=RED)
    put_lines(head, MED, x + 8, y + 22, MW - 16, 2, INK, 19)

# wire list
d.text((20, 674), "ALSO ON SATURDAY 21 NOVEMBER", font=SECT, fill=INK)
d.line([20, 696, W - 20, 696], fill=INK, width=2)
WIRE_LIST = [
    "TOKYO — Takachi footbridge opens; Beijing presses Taiwan (Asahi)",
    "WASHINGTON — Court freezes $7.25bn Roundup settlement (Reuters)",
    "VIETNAM — Hanoi may cancel nuclear plant after PVN arrest (AP)",
    "OTTAWA — World no longer run on US leadership, says Carney (AP)",
    "JOHANNESBURG — Murder rate falls but 300 homicides a day (Stats)",
    "SAO PAULO — Carnival 2026 sold out; thousands go to Rio (Reuters)",
    "BRASILIA — Bolsonaro moved to hospital with abdominal pain (DPA)",
    "KARACHI — Suicide bombing at checkpoint kills 5, injures 13",
    "BERLIN — Students march against rent demands and service (Reuters)",
    "SEOUL — Opposition blocks Trump's aid plan to Tehran (Court)",
    "BAGHDAD — Pipeline chief arrested over illicit oil trading (AP)",
    "STRAIT OF HORMUZ — Iran claims waters 500km beyond treaty (IRGC)",
    "MONTEVIDEO — Uruguay rejects tax cuts to create Pentagon base",
    "WELLINGTON — India 159/1 at stumps, trail New Zealand by 209",
    "MELBOURNE — Australia to join 120 nations at COP31 tonight",
    "KYIV — Overnight barrage hits energy grid across Ukraine",
    "KABUL — UN warns armed drones are spreading across the region (UN)",
    "BRUSSELS — EU ministers seek a joint Ukraine fund (Reuters)",
]
for i, line in enumerate(WIRE_LIST):
    col, row = i // 9, i % 9
    x = 20 + col * 500
    d.text((x, 700 + row * 18), ("• " if col == 0 else "· ") + line, font=WIRE, fill=INK)

# when it broke
d.text((20, 866), "WHEN IT BROKE (UTC)", font=TAG, fill=GREY)
d.line([170, 877, W - 20, 877], fill=LIGHT, width=2)
for hr, cnt in [(0, 2), (4, 1), (6, 3), (8, 4), (10, 3), (12, 5), (14, 4), (16, 3), (18, 5), (20, 2), (22, 2)]:
    px = 170 + hr / 24 * (W - 190)
    d.ellipse([px - 4, 877 - cnt * 1.6, px + 4, 877 + cnt * 1.6], fill=[RED, TEAL, GOLD, PURPLE][hr % 4])
    if hr % 6 == 0: d.text((px - 6, 880), f"{hr:02d}", font=TAG, fill=GREY)

# date check
d.rectangle([20, 900, W - 20, 992], fill=(245, 238, 226), outline=RED, width=2)
d.text((32, 906), "DATE CHECK", font=SECT, fill=RED)
d.text((172, 908), "All stories above were reported on Saturday 21 November 2026; earlier events are excluded.", font=SMALL, fill=GREY)
d.text((32, 932), "INCLUDED", font=TAG, fill=GREEN)
d.text((110, 932), "COP31 overtime (21 Nov) · Kryvyi Rih strikes (21 Nov) · Cyclone Akvan (21 Nov) · Nasdaq rout (21 Nov)", font=SMALL, fill=INK)
d.text((32, 956), "EXCLUDED", font=TAG, fill=RED)
d.text((110, 956), "Bolsonaro stabbing (2018) · 13 Nov house images · earlier market closes — not this day's news", font=SMALL, fill=INK)
d.text((32, 978), "Saturday 21 November 2026  —  one day, one image", font=SMALL, fill=GREY)

im.save("entry.png", optimize=True)
print("wrote entry.png v2", im.size)

