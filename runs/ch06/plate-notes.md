# Chapter 6 plate notes — 2026-09-20

**File:** `runs/ch06/plate.svg` · **Title (aria-label):** The Tally You Don't Read Aloud · **New drawing.**

## What it shows, and why that is the mechanism

Mechanism: **The Tally You Don't Read Aloud.** Conversation sentence:
"Resentment doesn't come from doing too much. It comes from being the only one
who can see it."

The plate is two bars and one fork.

- **THE WEEK** is a dashed outline: everything you actually carried, real and
  unreadable by anyone else. Caption: "the bucket you emptied, with no slot on
  the calendar."
- **TONIGHT** is the same bar, solid: "her hands moving, yours still." Under
  it: "The comment fires on the one the room can see."
- Below the rule, the fork the chapter turns on. **READ IT ALOUD** gives "now
  there are two tallies / and neither one gets shorter." **SAY WHAT YOU SEE**
  gives the chapter's own sentence back to her.

The closing pair states the mechanism plainly: "Keeping the tally is not the
problem. Reading it out is. / Read yours out and you have handed her a reason
to keep one."

That is the chapter's argument and not Chapter 7's. See the note below.

## How this differs from Chapter 7's plate

Both chapters have a tally. They are different claims and the two plates are
different diagrams.

- **Ch6** is about **visibility in a moment and what you do with it.** The
  tally is accurate; it is just invisible to her, and the damage is done by
  reciting it. The picture is two bars (unseen, seen) and a fork (recite,
  or name what she is doing). There is no rock, no sand, no proportion.
- **Ch7** is about **the tally's data being wrong.** It can only hold the few
  contributions big enough to remember, so it always says you are ahead. The
  picture is proportion: three big rocks against a field of small ones.

One plate says *do not read it out*. The other says *it was never a count*.

## The anchor image, and the prose it comes from

Ch6's own image is the **bucket**: "it just lives in the bucket labeled
'whatever needs doing'... There's no slot on the calendar that says 'ceiling
fan.' There's no moment where either of you notices it got emptied again." The
dashed bar is that bucket-week, drawn as a thing that exists and cannot be
seen. The solid bar is the chapter's visible moment: "What's in this room is
one person sitting and one person folding."

The quoted line on the right of the fork is the chapter's, lightly trimmed:
prose has "I see you're working. I appreciate it. You want to sit down, or
should I help first?"; the plate drops the middle sentence for width and keeps
the rest word for word. It is the author's sentence, not a source quotation, so
the citation rule for quotations does not apply.

Not drawn: Musonius Rufus on the "community of life", Marcus on getting out of
bed, and the Four D's. The Four D's already have their own plate
(`design/plates/four-ds.svg`), and drawing them here would make this the Ch3
plate a second time.

## Stoic terms

None on the plate, so no gloss is owed. The chapter itself uses no Greek or
Latin term (its Editor's Notes say the same), and the Marcus self-check is
carried in the chapter, not here.

## Style decisions, and what they were matched to

- Canvas `0 0 640 430`, white background rect, `style="color:#1a1a1a"` on the
  root: matched to `runs/ch12/plate.svg` and `four-ds.svg`.
- Two stacked bars with a left-hand `lbl` and a 10.5px caption under it is the
  exact form of the ch12 plate's rows (WALKING / RUNNING / READING, then
  ROMANCE with "no deadline, nobody watching" beneath).
- Solid bars are `fill="currentColor" opacity=".82"`, the ch12 value. The
  unseen bar uses `stroke-dasharray="3 5"` at 1.2 stroke and .5 opacity, the
  ch12 / operating-system treatment for what is not in play.
- The vertical hairline between the two halves of the fork is the divider from
  `small-rocks-big-rocks.svg`; the horizontal hairline above it is the
  `four-ds.svg` row rule. No arrowheads, none exist in the house set.
- Curly apostrophes and curly quotation marks, as in `four-ds.svg`.

**One technical correction worth keeping:** left-anchored captions are set with
`style="text-anchor:start"`, not the `text-anchor="start"` attribute. The `.cap`
class sets `text-anchor:middle`, and a CSS class beats a presentation
attribute, so the attribute form silently centres the caption and runs it off
the left edge. That is the defect `runs/design/svgcheck.py` was hardened for
mid-session; the ch12 plate has it.

