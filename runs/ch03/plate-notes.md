# Ch3 Plate Notes — 2026-09-20

**File:** `runs/ch03/plate.svg` — "The Closed Door"
**New.** `four-ds.svg` exists for this chapter but draws a different thing; see below.

## What it shows, and why that is the mechanism

**Mechanism: The Closed Door.** Four rows, each the same doorway seen again
later, the opening narrowing every time:

1. SHE BRINGS IT. Wide open. "She picked the time and came to you with it."
2. YOU EXPLAIN. A third shut. "Defend, deny, downplay, deflect. All four feel
   like honesty."
3. SHE UPDATES. Two thirds shut. "She counts what it costs to bring something
   to you."
4. SHE STOPS. A sliver. "The easy things still come. The ones that matter
   don't."

The conversation sentence is the mechanism's cost ("you taught her the
conversation wasn't worth having") and the drawing is the teaching happening:
nobody slams anything, the opening just gets smaller by degrees. The chapter's
own sequence is exactly this, "She does this enough times, and she stops. Not
the easy things... What stops is the harder stuff."

## Why it is not a competitor to `four-ds.svg`

`four-ds.svg` defines the four behaviours, one row each, as a taxonomy. It
does not draw a door and it does not draw accumulation. Here the four D's are
one row out of four, the thing that pushes, not the subject. The two plates
sit at different levels and can both exist; only this one is Ch3's chapter
plate.

## Anchor image and where it comes from

The door, the chapter's one image, held to the end: "Because she knows the
door is open" and "When she brings something to you tonight, the door is
either open or it isn't. She can tell. She's been keeping track longer than
you know." The two closing lines on the plate are that sentence, lightly
compressed. No new image is introduced.

## Plain English on Stoic terms

None on the plate. `praemeditatio malorum` is the chapter's remedy, not its
mechanism, so it is not drawn and therefore needs no gloss here. Flagged below
in case you want it.

## Style matched, and to what

- Canvas 640x430, house ink, white ground, class block, left margin 44,
  labels at x=44 with the figure starting at x=196: `four-ds.svg` and
  `runs/ch12/plate.svg` (which uses the same left label column against bars).
- Bars as the figure, with a solid fill against a light outline for what is
  closed: `runs/ch12/plate.svg`.
- Hairline rule above the closing lines, .28 opacity: same.
- No em-dash, no number, no study, no quotation. Gottman is in the chapter's
  prose and deliberately not on the plate: `gottman-four-horsemen.md` is
  `status: unverified`, and the plates README already records that no figure
  from it may appear.

## Checker output, verbatim

```
runs/ch03/plate.svg
  clean
```

The first pass was not clean. Two captions overflowed the right margin and
were shortened, and the closing sentence was split across two lines rather
than squeezed.

## What the render showed

The narrowing reads instantly, top to bottom, at phone width. The one risk the
render exposed: a row of bars with a filled portion can read as a progress bar
rather than a doorway, and a progress bar conventionally means *more done*.
The subtitle line ("The same doorway, four times. It never shuts in one go.")
and the row labels resolve it, and the direction of travel, open to shut,
matches the chapter. I judged it legible; it is the one call worth a second
pair of eyes.

Rendered through a padded viewport, because `chapter_pdf_local.svg_to_png`
drops everything below about 83% of the canvas. See `runs/ch01/plate-notes.md`.

## For the author to rule on

- **The subtitle is the conversation sentence shortened.** Full: "Every time
  you defended yourself, you taught her the conversation wasn't worth having."
  On the plate: "You taught her the conversation wasn't worth having." The
  dropped clause is what the four rows draw, and the full sentence overruns
  the artboard at subtitle size.
