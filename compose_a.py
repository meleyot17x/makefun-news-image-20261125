# THE BEACON POST - Layout A: classic broadsheet stack.
# Masthead centred, date band, number strip, region strip, lead trio,
# ten-card grid, timeline, map + date check, briefs, footer.
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import beacon_data as D
import beacon_sections as S
from beacon_draw import INK, PAPER


def build(path):
    img = Image.new("RGB", (1024, 1024), PAPER)
    draw = ImageDraw.Draw(img)

    S.draw_kicker(draw, 10)
    S.rule(draw, S.MARGIN, 27, S.INNER_W, 2)
    y = S.draw_masthead(draw, 31)
    S.rule(draw, S.MARGIN, y + 1, S.INNER_W, 3)
    y = S.draw_dateband(draw, y + 7, 46)
    y = S.draw_numstrip(draw, y + 6, 42)
    y = S.draw_regionstrip(draw, y + 4, 26)

    # Lead trio.
    y += 8
    lead_h = 236
    gap = 12
    cw = (S.INNER_W - 2 * gap) / 3
    for i, card in enumerate(D.LEADS):
        S.lead_card(draw, card, S.MARGIN + i * (cw + gap), y, cw, lead_h)
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

    # Map + date check band.
    y += 8
    S.draw_map_block(draw, S.MARGIN, y, 596, 138)
    S.draw_datecheck(draw, S.MARGIN + 616, y, S.INNER_W - 616, 138)
    y += 142

    y = S.draw_briefs(draw, y, cols=4)
    S.draw_footer(draw, y + 4)
    img.save(path)
    return path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "entry_a.png"
    print(build(out))
