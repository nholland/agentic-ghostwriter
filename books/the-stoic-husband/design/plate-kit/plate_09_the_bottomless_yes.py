"""The Bottomless Yes (Chapter 9).

A bill he wrote and never handed over. Each yes is an item; what he
expected back sits in the price column, joined by the dotted leaders of
any receipt. Where the total would be: "you never asked for it."
"""
from platekit import Plate, W, write

p = Plate(height=158, seed=97, title="The Bottomless Yes")

X0, X1 = 26, 298            # the slip
PAD = 16
TOP, TEAR = 5, 128
# (what he gave, what he expected back, set width of each in canvas units)
ITEMS = [("A night you did everything she wanted", "Respect", 141.5, 26.5),
         ("A plan you went along with, not yours", "Warmth", 139.5, 32),
         ("Her story, heard all the way through", "Being heard", 133.5, 45)]

# the slip: three ruled sides and a torn lower edge
p.seg(X0, TEAR, X0, TOP)
p.seg(X0, TOP, X1, TOP)
p.seg(X1, TOP, X1, TEAR)
teeth, n = [], 34
for i in range(n + 1):
    teeth.append(f"{X0 + (X1 - X0) * i / n:.2f} {TEAR + (3.4 if i % 2 else 0):.2f}")
p.parts.append(f'<path class="ink line" d="M{" L".join(teeth)}"/>')

# column heads
p.label(X0 + PAD, 24, "Every yes you gave")
p.label(X1 - PAD, 24, "Something back", anchor="end")
p.seg(X0 + PAD, 31, X1 - PAD, 31, cls="hair", wobble=0.06)

# the items, each with a leader to what he expected for it
for i, (gave, back, w_gave, w_back) in enumerate(ITEMS):
    y = 50 + i * 18
    p.label(X0 + PAD, y, gave, cls="ital")
    p.label(X1 - PAD, y, back, cls="ital", anchor="end")
    p.straight(X0 + PAD + w_gave + 4, y - 0.4, X1 - PAD - w_back - 4, y - 0.4, cls="line dotted")

# where the total would be
p.seg(X0 + PAD, 98, X1 - PAD, 98, cls="hair", wobble=0.06)
p.label((X0 + X1) / 2, 114.5, "you never asked for it", cls="ital", anchor="middle")

p.label((X0 + X1) / 2, TEAR + 23, "a list only you are keeping", cls="ital", anchor="middle")

write(p, "plate-09-the-bottomless-yes",
      deck="You never named the deal, so she never agreed to it.",
      caption="Say what you need before generosity becomes debt.")
