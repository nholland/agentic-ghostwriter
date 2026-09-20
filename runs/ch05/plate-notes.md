# Chapter 5 plate notes — 2026-09-20

**File:** `runs/ch05/plate.svg` · **Title (aria-label):** The Remaining Nails · **New drawing.**

## What it shows, and why that is the mechanism

The distillation names the mechanism **The Remaining Nails** and the
conversation sentence is "The fight ends before the real thing gets said.
That's not resolution. That's how a man becomes small without deciding to."

The plate is one board with five nail positions. Four nails are driven in and
still there: fights that ended when the noise stopped, before the real thing
was said. One nail lies loose above an empty hole: the fight somebody came
back to. Nothing else is drawn. The reader gets one relationship: an ending is
not a removal, and the only thing that removes a nail is going back.

The board is deliberately long and mostly empty to the right. There is room
for more nails, which is what "deferred conflict, with interest" looks like
without writing a number on it.

## The anchor image, and the prose it comes from

Chapter 5's one image is the nail. Beat heading: "**The trigger with the nail
in it.**" Then, in the same beat, "An apology will end the fight. The nail will
stay in," which is the plate's subtitle verbatim from the chapter. The image
returns at the end of the view-from-above beat: "Most couples never return to
it later. That's where the nails accumulate."

No metaphor_family line exists for this chapter, so the anchor was read from
the prose. The chapter's other images (weather, altitude) are Part I carry-over
and are not drawn, so the plate does not introduce a second picture.

## Stoic term and its gloss (01-voice.md)

One term appears: **PARRHESIA**, glossed on the plate as "frank speech, said
once you are calm". The chapter's "preferred indifferent" is carried in plain
words instead of the term, on the closing line: "You govern the saying. You do
not govern how it lands." That is the distillation's "releasing her response as
a preferred indifferent" without a second piece of Greek on a picture.

## Style decisions, and what they were matched to

- Canvas `0 0 640 430`, matched to `design/plates/four-ds.svg` and
  `virtue-question.svg`.
- White background rect and `style="color:#1a1a1a"` on the root, matched to
  `runs/ch12/plate.svg`, the most recent chapter plate.
- The seven-class style block (`ttl` / `sub` / `lbl` / `txt` / `cap` / `src` /
  `rule`) copied unchanged from the existing plates; no new class, no new size.
- The `lbl` at x=44 with `txt` at x=196 on the same baseline is the row form of
  `four-ds.svg`. The single hairline `rule` above it is the divider used in
  `four-ds.svg` and `ch12`.
- Stroke weight 1.6 for the board and 1.8 for nail shafts, inside the 1.2 to
  1.8 range the existing plates use. Dashes are `3 5` / `3 4` at low opacity,
  the treatment `the-operating-system.svg` and `ch12` use for "not there".
- No arrowheads anywhere in the house set, so none here.

## Checker output, verbatim

```
$ python3 runs/design/svgcheck.py runs/ch05/plate.svg

runs/ch05/plate.svg
  clean
```

## What rendering showed

Two defects the markup hid, both fixed:

1. **The nails read as arrows.** First draft drew each nail as a head bar, a
   shaft and a filled triangular point. Rendered, that is an arrow, and the
   pulled nail (drawn upright above the board) became an arrow pointing *into*
   the board, which is the opposite of the meaning. Fixed by giving each nail a
   flat filled head (18 x 4.5 rect), no point on the driven nails, and by
   laying the removed nail on its side above the hole.
2. **The board read as a segmented bar.** The shafts ran the full depth of the
   board and touched both edges, so the board looked like a five-cell table.
   Shortened the shafts to 21px so they stop inside the board.

After the fix the plate reads as a plank with four nails hammered in, one nail
lying loose, and a dashed hole where it came from.

**Rendering caveat:** `scripts/chapter_pdf_local.py:svg_to_png` clips the
bottom of the canvas (about 19%: on a 420-tall canvas nothing below y≈341 is
captured). That is a renderer defect, not a plate defect; it hides this plate's
PARRHESIA row and closing line, and it hides the bottom caption of every
existing plate including `ch12`. Rendered here through a padded window
(canvas height + 120) to see the whole plate. Reported to the Publisher.

## For the author to rule on

1. **PARRHESIA on the plate.** Ch5's prose italicises *parrhesia* and glosses
   it as "frank speech". The plate keeps the word. If plates should carry no
   Greek at all, the row becomes "FRANK SPEECH / the true thing, said once you
   are calm" and nothing else changes.
