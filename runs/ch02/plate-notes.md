# Ch2 Plate Notes — 2026-09-20

**File:** `runs/ch02/plate.svg` — "The Mood Mirror"
**New.** No existing plate draws this chapter.

## What it shows, and why that is the mechanism

**Mechanism: The Mood Mirror.** The plate draws the same evening twice, on two
tracks that start and end in the same place, so the only variable is what sits
in the middle.

- Track one: HER WEATHER, THE MIRROR, THE SAME WEATHER. One unbroken line. It
  runs straight through because nothing is in the way. Caption: "You match it
  before you notice. Two people in a low is a lower low."
- Track two: HER WEATHER, THE GOVERNING PART, YOUR OWN WEATHER. The middle
  stretch is dashed, because nothing carries you across it. Caption: "The day
  is still hers. What comes through the door is yours."

That is the chapter's argument in one relationship: her weather is the same on
both lines, so the mood you bring is not downstream of hers. The outsourcing
in the conversation sentence is visible as a line with nothing in the middle.

**Solid means it runs by itself; dashed means the part you have to do.** This
is the same convention as the approved `the-operating-system.svg`, where the
dashed span is the gap most men run straight through.

## Anchor image and where it comes from

Weather, the chapter's one image, carried in its closing line: "a man with his
own weather, who knows how to come home." The mirror is not a second metaphor
but the chapter's named mechanism ("The human mirror" is its own beat label),
and the Line Editor's 2026-06-24 note on this chapter records the same
judgement: mirroring is the named concept the chapter tracks, weather is the
metaphor family. The plate uses both the same way the prose does.

"Not to go cold. To bring something real through the door" is the chapter's
own closing beat, kept as the bottom line so the plate cannot be read as
Stoicism-as-armour, which `01-voice.md` forbids.

## Plain English on Stoic terms

`hegemonikon` appears only as a gloss under its plain-English label: "THE
GOVERNING PART" above the line, "hegemonikon, the part of you that governs
your own state" below it. Label plain, term second, the same order as THE GAP
/ prohairesis on `the-operating-system.svg`. "THE GOVERNING PART" is the
chapter's own phrase ("he wrote about the governing part of a man"), which is
why I used it over the distillation's "ruling faculty".

## Style matched, and to what

- Canvas 640x430, `style="color:#1a1a1a"`, white ground rect: `four-ds.svg`,
  `virtue-question.svg`, `runs/ch12/plate.svg`.
- Class block (ttl / sub / lbl / cap / rule / ln) copied from
  `the-operating-system.svg`, the closest structural precedent (a line with
  labelled stages). Unused classes kept, as the existing plates keep theirs.
- Title 17px letter-spaced caps at y=40, italic subtitle at y=66, hairline
  rule at .28 opacity dividing the two halves: `runs/ch12/plate.svg`, which
  divides the same way.
- Left margin 44, right bound 596.
- No em-dash anywhere on the plate. No number, no study, no quotation.

## Checker output, verbatim

```
runs/ch02/plate.svg
  clean
```

## What the render showed

Both tracks read at a glance, and the dashed middle is clearly different from
the solid one without needing a key. The three-line block at the bottom
(gloss, track caption, closing line) sits close; I opened the spacing once
after the first render. The plate's upper third is airier than its lower
third, which matches Ch12's balance.

Rendered through a padded viewport: `chapter_pdf_local.svg_to_png` drops
everything below about 83% of the canvas, so the straight call hid all three
bottom lines. See `runs/ch01/plate-notes.md` for the detail. Not a defect in
this file.

## For the author to rule on

- **"THE SAME WEATHER" as an element name.** It is the payoff of the mirror
  (what arrives in you is a copy), but it is the one label on the plate that
  is a result rather than a thing. "YOURS, COPIED" was the alternative and
  read as smaller.
- **Two tracks, one plate.** The corrective shares the plate with the failure.
  I read that as one mechanism shown twice rather than two ideas, on the Ch12
  precedent (the rule, then the corner nobody aimed at). If you read it as two
  plates' worth, the fix is to cut track two and let the chapter carry the
  corrective.

## Round 2 (2026-09-20 17:45)

Reader Panel review, section 2, Ch02: EDIT. The panel's diagnosis was that the
labels did the work the drawing should, with solid-versus-dashed on one thin
rule carrying the whole argument.

