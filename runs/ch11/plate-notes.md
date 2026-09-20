# Ch11 plate notes — The Conversation She Has Never Heard

**Date:** 2026-09-20
**File:** `runs/ch11/plate.svg` (aria-label, and so the landed filename:
*The Conversation She Has Never Heard*)

## What it shows, and why that is the mechanism

`chapters/ch11/distillation.md` names the mechanism **The Conversation She's Never
Heard** and the conversation sentence: *"He treated every hard thing as something
to endure, and ran the argument forty times in his head while she heard it zero."*

The plate is that count, made visible.

- **Left, INSIDE YOUR HEAD.** A closed box with the same bar drawn seven times, one
  under another, identical: one argument, rehearsed. Captioned *"the same
  argument, run again"*, counted **FORTY TIMES**.
- **Right, IN THE ROOM.** A dashed box the same height, empty, with *"nothing said
  out loud"* in the middle of it and *"where it would have to happen"* under it.
  Counted **ZERO**.
- **Between them**, one short arrow that leaves the head, points at the room and
  stops well short of it. The rehearsal always aims at her and never arrives.
- **Under the rule**, the deferral ratchet in two lines, which is why the count
  keeps climbing: *"Each pass makes the next one more expensive. Raise it now and
  you are also defending the delay."* Then the chapter's own closing instruction.

The chapter's three piles (a door, no door, friction) are not drawn. They are the
sorting the chapter teaches on the way to this, and the distillation's Mechanism
line is the conversation, not the taxonomy. A three-pile plate would be a
different chapter's plate, and it would make the rehearsal count a footnote.

## The anchor image, and the prose it comes from

The chapter has no `metaphor_family:` line, so the anchor was found in the prose.
The image the chapter returns to is the **argument running in his head with a
version of her who is not in the room**: *"whole arguments conducted with a
version of her that isn't in the room. You've rehearsed the argument forty times
by now. She still hasn't heard it once"*, and earlier, *"You've had this
conversation forty times inside your own head. She's heard it zero."*

The plate's two other figurative candidates, the seagull and the torpedo, stay in
the prose. Drawing either would replace the chapter's own anchor with a bird or a
weapon, and the one-image rule is most visible on a plate.

**On "forty times".** It is not a statistic and it is not invented for the plate.
It is the author's own figure, in the refined chapter twice and in the
distillation's conversation sentence. Nothing on the plate claims a share of men,
a study or a rate.

## Reuse check

Nothing in `design/plates/` draws this mechanism. `okf/frameworks/the-deferral-
ratchet.md` and `seagull-and-torpedo.md` have no plate. New plate.

## Style decisions, and what they were matched to

- Canvas 640x430 and the explicit white ground, as with Ch10.
- Class block from `runs/ch12/plate.svg` verbatim, plus `.capl` and `.lblc`,
  which are `.cap` and `.lbl` with the anchor set in the class rather than as an
  attribute. Same fonts, same sizes, same letter-spacing, same opacities.
- The stacked bars are ch12's bar language: solid fill at opacity .82, 8px tall,
  in a left-labelled row block. In ch12 the bars are capacities kept by use; here
  they are repetitions. Same object, same weight, so the two plates read as one
  hand.
- Solid box for what is real to him, dashed box for what never happened, which is
  the dashed-equals-absent grammar used in `the-operating-system.svg` and ch12.
- Counts set in the small-caps label face so the reader's eye lands on FORTY
  TIMES and ZERO as a pair, the way `four-horsemen.svg` sets its four names.
- No quotation on the plate. Marcus Aurelius is quoted twice in the chapter and
  is deliberately not here: a plate gets photographed, and the transcription rule
  does not relax for it.
- No Stoic term on the plate, so nothing needs a gloss.

## Checks

`python3 runs/design/svgcheck.py runs/ch11/plate.svg`

```
runs/ch11/plate.svg
  clean
```

## What the render showed

- The first version put a dashed stub in a 46px gap between the boxes; on the
  page it read as a printing artefact rather than a movement. Narrowed both boxes
  to open the gap to 66px and made it one short solid arrow that stops short of
  the room.
- The right-hand caption first read *"and she has never heard it"*, which said
  the same thing as *"nothing said out loud"* inside the box. Changed to *"where
  it would have to happen"*, so the box says what is missing and the caption says
  what the room is for.
- Checked at phone width: the two counts and the two box labels stay legible when
  the plate is scaled to a phone's screen; the italic captions are the first
  thing to soften, which is the same behaviour as the existing plates.

## For the author

1. **The title drops the contraction.** The mechanism is "The Conversation She's
   Never Heard"; the plate says SHE HAS NEVER HEARD, because `land.py` takes the
   filename from the aria-label and an apostrophe in a filename is a small
   nuisance forever. If he wants the contraction on the face of the plate, the
   title text can carry the apostrophe while the aria-label stays plain, on his
   word.
2. **"Forty times" is printed on the plate.** Sourced above. Flagged because a
   number on a diagram is the thing readers photograph and quote back.

## Round 2 (2026-09-20 17:45)

**Verdict acted on:** EDIT, small. All of it is subtraction except the title.

**Panel edits applied.** Retitled to the distillation's exact Mechanism, **THE
CONVERSATION SHE'S NEVER HEARD**, in the title and in the root `aria-label`. The
displayed FORTY TIMES / ZERO pair is cut, per the panel's recommendation to keep
the subtitle instead: the same two figures were set twice, in the two largest
type sizes on the plate. One of the three closing lines is cut. Canvas came in
from 430 to 390 and the divider and both remaining lines moved up with it.

**The line I cut, and why it is a question.** The panel said the two say the same
thing and did not say which to keep. I kept *"Each pass makes the next one more
expensive."* and cut *"Raise it now and you are also defending the delay."* The
kept line reads faster at phone width; the cut one is closer to the
distillation's Challenge wording. Easy to swap.

**Not applied, with the panel's agreement.** The three-way sort (a door, no door,
friction) is still not drawn. The sort is the chapter's coverage; the silence is
its mechanism, and the mechanism is what a plate draws.

**Checker output, verbatim**

```
$ python3 runs/design/svgcheck.py runs/ch11/plate.svg

runs/ch11/plate.svg
  clean
```

**What the render showed.** With the two big numerals gone, the argument is the
pair of boxes: one packed with identical bars, one dashed and empty with *nothing
said out loud* in the middle of it. The numbers survive where they belong, in the
subtitle, said as a sentence.

**For the author to rule on**

1. **Which of the two closing lines stays** (above).
2. **The apostrophe.** The title now carries a curly apostrophe in SHE'S, to
   match the distillation exactly. If plate titles should stay straight-quoted
   for the typesetter, say so and it is one character.
