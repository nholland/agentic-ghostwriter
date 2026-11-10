"""The Thing With No Deadline (Chapter 12).

Two strips from the same three weeks of calendar. Everything with a day
attached got done, every day. The one thing for her got done three
times, and then the squares are empty all the way to tonight.
"""
from platekit import Plate, W, write

p = Plate(height=120, seed=107, title="The Thing With No Deadline")

DAYS, CELL = 21, 14
X0 = (W - DAYS * CELL) / 2
ROW_H = 14


def strip(top, done):
    p.seg(X0, top, X0 + DAYS * CELL, top, wobble=0.08)
    p.seg(X0, top + ROW_H, X0 + DAYS * CELL, top + ROW_H, wobble=0.08)
    for d in range(DAYS + 1):
        p.seg(X0 + d * CELL, top, X0 + d * CELL, top + ROW_H, cls="hair", wobble=0.05)
    for d in done:                                         # a tick in the square
        cx, cy = X0 + (d + 0.5) * CELL, top + ROW_H / 2
        j = p.rng.uniform(-0.5, 0.5)
        p.curve([(cx - 3.4, cy + 0.2 + j), (cx - 1.1, cy + 3.0), (cx + 3.8, cy - 3.4 + j)])


# everything with a day attached
p.label(X0, 9, "The things with a day attached")
for d in range(DAYS):
    p.label(X0 + (d + 0.5) * CELL + 0.7, 25, "MTWTFSS"[d % 7], anchor="middle")
strip(30, range(DAYS))

# the one thing for her
Y2 = 76
p.label(X0, Y2 - 8, "The one thing for her")
strip(Y2, range(3))
tx = X0 + (DAYS - 1) * CELL                                # tonight
for a, b in (((tx, Y2), (tx + CELL, Y2)), ((tx + CELL, Y2), (tx + CELL, Y2 + ROW_H)),
             ((tx + CELL, Y2 + ROW_H), (tx, Y2 + ROW_H)), ((tx, Y2 + ROW_H), (tx, Y2))):
    p.seg(*a, *b, cls="bold", wobble=0.06)
p.label(X0 + DAYS * CELL, Y2 - 8, "Tonight", anchor="end")

# the empty stretch
b0, b1, by = X0 + 3 * CELL + 2, tx - 2, Y2 + ROW_H + 9
p.straight(b0, by, b1, by)
p.straight(b0, by - 2.6, b0, by + 2.6)
p.straight(b1, by - 2.6, b1, by + 2.6)
p.label((b0 + b1) / 2, by + 14, "the stretch you never felt go by", cls="ital", anchor="middle")

write(p, "plate-12-the-thing-with-no-deadline",
      deck="What has no deadline is easiest to neglect.",
      caption="You didn&#8217;t stop loving her. Love rarely becomes urgent.<br>That is why you have to make room for it.")