**Applied.** Row two is redrawn: her weather now runs in and **stops**, there is
a real white gap, and **the governing part is a short upright stroke standing in
that gap**, drawn at 2.6 against the tracks' 1.5 so it reads as an object rather
than a line style. Your own weather starts on the far side of the gap as its own
line. The dashed continuation is gone, so nothing on this plate now depends on
telling solid from dashed. Row one keeps the same two tick marks at the same two
x positions and runs straight through them, so the difference between the rows
is a physical break in one place, not a change of texture. THE MIRROR is
relabelled **YOU, MATCHING IT** (a mirror is not a line; a man matching her is).
The *hegemonikon* gloss is cut, and with the Greek word gone the label THE
GOVERNING PART is already plain English and needs no gloss.

**Applied with one judgement call.** The panel said "cut one of the three
closing lines (keep *The day is still hers...*)". I cut the *hegemonikon* line
and moved *"Not to go cold. To bring something real through the door."* up to
sit under row two as that row's gloss, leaving exactly one closing line. The
alternative reading, cutting it outright, loses the chapter's explicit guard
against reading the plate as "go cold", which is the misreading the chapter
spends a section preventing. The plate now runs at the panel's cap: subtitle,
one setup line, one gloss per row, one closing line.

The setup line changed one word, *"What sits in the middle"* to *"What stands in
the middle"*, because something now stands there.

**Checker output, verbatim:**

```
$ python3 runs/design/svgcheck.py runs/ch02/plate.svg

runs/ch02/plate.svg
  clean
```

**What the render showed.** The break in row two is the first thing the eye
finds, and the upright stroke reads as planted. At phone width the two rows
still read as the same evening twice. Row one's ticks sit at exactly the x
values where row two breaks, which is what makes the comparison land.

**For the author to rule on.**

1. **The guard line as a gloss.** If you would rather the plate carry only the
   panel's single closing line, deleting *"Not to go cold..."* is one line and
   nothing else moves.

## Round 4, edits from the standalone sweep (2026-09-20 21:50)

Brief: `runs/design/2026-09-20-plate-standalone-sweep.md`, section "FAIL 02 — The
Mood Mirror". All four edits applied, no new concept.

1. **Row two's line is closed.** The break Round 2 opened is gone: row two is now
   one continuous `M60 344h520`, the same span as row one, with the same two ticks
   at x=250 and x=390. The governing stroke at x=320 runs `v314..374`, straight
   **through** the line rather than sitting in a gap in it. The panel's cold read
   was "disconnect from her, go cold", which the closing line then had to deny in
   words; with the line closed the drawing no longer argues against its own caption.
2. **THE GOVERNING PART is now SOMETHING OF YOURS.** Faculty language, even in
   English, stops a reader who has not read the chapter.
3. **THE SAME WEATHER is now HER WEATHER, DOUBLED**, set on two lines (y=150, y=170)
   at the same x=510 column centre because one line of twenty letter-spaced caps
   overruns the right margin band. Row one now reads as loss, not symmetry.
4. **Second footer cut.** Two footer lines existed; "The day is still hers. What
   comes through the door is yours." (y=416) is deleted and "Not to go cold. To
   bring something real through the door." is the only closing line. Row two was
   nudged down 8px (labels 306, line 344, footer 390) to take up the slack.

**Checker output, verbatim:**

