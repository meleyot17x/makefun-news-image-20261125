# THE BEACON POST - drawing kit: palette, type helpers, flat layered
# scenes and the dotted world map. All artwork is original, drawn with
# PIL primitives for this page only.
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
PLAYFAIR_BLACK = FONT_DIR + "PlayfairDisplay-Black.ttf"
PLAYFAIR_BOLD = FONT_DIR + "PlayfairDisplay-Bold.ttf"
ARCHIVO = FONT_DIR + "Archivo.ttf"
ARCHIVO_BOLD = FONT_DIR + "Archivo-Bold.ttf"

# Turmeric paper + brown ink identity.
PAPER = (243, 197, 66)
PAPER_LIGHT = (250, 224, 138)
PAPER_CARD = (252, 231, 155)
INK = (56, 34, 14)
INK_SOFT = (104, 68, 28)
RUST = (150, 52, 20)
CREAM = (252, 236, 175)
WHITE = (255, 250, 235)

REGION_COLORS = {
    "EUROPE": (35, 62, 112),
    "MIDDLE EAST": (156, 59, 30),
    "WORLD": (96, 80, 58),
    "AFRICA": (104, 122, 40),
    "AMERICAS": (120, 60, 122),
    "ASIA": (186, 106, 8),
    "SOUTH ASIA": (12, 116, 106),
    "ASIA-PACIFIC": (92, 78, 158),
    "OCEANIA": (0, 122, 152),
}

_cache = {}


def font(path, size):
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size)
    return _cache[key]


def text_w(draw, s, fnt):
    return draw.textlength(s, font=fnt)


def fit_font(draw, s, path, start, max_w, min_size=8):
    size = start
    while size > min_size and text_w(draw, s, font(path, size)) > max_w:
        size -= 1
    return font(path, size)


def wrap(draw, s, fnt, max_w):
    words = s.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(draw, trial, fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, s, fnt, max_w, fill, leading=None, max_lines=None):
    lines = wrap(draw, s, fnt, max_w)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
    lh = leading or int(fnt.size * 1.18)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


# ---------------------------------------------------------------- scenes
# Each scene draws inside (x, y, w, h) with layered flat shapes.

def _bands(draw, box, top, bottom):
    x, y, w, h = box
    split = y + int(h * 0.62)
    draw.rectangle([x, y, x + w, split], fill=top)
    draw.rectangle([x, split, x + w, y + h], fill=bottom)
    return split