2. **"the one you went back to"** is the plate's only claim beyond the drawing.
   It is the chapter's fourth outcome ("someone has the courage to come back")
   in four words. If he wants the chapter's word "courage" in it, the caption
   can read "the one you had the courage to go back to" and still fit.

## Round 2 (2026-09-20 17:45)

Reader Panel review, section 2, Ch05: EDIT, structural. Ranked third worst in
the set, and the one plate the panel said actively misleads, because Ch04's
caption promises "the nail comes out, the hole stays where it was" and this
plate showed a nail out and no hole.

**Applied.** The plate is redrawn.

- **The hole is drawn.** The dashed vertical rule is gone; in its place is a
  filled dark circle in the board's face, **Ch04's hole glyph at Ch04's radius**.
  The two adjacent plates now make one promise with one object.
- **One nail glyph across both chapters.** The driven nails are Ch04's exactly:
  1.6 shaft, 16px head stroke, 10px of nail proud of the board, board 26px deep
  at stroke 1.2 and opacity .55. The old rect-headed nails are gone.
- **The removed nail lies flat and blunt.** Head at the left as a short upright
  stroke, shaft running right, `stroke-linecap="butt"` so the far end is square.
  Nothing on it points, so it can no longer read as being driven in.
- **It sits beside its hole.** The loose nail lies 30px above the board,
  directly over the hole it left, so the nail and the hole read as one event.
- **The board was raised** and the whole drawing recentred, killing the dead
  space that used to sit above it.
- **Relabelled** *the one you went back to* to **the one you went back and
  said**, the panel's wording.
- **The display-size PARRHESIA row is cut** and folded into the one closing
  line, which glosses the term where it stands: *"Parrhesia, frank speech: said
  once you are calm. How it lands is hers."* The gloss requirement in
  `01-voice.md` is met on the plate, and the plate no longer uses a type size
  nothing else in the set uses.

**Not applied.** Nothing the panel asked for was declined. The closing line is
shorter than the round-one draft because the longer version overran the right
margin; the checker caught it and the line was cut to fit rather than shrunk.

**Checker output, verbatim:**

```
$ python3 runs/design/svgcheck.py runs/ch05/plate.svg

runs/ch05/plate.svg
  clean
```

An earlier state of this same plate was not clean, and the output is kept here
because it is what forced the wording:

```
runs/ch05/plate.svg
  MARGIN  y=278.0 'every fight that ended before the ' 42..424
  MARGIN  y=374.0 'Parrhesia, frank speech: said once' 36..604
```

**What the render showed.** Rendered three times. The first render had the nails
standing 30px proud of the board, which made them read as tall posts rather than
as Ch04's nails; they were cut back to Ch04's 10px. The second showed the
drawing sitting high with a heavy blank bottom third; the whole drawing was
moved down 24px. The final render reads, in this order: four nails still in, one
lying out, a hole under it. That is the chapter.

**For the author to rule on.**

1. **The hole is unlabelled.** It relies on the reader having met the same dot
   one chapter earlier, on Ch04's apology row, where the caption names it. That
   is deliberate and it is the panel's own argument for a stable set of
   primitives, but it does mean a reader who opens at Chapter 5 sees an
   unexplained dot. Adding a three-word gloss is one line if you want it.
2. **Parrhesia stays on the plate,** now glossed inside the closing line. Round
   one raised the same question about the display row; the question survives the
   redraw in smaller form.

---

## Round 4, draft from concept B (2026-09-20 22:30)

Concept B, picked by the Reader Panel (`runs/ch05/plate-pick.md`), drawn to
finish. Rounds 1 to 3 drew Ch04's nails; that drawing is superseded, not
revised.

**What the plate shows.** The same man's height, drawn walking into a fight and
walking out of it, twice. A dashed line runs from the top of the walk-in bar
across to the walk-out bar: the size he was when it started. In the top row the
walk-out bar falls short of that line, and the missing piece is drawn as a
dashed empty box labelled *the real thing, never said*. In the bottom row the
same box is solid and outlined, labelled *the real thing, said*, and the bar
reaches the line.

**The carrier.** The height he loses *is* the thing he did not say. One shape,
drawn empty once and filled once; nothing else differs between the two rows.
That is the whole argument, and it is why the plate answers the Panel's flagged
misreading (*the short bar means fighting costs you*): the orienting line under
the subtitle says the fight is the same both times, so the only variable left in
the picture is the saying. The cost is the silence.

**Every phrase and its source.**