```
$ python3 scripts/plate_check.py runs/ch02/plate.svg --chapter 2

runs/ch02/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x430
  [ ok ] title       title 'THE MOOD MIRROR' / aria-label 'The Mood Mirror' vs Mechanism 'The Mood Mirror'
  [WARN] grounded    no three-word run of these appears in the chapter, its distillation or plate-brief.md: 'The same evening, twice. What stands in ', 'YOU, MATCHING IT', 'SOMETHING OF YOURS', 'YOUR OWN WEATHER'
  [ ok ] captions    4 italic lines against a cap of 9 (7 labels + subtitle + closing line)
  [ ok ] alignment   12 centred texts on the axis or a shared column; 4 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

No FAIL rows. The `grounded` WARN is the sweep's own wording plus two labels held
from earlier rounds; the chapter has "her weather", "his own weather", "the
governing part", and "To bring something real through the door", so every label is
a phrase the chapter could have written, but "something of yours" and "her weather,
doubled" are not verbatim in it. Author's call if he wants them chapter-exact.

**What the render showed.** `runs/ch02/pdf/plate.png`. The bottom line reads
continuous at a glance: the eye crosses row two without a stop, and the heavy
upright at x=320 reads as one thing planted in the line rather than as a wall
between her and you. The two rows now differ by exactly one added object, which is
the comparison the plate is making. Ten-second read at phone width: her weather in,
her weather doubled out; her weather in, something of yours in the middle, your own
weather out. That is the Conversation sentence.

**For the author to rule on.** Row two keeps the two plain ticks at x=250 and x=390
so it is visibly the same line as row one. They cluster near the heavy stroke and
could be read as noise; cutting them would make the stroke lonelier but would break
the parallel that carries "the same evening, twice".

## Round 5, the symbol pass (2026-09-21 04:53)

**Brief.** Outside reader feedback, accepted by the author: "intellectually
correct, but probably one of the more abstract plates. The horizontal lines and
tick marks look like a mathematical diagram. 'Something of yours' is also too
vague." His weather-panel redraw is excluded; the drawing stays two lines.

**What changed.**

1. **The axis ticks are gone.** The four small ticks at x=250 and x=390 were
   what made the plate read as a number line, and the Round 3 note already had
   them open as a question ("could be read as noise"). Both rows are now one
   clean span of the same length, so the parallel the ticks were protecting is
   carried by the lines themselves.
2. **The doubling is drawn instead of asserted.** Row one's line enters at
   stroke 1.5 and leaves at stroke 5 from the midpoint on. That is weighting,
   not a new object, and it is the one visual action the plate needed: her
   weather comes in, and what leaves is heavier. Row two's line is the same
   weight end to end, because something of his is planted in it. The two rows
   now differ in a way a stranger can see before reading anything.
3. **SOMETHING OF YOURS is gone.** The upright is labelled **YOUR OWN WEATHER**,
   which is the chapter's own image ("a man with his own weather") and the
   author's endorsed line ("Bring your own weather"). Row one's right end is
   **THE STORM DOUBLES**, also endorsed. The vaguest label in the set is out and
   both remaining labels are concrete.
4. **Copy count.** YOU, MATCHING IT and the two mid-plate captions are cut. What
   is left is the title, the subtitle, four labels and one closing line.

**Reviewer suggestions taken:** the abstraction complaint (ticks cut, doubling
drawn), and the label complaint in full.
**Declined:** the weather-panel redraw (excluded by the author's ruling). The
weather language lives in the copy, which is where he put it.

**One asymmetry, on purpose.** Row two has no right-hand label. Row one produces
something new and worse and says so; row two produces nothing new, and the line
running on unchanged is the statement. Adding a fourth label there would have
meant inventing copy.

**Checker output, verbatim:**

```
$ python3 scripts/plate_check.py runs/ch02/plate.svg --chapter 2
runs/ch02/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x368
  [ ok ] title       title 'THE MOOD MIRROR' / aria-label 'The Mood Mirror' vs Mechanism 'The Mood Mirror'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    2 italic lines against a cap of 6 (4 labels + subtitle + closing line)
  [ ok ] alignment   4 centred texts on the axis or a shared column; 4 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

No FAIL rows, and the `grounded` WARN that stood through Rounds 3 and 4 is
cleared: every phrase on the plate is now the chapter's or an Author addition on
file. That closes the "author's call if he wants them chapter-exact" question
from Round 4.

**What the render showed** (`runs/ch02/pdf/plate.png`). The thickening reads at a
glance and lands as *more of the same thing*, not as a different object. Row two
reads as one continuous line with a post planted in it; the Round 4 finding that
the line must not break still holds. Covering every word but the title leaves a
line that doubles and a line that does not, which is the mechanism. The upright
is the only mark that leaves the line in either row, so it stays the thing the
eye goes to in row two.

**For the author to rule on.**

1. **The missing fourth label.** See the asymmetry note above. If you want row
   two's outcome named, the words have to come from you.
2. **Stroke 5 against 1.5 is more than double.** Drawn at exactly double the
   difference is too small to see at phone width. The claim on the plate is the
   endorsed sentence's, not a measurement.
