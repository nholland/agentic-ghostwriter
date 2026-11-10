"""The Hole Maker (Chapter 4).

The fence board from the father's story, three times. Nails driven in,
the same nails pulled, and the board months on. The holes sit exactly
where the nails were; the grain never closes over them.
"""
import math
from platekit import Plate, W, write

p = Plate(height=172, seed=47, title="The Hole Maker")
rng = p.rng

BOARD_H, HEAD_ROOM, PITCH = 21, 17, 62
NAILS = [(52, 0.55), (96, 0.34), (151, 0.66), (208, 0.42), (262, 0.6)]          # (x, depth down the board)
LATER = NAILS + [(28, 0.36), (74, 0.7), (122, 0.5), (176, 0.3), (186, 0.72),
                 (232, 0.68), (243, 0.3), (287, 0.36), (302, 0.66)]


def board(top):
    """A plank: two sawn edges, two ends, and a few lines of grain."""
    grain = p._noise(0.9, 120)
    p.seg(0, top, W, top)
    p.seg(0, top + BOARD_H, W, top + BOARD_H)
    p.seg(0.4, top, 0, top + BOARD_H)
    p.seg(W, top, W - 0.4, top + BOARD_H)
    for frac in (0.14, 0.28, 0.43, 0.57, 0.72, 0.86):
        y = top + BOARD_H * frac
        a, b = rng.uniform(3, 26), rng.uniform(W - 26, W - 3)
        p.stroke(lambda x, y=y: y + grain(x) * math.sin(math.pi * (x / W)) * 0.7, a, b, cls="hair", wobble=0.25)


def row(i, name, line, marks, nails):
    y0 = 8 + i * PITCH
    top = y0 + HEAD_ROOM
    p.label(1, y0, name)
    p.label(W, y0 + 0.6, line, cls="ital", anchor="end")
    board(top)
    for x, d in marks:
        y = top + BOARD_H * d
        if nails:                                   # driven at a slight angle, head standing proud
            lean = rng.uniform(-2.2, 3.2)
            hx, hy = x + lean, top - 8.5
            p.seg(x, y, hx, hy, cls="bold", wobble=0.0)
            p.seg(hx - 3.2, hy + lean * 0.12, hx + 3.2, hy - lean * 0.12, cls="bold", wobble=0.0)
        else:                                       # the hole it leaves
            p.dot(x, y, r=2.1, clear=3.5)


row(0, "The outburst", "Every outburst drives a nail.", NAILS, nails=True)
row(1, "The apology", "An apology can pull it out.", NAILS, nails=False)
row(2, "Months on", "It&#8217;s full of holes.", LATER, nails=False)

write(p, "plate-04-the-hole-maker",
      deck="Anger isn&#8217;t strength.",
      caption="Sometimes it&#8217;s cold, and cold is often worse. Both make holes.")