def scene_gaza(draw, box):
    x, y, w, h = box
    gy = _bands(draw, box, (196, 110, 52), (84, 52, 26))
    # smoke plume
    for i, r in enumerate((10, 15, 20)):
        draw.ellipse([x + w * 0.62 - r, y + 8 + i * 9 - r // 2,
                      x + w * 0.62 + r, y + 8 + i * 9 + r // 2],
                     fill=(120, 96, 70))
    # rooftops skyline
    bx = x + 6
    for bw, bh in ((34, 26), (26, 36), (40, 22), (28, 32), (36, 24)):
        draw.rectangle([bx, gy - bh, bx + bw, gy], fill=(56, 34, 14))
        draw.rectangle([bx + 5, gy - bh + 6, bx + 11, gy - bh + 12],
                       fill=(250, 224, 138))
        bx += bw + 5
    # drone: body, arms, rotors
    cx, cy = x + int(w * 0.30), y + 16
    draw.rectangle([cx - 9, cy - 3, cx + 9, cy + 3], fill=(30, 20, 10))
    for dx, dy in ((-13, -6), (13, -6), (-13, 6), (13, 6)):
        draw.line([cx, cy, cx + dx, cy + dy], fill=(30, 20, 10), width=2)
        draw.line([cx + dx - 5, cy + dy, cx + dx + 5, cy + dy],
                  fill=(30, 20, 10), width=2)
    draw.line([x, gy + 6, x + w, gy + 6], fill=(56, 34, 14), width=2)


def scene_iraq(draw, box):
    x, y, w, h = box
    gy = _bands(draw, box, (250, 224, 138), (150, 96, 40))
    draw.ellipse([x + w - 34, y + 6, x + w - 10, y + 30], fill=(214, 130, 24))
    # two pumpjacks
    for px, s in ((x + 26, 1.0), (x + int(w * 0.55), 0.75)):
        base = gy + 4
        draw.polygon([(px, base), (px + int(46 * s), base),
                      (px + int(23 * s), base - int(30 * s))],
                     outline=(56, 34, 14), width=2)
        draw.line([px + int(4 * s), base - int(26 * s),
                   px + int(58 * s), base - int(38 * s)],
                  fill=(56, 34, 14), width=3)
        draw.rectangle([px + int(52 * s), base - int(40 * s),
                        px + int(62 * s), base - int(30 * s)],
                       fill=(150, 52, 20))
    # pipeline
    draw.rectangle([x + 4, gy + 10, x + w - 4, gy + 16], fill=(56, 34, 14))
    # flag pole
    draw.line([x + 10, gy - 44, x + 10, gy + 4], fill=(56, 34, 14), width=2)
    draw.polygon([(x + 10, gy - 44), (x + 28, gy - 38), (x + 10, gy - 32)],
                 fill=(150, 52, 20))


def scene_eu(draw, box):
    x, y, w, h = box
    gy = _bands(draw, box, (35, 62, 112), (104, 68, 28))
    # circle of stars
    import math
    cx, cy, r = x + w // 2, y + int(h * 0.30), int(min(w, h) * 0.20)
    for i in range(12):
        a = 2 * math.pi * i / 12
        sx, sy = cx + int(r * math.cos(a)), cy + int(r * math.sin(a))
        draw.polygon([(sx, sy - 4), (sx + 3, sy + 3), (sx - 3, sy + 3)],
                     fill=(250, 224, 138))
    # parliament block with columns
    bx, bw = x + int(w * 0.18), int(w * 0.64)
    draw.rectangle([bx, gy - 30, bx + bw, gy - 24], fill=(252, 236, 175))
    for i in range(5):
        cxx = bx + 8 + i * (bw - 12) // 4
        draw.rectangle([cxx, gy - 24, cxx + 5, gy - 4], fill=(252, 236, 175))
    draw.rectangle([bx - 4, gy - 4, bx + bw + 4, gy], fill=(252, 236, 175))


def scene_awacs(draw, box):
    x, y, w, h = box
    gy = _bands(draw, box, (120, 158, 196), (104, 68, 28))
    # radar rings
    cx, cy = x + int(w * 0.72), y + int(h * 0.34)
    for r in (8, 15, 22):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                     outline=(252, 236, 175), width=1)
    # plane silhouette with radar dome
    px, py = x + int(w * 0.16), y + int(h * 0.40)
    draw.polygon([(px, py), (px + 86, py - 4), (px + 104, py + 4),
                  (px + 88, py + 10), (px + 8, py + 10)], fill=(56, 34, 14))
    draw.polygon([(px + 6, py), (px - 8, py - 12), (px + 14, py - 2)],
                 fill=(56, 34, 14))
    draw.ellipse([px + 38, py - 12, px + 62, py - 4], fill=(56, 34, 14))
    draw.rectangle([x + 4, gy + 8, x + w - 4, gy + 11], fill=(56, 34, 14))


def scene_hormuz(draw, box):
    x, y, w, h = box
    gy = _bands(draw, box, (250, 224, 138), (0, 122, 152))
    # tanker
    hx, hy = x + int(w * 0.10), gy - 16
    draw.polygon([(hx, hy), (hx + int(w * 0.62), hy), (hx + int(w * 0.56), hy + 12),
                  (hx + 8, hy + 12)], fill=(150, 52, 20))
    for i in range(3):
        draw.rectangle([hx + 12 + i * 26, hy - 9, hx + 34 + i * 26, hy],
                       fill=(56, 34, 14))
    draw.rectangle([hx + int(w * 0.52), hy - 16, hx + int(w * 0.58), hy - 9],
                   fill=(56, 34, 14))
    # three naval mines
    import math
    for mx in (x + int(w * 0.30), x + int(w * 0.55), x + int(w * 0.78)):
        my = gy + int(h * 0.22)
        draw.ellipse([mx - 7, my - 7, mx + 7, my + 7], fill=(30, 20, 10))
        for i in range(8):
            a = 2 * math.pi * i / 8
            draw.line([mx, my, mx + int(11 * math.cos(a)),
                       my + int(11 * math.sin(a))], fill=(30, 20, 10), width=2)
    # wave strokes
    for i in range(4):
        wx = x + 8 + i * int(w * 0.24)
        draw.arc([wx, gy + int(h * 0.30), wx + 22, gy + int(h * 0.30) + 10],
                 0, 180, fill=(252, 236, 175), width=2)


