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
