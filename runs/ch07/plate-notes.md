# Chapter 7 plate notes — 2026-09-20

**File:** `runs/ch07/plate.svg` · **Title (aria-label):** Small Rocks, Big Rocks ·
**Reused** from `books/the-stoic-husband/design/plates/small-rocks-big-rocks.svg`,
with two label centres nudged (see below). No competing plate drawn.

## Why this is a reuse and not a new drawing

Mechanism: **The Private Tally.** Conversation sentence: "The ledger you keep
in your head can only count the visible things, so it was always going to tell
you that you're ahead."

The existing plate's subtitle is *"The ledger can only count what it can see."*
Its two labelled groups are "BIG ROCKS: Countable. Citable in an argument. A
small share of the total." and "SMALL ROCKS: Too many and too small to count.
Almost all of it." That is the chapter's claim, in the chapter's own terms, and
it is already traceable to `okf/frameworks/small-rocks-big-rocks.md`. Drawing a
second picture of the same proportion would give the book two visual languages
for one idea, which is what the reuse rule exists to stop.

It draws the mechanism, but not all of it. See the ruling below.

## What it leaves out

The distillation's Challenge has a second half: "that tally only ever had
access to half the data: your side, not hers." The plate shows *what a tally
can count*; it does not show *whose column it is*. The chapter's line
"arithmetic done on one page of a two-page ledger" is not in the picture.

I did not draw that second half, because doing so would have meant a second
rocks-and-sand diagram in the same book.

## The anchor image, and the prose it comes from

Ch7 beat "**Two honest ledgers**": "Picture a jar filled with rocks. A few big
ones go in first... What fills most of the space is sand: hundreds of small
acts done without tracking them... The big contributions are countable,
memorable, citable in an argument." The existing plate is that paragraph drawn
as two fields rather than as a jar, and the closing line of the chapter, "no
math was ever going to find the bottom of that jar," survives it.

Deliberately absent, and should stay absent: the 60/40 figure and the Pillemer
and 7,000-couple study. Numbers on a plate are exactly what Rule 2 guards, and
`design/plates/README.md` records the same decision for the Four Horsemen
plate.

## What changed in the copy

Nothing in the drawing and no word of the labels. The left label group moved
from x=158 to x=168 and the right from x=483 to x=478, because the checker
measures against the widest plausible serif fallback (DejaVu Serif) and the two
caption lines overflowed the 44px margins there: 36..280 on the left and
368..598 on the right. Rendered, the labels still sit centred under their
fields. **This is a defect in the source file** and belongs to whoever is
reviewing `design/plates/`; the source is unchanged by me.

## Style

Nothing to match: this is the house style, drawn by the author's desk. Canvas
`0 0 640 420`, the standard seven-class style block, stroke 1.6 circles, dot
field at `opacity .62`, one hairline divider.

## Checker output, verbatim

```
$ python3 runs/design/svgcheck.py runs/ch07/plate.svg

runs/ch07/plate.svg
  clean
```

(Before the two label nudges, the same command printed:
`MARGIN  y=354.0 'Countable. Citable in an argument.' 36..280` and
`MARGIN  y=354.0 'Too many and too small to count.' 368..598`.)

## What rendering showed

The proportion reads instantly at phone width: three outlined rocks against a
field too dense to count. Labels sit centred under their fields after the
nudge. No collisions.

Renderer caveat, same as the other chapters: `svg_to_png` clips the bottom
~19% of the canvas, so in the shipped helper's PNG both caption pairs
disappear and the plate becomes two unexplained fields. That must be fixed
before the reader PDF is compiled or this plate loses its argument.

## For the author to rule on

1. **Reuse or new.** If he wants the chapter's plate to carry the "your column
   only" half, say so and I will draw **The Private Tally**: your column
   legible with three named entries, her column ruled and empty, both standing
   on the same uncounted field. That would replace this reuse, not join it.
2. **The title.** The plate is titled SMALL ROCKS, BIG ROCKS; the mechanism is
   called The Private Tally, and `land.py` names the file from the title. If
   chapter plates should be titled by their mechanism, this is a one-line
   change to the copy, and then the book has two files with the same drawing
   and different titles, which I would rather he decided than I did.