- **The doorway-versus-progress-bar reading above.**
- **No `praemeditatio malorum` on the plate.** The mechanism is the door. If
  you want the remedy on it, the honest way is a fifth line, not a fifth row,
  and it would need the gloss ("pre-living the conversation before it
  arrives"), which is the chapter's own plain wording.

## Round 2, the symbol pass (2026-09-21 04:53)

**Brief.** Outside reader feedback, accepted by the author. He wanted literal
doors; that is excluded and the bars stay. What was released for use: his copy,
which is tougher and clearer than the old subtitle and is on file as an Author
addition; a four-step progression that reads faster at phone size; and a final
state more final than a sliver.

**What changed.**

1. **The subtitle is the endorsed line.** *"Defend yourself enough times, and
   she stops bringing you the truth."* The old one ("You taught her the
   conversation wasn't worth having.") named the lesson; this one names the
   cost, and it also retires the Round 1 question about the conversation
   sentence being shortened to fit.
2. **The door actually shuts.** Row four was a sliver of light at the left end.
   It is now solid across the full width. Open, a third, two thirds, shut: four
   states, three visible steps, and an end state that is an end.
3. **The four rows read as one object.** Row pitch cut from 64px to 44px and bar
   height from 20px to 30px, so the stack is a single narrowing figure rather
   than four spaced rows. The four per-row captions are gone; the left labels
   alone carry the sequence.
4. **Labels.** SHE BRINGS IT was the one label the chapter does not say. It is
   now SHE BRINGS SOMETHING, the chapter's own words ("When she brings something
   to you tonight"). YOU EXPLAIN became YOU DEFEND, which is the first of the
   four D's and the verb the endorsed subtitle uses. SHE UPDATES and SHE STOPS
   stand.
5. **One closing line, not two.** "She can tell whether the door is open." is
   cut; "She's been keeping track longer than you know." is the last beat.
6. **Canvas 640x430 to 640x360**, the space the cut captions were holding.

**Reviewer suggestions taken:** the copy, the faster progression, the final
state. **Declined:** drawing literal doors (excluded by the author's ruling).

**Checker output, verbatim:**

```
$ python3 scripts/plate_check.py runs/ch03/plate.svg --chapter 3
runs/ch03/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x360
  [ ok ] title       title 'THE CLOSED DOOR' / aria-label 'The Closed Door' vs Mechanism 'The Closed Door'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    2 italic lines against a cap of 6 (4 labels + subtitle + closing line)
  [ ok ] alignment   3 centred texts on the axis or a shared column; 2 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

Both WARNs from the previous state are cleared (`grounded`, from SHE BRINGS IT
and the old orienting line; `captions`, which was 8 italic lines against a cap
of 6).

An earlier pass of this round was not clean and the row is kept because it set
the label size:

```
  [FAIL] geometry    MARGIN  y=138.0 'SHE BRINGS SOMETHING' 43..228
  [FAIL] ink         rendered ink inside the 40px margin bands: left=125
```

The label overran the left margin by one pixel at 12.5px. Set to 12px rather
than shortened, because the shorter version is the one the chapter does not say.

**What the render showed** (`runs/ch03/pdf/plate.png`). The narrowing is the
first thing the eye gets and it now arrives in one movement instead of four
stops. Covering every word but the title leaves an opening that closes in three
steps and then is closed, which under THE CLOSED DOOR is the chapter. Round 1's
open risk (a filled bar reading as a progress bar, which conventionally means
*more done*) is reduced but not eliminated: what settles it is that the last row
is entirely dark and nothing on the plate rewards that as completion.

**For the author to rule on.**

1. **The orienting line is gone.** "The same doorway, four times. It never shuts
   in one go." was the sentence telling a reader the four bars are one doorway.
   It was also copy the chapter does not say. The title plus the progression now
   carry it. If you want it back it is one line at y=98 and the rows drop 20px.
2. **YOU DEFEND for YOU EXPLAIN.** The four D's are all in the chapter and
   Defend is the first; explaining is what it feels like from the inside. I
   chose the reader's word over his. Say the word and it goes back.
