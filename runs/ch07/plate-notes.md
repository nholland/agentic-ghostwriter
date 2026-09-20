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

## Round 2 (2026-09-20 17:45)

**Verdict acted on:** REPLACE CONCEPT. The reuse of
`design/plates/small-rocks-big-rocks.svg` is gone; this is the Designer's own
option 1 from the round-1 ruling above, drawn.

**Panel edits applied, all of them.** Retitled **THE PRIVATE TALLY** (aria-label
matches the distillation's Mechanism). Two ruled columns headed WHAT YOU COUNTED
and WHAT SHE COUNTED, ruled identically; the left carries three legible entries,
the right is completely empty. Both stand on one shared field, captioned *the
part neither column reached*. Subtitle kept: *The ledger can only count what it
can see.* Closing line added, as written: *Half the data, and it always said you
were ahead.* Nothing else was added.

**Copy, and where it comes from.** The three entries are the chapter's own
examples from beat one: "The router, that Tuesday" ("The internet goes down on a
Tuesday night... You reset the router"), "The coaching weekend" ("an entire
weekend at a tournament three hours away, coaching your kid's team"), "The day
off work" ("The day you took off work for the family"). No number appears
anywhere: the 60/40 line, Pillemer and the 7,000-couple study stay off the plate,
same as round 1.

**One drawing decision the panel did not name.** The right column's frame and
rules are **dashed**, the left's solid. That is the set's existing grammar for
*not visible to you*, and it is a mark rather than a sentence, so it does the
work a gloss would otherwise have to do. See the ruling below.

**The dot problem, fixed.** Ch7's field and Ch8's pan both used filled round dots
for different things. Ch7's field is now a field of **short tally strokes** (the
mechanism is a tally, and these are the marks nobody made); Ch8 keeps the round
dots as units of weight. The two are now different marks at a glance.

**Checker output, verbatim**

```
$ python3 runs/design/svgcheck.py runs/ch07/plate.svg

runs/ch07/plate.svg
  clean
```

**What the render showed.** Ten-second read: my page has three lines written on
it, her page has the same lines and I cannot read one of them, and under both
sits a field far larger than either column. The tally strokes read as marks, not
as texture, and they are plainly not the same object as Ch8's dots. No
collisions; the rasteriser now captures the full canvas, and both the field
caption and the closing line are visible.

**For the author to rule on**

1. **The empty column can be misread as "she counted nothing."** The dashed rules
   say *you never saw this page*, but they say it quietly. The one-gloss fix
   would be four words inside the right column, *you never saw this page*. The
   panel did not ask for it and the brief said not to add copy, so it is not
   there. One word from him and it goes in.
2. **The round-1 title question is now closed in practice**: this plate is titled
   by its Mechanism. If he wants plates titled by framework instead, this is the
   plate to say so on, because `design/plates/small-rocks-big-rocks.svg` still
   exists untouched and would become the chapter plate again.

---

## Round 3 (2026-09-20 19:25)

**What changed.** One line of copy, on the author's own words: the third entry in
WHAT YOU COUNTED goes from *The day off work* to *Cleaning the kitchen*. His
reason, verbatim: "On the private tally, let's swap the day off work with
cleaning the kitchen. The day off work is a bit vague." Nothing else on the plate
moved.

**Author addition, recorded as such.** *Cleaning the kitchen* is the author's
phrase, not the chapter's. Ch7's prose names the router and the coaching weekend;
it does not name the kitchen. The plate is therefore carrying one item that a
reader will not meet in the text. That is his call and he made it, but it needs
to survive into `plate-brief.md` under an **Author additions** heading when that
file is written, so a later desk does not "correct" it back to the prose.

**Checker output, verbatim**

```
$ python3 runs/design/svgcheck.py runs/ch07/plate.svg

runs/ch07/plate.svg
  clean
```

**What the render showed.** The new line sits well inside its rule: at the widest
plausible serif fallback it runs 76..232 against a rule that ends at 284, so there
is no crowding in any font. It is also the most concrete of the three entries now,
which helps the plate stand on its own: a router, a coaching weekend, a kitchen
are all things a reader can picture without the chapter.

**A note against the new standard.** The author's standing rule from this session
is "these plates need to stand on their own even if somebody hasn't read the
chapter." This plate passes on the left column and the field of marks. The
**right column is still empty by design**, and a cold reader may read that as
*she counted nothing* rather than *you never saw her page*. That is the same
open question raised in Round 1, and the new standard sharpens it rather than
settling it. Still one word from him: four words inside the dashed box, *you never
saw this page*, would close it.