def scene_warcount(draw, box):
    x, y, w, h = box
    gy = _bands(draw, box, (214, 150, 70), (96, 66, 30))
    draw.ellipse([x + 10, y + 6, x + 34, y + 30], fill=(150, 52, 20))
    # rows of small grave markers
    for row in range(3):
        for col in range(9):
            mx = x + 14 + col * int(w * 0.105)
            my = gy - 6 + row * 11
            draw.line([mx, my, mx, my + 8], fill=(56, 34, 14), width=2)
            draw.line([mx - 3, my + 3, mx + 3, my + 3],
                      fill=(56, 34, 14), width=2)


def scene_nvidia(draw, box):
    x, y, w, h = box
    draw.rectangle([x, y, x + w, y + h], fill=(24, 46, 24))
    # rising chart
    pts = [(x + 8, y + h - 12), (x + int(w * 0.3), y + h - 20),
           (x + int(w * 0.5), y + h - 30), (x + int(w * 0.72), y + 16),
           (x + w - 10, y + 8)]
    draw.line(pts, fill=(120, 220, 120), width=3)
    draw.polygon([(x + w - 10, y + 8), (x + w - 20, y + 10),
                  (x + w - 13, y + 18)], fill=(120, 220, 120))
    # chip with pins
    cx, cy, s = x + int(w * 0.16), y + 10, 22
    draw.rectangle([cx, cy, cx + s, cy + s], outline=(250, 224, 138), width=2)
    for i in range(3):
        draw.line([cx - 5, cy + 4 + i * 7, cx, cy + 4 + i * 7],
                  fill=(250, 224, 138), width=2)
        draw.line([cx + s, cy + 4 + i * 7, cx + s + 5, cy + 4 + i * 7],
                  fill=(250, 224, 138), width=2)


def scene_pce(draw, box):
    x, y, w, h = box
    _bands(draw, box, (252, 231, 155), (104, 68, 28))
    # report sheet
    sx, sy = x + int(w * 0.14), y + 8
    draw.rectangle([sx, sy, sx + int(w * 0.44), sy + int(h * 0.66)],
                   fill=(255, 250, 235), outline=(56, 34, 14), width=2)
    for i in range(3):
        draw.line([sx + 7, sy + 10 + i * 9, sx + int(w * 0.44) - 7,
                   sy + 10 + i * 9], fill=(104, 68, 28), width=2)
    draw.line([sx + 7, sy + 40, sx + 24, sy + 40], fill=(150, 52, 20), width=3)
    # clock: due today
    cx, cy, r = x + int(w * 0.76), y + int(h * 0.36), 15
    draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                 outline=(56, 34, 14), width=3)
    draw.line([cx, cy, cx, cy - 9], fill=(56, 34, 14), width=2)
    draw.line([cx, cy, cx + 7, cy + 3], fill=(56, 34, 14), width=2)


