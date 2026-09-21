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

## Round 2 (2026-09-20 17:45)

**Verdict acted on:** EDIT, trim. Nothing was added.

**Panel edits applied.** The three short dashed stubs to the right of *Respect /
Warmth / Being asked about* are gone; they duplicated the long return arrow and
read as unfinished drawing. One closing line is gone. The canvas came in from 460
to 440 and the kept line moved up with it.

**The line I cut, and why it is a question.** The panel said cut one and keep
*"Say it plainly and kindly, while the list is still short."* So the line that
went is *"Kept up long enough, that is not peace. It is apathy with better
manners."* That is the chapter's title claim in one sentence, and it is the only
place on the plate where the cost of the silence is named. I cut it as
instructed, and I am flagging it rather than quietly choosing for him.

**Kept, deliberately.** The ruled list with *a list only you are keeping*, which
the panel called the best mark on the plate and the one that connects to Ch11's
box; the long dashed return arrow that comes back empty, which is the carrier.

**Checker output, verbatim**

```
$ python3 runs/design/svgcheck.py runs/ch09/plate.svg

runs/ch09/plate.svg
  clean
```

**What the render showed.** The right-hand column is quieter now and the eye
follows three arrows out, then one long dashed line back with nothing on it, then
the list. Ten-second read: everything went one way and the list is his alone.

**For the author to rule on**

1. **The apathy line.** Restore it, or leave the plate with one closing line? The
   panel's cross-set finding is that these plates carry too much italic copy, and
   this is the cheapest place to prove it. But "silence is not peace" is the
   chapter's name.

---

## Round 3 (2026-09-20 19:25)

**(a) The vague label is gone.** *Being asked about* becomes **Being heard**. The
author: "'Being asked about' is super vague." The replacement is not mine; it is
the chapter's own word. `chapters/ch09/refined.md` line 105 names the reward he
expected as "(respect, warmth, being heard)", which is exactly the three-item
column the plate draws, in the chapter's order. So the right column is now a
straight lift from the prose rather than a paraphrase of it.

**(b) The lower block is one centred object.** It was not laid out; it had drifted.
The five ruled lines sat at x=170..380, left of centre, with the gloss floating
at x=486 beside them and the closing caption centred under neither. Of the two
fixes offered I took the first, lines centred on 320 with the gloss directly
beneath, because the second (centre the combined bounding box of lines-plus-gloss)
centres on a *text width*, and text width changes with the font. On the author's
machine, with real Georgia, a bounding box tuned to the fallback serif would drift
off centre again. Middle-anchored text and a geometric rule centre themselves in
any font. The fix should not be able to come undone by a font substitution.

Vertical room for the stack came from tightening the upper block, not from
growing the canvas: rows moved from 32px apart to 28, and every element above the
rule moved up by between 4 and 28px. Canvas stays 640x440. No copy was cut or
added to make it fit.

**(c) The upper block, which was also off.** The two columns now sit on one grid,
left edge 44 and right edge 596, so the pair is centred on 320 and spans exactly
the same width as the horizontal rule below it. The dashed return arrow spans that
same 44..596, so it now visibly travels the full width of the two columns instead
of starting in white space 156px past the last word of the right column, which is
what it did before. The three outbound arrows sit in the gutter between the
columns at 345..389, centred in it.

**A defect the checker could not see, and how it was caught.** `svgcheck.py`
measures margins and collisions against DejaVu Serif metrics. It passed the plate
while the right column label overshot the right edge of the grid by 11px in the
actual render, because the rasteriser's bold serif sets those capitals wider than
DejaVu does. It was found by decoding the rendered PNG and measuring the ink
extent of each horizontal band, then moving the right column from x=415 to x=404.
Final measured ink, in plate units:

```
both column labels           44.0 .. 595.7  centre 319.8
dashed return arrow          44.3 .. 595.7  centre 320.0
horizontal rule              44.0 .. 595.7  centre 319.8
five ruled lines            214.3 .. 425.3  centre 319.8
gloss                       257.0 .. 382.7  centre 319.8
closing caption             197.0 .. 441.7  centre 319.3
```

Every band is on the 44..596 grid or centred on 320 within a pixel. The lesson is
worth keeping: **the checker is a floor, not a proof of layout.** It knows nothing
about centring, and its font is a guess. Render and measure.

**A second defect, in the checker itself.** `runs/design/svgcheck.py` would not run
at all: it imported `ttfwidth` from its own directory, where only a stale
`__pycache__/ttfwidth.cpython-311.pyc` remained; the source lives in `scripts/`,
and Python 3.11 will not import a pyc without its source. Every invocation died
with ModuleNotFoundError. Fixed in place by searching this file's directory and
then the repo's `scripts/`, with the history written into the comment so the path
does not get "corrected" a fourth time. Worth the author knowing, because it means
any plate checked between that move and now was **unchecked, not clean.**

