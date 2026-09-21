# Ch4 Plate Notes — 2026-09-20

**File:** `runs/ch04/plate.svg` — "The Hole Maker"
**New.** No existing plate draws this chapter.

## What it shows, and why that is the mechanism

**Mechanism: The Hole Maker.** One fence post, drawn three times:

1. THE OUTBURST. Five nails driven through the post. "A nail goes in. You know
   which one it was."
2. THE APOLOGY. The nails are gone. Five holes are still there, in the same
   places. "The nail comes out. The hole stays where it was."
3. MONTHS ON. Ten holes, the first five among them. "Nothing she could point
   to. Just a settled sense of you."

Then the turn the chapter actually argues: "The holes stop being incidents.
They become what she believes." And the chapter's own instruction: "Stop
making holes."

That is the conversation sentence made visible. The nail is retrievable and
the hole is not, so the plate shows what an apology does and what it does not
do, which is the whole mechanism. The three panels are the accumulation the
prose describes, "the accumulated weight of incidents each addressed and moved
past."

## Anchor image and where it comes from

The nails and the fence post, the chapter's one image, from the parable in
"The holes": the father, the box of nails, a nail driven for every lost
temper, one pulled for every day without one, and a fence full of holes at the
end. The plate stays inside that image and adds nothing to it.

**No words from the parable are quoted.** The chapter itself calls it "origin
unknown and widely circulated", so the father's lines get no quotation marks
and no place on a plate that will be photographed.

## Plain English on Stoic terms

None on the plate. Seneca's two stages, the involuntary jolt and the choice
after it, are the chapter's remedy, not the mechanism the distillation names,
so they are not drawn. Flagged below.

## What is deliberately absent

No number, no study, no percentage. The chapter cites Sell et al. 2009 and
Gottman on contempt; neither is on the plate. `gottman-four-horsemen.md` is
`status: unverified`, and the plates README already records that its
specifics may not appear in the manuscript, let alone on a shareable plate.
The contempt claim on the plate is stated as the book's own chain of cause
("they become what she believes"), not as a research finding and not with a
name attached.

## Style matched, and to what

- Canvas 640x430, house ink `#1a1a1a`, white ground rect: `runs/ch12/plate.svg`.
- Left label column at x=44 against a figure starting at x=216, three stacked
  rows, hairline rule at .28 before the closing lines: `runs/ch12/plate.svg`,
  which stacks three labelled bars the same way.
- Class block from `four-ds.svg`.
- Stroke weight 1.2 for the post outline, 1.6 for the nails, matching the
  1.2 to 1.5 range the existing plates use; filled circles for the holes, the
  only fill on the plate besides the ground.
- No em-dash. Contractions kept, per the voice spec.

## Checker output, verbatim

```
runs/ch04/plate.svg
  clean
```

The first pass overflowed the right margin on one caption, which was
shortened; the three captions were also re-centred on 376 rather than on the
post's own centre to buy margin.

## What the render showed

The nails read as nails (head above the post, shaft through it), the holes
read as holes, and the three rows read as one post over time rather than three
posts. Row 2's holes sit at exactly row 1's nail positions, which is what
makes the sequence work; row 3 keeps those five and adds five more. Legible at
phone width.

Rendered through a padded viewport, because `chapter_pdf_local.svg_to_png`
drops everything below about 83% of the canvas. See `runs/ch01/plate-notes.md`.

## For the author to rule on

- **"Just a settled sense of you."** The chapter says "an updated sense of who
  she was dealing with", which will not fit the line. My compression keeps the
  meaning but is my wording, not yours.
- **Seneca's two stages are not on the plate.** The distillation names both
  the holes and the gap between the first surge and the second stage. One
  plate draws one mechanism, and the distillation's Mechanism line says The
  Hole Maker, so the stages went to the chapter. If you want them drawn, that
  is a second plate and a finding about the distillation, not a change to this
  one.

## Round 2 (2026-09-20 17:45)

Reader Panel review, section 2, Ch04: EDIT, one change, with two options. The
panel recommended the second and that is what was done.

