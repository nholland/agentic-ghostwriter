"""The Tally You Don't Read Aloud (Chapter 6).

Seven days of tally marks: everything he has been counting. The one bold
frame is what she can actually see, and it holds tonight's single mark.
"""
from platekit import Plate, W, write

p = Plate(height=96, seed=67, title="The Tally You Don&#8217;t Read Aloud")
rng = p.rng

DAY = 40
X0 = (W - 7 * DAY) / 2
TOP, BOT = 32, 56
COUNTS = [6, 4, 7, 5, 8, 5, 1]         # what he did each day; tonight, one thing
STEP = 4.3


def tally(cx, n, cls):
    """n tally marks centred on cx, in gates of five."""
    gates, rest = divmod(n, 5)
    width = gates * (3 * STEP + 6) + max(rest - 1, 0) * STEP - (6 if gates and not rest else 0)
    x = cx - width / 2
    for _ in range(gates):
        for k in range(4):
            p.seg(x + k * STEP + rng.uniform(-0.3, 0.3), TOP, x + k * STEP + rng.uniform(-0.5, 0.5), BOT, cls=cls, wobble=0.1)
        p.seg(x - 2.2, BOT - 5, x + 3 * STEP + 2.2, TOP + 5, cls=cls, wobble=0.1)
        x += 3 * STEP + 6
    for k in range(rest):
        p.seg(x + k * STEP + rng.uniform(-0.3, 0.3), TOP, x + k * STEP + rng.uniform(-0.5, 0.5), BOT, cls=cls, wobble=0.1)


for d, n in enumerate(COUNTS):
    tally(X0 + DAY * (d + 0.5), n, "line")

# what she can see
fx0, fx1, fy0, fy1 = X0 + 6 * DAY + 4, X0 + 7 * DAY - 4, TOP - 10, BOT + 10
for a, b in (((fx0, fy0), (fx1, fy0)), ((fx1, fy0), (fx1, fy1)), ((fx1, fy1), (fx0, fy1)), ((fx0, fy1), (fx0, fy0))):
    p.seg(*a, *b, cls="bold", wobble=0.12)

# the week, measured in days
my = 82
p.straight(X0, my, X0 + 7 * DAY, my)
for d in range(8):
    p.straight(X0 + d * DAY, my - 2.6, X0 + d * DAY, my + 2.6)

p.label(X0, 10, "The week")
p.label(X0 + 6.5 * DAY, 10, "Tonight", anchor="middle")

write(p, "plate-06-the-tally-you-dont-read-aloud",
      deck="You are counting the week. She can only see tonight.",
      caption="Resentment grows when you expect someone<br>to read a tally you never showed them.")