**Checker output, verbatim**

```
$ python3 runs/design/svgcheck.py runs/ch09/plate.svg

runs/ch09/plate.svg
  clean
```

**What the render showed.** Three arrows out to three short words, one long dashed
line back with nothing on it, then a ruled list sitting squarely on the plate's
centre line with its own caption tucked under it. The gloss now reads as the label
of the list instead of a stray remark beside it, and the 20px gap above it against
the 32px gap below keeps it grouped with the lines rather than with the closing
sentence. No copy changed except the one word the author asked for. No
em-dashes; every text-anchor is set in a class, none as a bare attribute.

**Still open, carried from Round 2.** The cut apathy line ("Kept up long enough,
that is not peace. It is apathy with better manners."). Under the author's new
standard, that the plates must stand on their own for somebody who has not read
the chapter, the case for restoring it is stronger than it was: it is the only
place the *cost* of the silence gets named, and without it a cold reader sees an
unfair trade but not why it matters. The counter is the panel's cross-set finding
that these plates carry too much italic copy. His call, not mine.

---

## Round 4, the outside-reader round (2026-09-21 04:53)

**Scope.** The author's ruling: *"No rethinks. Just improve our existing
concepts."* Objects are round 3's: short solid arrows running one way, one long
dashed arrow running back to empty space, a small stack of ruled lines with the
last one cut short.

**The reviewer's verdict.** "The intellectual structure is excellent. The
illustration is too much like a business transaction diagram." He wanted the
contrast between everything going out and nothing coming back to be the first
thing the eye reads, rather than something assembled from labels.

**What changed, and it is all weighting.** The plate used to be two text columns
with thin arrows between them, so the eye landed on reading. Now:

- The three outgoing arrows are stroke 3, solid black, with solid heads. They
  are the darkest thing on the plate.
- **What you gave is dark; what you expected is pale.** The right column's
  entries sit at .32 and its label at .42. That is the argument drawn rather
  than captioned: the things you actually did are solid, the things you were
  waiting for were never more than an expectation.
- The return trip is one hairline dashed line at .34, running the full width
  back to an arrowhead with nothing behind it, and it has been moved up to sit
  directly under the three rows so out-and-back reads as one unit.
- The list stack went heavier, stroke 2.4 at .88, because it is where all of it
  actually lands.

**Copy.** The subtitle is kept exactly as the reviewer asked: **You never named
the deal, so she never agreed to it.** The closing is now the author-endorsed
line on file, **Say what you need before generosity becomes debt**
(`plate-brief.md`, 2026-09-21), replacing *Say it plainly and kindly, while the
list is still short.* It is warmer and it names the mechanism.

Two captions were cut and one short one put in their place. *Nothing comes back,
and you never once asked for it* and *Every yes that does not come back becomes
a line on a list* are gone; the return arrow now carries **you never asked for
it** (the chapter's own clause, "something you never asked for directly"), and
the stack keeps **a list only you are keeping**. Italic count went from five,
which was over cap and a standing WARN, to four, which is at cap.

The two column labels were both `grounded` misses. WHAT YOU GAVE became **EVERY
YES YOU GAVE** ("A yes you gave expecting something back for it") and WHAT YOU
EXPECTED became **SOMETHING BACK** ("you expect something back for it"). Both
are the chapter's words now and the WARN is cleared.

**What I declined, and why.** The reviewer's redraw was a hidden receipt being
handed over. It is excluded twice over: it introduces objects this plate does
not have, and it needs a hand, and the author ruled objects only, no human
figures. Not attempted.

**plate_check.py, verbatim**

```
$ python3 scripts/plate_check.py runs/ch09/plate.svg --chapter 9
runs/ch09/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x430
  [ ok ] title       title 'THE BOTTOMLESS YES' / aria-label 'The Bottomless Yes' vs Mechanism 'The Bottomless Yes'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    4 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   5 centred texts on the axis or a shared column; 6 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

Round 3 carried two WARNs (`grounded`, `captions`). Both cleared.

**What the render showed.** Rendered twice at 2x. The first render had the
return arrow sitting far below the columns with white space between, so out and
back read as two separate events; moving it to y=236 fixed that. Final render:
three black arrows leaving solid words and arriving at grey ones, a dotted line
coming back to nothing, and a heavy list underneath. The left column entries run
to x=322 at the widest serif fallback and the arrows start at 336, so the gutter
holds in any font.

**For the author.** One thing worth his eye: the left entries are set at 12.5px
rather than the house 13px, because the longest of them ("A night you did
everything she wanted") needs the room to clear the arrow gutter. If he wants
13px back, the shortest fix is to trim that entry, which is the chapter's line.
