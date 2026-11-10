"""Keep learning her after you've won her (Chapter 13).

Same man, two ways of finding the one thing she'd be excited about this
Saturday. Planning from memory reaches a dotted woman: who she was at
twenty-six. Asking reaches the woman who is actually there.
"""
from platekit import Plate, W, write

p = Plate(height=222, seed=109, title="Keep learning her after you&#8217;ve won her")

HIM, HER = 66, 258


def row(y0, name, line, now, then=""):
    floor = y0 + 76
    chest = floor - 37
    p.label(1, y0, name)
    if then:                                             # the rest of the instruction, on the same line
        p.label(1 + len(name) * 6.6 + 3, y0 + 0.4, then, cls="ital")
    for i, text in enumerate(line):                       # the words sit under the woman they describe
        p.label(HER, floor + 14.5 + i * 12, text, cls="ital", anchor="middle")
    p.straight(HIM - 40, floor, HER + 40, floor)
    p.person(HIM, floor, "man")
    p.person(HER, floor, "woman", cls="line" if now else "line dotted")
    drift = p._noise(0.8, 70)
    p.stroke(lambda x: chest + drift(x), HIM + 26, HER - 27, cls="bold" if now else "line", wobble=0.0)


row(9, "Planning a date", ["what she liked at twenty-six"], now=False)
row(126, "Ask her", ["who she is now"], now=True,
    then="and ask about it again later in the week")

write(p, "plate-13-keep-learning-her",
      deck="One thing she&#8217;d be excited about this Saturday.",
      caption="You can love her and keep doing things<br>for her, and still have stopped<br>being curious about who she is now.")