| On the plate | Source |
|---|---|
| THE COURAGE TO COME BACK | `refined.md` beat heading, verbatim |
| Are you leaving the fight the same size you were when it started? | `refined.md`, "Becoming small", verbatim |
| Same fight both times. What changes is whether the real thing gets said. | distillation, "The fight ends before the real thing gets said"; the "both times" framing is the Ch10 plate's house move |
| GOES QUIET / nobody comes back to it | distillation Challenge, "once it goes quiet"; `refined.md` 5.5, "comes back to the unresolved conversation" |
| GOES BACK / he says the true thing | `refined.md` 5.5, "He says the true thing." |
| the real thing, never said / the real thing, said | distillation, "the real thing gets said" |
| walks in / walks out | the drawing's own deictics, two words each |
| he becomes small without deciding to | distillation Conversation sentence, "becomes small without deciding to" |
| he leaves the fight the same size | `refined.md`, "leaving the fight the same size" |
| Parrhesia, frank speech: say it, then let it land however it lands. | `refined.md` 5.5, "frank speech" and "he lets it land however it lands" |

No numbers, no quotation, no em-dash, no Stoic term ungossed: *parrhesia* is
glossed inline in the closing line and set at caption size, not display size.
The checker's grounded row passes: every run of three or more words is the
chapter's.

**The title diverges from the distillation's Mechanism line, on purpose, for the
author to rule on.** The Mechanism line is **The Remaining Nails**, which is
Chapter 4's picture in words, and there is no nail anywhere in this concept. A
man who reads the old title over this drawing lands back on the anger chapter.
Rather than invent a title, the plate takes Chapter 5's own beat heading, **the
courage to come back**, verbatim. `plate_check.py` reports this as a title WARN
and that WARN is expected. It is not the Designer's to resolve: either the
distillation's Mechanism line changes to the chapter's own heading, or the
author rules that the plate carries the Ch04 title anyway. Flagged in the
concepts note, carried by the Panel, now standing on the finished plate.

**Style decisions and what they were matched to.** Canvas 640 wide, Georgia with
a serif fallback, `#1a1a1a` via `currentColor` on white, title at y=40 with
.20em letter-spacing, italic subtitle at y=66, hairline rules at .28 opacity,
bars at .82 fill, dashed strokes at 1.2 / `3 5`: all from `runs/ch10/plate.svg`
and the nine plates in `design/plates/`. The two-row structure with a left label
column, an orienting line under the subtitle and a closing line under a rule is
Ch10's layout exactly, because Ch10 is the same argument shape: one object, same
pressure, twice. Height is 460, not 430, which is within the existing range
(`design/plates/` runs 360 to 540). One divergence worth naming: the in-drawing
annotations are set roman, not italic, so that italic stays commentary only and
the caption cap holds at four with two labels. Ch10 sets everything italic and
runs at twelve against a cap of four.

**Still no `design/plates/style.md`.** The written style does not exist; the
proposal from the concepts round stands and still needs the author to ratify it,
not the Designer to write it.

**Checker output, verbatim:**

```
$ python3 scripts/plate_check.py runs/ch05/plate.svg --chapter 5
runs/ch05/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x460
  [WARN] title       title 'THE COURAGE TO COME BACK' / aria-label 'The courage to come back: the same fight twice, once with the real thing left unsaid and once with it said' vs Mechanism 'The Remaining Nails' (differs; inbox #065)
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    4 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   12 centred texts on the axis or a shared column; 11 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

An earlier state of this draft was not clean, and the rows are kept because they
are what set the wording of two lines:

```
  [FAIL] geometry    MARGIN  y= 94.0 'The same fight both times. What ch' 35..605; MARGIN  y=452.0 'Parrhesia, frank speech: say the t' 36..604
```

The orienting line lost its opening article and the closing line lost "the true
thing", which the row-two gloss already says. Both were cut to fit rather than
shrunk.

**What the render showed** (`runs/ch05/pdf/plate.png`). The two rows read as one
comparison at phone size, and the eye goes to the short bar first, then to the
dashed box above it, then to the label. The solid outline on the row-two block
makes a visible seam where the missing piece was restored, which is the intended
reading and the one thing to check with fresh eyes: it must read as *the piece
is here now*, not as two stacked boxes. The long empty span between walk-in and
walk-out was left as drawn; it reads as the length of the fight.

**For the author to rule on.**

1. **The title, above.** The Mechanism line and the plate disagree, and only he
   can settle which moves.
2. **"walks in" and "walks out" are the plate's own words,** not the chapter's,
   at two words each and below the grounded row's three-word floor. They are
   deictic labels for the drawing rather than claims. If he wants nothing on a
   plate the chapter does not say, they come off and the drawing loses its
   clearest cue that these are the same man twice.