## Checker output, verbatim

```
$ python3 runs/design/svgcheck.py runs/ch06/plate.svg

runs/ch06/plate.svg
  clean
```

## What rendering showed

No geometry defects. The two bars read as the same week twice, once unseen and
once seen, and the fork reads as a choice rather than a sequence. First
rendering carried the caption "The comment fires on the solid one," which is
studio language about the drawing rather than prose about a marriage; changed
to "The comment fires on the one the room can see."

Same renderer caveat as Ch5: `svg_to_png` clips the bottom of the canvas, so
the two closing lines vanish in the shipped helper's PNG. Checked through a
padded window instead.

## For the author to rule on

1. **The subtitle carries half the conversation sentence.** "Resentment does
   not come from doing too much" fits; the whole sentence with "It comes from
   being the only one who can see it" does not fit one line at the house
   subtitle size, and every existing plate has a one-line subtitle. The second
   half is carried by the dashed bar and its caption. If he wants the whole
   sentence, the plate needs a two-line subtitle, which would be a new house
   pattern and is his call, not mine.
2. **The trimmed quoted line.** "I appreciate it." was dropped for width. If it
   matters, the fork's right column becomes three lines instead of two.

## Round 2 (2026-09-20 17:45)

Reader Panel review, section 2, Ch06: EDIT, cut half. The panel's finding was
that this was two plates on one page, and that the divider split attention
exactly where the plate should land.

**Applied.** The entire lower two-column panel is cut: READ IT ALOUD, SAY WHAT
YOU SEE, the vertical divider, and with them **the set's only quotation**, the
scripted line in quotation marks. That removes the one place in the set where a
plate could be photographed carrying speech. One caption is added under the
remaining pair, the panel's wording: *"The week is real. Only tonight is
visible."* The two closing lines are kept as the closing block, as the panel
asked, because they are the mechanism.

With half the plate gone the remaining pair was re-laid out to fill the canvas:
both bars are wider and deeper, and each label and its gloss now sit clear of
the bar rather than tucking under its edge.

**Not applied.** Nothing the panel asked for was declined. The two bars remain
the same length: the argument is visibility, not volume, and making the week
longer would restate Ch07's claim about size.

**Checker output, verbatim:**

```
$ python3 runs/design/svgcheck.py runs/ch06/plate.svg

runs/ch06/plate.svg
  clean
```

**What the render showed.** The first render after the cut had the row-one gloss
running under the dashed bar and touching it; the checker does not see
text-on-shape collisions, the render does. Both glosses were dropped clear and
the bars nudged. The final render reads as one comparison: a dashed empty bar
and a solid black one, the same size, one of them visible. At phone width the
dashed outline still reads as an outline.

**For the author to rule on.**

1. **The filled bar's meaning.** Here it means *visible*; the panel notes the
   same filled bar means accruing cost on Ch03 and rehearsal on Ch11. That is a
   book-wide call, not this plate's, and it is the panel's `design-language.md`
   recommendation in section 4.

## Round 4, edits from the standalone sweep (2026-09-20 21:50)

