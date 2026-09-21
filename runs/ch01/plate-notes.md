# Ch1 Plate Notes — 2026-09-20

**File:** `runs/ch01/plate.svg` — "The Three-Second Window"
**Reused, not new.** Copied from `books/the-stoic-husband/design/plates/three-second-window.svg`.

## What it shows, and why that is the mechanism

The distillation's **Mechanism: The Gap**, and its conversation sentence is
"Between what she says and your response is three seconds. What fills it,
chosen or inherited, is your marriage." The existing plate draws exactly that
and nothing else: one three-second bar, split 0.5s filled / 2.5s open, with
"she says something" at the left end and "the words are already out" at the
right. The filled part is the window; the rest is already firing. Its subtitle
is the second half of the conversation sentence verbatim.

Nothing I could draw would put the mechanism better, and a second Gap diagram
would be a competitor to an approved one.

## Runners-up, for the author's record

Both are Ch1's, both were left where they are:

- `the-operating-system.svg` — draws trigger + loaded meaning + THE GAP +
  automatic response. It is the *route* the impression takes, the chapter's
  umbrella mechanism, not "The Gap" as the distillation names it. It also
  fails the checker as it stands (two labels overflow the right margin, see
  below) and carries an em-dash in a label ("an impression — phantasia").
- `virtue-question.svg` — draws the chapter's practice (the four virtue
  labels), not its mechanism.

One plate per chapter: Ch1 ends with the window.

## Anchor image

The window itself, from the chapter's own line quoted in the plates README:
"that half-second where you're still somewhere between deciding and
reacting... and then the two and a half seconds after." No new image
introduced.

## Two changes I made to the copy

1. **A real defect, caught by the hardened checker and confirmed by
   rendering.** The source file sets `text-anchor="start"` / `"end"` as
   presentation attributes on two captions whose class already says
   `text-anchor:middle`. The stylesheet wins in a browser, so both captions
   rendered centred on the bar ends: "she says something" started 36px outside
   the left margin and "the words are already out" ran 16px past the right
   edge of the artboard. Fixed in the copy by moving the anchors to inline
   `style=`, which does win. The rendered result now matches the intent.
   **The same defect is still live in `design/plates/three-second-window.svg`.**
   I did not touch it (Rule 8). The desk reviewing the existing plates should
   make the same fix there, or the author should rule.
2. **House ink and ground.** Added `style="color:#1a1a1a"` and a white
   background rect, matching `runs/ch12/plate.svg`, the most recent chapter
   plate. Without them the filled block prints pure black against the other
   plates' near-black, and the plate has no opaque ground in the reader PDF.
   Purely a conformance change; no geometry or wording altered.

## Checker output, verbatim

```
runs/ch01/plate.svg
  clean
```

## What the render showed

Correct after the anchor fix: title, subtitle, both stage labels with their
durations, the split bar, both end captions inside the margins, the bracket,
THREE SECONDS, and the closing caption.

**A renderer finding the author should know about, not a plate defect.**
`chapter_pdf_local.svg_to_png` drops everything below roughly 83% of the
canvas height: Chrome is screenshotting a viewport shorter than the requested
window. It cuts the bottom two lines off this plate, the bottom three lines
off `runs/ch12/plate.svg`, and the closing lines off all three of my new
plates. I verified every plate by re-rendering into a viewport padded 140px
taller. Anything compiling plates into the reader PDF today should check that
it is not using the same call, or the bottom of every plate will be missing.

## For the author to rule on

- **Canvas.** This plate is 660x380; the house landscape standard is 640x430
  and Ch12 is 640x460. Three different canvases will show as three different
  page sizes in a reader PDF. I left the reused plate at its own size rather
  than reflowing the author's layout. Say the word and I will reset it to
  640x430.

## Round 2 (2026-09-20 17:45)

Reader Panel review `runs/design/2026-09-20-plate-reader-review.md`, section 2,
Ch01: EDIT. Every edit it named was applied.

**Applied.** Cut both time labels (*half a second*, *two and a half seconds*),
which is what fought the title. Cut the bracket measure and the displayed
THREE SECONDS. The span now carries two end labels only: *she says something*
at the left end, *the words are already out* at the right. The dark block is
relabelled **THE GAP**, the distillation's Mechanism name. Two short strokes now
rise out of that block at the same place, one solid glossed *chosen*, one dashed
glossed *inherited*: the chapter's own "chosen or inherited" made a mark rather
than a sentence, which is the panel's cross-set fix (section 4, the Lesson as a
mark). Closing line reworded off measurement to *"The part you choose is the
small one. It is still the one that decides."*

