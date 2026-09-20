# Ch9 plate notes — The Bottomless Yes

**Date:** 2026-09-20
**File:** `runs/ch09/plate.svg` (aria-label, and so the landed filename: *The Bottomless Yes*)

## What it shows, and why that is the mechanism

`chapters/ch09/distillation.md` names the mechanism **The Bottomless Yes** and the
conversation sentence: *"He kept saying yes expecting something back for it, and
when it didn't come, the disappointment piled up quietly instead of turning into
one big blowup."*

The plate draws exactly that transaction and nothing else:

- **Left column, what you gave.** Three specific yeses, all three of them the
  author's own from the refined chapter: the night you did everything she wanted,
  the plan you went along with, her story heard all the way through.
- **Right column, what you expected.** Respect, warmth, being asked about. Each
  sits on a blank line that never gets filled in. The blanks are uniform so the
  column reads as one unpaid account rather than three separate ones.
- **The return trip.** One long dashed arrow running right to left under both
  columns, ending in nothing, captioned *"Nothing comes back, and you never once
  asked for it."* That is the deal that was never named, which is the chapter's
  whole engine.
- **Below the rule, where the shortfall goes.** Five ruled lines, the last one
  still being written, labelled *"a list only you are keeping."* Then the cost in
  the chapter's own words, apathy rather than peace, and the practice in one line.

No blowup, no Four Horsemen, no Glover, no self-silencing. Those are the
chapter's supporting material; the mechanism is the unpaid trade and the private
list, so that is all the plate carries.

## The anchor image, and the prose it comes from

The chapter's one image is the **list / gunnysack**: *"Gunnysacking. You keep every
one of these small disappointments quietly out of sight"* and *"Every
unreciprocated night adds one more line to it."* The anti-slop pass on the
chapter counted the sack family at two mentions and noted the chapter no longer
needs the sack to burst, so the plate draws the **list**, which is the form the
image takes in the body of the chapter, and the closing caption adapts the
chapter's own last line (*"while the sack is still light"*) to the drawn image:
*"Say it plainly and kindly, while the list is still short."* Drawing a literal
sack as well would have put two versions of one image on the page.

Two captions are the chapter's sentences, lightly compressed, not new claims:
*"Kept up long enough, that is not peace. It is apathy with better manners."*
(refined.md: *"But quiet unhappiness, kept up long enough, is just apathy with
better manners."*), and the subtitle, from *"You never named the deal out loud,
so she never agreed to it."*

## Reuse check

`design/plates/four-horsemen.svg` exists and its README row says the framing is
from Ch9 prose. It is **not** this chapter's plate: it draws Gottman's taxonomy,
which the distillation uses as a destination, not as the mechanism. It is a
framework plate, traceable to `okf/citations/gottman-four-horsemen.md`, and it
should stay that. `design/plates/four-ds.svg` belongs to Ch3 and Ch5 by its
concept's `chapter_slugs`. So: new plate, no competitor drawn.

## Style decisions, and what they were matched to

- Canvas 640x460 with an explicit white ground, matching `runs/ch12/plate.svg`,
  the most recent chapter plate. The 640-wide landscape and the left margin at
  x=44 match every plate in `design/plates/`.
- The full class block from ch12 verbatim (`.ttl .sub .lbl .txt .cap .src .rule`),
  same sizes, same letter-spacing, same opacities. `.txt` is set at 13px rather
  than 14 because two columns share the width; everything else is untouched.
- Title in spaced small caps, italic subtitle underneath, a hairline rule at
  opacity .28 dividing the two halves, italic captions carrying the argument.
  That is the pattern of `four-ds.svg`, `tipping-scale.svg` and ch12.
- Solid strokes for what actually happens, dashed strokes for what does not.
  Taken from `the-operating-system.svg`, where the unused gap is the dashed
  span, and from ch12, where the reach romance no longer has is dashed.
- No quotation on the plate, so Rule 3 and the transcription rule do not apply.
  No number, no statistic. No Stoic term, so nothing needs a gloss.

## Checks

`python3 runs/design/svgcheck.py runs/ch09/plate.svg`

```
runs/ch09/plate.svg
  clean
```

## What the render showed

Rendered at 3x through `scripts/chapter_pdf_local.py` and looked at.

- First render lost everything below y=373. That was the renderer, not the plate:
  Chromium's `--window-size` includes browser chrome the viewport does not, so the
  bottom band of every plate was dropped. The plate-review desk fixed
  `svg_to_png` to use Playwright while this desk was drawing; re-rendered after
  the fix and the whole canvas paints.
- First layout had the never-filled blanks trailing each expected item at
  different lengths. On the page they read as stray dashes. Set to one uniform
  column, x=470 to 576, and they read as one account never settled.
- "An evening spent the way she wanted" was too close to the row above it in
  sense and in width. Changed to "A plan you went along with, not yours."

## For the author

1. **The three yeses are named specifics.** They are the author's own, from the
   chapter's list beat. If any of them is too close to the real thing to print on
   a page that gets photographed, say which and it comes off.
2. **"a list only you are keeping"** is the plate's label for the tally. The
   chapter calls it both a list and a gunnysack. The plate uses only the list,
   for the one-image rule. Ruling wanted only if he wants the sack drawn instead.