Brief: `runs/design/2026-09-20-plate-standalone-sweep.md`, FAIL 06. The finding
was polarity, not layout: the solid black bar was captioned "her hands moving,
yours still," so black read as *her* contribution and the ghost as his, flipping
the plate into the self-pity position ("I do the invisible work and get no
credit") that the subtitle exists to deny.

**Applied, exactly three edits.**

1. **Fills swapped.** THE WEEK (y=124) is now the solid bar,
   `fill="currentColor" opacity=".82"`. TONIGHT (y=216) is now the dashed ghost,
   `stroke-dasharray="3 5"` at 1.2 stroke, .5 opacity. Geometry, widths and
   positions are untouched, so the two bars remain the same length: the argument
   is still visibility and not volume (Round 2's note stands).
2. **TONIGHT's gloss relabelled** from "her hands moving, yours still" to
   "what she can see right now."
3. **Title untouched.** The sweep also asked for a retitle to THE WEEK SHE
   DIDN'T SEE. Not applied: the title is the distillation's Mechanism line
   (inbox #065) and a retitle is the author's call, not this desk's.

**Checker output, verbatim:**

```
$ python3 scripts/plate_check.py runs/ch06/plate.svg --chapter 6
runs/ch06/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x430
  [ ok ] title       title 'THE TALLY YOU DON’T READ ALOUD' / aria-label "The Tally You Don't Read Aloud" vs Mechanism "The Tally You Don't Read Aloud"
  [WARN] grounded    no three-word run of these appears in the chapter, its distillation or plate-brief.md: 'what she can see right now', 'The week is real. Only tonight is visibl', 'Keeping the tally is not the problem. Re'
  [WARN] captions    6 italic lines against a cap of 4 (2 labels + subtitle + closing line) (over; inbox #066)
  [ ok ] alignment   5 centred texts on the axis or a shared column; 3 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

No FAIL rows. Both WARNs are carried over from Round 3 and neither is new work
from this round: the caption count is unchanged (inbox #066), and the new gloss
is the sweep's own wording, adjacent to the chapter's "It fires on what's
visible right now, in the room, tonight" and the distillation's "What's visible
right now isn't the same as what's actually true," but not a three-word match.

**What the render showed** (`runs/ch06/pdf/plate.png`). The polarity now reads
the intended way in the first second: the heavy black mark is the reader's own
week, and the empty dashed outline is the thin slice of it she is standing in
front of tonight. The self-pity reading is gone, because the black no longer
belongs to her. The closing pair then does the work the title promises: the
solid bar is real and still must not be recited.

**For the author to rule on.**

1. **Dashed now carries "tonight."** In the rest of the set dashed means *not
   real* or *not in play*; here it means *small and visible*. The caption "The
   week is real. Only tonight is visible." holds it, but a reader who skips the
   caption could read the ghost as "tonight doesn't count," which is not the
   claim. The alternative is dashed for the week and a short solid bar for
   tonight, which draws size and so drifts toward Ch07. Flagging, not changing.
2. **The retitle stands open.** The sweep's collision finding against Ch07 (both
   plates titled around a tally) is unresolved until he rules on the Mechanism
   line.

## Round 5, the symbol pass (2026-09-21 04:53)

**Brief.** Outside reader feedback, accepted by the author: "the black horizontal
bar again feels like data visualization rather than marriage", and separately,
Ch06 and Ch07 are starting to read as two variations of one accounting graphic.
His calendar redraw is excluded; the two bars stay.

**What changed.**

1. **The two bars became one bar and a window.** They were the same length,
   stacked, one solid and one a dashed ghost, which is the shape of a bar chart
   comparing two quantities. The week is now a single long solid bar, and the
   dashed outline is a small frame standing around its last stretch, taller than
   the bar so the dashes read above and below it. One object, one thing happening
   to it: the whole week is real and only its last inch is standing in the light.
   That is the endorsed sentence drawn.
2. **This is the one place I stretched the ruling, and it should be checked.**
   The objects are the same two: a solid bar and an empty dashed outline. What
   changed is their relationship, from side by side to one inside the other. If
   you read that as changing an object rather than its arrangement, say so and it
   goes back to two stacked bars with the new copy, which is a smaller but real
   improvement.
3. **The collision with Ch07 is gone.** Ch07 is two ruled ledger pages side by
   side with a field of tally marks. Ch06 is now one heavy bar with a small frame
   at its end. Nobody will mistake one for a variant of the other.
4. **The copy is the author's endorsed lines and nothing else.** Subtitle: *"You
   are counting the week. She can only see tonight."* Closing, over two lines:
   *"Resentment grows when you expect someone to read a tally you never showed
   them."* That states the asymmetry far more plainly than the old plate did, and
   it keeps the blame where the chapter puts it, on the man holding the tally.
5. **Four lines cut:** both glosses, "The week is real. Only tonight is visible."
   and "Keeping the tally is not the problem. Reading it out is." The last is the
   one I would most want back if a line is ever added here; the endorsed closing
   covers it with "a tally you never showed them."
6. **Canvas 640x430 to 640x338.**

**Reviewer suggestions taken:** the data-visualisation complaint, the Ch07
collision, the copy. **Declined:** the calendar redraw (excluded by the author's
ruling).

**Checker output, verbatim:**

```
$ python3 scripts/plate_check.py runs/ch06/plate.svg --chapter 6
runs/ch06/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x338
  [ ok ] title       title 'THE TALLY YOU DON’T READ ALOUD' / aria-label "The Tally You Don't Read Aloud" vs Mechanism "The Tally You Don't Read Aloud"
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    3 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   4 centred texts on the axis or a shared column; 2 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

Both previous WARNs cleared: `grounded` was flagging three lines, all now cut or
replaced by endorsed copy, and `captions` was 6 italic lines against a cap of 4.

An intermediate state of this round produced one row worth keeping, because it
set how the drawing is grouped:

```
  [WARN] alignment   drawing off centre with no mirror and no text on its axis: block 484..572 centred at 528
```

The frame was its own top-level group and read as an off-centre block. Both rects
now sit in one group, which is also what they are: one figure.

**What the render showed** (`runs/ch06/pdf/plate.png`). The polarity the Round 4
sweep fixed still holds: the heavy black mark is his week, not hers, so the
self-pity reading has nothing to stand on. Covering every word but the title
leaves a long black record with a small window around its last inch, which reads
as *most of this is not in view* before any word is read. The Round 4 worry about
dashed meaning "not real" is weaker here than it was, because the dashes now
enclose part of the solid bar rather than replacing it: the frame reads as a
viewport, not as an absence.

**For the author to rule on.**

1. **The nesting, above.** The one change in the six that goes further than
   rearranging.
2. **"Keeping the tally is not the problem. Reading it out is."** is off the
   plate. It is the chapter's sharpest nuance and the title's own logic. Adding
   it back is one line inside the caption cap.
3. **The retitle question from Round 4 is closed by this round in practice.** The
   sweep wanted THE WEEK SHE DIDN'T SEE; the drawing now says that without the
   words, and the title stays the Mechanism line.

## Round 6, the standalone-read fix (2026-09-21 05:10)

**Brief.** `runs/design/2026-09-21-plate-standalone-read.md`, **FAIL 06**. Cold, the
Panel got *the week is long and tonight is a sliver*, which is proportion. The
chapter is about visibility. Its diagnosis: the bar was solid black through both
regions, so nothing in the ink separated what you count from what she can see,
and the dashed frame read as a crop mark.

**What changed, one edit.** The bar is ghosted outside the frame and solid inside
it. The single rect `x=76 w=488 opacity=.85` is now two abutting rects of the same
bar: `x=76 w=412 opacity=.17` and `x=488 w=76 opacity=.88`. No geometry moved, no
object was added, no copy changed. The dashed frame is untouched at `.75`.

That is the Ch08 grammar borrowed exactly, as the Panel asked: **faint means it
landed and nothing counted it, dark means it was named.** Here, faint is the week
she cannot see and dark is the stretch standing in her view. It also settles the
Round 4 worry in these notes about dashed meaning *not real*: the dashes now
enclose the only solid thing on the plate, so they read as the edge of a field of
view rather than as an absence.

**Not applied.** The Panel also wanted the closing caption down to one line. It is
the author's endorsed sentence and it cannot be halved without writing new copy;
one line needs the caption set at 11.5px to clear the margin (measured 569px at
12px against 552px of live width), which shrinks the best sentence on the plate to
win a line. Two-line captions already exist on Ch11 and Ch12. Left for the author.
Its retitle recommendation (the word *tally* colliding with Ch07) is unchanged and
still the author's, inbox #065.

**plate_check.py, verbatim**

```
$ python3 scripts/plate_check.py runs/ch06/plate.svg --chapter 6
runs/ch06/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x338
  [ ok ] title       title 'THE TALLY YOU DON’T READ ALOUD' / aria-label "The Tally You Don't Read Aloud" vs Mechanism "The Tally You Don't Read Aloud"
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    3 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   4 centred texts on the axis or a shared column; 2 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

No FAIL rows and no WARNs.

**What the render showed** (`runs/ch06/pdf/plate.png`, 2x, and again at 0.62x for
phone width). The plate now says *she sees only this much* before a word is read:
a long pale record with one black stretch inside a window at its end. At phone
width the pale bar still holds as a bar, and the black is the only thing the eye
lands on. The junction of pale and dark falls exactly on the frame's left edge,
which is what makes the frame read as a limit of view rather than as a highlight.

**For the author.** Nothing new. Two standing items: the second caption line,
above, and the retitle.