The block widened from 87px to 120px so both strokes stand inside it with room
to gloss them. It is still plainly the small part of the span, which is what the
closing line claims.

**Not applied.** Nothing the panel asked for was declined.

**Checker output, verbatim:**

```
$ python3 runs/design/svgcheck.py runs/ch01/plate.svg

runs/ch01/plate.svg
  clean
```

**What the render showed.** Rendered with `chapter_pdf_local.svg_to_png` and
read at full size and at phone width. The eye lands on the black block, then on
the two strokes standing in it, then on the two end labels. The solid and the
dashed stroke are legible against white at phone width because they sit above
the block, not inside it. No quantitative register remains: there is no number
anywhere on the plate. Nothing collides, and the strokes clear the dashed
stroke's gloss by more than the checker's 10px clearance.

**For the author to rule on.**

1. **Plate title versus Mechanism.** This plate is still titled by the chapter,
   THE THREE-SECOND WINDOW, while the distillation's Mechanism is **The Gap**,
   now the label on the dark block. The panel's edit put the Mechanism on the
   block and left the title alone; the standing house question ("are chapter
   plates titled by Mechanism") would retitle the plate THE GAP and leave the
   block unlabelled. One word, one file, your call.

## Round 3, the symbol pass (2026-09-21 04:53)

**Brief.** Outside reader feedback, accepted by the author: the plate read as a
progress indicator and only resolved once the labels were read. His fix, which
the author released for use: make the gap itself the hero rather than the
proportion, and name the two sides plainly. His falling-dominoes alternative is
excluded. Objects unchanged: one horizontal bar, a black block, tick/label marks.

**What changed.**

1. **The gap moved to the middle and became the biggest thing on the plate.**
   It was a short black block flush against the far left of the span, which is
   the shape of a progress bar and reads as *how far along you are*. It is now
   inset at dead centre, with a light outlined segment on each side, and it
   stands 12px proud of those segments top and bottom. Nothing else is dark. The
   eye lands on the interval first, which is the whole point of the chapter.
2. **The two sides are named.** WHAT SHE SAYS leans in from the left, WHAT YOU
   SAY NEXT from the right, both anchored toward the block so they point at it.
   Both are the author's endorsed sentence, split.
3. **Copy cut from six lines to three.** Subtitle: *"Between what she says and
   what you say next are three seconds."* Closing: *"Your marriage lives there."*
   That is the 2026-09-21 Author addition, one sentence, with the drawing sitting
   inside it: read the top, look, read the bottom. The old subtitle, the two end
   captions and the old closing line are gone.
4. **The chosen / inherited pair is gone from the drawing.** The solid and dashed
   strokes standing in the block were a second visual action competing with the
   interval, and an upright planted in a line is Ch02's device. The block keeps
   the Mechanism label, THE GAP.
5. **Canvas 660x380 to 640x340**, which settles the open question from Round 1:
   every other chapter plate in `runs/` is 640 wide and the checker's canvas row
   expects it.

**Reviewer suggestions taken:** the gap as hero, the two sides named plainly.
**Declined:** the dominoes redraw (excluded by the author's ruling), and any
human figure (excluded set-wide).

**Checker output, verbatim:**

```
$ python3 scripts/plate_check.py runs/ch01/plate.svg --chapter 1
runs/ch01/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x340
  [WARN] title       title 'THE THREE-SECOND WINDOW' / aria-label 'The Three-Second Window' vs Mechanism 'The Gap' (differs; inbox #065)
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    2 italic lines against a cap of 5 (3 labels + subtitle + closing line)
  [ ok ] alignment   4 centred texts on the axis or a shared column; 3 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

The captions row was WARN (6 italic lines against a cap of 3) before this round
and is now clear. The title row is the standing inbox #065 question and is the
only WARN left.

**What the render showed** (`runs/ch01/pdf/plate.png`, viewed at full size). The
dark block is the first thing the eye finds and the two names read as arriving at
it from either side. Covering every word but the title leaves a heavy block held
between two lighter ones, which is an interval; with the title above it, it is
three seconds between her words and yours. The proud block no longer reads as
fill, so the progress-bar misreading is gone. Nothing collides; the two side
labels clear each other by 160px.

**For the author to rule on.**

1. **The title, still.** Inbox #065. The plate is titled by the chapter (THE
   THREE-SECOND WINDOW) and the block by the Mechanism (THE GAP). One word, one
   file, and nothing else on the plate moves either way.
2. **"Chosen or inherited" is no longer anywhere on this plate.** It was in the
   old subtitle and drawn as two small strokes. The endorsed sentence replaced
   both. If you want the idea back, it is a third caption, not a mark, and it
   costs the plate its one-action reading.
