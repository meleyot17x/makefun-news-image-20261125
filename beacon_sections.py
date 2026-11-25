# THE BEACON POST - shared page sections used by both layout variants.
from PIL import ImageDraw

import beacon_data as D
from beacon_draw import (ARCHIVO, ARCHIVO_BOLD, PLAYFAIR_BLACK, PLAYFAIR_BOLD,
                         CREAM, INK, INK_SOFT, PAPER, PAPER_CARD, PAPER_LIGHT,
                         REGION_COLORS, RUST, SCENES, WHITE, draw_map,
                         draw_wrapped, fit_font, font, text_w, wrap)

PAGE_W = 1024
MARGIN = 16
INNER_W = PAGE_W - 2 * MARGIN


def rule(draw, x, y, w, weight=2):
    draw.rectangle([x, y, x + w, y + weight], fill=INK)


def draw_kicker(draw, y=10):
    f = font(ARCHIVO_BOLD, 13)
    draw.text((MARGIN, y), D.KICKER_LEFT, font=f, fill=INK)
    draw.text((PAGE_W - MARGIN, y), D.KICKER_RIGHT, font=f, fill=RUST,
              anchor="ra")


def draw_masthead(draw, y=30, align="center"):
    f = fit_font(draw, D.MASTHEAD, PLAYFAIR_BLACK, 64, INNER_W - 40)
    if align == "center":
        draw.text((PAGE_W // 2, y), D.MASTHEAD, font=f, fill=INK, anchor="ma")
    else:
        draw.text((MARGIN + 54, y), D.MASTHEAD, font=f, fill=INK, anchor="ma")
    return y + f.size + 6


def draw_beacon_mark(draw, x, y, s=44):
    # small lighthouse mark: tower, lamp room, rays.
    draw.polygon([(x + s * 0.38, y + s), (x + s * 0.62, y + s),
                  (x + s * 0.56, y + s * 0.34), (x + s * 0.44, y + s * 0.34)],
                 fill=INK)
    draw.rectangle([x + s * 0.40, y + s * 0.52, x + s * 0.60, y + s * 0.62],
                   fill=RUST)
    draw.rectangle([x + s * 0.42, y + s * 0.16, x + s * 0.58, y + s * 0.32],
                   fill=INK)
    draw.ellipse([x + s * 0.455, y + s * 0.19, x + s * 0.545, y + s * 0.29],
                 fill=PAPER_LIGHT)
    for dx in (-1, 1):
        draw.line([x + s * 0.5 + dx * s * 0.12, y + s * 0.24,
                   x + s * 0.5 + dx * s * 0.34, y + s * 0.24],
                  fill=RUST, width=2)


def draw_dateband(draw, y, h=46):
    draw.rectangle([MARGIN, y, MARGIN + INNER_W, y + h], fill=INK)
    f = fit_font(draw, D.DATE_LINE, PLAYFAIR_BLACK, 37, INNER_W - 330)
    draw.text((MARGIN + 14, y + h // 2), D.DATE_LINE, font=f, fill=PAPER_LIGHT,
              anchor="lm")
    fs = font(ARCHIVO_BOLD, 12)
    draw.text((MARGIN + INNER_W - 14, y + h // 2 - 8),
              "THE DAY IN 37 CHECKED STORIES", font=fs, fill=CREAM, anchor="rm")
    draw.text((MARGIN + INNER_W - 14, y + h // 2 + 9),
              "EVERY STORY DATED & SOURCED", font=fs, fill=CREAM, anchor="rm")
    return y + h


def draw_numstrip(draw, y, h=42):
    n = len(D.NUMBERS)
    gap = 6
    cw = (INNER_W - gap * (n - 1)) / n
    fb = font(ARCHIVO_BOLD, 17)
    fs = font(ARCHIVO_BOLD, 8)
    for i, (big, small) in enumerate(D.NUMBERS):
        cx = MARGIN + i * (cw + gap)
        draw.rectangle([cx, y, cx + cw, y + h], fill=PAPER_CARD,
                       outline=INK, width=1)
        draw.text((cx + cw / 2, y + 3), big, font=fb, fill=RUST, anchor="ma")
        lines = wrap(draw, small, fs, cw - 6)
        ly = y + 24
        for ln in lines[:2]:
            draw.text((cx + cw / 2, ly), ln, font=fs, fill=INK, anchor="ma")
            ly += 9
    return y + h


def draw_regionstrip(draw, y, h=26):
    f = font(ARCHIVO_BOLD, 11)
    draw.text((MARGIN, y + h // 2), "REGIONS:", font=f, fill=INK, anchor="lm")
    x = MARGIN + 62
    for name, count in D.REGIONS:
        label = "%s %d" % (name, count)
        w = text_w(draw, label, f) + 14
        draw.rectangle([x, y + 2, x + w, y + h - 2],
                       fill=REGION_COLORS[name])
        draw.text((x + w / 2, y + h // 2), label, font=f, fill=WHITE,
                  anchor="mm")
        x += w + 5
    return y + h


def _card_frame(draw, card, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=PAPER_CARD, outline=INK,
                   width=2)
    col = REGION_COLORS[card["region"]]
    draw.rectangle([x, y, x + w, y + 17], fill=col)
    fh = font(ARCHIVO_BOLD, 10)
    left = "%d - %s - %s" % (card["no"], card["region"], card["place"].upper())
    if card.get("tag"):
        left += " - " + card["tag"]
    draw.text((x + 6, y + 8), left, font=fh, fill=WHITE, anchor="lm")
    draw.text((x + w - 6, y + 8), card["cert"], font=fh, fill=WHITE,
              anchor="rm")


def _chip_row(draw, card, x, y, w, small=False):
    fc = font(ARCHIVO_BOLD, 10 if not small else 8)
    label = card["chip"]
    cw = text_w(draw, label, fc) + 12
    draw.rectangle([x, y, x + cw, y + (15 if not small else 12)], fill=INK)
    draw.text((x + 6, y + (7 if not small else 6)), label, font=fc,
              fill=CREAM, anchor="lm")
    fs = font(ARCHIVO, 9 if not small else 8)
    draw.text((x + w, y + (7 if not small else 6)),
              card["src"], font=fs, fill=INK_SOFT, anchor="rm")


def lead_card(draw, card, x, y, w, h):
    _card_frame(draw, card, x, y, w, h)
    scene_h = 96
    SCENES[card["scene"]](draw, (x + 3, y + 20, w - 6, scene_h))
    ty = y + 20 + scene_h + 6
    fh = fit_font(draw, card["head"], PLAYFAIR_BOLD, 21, w - 16)
    ty = draw_wrapped(draw, x + 8, ty, card["head"], fh, w - 16, INK,
                      leading=int(fh.size * 1.08), max_lines=2)
    fd = font(ARCHIVO, 11)
    ty = draw_wrapped(draw, x + 8, ty + 3, card["deck"], fd, w - 16,
                      (40, 26, 10), leading=13, max_lines=4)
    _chip_row(draw, card, x + 8, y + h - 21, w - 16)


def grid_card(draw, card, x, y, w, h):
    _card_frame(draw, card, x, y, w, h)
    scene_h = 27
    SCENES[card["scene"]](draw, (x + 3, y + 20, w - 6, scene_h))
    ty = y + 20 + scene_h + 3
    fh = font(ARCHIVO_BOLD, 12)
    ty = draw_wrapped(draw, x + 6, ty, card["head"], fh, w - 12, INK,
                      leading=13, max_lines=2)
    fd = font(ARCHIVO, 8)
    draw_wrapped(draw, x + 6, ty + 1, card["deck"], fd, w - 12,
                 (40, 26, 10), leading=9, max_lines=3)
    _chip_row(draw, card, x + 6, y + h - 16, w - 12, small=True)


def draw_timeline(draw, y, h=34):
    draw.rectangle([MARGIN, y, MARGIN + INNER_W, y + h], fill=INK)
    f = font(ARCHIVO_BOLD, 11)
    draw.text((MARGIN + 10, y + h // 2), "THE DAY\nIN HOURS", font=f,
              fill=PAPER_LIGHT, anchor="lm")
    x = MARGIN + 92
    slot_w = (INNER_W - 100) / len(D.TIMELINE)
    ft = font(ARCHIVO_BOLD, 10)
    fs = font(ARCHIVO, 8)
    for i, (when, what) in enumerate(D.TIMELINE):
        sx = x + i * slot_w
        if i:
            draw.line([sx - 4, y + 5, sx - 4, y + h - 5], fill=INK_SOFT,
                      width=1)
        draw.text((sx, y + 4), when, font=ft, fill=PAPER_LIGHT)
        draw_wrapped(draw, sx, y + 17, what, fs, slot_w - 8, CREAM,
                     leading=9, max_lines=2)
    return y + h


def draw_map_block(draw, x, y, w, h):
    f = font(ARCHIVO_BOLD, 12)
    draw.text((x, y), "WHERE IT HAPPENED - 13 SCENES PINNED", font=f, fill=INK)
    draw_map(draw, x, y + 16, w, h - 44)
    fl = font(ARCHIVO, 9)
    left = " - ".join("%d %s" % (i + 1, s) for i, s in
                      enumerate(D.PIN_LABELS[:7]))
    right = " - ".join("%d %s" % (i + 8, s) for i, s in
                       enumerate(D.PIN_LABELS[7:]))
    draw.text((x, y + h - 24), left, font=fl, fill=INK)
    draw.text((x, y + h - 12), right, font=fl, fill=INK)


def draw_datecheck(draw, x, y, w, h):
    f = font(ARCHIVO_BOLD, 12)
    draw.text((x, y), "DATE CHECK - NOT TODAY'S NEWS", font=f, fill=RUST)
    fs = font(ARCHIVO, 10)
    ty = y + 18
    for item in D.DATE_CHECKS:
        draw.text((x, ty), "x", font=font(ARCHIVO_BOLD, 11), fill=RUST)
        ty = draw_wrapped(draw, x + 13, ty, item, fs, w - 13, INK,
                          leading=12, max_lines=2) + 3
    note = ("Checked against the day: every story on this page happened or "
            "was first reported on Tuesday 25 November 2026.")
    draw_wrapped(draw, x, ty + 2, note, font(ARCHIVO, 9), w, INK_SOFT,
                 leading=11, max_lines=3)


def draw_briefs(draw, y, cols=4):
    f = font(ARCHIVO_BOLD, 12)
    draw.text((MARGIN, y), "ALSO ON THE PAGE - 24 MORE, NUMBERED 14-37",
              font=f, fill=INK)
    fs = font(ARCHIVO, 9)
    fn = font(ARCHIVO_BOLD, 9)
    col_w = INNER_W / cols
    rows = (len(D.BRIEFS) + cols - 1) // cols
    for i, brief in enumerate(D.BRIEFS):
        col, row = divmod(i, rows)
        bx = MARGIN + col * col_w
        by = y + 16 + row * 12
        num = "%d." % (14 + i)
        draw.text((bx, by), num, font=fn, fill=RUST)
        draw.text((bx + 20, by), brief, font=fs, fill=INK)
    return y + 16 + rows * 12


def draw_footer(draw, y):
    rule(draw, MARGIN, y, INNER_W, 2)
    f = font(ARCHIVO, 9)
    draw.text((MARGIN, y + 5), D.FOOTER_LEFT, font=f, fill=INK_SOFT)
    draw.text((PAGE_W - MARGIN, y + 5), D.FOOTER_RIGHT, font=f, fill=INK_SOFT,
              anchor="ra")