def scene_xiamen(draw, box):
    x, y, w, h = box
    gy = _bands(draw, box, (120, 158, 196), (104, 68, 28))
    # climbing jet
    px, py = x + int(w * 0.18), gy - 26
    draw.polygon([(px, py + 10), (px + 62, py - 8), (px + 74, py - 4),
                  (px + 20, py + 14)], fill=(255, 250, 235))
    draw.polygon([(px + 26, py + 2), (px + 14, py + 14), (px + 34, py + 12)],
                 fill=(150, 52, 20))
    draw.polygon([(px + 2, py + 8), (px - 8, py - 2), (px + 10, py + 2)],
                 fill=(255, 250, 235))
    # terminal blocks + runway dashes
    draw.rectangle([x + w - 52, gy - 16, x + w - 8, gy], fill=(56, 34, 14))
    for i in range(5):
        draw.rectangle([x + 8 + i * 26, gy + 8, x + 22 + i * 26, gy + 11],
                       fill=(252, 236, 175))


def scene_madrid(draw, box):
    x, y, w, h = box
    _bands(draw, box, (52, 44, 84), (46, 96, 46))
    # stadium bowl + floodlights
    draw.arc([x + 10, y + 8, x + w - 10, y + int(h * 0.95)], 0, 180,
             fill=(252, 236, 175), width=3)
    for fx in (x + 16, x + w - 22):
        draw.line([fx + 3, y + 22, fx + 3, y + 6], fill=(252, 236, 175), width=2)
        draw.ellipse([fx - 2, y + 1, fx + 9, y + 8], fill=(250, 224, 138))
    # scoreboard
    draw.rectangle([x + w // 2 - 24, y + int(h * 0.30), x + w // 2 + 24,
                    y + int(h * 0.30) + 20], fill=(56, 34, 14))
    f = font(ARCHIVO_BOLD, 14)
    draw.text((x + w // 2, y + int(h * 0.30) + 10), "5-1", font=f,
              fill=(250, 224, 138), anchor="mm")
    # ball
    draw.ellipse([x + int(w * 0.30), y + h - 18, x + int(w * 0.30) + 11,
                  y + h - 7], fill=(255, 250, 235))


def scene_coral(draw, box):
    x, y, w, h = box
    draw.rectangle([x, y, x + w, y + h], fill=(0, 122, 152))
    draw.rectangle([x, y, x + w, y + int(h * 0.3)], fill=(64, 168, 196))
    # coral branches
    def branch(bx, by, ang, ln, wd):
        import math
        ex, ey = bx + int(ln * math.cos(ang)), by - int(ln * math.sin(ang))
        draw.line([bx, by, ex, ey], fill=(232, 116, 84), width=wd)
        if ln > 8:
            branch(ex, ey, ang + 0.5, ln * 0.68, max(1, wd - 1))
            branch(ex, ey, ang - 0.4, ln * 0.68, max(1, wd - 1))
    branch(x + int(w * 0.3), y + h - 4, 1.35, 20, 4)
    branch(x + int(w * 0.62), y + h - 4, 1.7, 24, 4)
    # fish + bubbles
    for fx, fy in ((x + int(w * 0.45), y + 14), (x + int(w * 0.78), y + 22)):
        draw.ellipse([fx, fy, fx + 14, fy + 7], fill=(250, 224, 138))
        draw.polygon([(fx + 13, fy + 1), (fx + 19, fy + 3), (fx + 13, fy + 6)],
                     fill=(250, 224, 138))
    for bx, by in ((x + int(w * 0.2), y + 16), (x + int(w * 0.86), y + 10)):
        draw.ellipse([bx, by, bx + 4, by + 4], outline=(252, 236, 175))


def scene_fiji(draw, box):
    x, y, w, h = box
    gy = _bands(draw, box, (250, 224, 138), (176, 128, 52))
    draw.ellipse([x + 8, y + 5, x + 32, y + 29], fill=(214, 130, 24))
    # island mound + palm
    draw.pieslice([x + int(w * 0.2), gy - 12, x + int(w * 0.8), gy + 16],
                  180, 360, fill=(104, 122, 40))
    px, py = x + w // 2, gy - 8
    draw.line([px, py, px + 4, py - 24], fill=(56, 34, 14), width=3)
    import math
    for a in (0.2, 0.9, 1.6, 2.3, 2.9):
        ex = px + 4 + int(15 * math.cos(a))
        ey = py - 24 - int(8 * math.sin(a))
        draw.arc([px + 4 - 14, py - 32, px + 4 + 16, py - 12],
                 int(math.degrees(a)) - 40, int(math.degrees(a)) + 30,
                 fill=(104, 122, 40), width=2)
        draw.line([px + 4, py - 24, ex, ey], fill=(104, 122, 40), width=2)
    # cracked dry earth
    for cx0 in (x + 14, x + int(w * 0.7)):
        draw.line([cx0, gy + 8, cx0 + 9, gy + 13, cx0 + 4, gy + 19],
                  fill=(56, 34, 14), width=1)


def scene_storms(draw, box):
    x, y, w, h = box
    _bands(draw, box, (96, 104, 122), (0, 90, 120))
    # two storm clouds
    for cx, cy in ((x + int(w * 0.26), y + 14), (x + int(w * 0.74), y + 12)):
        for dx, r in ((-14, 10), (0, 13), (14, 10)):
            draw.ellipse([cx + dx - r, cy - r // 2, cx + dx + r, cy + r],
                         fill=(56, 60, 72))
        for i in range(3):
            rx = cx - 10 + i * 10
            draw.line([rx, cy + 12, rx - 3, cy + 22], fill=(120, 190, 230),
                      width=2)
    # small plane between the coasts
    px, py = x + w // 2 - 12, y + int(h * 0.55)
    draw.polygon([(px, py), (px + 24, py), (px + 30, py + 4), (px + 4, py + 4)],
                 fill=(255, 250, 235))
    draw.polygon([(px + 10, py), (px + 6, py - 6), (px + 16, py)],
                 fill=(255, 250, 235))


SCENES = {
    "gaza": scene_gaza, "iraq": scene_iraq, "eu": scene_eu,
    "awacs": scene_awacs, "hormuz": scene_hormuz, "warcount": scene_warcount,
    "nvidia": scene_nvidia, "pce": scene_pce, "xiamen": scene_xiamen,
    "madrid": scene_madrid, "coral": scene_coral, "fiji": scene_fiji,
    "storms": scene_storms,
}

# ------------------------------------------------------------- world map
# Coarse dotted world: '#' is land. 66 x 20 grid, drawn as dots.
WORLD = [
    "..........####................................................",
    ".....##########...#####......##################..........###....",
    "...############..#######...#######################......#####...",
    "....#########.....#####...#########################....#######..",
    ".....#######.......###....########..################...########.",
    "......#####.................######....#############.....######..",
    ".......###...................####......##########........####...",
    ".......##.....................##........########..........##....",
    "......###.................................######................",
    "......####.................................####..........##.....",
    ".......####.................................###..........###....",
    ".......#####................................##...........####...",
    "........####..............................................##....",
    "........###.....................................................",
    ".........##..............................................####...",
    ".........##.............................................######..",
    "..........#..............................................####...",
    "................................................................",
    "................................................................",
    "................................................................",
]

# Pin positions (grid col, row) for page cards 1..13.
PINS = {
    1: (35, 8), 2: (37, 7), 3: (29, 4), 4: (31, 3), 5: (39, 9),
    6: (33, 3), 7: (6, 5), 8: (11, 5), 9: (52, 7), 10: (28, 6),
    11: (57, 14), 12: (63, 15), 13: (12, 7),
}


def draw_map(draw, x, y, w, h):
    rows = len(WORLD)
    cols = max(len(r) for r in WORLD)
    dx = w / cols
    dy = h / rows
    r = max(1.6, dx * 0.32)
    for ri, row in enumerate(WORLD):
        for ci, ch in enumerate(row):
            if ch == "#":
                cx = x + ci * dx + dx / 2
                cy = y + ri * dy + dy / 2
                draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                             fill=(104, 68, 28))
    f = font(ARCHIVO_BOLD, 10)
    for no, (ci, ri) in PINS.items():
        cx = x + ci * dx + dx / 2
        cy = y + ri * dy + dy / 2
        draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=RUST,
                     outline=(255, 250, 235), width=1)
        draw.text((cx, cy), str(no), font=f, fill=(255, 250, 235),
                  anchor="mm")
