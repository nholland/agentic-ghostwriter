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