**Applied.** The sub-caption reads **"One fence post, over the years. Hot or
cold, both drive a nail."** Row three shows ten holes where rows one and two
show five; with "three times" gone the drawing no longer contradicts its own
caption, and the doubling reads as more years rather than as an error. Nothing
else on the plate moved.

**Not applied.** The panel's first option (setting the five original holes solid
and the five later ones light grey, and relabelling row three) was not taken;
the panel itself recommended the second as the complete fix, and greying half
the holes would have introduced a fourth meaning for a filled dot in a set the
panel already flags for unstable primitives.

**Cross-plate.** Ch04 and Ch05 now share one nail glyph and one hole glyph
exactly, as the brief required. Ch04 is the reference: nail as a 1.6 shaft with
a 16px head stroke across the top, hole as a filled circle r=4, board as a 26px
rect at stroke 1.2 and opacity .55. Ch05 was redrawn to those numbers, so the
promise "the nail comes out, the hole stays where it was" is now the same two
objects across the two chapters.

**Checker output, verbatim:**

```
$ python3 runs/design/svgcheck.py runs/ch04/plate.svg

runs/ch04/plate.svg
  clean
```

**What the render showed.** Unchanged from round one apart from the caption. The
three rows still read top to bottom as one post over time.

## Round 3, the symbol pass (2026-09-21 04:53)

**Brief.** Outside reader feedback, accepted by the author. He called this one of
the strongest concepts in the packet and asked for two things: a clearer
sequence, and a fix for a real logic bug. The bug: the plate's subtitle said
every outburst drives a nail *you will never fully pull out*, when the whole
metaphor depends on the nail coming out. It is the hole that stays. The endorsed
line on file fixes it.

**What changed.**

1. **The bug is gone.** The subtitle is now *"Anger isn't strength."*, the
   chapter's own sentence, and the three rows carry the author's endorsed
   sequence one sentence each:
   THE OUTBURST, *"Every outburst drives a nail."*
   THE APOLOGY, *"An apology can pull it out."*
   MONTHS ON, *"The hole remains."*
   Nothing on the plate now claims the nail cannot be pulled out, and the
   sentence that runs down the page is the argument in the order the drawing
   makes it.
