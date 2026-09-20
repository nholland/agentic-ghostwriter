# Chapter 8 plate notes — 2026-09-20

**File:** `runs/ch08/plate.svg` · **Title (aria-label):** The Tipping Scale ·
**Reused verbatim** from `books/the-stoic-husband/design/plates/tipping-scale.svg`.
Also here: `runs/ch08/plate-proposed-fix.svg`, a proposal, not a deliverable.

## Why this is a reuse

Mechanism: **The Tipping Scale.** Conversation sentence: "Unfairness rarely
arrives as one moment. It's small things you never counted, tipping quietly
until you finally feel the weight."

The existing plate is named for the mechanism, its subtitle is "The tip feels
sudden. It never is," its loaded pan is labelled "weeks of weight nobody saw
land," and its closing line is "Relitigating the last one misses where the
weight came from." That is Ch8's first beat drawn by the author's own desk,
from `okf/frameworks/the-tipping-scale.md`. No competitor drawn; the file is
copied with nothing changed.

The plate draws the accumulation, not the two responses (Marcus's true-or-not
test, Seneca's paid-at-the-doing). That is correct: the Mechanism line names
the scale, and the two tools are the chapter's answer to it, not the mechanism
itself. One plate, one relationship.

## The anchor image, and the prose it comes from

"Individually, each one is nothing. Together, over weeks, they add weight to an
invisible scale. One day something small tips it, and the feeling that arrives
seems to come from nowhere." The scale is the chapter's one image and it is the
one on the plate.

No quotation appears on the plate. Ch8's prose quotes Marcus 5.28 and Seneca
Letter 81; neither is on the picture, which is the right outcome under the
quotation rule regardless of their status.

## Checker output, verbatim

```
$ python3 runs/design/svgcheck.py runs/ch08/plate.svg

runs/ch08/plate.svg
  clean
```

```
$ python3 runs/design/svgcheck.py runs/ch08/plate-proposed-fix.svg

runs/ch08/plate-proposed-fix.svg
  clean
```

## What rendering showed — and the one thing the author must rule on

Rendered, the plate says something the chapter does not.

The weight labelled **"the one that finally tipped it" sits on the pan that is
up.** All the accumulated weight is on the other pan, which is down. Read as a
scale, the lone weight tipped nothing: it is on the light side. The chapter
says the opposite, that the last one is another small one landing on the same
pile: "One day something small tips it."

The caption can be read as rescuing it ("Relitigating the last one misses where
the weight came from", so the thing you are arguing about is weightless), but
then the label on that weight is wrong, because it says that weight did the
tipping. Either the label or the position has to move.

This is the same family of defect the plates README already records for this
drawing's first draft ("the beam missed the fulcrum, the weights floated above
the pan"), caught by rendering and not by reading.

Two fixes, both one change:

- **Move the weight** to the loaded side, still falling, so the picture is a
  pile plus the last small one landing on it. Drawn in
  `runs/ch08/plate-proposed-fix.svg`, which changes nothing else: the lone dot
  moves from (480,243) to (160,232) with a short dashed fall line, and its
  caption moves with it. Rendered and checked clean.
- **Or change the label** on the existing plate from "the one that finally
  tipped it" to "the one you are arguing about", and leave the drawing alone.

I have not touched `design/plates/tipping-scale.svg`. The desk reviewing the
existing plates owns that file; this is its Chapter 8 consequence.

## Renderer caveat

`scripts/chapter_pdf_local.py:svg_to_png` clips roughly the bottom 19% of the
canvas (on a 420-tall canvas, nothing below y≈341 is captured). On this plate
that removes the closing line "Relitigating the last one misses where the
weight came from," which is the line carrying the argument. Verified with a
marker SVG: captions at y=330 render, y=346 and below do not. Every plate in
the book is affected, including ch12. Must be fixed before the reader PDF is
compiled. All visual checks in these notes were made through a padded window
(canvas height + 120px) instead.

## For the author to rule on

1. **The tipped-weight position or label** (above). Until he rules, the
   deliverable is the approved plate, unchanged.

## Round 2 (2026-09-20 17:45)

**Verdict acted on:** EDIT. The scale is kept; the panel called it the strongest
physical object in the set.

**Panel edits applied, all three.** The raised pan is now named: *everything you
told yourself was fine*, so the balance has a second term. *Relitigating the last
one misses where the weight came from* is now **Arguing about the last one misses
where the weight came from** ("relitigating" was the least plain word on any
plate). The corrective is on the plate for the first time, one line under the
loaded pan: *Name each one as it lands, and nothing has to tip* — the chapter's
first practice, and the Lesson arriving as something you can do rather than a
diagnosis.

**Two things the panel did not name, done anyway.** The drawing sat in the middle
of a canvas with a third of the height empty above it; the whole scale and its
four glosses moved up 68px and the canvas came in from 420 to 350, so the plate
is denser at phone width. And the file's opening comment no longer calls itself a
proposal: it is the chapter plate, and it records the one geometry change from
`design/plates/tipping-scale.svg` (the last small weight sits on the loaded side,
because Ch8's prose says the last one is another small one landing on the same
pile). The source file in `design/plates/` is still untouched by this desk.

**Not applied.** Nothing. The two Stoic tools of the chapter's Lesson (Marcus's
true-or-not-true test, Seneca's deed that pays itself) are still absent: they are
two tools for two directions, and drawing both would make a second plate. The
single corrective line covers the direction the drawing is about.

**Checker output, verbatim**

```
$ python3 runs/design/svgcheck.py runs/ch08/plate.svg

runs/ch08/plate.svg
  clean
```

(Two margin failures were fixed in between, both on the new copy: the pan label
at 613px and the corrective line at 375px against the 596 and 44 bounds.)

**What the render showed.** The scale now has two named sides, and the eye goes
loaded pan, raised pan, then the line that says what to do. The dot mass and the
single falling dot still read as the same kind of object, which is the point of
that pan. Ch7's field no longer uses this mark.

**For the author to rule on**

1. **The raised pan's label sits below and right of the pan**, not on it, because
   at 12px the copy is 266px wide and the pan is 64px. If he wants it visually
   attached, the copy has to get shorter, and the panel wrote that copy.

## Round 3, draft from concept A (2026-09-20 19:50)

**What it shows.** Two identical scales, mirrored about x=320, fed by the same
six small weights. Left, under UNCOUNTED, the weights fall on long dashed lines
that all lean toward one pan; a pile of twelve already sits in it and the beam
has tipped. Right, under NAMED, the same six weights are stopped the moment they
land, each resting on its own short stroke, and the beam holds level. The weights
on the right are still drawn, the same mark at the same size and opacity as the
left's: stopped, not gone. The space the left spends falling is, on the right,
the space where the naming happens, and that space holds the chapter's two tools.

**The carrier.** Same input, two outcomes, and the difference is whether anything
counted them. The drawing argues it; every caption only names what is drawn.

**The two misreadings, and what stops each.** "A comment every time something
bugs me" is stopped by the right gloss, which is the chapter's own practice and
says *to yourself*, and by the strokes being six small calm marks rather than a
stream. "The work disappears if you talk about it" is stopped by the weights
still being there on the right, in plain sight, resting on what stopped them.

**Every phrase and where it comes from.**

| On the plate | Source |
|---|---|
| THE TIPPING SCALE | distillation Mechanism, word for word |
| Unfairness rarely arrives as one moment. | Conversation sentence, first half |
| UNCOUNTED / NAMED | one word each, the chapter's own terms |
| WHEN IT LANDS ON YOU | refined.md section heading |
| is it true, or not true? | refined.md, "Is what she's saying true, or not true?" |
| WHEN IT'S YOURS | refined.md section heading |
| the work already paid itself | distillation Practice 3 |
| One day something small tips it. | refined.md, verbatim |
| Name it to yourself right then. | distillation Practice 1 |
| It's small things you never counted, / tipping quietly until you finally feel the weight. | Conversation sentence, second half, verbatim |

The subtitle is no longer "The tip feels sudden. It never is." That line is not
in the chapter; the Conversation sentence is, so it now opens the plate at the
top and closes it at the bottom, with the drawing in between. No quotation, no
number, no em-dash, no Stoic term unglossed: Marcus's test and Seneca's teaching
are on the plate as what they do, not as names.

**Checker output, verbatim**

```
$ python3 scripts/plate_check.py runs/ch08/plate.svg --chapter 8

runs/ch08/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x430
  [ ok ] title       title 'THE TIPPING SCALE' / aria-label 'The Tipping Scale' vs Mechanism 'The Tipping Scale'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    5 italic lines against a cap of 6 (4 labels + subtitle + closing line)
  [ ok ] alignment   12 centred texts on the axis or a shared column; 8 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

One FAIL was fixed in between: the Conversation sentence on a single line
measured 626px against the 552px text column, so it is set as two centred lines
and the block below the rule moved up ten pixels to keep the last baseline clear
of the bottom band.

**What the render showed.** The tipped beam and the loaded pan read first, the
level beam second, and the eye finishes on the sentence under the rule. The pile
sits inside the pan rather than on the cords, which was the round 1 defect. The
right pans are empty and that is the point: nothing reached them. The six stopped
weights are the ones carrying the reader's sense that the work still happened, so
they are drawn at full weight and are the only marks on the plate that touch a
solid stroke.

**For the author to rule on**

1. **The right pans are empty.** A stranger could read an empty pan as "nothing
   happened" rather than "nothing piled". The fix, if he wants one, is to move
   the six stopped weights down into the two right pans, three a side, level; the
   cost is that a scale with matched piles can read as keeping score, which is
   the thing Chapter 7 took apart.
2. **The subtitle changed** from the approved plate's "The tip feels sudden. It
   never is." to the chapter's own words. If he wants the old line back it needs
   to enter the chapter first, or be recorded as an Author addition in the brief.

## Round 3, revision from the Panel's read (2026-09-20 20:35)

**Verdict acted on:** EDITS, from `runs/ch08/plate-read.md`. All six addressed;
four applied as written, two applied in substance with the reason below.

1. **Applied.** *WHEN IT LANDS ON YOU / is it true, or not true?* and *WHEN IT'S
   YOURS / the work already paid itself* are off the plate. They were the Lesson,
   and "the work already paid itself" printed above a level beam was the pick's
   second misreading in ink. The plate now draws the Mechanism and nothing else.
2. **Applied with one word changed.** The right header is **NAMED WHEN IT LANDS**,
   not "NAMED AS IT LANDS": the grounded rule is that every run of three or more
   words is the chapter's, and "as it lands" is nowhere in Ch8, while "when it
   lands" is the chapter's own section heading. Same sense, chapter's words. The
   practice line *Name it to yourself right then.* now sits where the cut block
   was, directly under that header, as the right column's one gloss.
3. **Applied.** The six underlines are gone. The right weights now fall on their
   own short lines, straight down, three to each pan, and sit singly with space
   between them: the weight arrives, nothing stacks. Contrast with the left, where
   six lines funnel into one pan that already holds a pile.
4. **Applied, by compression rather than by moving one row.** The dot rows stay
   mirrored at the same height, because the argument is that the same things land
   on both men; moving the left row alone would break that. Instead the whole
   drawing is tighter (canvas 430 to 360, scales up 60px, beam span 160 to 120)
   and each column now carries a header, a gloss and a drawing of equal mass.
5. **Declined as written, addressed in the drawing.** The caption cannot centre on
   the loaded pan: at 12px it is about 190px wide, so centred at the pan's x it
   would cross the 40px left margin and fail the ink row, and it would be the only
   centred text on that axis, which fails the alignment row. Rule wins. So the
   mass moved to the caption instead: the beam is narrower, and the loaded pan
   sits at x=108 rather than x=88, inside the caption's own width.
6. **Applied.** The two-line footer is gone with its rule. The Conversation
   sentence appears once, as the subtitle. *One day something small tips it.* is
   the only line under the drawing, and it names what the left scale does.

**Format checklist**

- Every centred text on the axis or a shared column: title and subtitle x=320;
  UNCOUNTED, its gloss and the closing caption all x=168; NAMED WHEN IT LANDS and
  its gloss both x=472. Checker: 7 centred texts, none stray.
- The two scales mirrored about the centre: left block 86..250, right 390..554,
  exact mirror. Fulcrums at 168 and 472. Dot rows 88..248 and 392..552.
- Drawing blocks centred or mirrored: checker counts 8, all paired.
- Canvas 640 wide (640x360).
- Caption count within the cap: 4 italic lines against a cap of 4 (subtitle, one
  gloss per labelled element, one closing line). No room was left over, which is
  why the right column has no bottom caption.
- No bare `text-anchor` attribute: anchors are in `.ttl`, `.sub`, `.lblc`, `.cap`.
- No em-dashes, no digits, no quotation, no invented number.
- Nothing the chapter does not say: every phrase is `refined.md` or the
  distillation. *Each one was too small to name.* is the chapter's "because each
  one was too small to name"; *Name it to yourself right then.* is Practice 1;
  *One day something small tips it.* is verbatim; the subtitle is the
  Conversation sentence's first half.

**Checker output, verbatim**

```
$ python3 scripts/plate_check.py runs/ch08/plate.svg --chapter 8

runs/ch08/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x360
  [ ok ] title       title 'THE TIPPING SCALE' / aria-label 'The Tipping Scale' vs Mechanism 'The Tipping Scale'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    4 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   7 centred texts on the axis or a shared column; 8 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

No FAIL rows, and none were fixed in between: the first render of the new layout
passed every row.

**What the render showed.** The eye goes to the loaded pan and the tipped beam
first, then across to the level one. The pile reads as a mass of the same small
mark the falling weights are, so the weight is plainly cumulative and plainly
small-grained. On the right the three-and-three dots sit apart and low in the
pans, which reads as arrived and not stacked, and the level beam is the second
thing seen. No text block outweighs the drawing now; both columns end at the same
height and the only remaining asymmetry is the closing caption under the left
scale, which is where the tipping is.

**For the author to rule on**

1. **The right scale is level with weight in both pans.** It answers the pick's
   second misreading (the work does not vanish when you name it), but a defensive
   reader could read two equal pans as a score kept even with her, which is what
   Chapter 7 took apart. The alternative is empty right pans, which the last round
   showed reads as "nothing happened". I chose the first; it is his call.
2. **"NAMED WHEN IT LANDS"** is the Panel's label with one word swapped to stay
   inside the chapter's vocabulary (item 2 above). If he prefers "as it lands", it
   needs to enter the chapter or be recorded as an Author addition in the brief.
