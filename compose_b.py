# THE BEACON POST - Layout B: beacon-mark masthead at left, mirrored
# date band, region strip above the number strip, a widened centre
# lead, and the map / date-check band swapped left-for-right.
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import beacon_data as D
import beacon_sections as S
from beacon_draw import (ARCHIVO_BOLD, CREAM, INK, PAPER, PAPER_LIGHT,
                         PLAYFAIR_BLACK, fit_font, font)


def dateband_mirrored(draw, y, h=46):
    draw.rectangle([S.MARGIN, y, S.MARGIN + S.INNER_W, y + h], fill=INK)
    fs = font(ARCHIVO_BOLD, 12)
    draw.text((S.MARGIN + 14, y + h // 2 - 8),
              "THE DAY IN 37 CHECKED STORIES", font=fs, fill=CREAM)
    draw.text((S.MARGIN + 14, y + h // 2 + 9),
              "EVERY STORY DATED & SOURCED", font=fs, fill=CREAM)
    f = fit_font(draw, D.DATE_LINE, PLAYFAIR_BLACK, 37, S.INNER_W - 330)
    draw.text((S.MARGIN + S.INNER_W - 14, y + h // 2), D.DATE_LINE, font=f,
              fill=PAPER_LIGHT, anchor="rm")
    return y + h


def build(path):
    img = Image.new("RGB", (1024, 1024), PAPER)
    draw = ImageDraw.Draw(img)

    S.draw_kicker(draw, 10)
    S.rule(draw, S.MARGIN, 27, S.INNER_W, 2)
    S.draw_beacon_mark(draw, S.MARGIN, 33, 46)
    y = S.draw_masthead(draw, 31, align="left")
    S.rule(draw, S.MARGIN, y + 1, S.INNER_W, 3)
    y = dateband_mirrored(draw, y + 7, 46)
    y = S.draw_regionstrip(draw, y + 6, 26)
    y = S.draw_numstrip(draw, y + 4, 42)

    # Lead trio with a widened centre card (Iraq).
    y += 8
    lead_h = 236
    widths = (300, 380, 288)
    x = S.MARGIN
    for card, cw in zip(D.LEADS, widths):
        S.lead_card(draw, card, x, y, cw, lead_h)
        x += cw + 12
    y += lead_h

    # Grid of ten.
    y += 6
    row_h = 118
    ggap = 10
    gw = (S.INNER_W - 4 * ggap) / 5
    for i, card in enumerate(D.GRID):
        col, row = i % 5, i // 5
        S.grid_card(draw, card, S.MARGIN + col * (gw + ggap),
                    y + row * (row_h + 8), gw, row_h)
    y += 2 * row_h + 8

    y = S.draw_timeline(draw, y + 6, 34)

    # Date check left, map right (swapped vs Layout A).
    y += 8
    S.draw_datecheck(draw, S.MARGIN, y, 330, 138)
    S.draw_map_block(draw, S.MARGIN + 350, y, S.INNER_W - 350, 138)
    y += 142

    y = S.draw_briefs(draw, y, cols=4)
    S.draw_footer(draw, y + 4)
    img.save(path)
    return path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "entry_b.png"
    print(build(out))