2. **"Stop making holes."** stays, and is promoted to subtitle size (13.5px
   against the captions' 12px) under the rule, because it is the only
   instruction on the plate and the reviewer called it excellent.
3. **Two lines cut.** The orienting line "One fence post, over the years. Hot or
   cold, both drive a nail." and the closing pair's first half, "The holes stop
   being incidents. They become what she believes." The second was also the
   longest ungrounded phrase on the plate.
4. **Nothing drawn moved.** The post, the nail glyph (1.6 shaft, 16px head), the
   hole glyph (filled circle r=4), the five nail positions, row two's holes at
   row one's nail positions and row three's ten: all identical, shifted up 14px
   as a block to take the space the cut orienting line left. The Ch04/Ch05 glyph
   promise recorded in Round 2 is unaffected, and Ch05 no longer draws nails at
   all.
5. **Captions re-centred on the post's own axis (388, was 376).** Optical
   alignment only.
6. **Canvas 640x430 to 640x396.**

**Reviewer suggestions taken:** the logic fix and the sequence.
**Declined:** nothing he asked for on this plate.

**Checker output, verbatim:**

```
$ python3 scripts/plate_check.py runs/ch04/plate.svg --chapter 4
runs/ch04/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x396
  [ ok ] title       title 'THE HOLE MAKER' / aria-label 'The Hole Maker' vs Mechanism 'The Hole Maker'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    5 italic lines against a cap of 5 (3 labels + subtitle + closing line)
  [ ok ] alignment   6 centred texts on the axis or a shared column; 7 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

Both previous WARNs cleared. `grounded` was flagging "A nail goes in. You know
which one it was." and "The holes stop being incidents..."; `captions` was 7
italic lines against a cap of 5. It now sits exactly at the cap, so any line
added here costs a line somewhere else.

**What the render showed** (`runs/ch04/pdf/plate.png`). Nails, then holes, then
more holes, reading straight down with one short sentence per row. Covering every
word but the title leaves a post with nails in it, the same post with the nails
gone and the marks still there, and the same post later with twice as many marks.
That is the mechanism without a caption. The earlier reading still holds: the
three rows are one post over time, not three posts, because row two's holes sit
at row one's nail positions exactly.

**For the author to rule on.**

1. **"Hot or cold, both drive a nail." is off the plate.** It was the Reader
   Panel's Round 2 fix against a reader assuming only shouting counts, and the
   chapter still carries the point in full. Restoring it means either a fourth
   caption (over the cap) or replacing "Every outburst drives a nail." in row
   one, which breaks the endorsed sentence sequence. My call was the sequence;
   this is the one thing in this round I would most want a second opinion on.
2. **The Round 1 question about "Just a settled sense of you." is now moot.**
   That caption is cut.

## Round 6, the standalone-read fix (2026-09-21 05:10)

**Brief.** `runs/design/2026-09-21-plate-standalone-read.md`, Ch04 PASS with the
round's most expensive word-level loss. The Panel's finding: the title, the row
label and the deck all said *outburst*, so cold this is a plate about men who
shout, and the silently withdrawing husband, who is the subject of Ch05 and Ch11,
is let off the hook inside ten seconds. Round 5's open question in these notes
("Hot or cold, both drive a nail." is off the plate) is what the Panel
independently found, so it is closed here.

**What changed, one line of copy.** The closing deck is now:

> *Sometimes it's cold, and cold is often worse. Both make holes.*

replacing **Stop making holes.**, which the Panel asked to cut on its own merits:
it is the one hectoring line in the set, and the three row captions plus the
subtitle have already delivered the argument by the time the eye reaches it. So
the guard came back at no cost to the caption cap, which was exactly at five and
still is.

**Why not the Panel's wording.** It suggested *"Anger isn't strength. Hot or cold,
both drive a nail."* I checked it before writing it, as instructed, and it is not
grounded: the chapter never says "hot or cold" and never says "both drive a nail".
What it says, verbatim, is: *"Sometimes it's hot: a raised voice... Sometimes it's
cold, and cold is often worse. Three days of silence... Both are anger. Both make
holes."* The line on the plate is two of those sentences joined, unaltered, and
"Both make holes" has the further merit of naming the object that is drawn. The
first half of the Panel's version is also already the subtitle. **If he prefers the
Panel's exact wording it needs an Author addition on file in `plate-brief.md`;** it
is one line and nothing in the drawing moves.

**One typographic tidy.** The subtitle's apostrophe was straight while every other
apostrophe in the set is curly; it is now *Anger isn't strength.* with the curly
form. Same words.

**plate_check.py, verbatim**

```
$ python3 scripts/plate_check.py runs/ch04/plate.svg --chapter 4
runs/ch04/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x396
  [ ok ] title       title 'THE HOLE MAKER' / aria-label 'The Hole Maker' vs Mechanism 'The Hole Maker'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    5 italic lines against a cap of 5 (3 labels + subtitle + closing line)
  [ ok ] alignment   6 centred texts on the axis or a shared column; 7 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

No FAIL rows, no WARNs. `captions` sits exactly at the cap, as it did before, so
anything added here still costs a line somewhere else.

**What the render showed** (`runs/ch04/pdf/plate.png`, 2x). The deck is 502px wide
measured against the widest serif fallback, inside 552px of live width, and it sits
on one line under the rule with room either side. The read is unchanged above the
rule; below it, the last thing a cold reader takes is that the cold version counts
too, which is the whole purpose of the restoration.

**Not done.** The Panel also wanted row three's caption changed to "The holes
remain. And they keep coming." to match its ten dots against rows one and two's
five. That is a second copy change and it was not in this round's brief; it is
cheap, grounded-adjacent, and worth doing next time someone opens this file.
