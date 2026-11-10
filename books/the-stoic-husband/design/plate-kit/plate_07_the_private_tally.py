"""The Private Tally (Chapter 7).

An open ledger. His page has three entries he can read. Her page is just
as full, but every line is dotted: it is there, and he cannot read it.
Under the book, the small things nobody wrote down at all.
"""
import math
from platekit import Plate, W, write

p = Plate(height=190, seed=71, title="The Private Tally")
rng = p.rng

TOP, BOT = 18, 94
L0, L1, R0, R1 = 20, 158.5, 165.5, 304
RULES = [36, 52, 68, 84]
ENTRIES = ["Fixing the router", "The coaching weekend", "Cleaning the kitchen"]


def page(x0, x1, outer):
    p.seg(x0, TOP, x1, TOP)
    p.seg(x0, BOT, x1, BOT)
    p.seg(outer, TOP, outer, BOT)
    # the thickness of the book: two more page edges showing below and outside
    for k in (1, 2):
        d = 1.9 * k
        side = outer - d if outer == x0 else outer + d
        p.seg(side, TOP + d, side, BOT + d, cls="hair", wobble=0.08)
        p.seg(min(side, x0 if outer == x0 else x0 + 2), BOT + d, max(side, x1 if outer == x1 else x1 - 2), BOT + d, cls="hair", wobble=0.08)


page(L0, L1, L0)
page(R0, R1, R1)
mid = (L1 + R0) / 2                                     # the gutter
p.curve([(L1, TOP), (mid, TOP + 2.6), (R0, TOP)])
p.curve([(L1, BOT), (mid, BOT + 2.6), (R0, BOT)])
p.seg(mid, TOP + 2.6, mid, BOT + 2.6, cls="hair", wobble=0.05)

# his page: ruled, with what he remembers doing
for i, y in enumerate(RULES):
    p.seg(L0 + 10, y, L1 - 9, y, cls="hair", wobble=0.08)
    if i < len(ENTRIES):
        p.label(L0 + 12, y - 3.6, ENTRIES[i], cls="ital")

# her page: every line taken, none of it legible from here
for y in RULES:
    p.seg(R0 + 9, y, R1 - 10, y, cls="hair dotted", wobble=0.0)
    hand = p._noise(1.1, 17)
    p.stroke(lambda x, y=y: y - 5.2 + hand(x), R0 + 11, R1 - rng.uniform(14, 62), cls="line dotted", wobble=0.0, step=2.5)

# the smaller things neither of them tracks
FY0, FY1 = 136, 166
cols, rows = 46, 4
for r in range(rows):
    for c in range(cols):
        if rng.random() < 0.12:
            continue
        x = 16 + (W - 32) * (c + rng.uniform(0.1, 0.9)) / cols
        y = FY0 + (FY1 - FY0) * (r + rng.uniform(0.15, 0.85)) / rows
        a = rng.uniform(-0.3, 0.3)
        h = rng.uniform(1.8, 2.8)
        p.straight(x - math.sin(a) * h, y - h, x + math.sin(a) * h, y + h, cls="hair")

p.label(L0, 9, "Your page")
p.label(R0, 9, "Her page")
p.label((R0 + R1) / 2, BOT + 19.5, "a ledger you can&#8217;t fully read", cls="ital", anchor="middle")
p.label(W / 2, FY1 + 15, "the smaller things neither of you tracks", cls="ital", anchor="middle")

write(p, "plate-07-the-private-tally",
      deck="The ledger can only count what it can see.",
      caption="Half the data, and it always says you&#8217;re ahead.")
