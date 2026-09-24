## Approved-prose copy refresh — 2026-09-24

This entry supersedes the historical copy rationale below. The 2026-09-22 verdict explicitly excluded the old plate from its approved PDF. The current compilation request includes a plate, so its copy now follows the landed chapter and distillation.

Geometry, bars, dashed empty box, arrow, divider, canvas, font classes, and colors are unchanged. The subtitle is now “You keep arguing with her in your head.” from the landed distillation's conversation sentence. The box labels are “IN YOUR HEAD” and “WITH HER”; the empty box says “you haven’t told her,” also from that sentence. The closing lines are “Tell her what’s bothering you.” from its Lesson and “Then listen.” from Practice 2. This removes the obsolete numerical rehearsal count and the misleading implication that one conversation always suffices.

Checked against the landed chapter directly, rather than relying on the old brief's broader grounding corpus. Rendered at 3x with Sharp and visually inspected: no overlap, clipping, or crowded labels; the repeated argument remains visibly confined to his head, with the conversation with her still absent. The house style matches the existing Chapter 12 plate and the design/plates collection.

`python3 runs/ch13/check-plate-local.py runs/ch11/plate.svg --chapter 11`

All eleven rows pass: charset, geometry, anchor-attr, em-dash, digits, canvas (640x376), title, grounded, captions (4/4), alignment, ink. No remaining checker warnings. No book files edited.

---

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

---

## Round 4, the outside-reader round (2026-09-21 04:53)

**Scope.** The author's ruling: *"No rethinks. Just improve our existing
concepts."* The reviewer called this one of the strongest plates in the packet
and said to barely touch it. Every object, size and position is round 3's: two
boxes at the same size, one solid-bordered and packed with heavy dark bars, one
an empty dashed outline, one arrow crossing between them.

**The one change he asked for, done.** The closing sentence was doing too much
at once. It is now the two author-endorsed lines on file (`plate-brief.md`,
2026-09-21): a short instruction, **Say the true thing while it is still small**,
and under it a two-word maxim, **Kindly. Once.**, set at 15px so it carries. The
old single line, *Say the true thing on the Tuesday you notice it, small and
kind and once*, is gone. Breaking it gives the words the weight he wanted.

**The opening line is kept exactly**, as he singled it out: *You have run it
forty times. She has heard it zero.*

**Three glosses cut, and this is more than "barely touch".** *the same argument,
run again* only restated the label INSIDE YOUR HEAD above a stack of seven
identical bars. *where it would have to happen* only restated IN THE ROOM. Both
were also `grounded` misses, and the first was the plate's `alignment` WARN, a
centred text sitting alone on x=180. Cutting them also made room for the split
closing without going over the caption cap. **nothing said out loud** stays,
because it is the one gloss that stops the empty box being read as a to-do list,
and it is now start-anchored inside the box rather than centred, which keeps the
axis clean.

That is three lines removed where he said to change one. It is caption-cutting
only, the cross-cutting rule for this round, and no line, box, bar or arrow
moved. Flagging it because it exceeds "barely" in letter if not in spirit.

**One drawing touch.** The crossing arrow is dashed now instead of solid, at
.45. It reads as setting out rather than arriving, which is the chapter's point
and was previously being carried by the gloss that is gone.

**plate_check.py, verbatim**

```
$ python3 scripts/plate_check.py runs/ch11/plate.svg --chapter 11
runs/ch11/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x376
  [ ok ] title       title 'THE CONVERSATION SHE’S NEVER HEARD' / aria-label 'The Conversation She’s Never Heard' vs Mechanism "The Conversation She's Never Heard"
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    4 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   4 centred texts on the axis or a shared column; 6 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

Round 3 carried three WARNs (`grounded`, `captions`, `alignment`). All cleared.
The title row passes because the checker normalises the curly apostrophe; the
plate keeps ’ and the distillation keeps ', which is a typographic difference
and not a discrepancy.

**What the render showed.** Rendered at 2x. Seven black bars in a solid box, an
identical empty dashed box beside it, and a dotted arrow that does not reach.
*Kindly. Once.* lands as the last thing on the plate and is the line a reader
would photograph.

**For the author.** One judgement: *Each pass makes the next one more expensive*
was cut, and it was a good line. It went rather than **nothing said out loud**
because the caption cap allowed only one of the two and the other one is what
stops the empty box being misread. If he wants it back, it costs the gloss.
