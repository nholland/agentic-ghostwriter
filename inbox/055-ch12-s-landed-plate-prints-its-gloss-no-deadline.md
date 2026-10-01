---
id: 055
status: resolved
raised_by: gw-designer
chapter: 12
opened: 2026-09-20 16:33
resolved: 2026-10-01 15:56
okf_receipt: runs/reconciliation/2026-10-01-inbox-055.json
---

# Ch12's landed plate prints its gloss 'no deadline, nobody watching' a quarter off the left edge. Land the one-line fix in runs/ch12/plate.svg?

A text-anchor attribute lost to the class's text-anchor:middle, so the browser centred the label on x=44. The checker trusted the attribute and said clean; it is fixed now and flags the landed copy. The run copy uses an inline style and renders inside the frame.

**Recommendation:** Land it; it is a position fix, no words change.

**Checked:**

```
python3 runs/design/svgcheck.py books/the-stoic-husband/design/plates/the-muscle-you-stopped-using.svg -> MARGIN y=340.0 'no deadline, nobody watching' -44..132. Same on runs/ch12/plate.svg -> clean.
```

**What unblocks this:** Replacing design/plates/the-muscle-you-stopped-using.svg with runs/ch12/plate.svg.

**Resolution (2026-10-01 15:56):** yes
