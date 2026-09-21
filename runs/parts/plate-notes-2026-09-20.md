# Part closing plates 3, 4, 5 — Designer's notes

2026-09-20 16:27. Drawn cold against `books/the-stoic-husband/parts/README.md`
("Closing plates"), `plate-1-steady-river.svg`, `plate-2-sturdy-oak.svg` and the
three Part opening pages. Nothing under `books/` was written or altered.

Files: `runs/parts/plate-3-warm-sun.svg`, `runs/parts/plate-4-fall-to-winter.svg`,
`runs/parts/plate-5-spring-to-summer.svg`. The generator that produced them,
kept so the set can be re-tuned rather than re-invented:
`runs/parts/gen-plates-345.py`.

## What I measured off plates 1 and 2 before drawing

| Decision | Value in plate 1 / plate 2 | Value used in 3, 4, 5 |
|---|---|---|
| Canvas | `width=600 height=900 viewBox="0 0 600 900"` | identical |
| Background | `<rect width="600" height="900" fill="#ffffff"/>` first element | identical |
| Ink | `#111111` on every stroke | identical |
| Field weight | 1.1 (plate 1 strata), 1.05 (plate 2 rings) | 1.1 |
| Accent weight | 1.6 canyon walls, 1.4 river, 1.35 every fourth ring | 1.6 (plate 4 band edges), 1.4 (plate 5 surface and water) |
| Fill | explicit on every shape; `fill="none"` on every open path | identical |
| Drawing box | x 90..510; y 190..640 (plate 1 strata), river wiggle to 652 | x 90..510; y 190..640, plate 5's water to 681 |
| Field density | 20 strata rows (plate 1); 30 rings (plate 2) | 20 arcs / 24 layers / 21 layers |
| Hand wobble | plate 2's rings are not true circles; radii drift ~1-3px | same, a smooth 3-term sine wobble, amplitude 1.3-1.6px |
| Caption type | `Georgia, "Times New Roman", serif`, 17px, italic, `text-anchor="middle"`, `x="300.0"`, `fill="#111111"` | identical |
| Caption baseline | 730, and 756 for the second line | 730 (all three captions are one line) |

No colour, no fill on any drawn shape, no shading, no text on any plate but the
caption, no numbers, no quotations, no em-dashes, nothing domestic or human.

## Plate 3 — Part III, The Warm Sun

**The image.** Twenty arcs laid one over the other, each spanning the full width
of the box, each reaching a little higher and a little deeper than the one below
it. Days of light, stacked: not a picture of the sun but what the sun leaves
behind, the way plate 1 draws the river's canyon rather than the river.

**The irregularity and the sentence it carries.** One arc, the eleventh, is
broken on its morning side: a 72px gap between x=210 and x=282. Every arc laid
down after it crosses that same stretch of sky unbroken.

> "It comes back every morning, whether or not anyone thanked it for yesterday."

**Form decisions matched.** Field weight 1.1, the only weight on the plate, the
way plate 1's twenty strata are all 1.1. Twenty layers, matching plate 1's twenty
strata rows. The arcs run flush to x=90 and x=510, as plate 1's strata do. Apex
of the top arc at y=190, edge of the bottom arc at y=634: plate 1's box exactly.

## Plate 4 — Part IV, Fall to Winter

**The image.** Twenty-four layers of a settling year, thinning from 22px of
spacing at the bottom to 6px near the top, long before anything else changes.
Then one band, 61px deep, where nothing was laid down at all. Above it the layers
are back at the spacing they had before.

**The irregularity and the sentence it carries.** The empty band has a top edge,
and eight layers stand on it.

> "Every winter ends."

The slow thinning under the band carries the page's other structural sentence,
"By the time you feel the cold, it's been coming for months," but the band is
the one irregularity, as the README requires.

**Form decisions matched.** The two layers that bound the band are drawn at 1.6,
the weight plate 1 gives its canyon walls; every other layer is 1.1. Field runs
y 640 to 190, x 90 to 510.

## Plate 5 — Part V, Spring to Summer

**The image.** The same layers as plate 4, opening instead of closing: tight
bands at the bottom giving way to wider and wider ones as the days stretch.
Below them, one straight hard line at y=652 is the surface.

**The irregularity and the sentence it carries.** Under that straight surface
line, at y=676, the water is already moving in a small wave, while the layers
directly above it are still at their tightest.

> "The thaw starts under the ice, weeks before anything shows on the surface."

**Form decisions matched.** The wave is drawn at 1.4, the exact weight and the
same 48px period as plate 1's river, so the river reads as the river across the
set. The surface line is 1.4. The field is 1.1 throughout.

## The set logic, stated plainly

- Plates 1, 2 and 3 are the three elements, each with its own geometry: strata,
  rings, arcs.
- Plates 4 and 5 are the two seasons, and they deliberately share one geometry,
  mirrored. Plate 4's layers close and stop; plate 5's open. This is the same
  move the pages make, where "No summer is the last one" answers "No winter is
  the last one."

## Checker output, verbatim

```
$ python3 runs/design/svgcheck.py runs/parts/plate-3-warm-sun.svg runs/parts/plate-4-fall-to-winter.svg runs/parts/plate-5-spring-to-summer.svg

runs/parts/plate-3-warm-sun.svg
  clean

runs/parts/plate-4-fall-to-winter.svg
  clean

runs/parts/plate-5-spring-to-summer.svg
  clean
```

`svgcheck.py` only measures `<text class="...">`; like plates 1 and 2, these
captions are unclassed, so "clean" here means "nothing to measure," not "type
verified." The captions were verified separately against the part pages:

```
plate-3-warm-sun.svg
  caption   : 'What it reaches, opens.'
  page last : 'What it reaches, opens.'
  match=True  em-dash=False  viewBox=0 0 600 900  strokes=['1.1']  fills=['#111111', '#ffffff', 'none']  lines=21
plate-4-fall-to-winter.svg
  caption   : 'No winter is the last one.'
  page last : 'No winter is the last one.'
  match=True  em-dash=False  viewBox=0 0 600 900  strokes=['1.1', '1.6']  fills=['#111111', '#ffffff', 'none']  lines=24
plate-5-spring-to-summer.svg
  caption   : 'Stand in the summer you built.'
  page last : 'Stand in the summer you built.'
  match=True  em-dash=False  viewBox=0 0 600 900  strokes=['1.1', '1.4']  fills=['#111111', '#ffffff', 'none']  lines=23
```

## What the renders showed, and what changed because of them

Every plate was rasterised with `scripts/chapter_pdf_local.py:svg_to_png` and
looked at beside renders of plates 1 and 2. Two rounds of fixes, then stop.

**First attempt, discarded.** Plate 3 was nested arcs sharing one baseline; at
6x9 they crowded into a hive of near-vertical lines along the bottom and read as
a fingerprint. Plates 4 and 5 were three horizontal lanes, one per element: a row
of day arcs for the sun, ring ticks for the oak, a wave for the river, with a
winter column crossing all three. Rendered, that is an infographic, not a plate.
Three lanes of marks with white alleys between them read as three charts stacked
on a page, and nothing in plates 1 or 2 licenses it. Both were redrawn as single
unified fields.

**Round two.** Plate 3's break was at x=152..214, on the steep morning limb,
where the two cut ends sat 25px apart vertically and read as two different lines
failing rather than one line broken; moved to x=210..282, where the arc is
flatter and the break reads as one gap. Plate 4's band was 76px with 1.35 edges
and split the plate into two separate-looking fields; narrowed to 61px and the
bounding layers taken to 1.6, so the band reads as a hiatus inside one field.
Plate 5's field topped out at y=265, well inside plate 1's box; the spacings are
now scaled to land exactly on y=190.

**Side by side at the end.** Line counts 20/24/21 against plate 1's 20 and plate
2's 30. Margins identical on all five. Caption sits in the same place and the
same type on all five. At phone width (600px wide render scaled to ~390) each
irregularity is still visible: the gap in plate 3, the band in plate 4, the wave
under the line in plate 5.

## For the author to rule on

1. **Single-line captions sit at y=730, the first of plate 1's two baselines.**
   All three of these last sentences are short enough for one line, where plates
   1 and 2 both run to two. Starting at the same baseline keeps the caption
   beginning in the same place on every page; optically centring the single line
   against the two-line blocks would mean y=743. One number, three files, your
   call.
2. **Plates 4 and 5 share a geometry on purpose.** They are the season pair and
   they mirror: layers closing to a band, layers opening from the ice. If you
   would rather every plate look unlike every other, 4 is the one to redraw, and
   I would want a different sentence from its page to carry.
3. **The three elements are not all on plates 4 and 5.** The brief allowed them
   and the pages name all three, but the only version that fitted all three on a
   plate was the three-lane chart described above, which failed. Plate 5 carries
   the river explicitly, at plate 1's weight and wavelength; the layers on both
   plates are the days. If you want the oak visible by name on either plate, that
   is a fourth mark and I would rather you decided it than I assumed it.
4. **Plate 5's water runs to y=681,** 29px lower than anything on plates 1 and 2,
   because the surface line has to sit above it. Caption clearance is 49px. If
   `chapter_pdf.py` crops tighter than the viewBox on that page, tell me and I
   will lift the whole field.

## Round 2 (2026-09-20 17:45)

Reader Panel review `runs/design/2026-09-20-plate-reader-review.md`, section 3.
Plates 1 and 2 are untouched and were not opened. Plates 4 and 5 were not
touched either; only `plate-3-warm-sun.svg` was redrawn.

**The finding.** Plate 3 rendered as a dome or a fingerprint rather than as
warmth or reaching; the two small gaps carrying the irregularity were far too
subtle to be felt at page size; and it broke the set's own logic, since plates 1
and 2 show the thing the element made while this showed an ambiguous surface.

**Applied, as the panel suggested: the opening drawn plainly.** The line
vocabulary is unchanged, which is what holds the set together: a field of
stacked layers, black on white, one weight at 1.1, the same drawing box x
90..510 and y 190..640, the same hand wobble, the caption in the same type at
the same baseline. What changed is what the field does. From one point low on
the page the layers part, and every layer laid down above it parts a little
wider, its inner end lifting toward the opening. Below that point the layers are
whole. The parting widens slowly at first and fast near the top, so the two arms
are curved rather than a plain wedge.

**The irregularity and the sentence it carries.** The parting itself, and the
lift at each layer's inner end:

> "Everything alive leans toward the light."

That replaces round one's broken arc, which carried "It comes back every morning,
whether or not anyone thanked it for yesterday." Both sentences are on the Part
III page; this one is the sentence the drawing can actually show.

**Form rules held, checked one by one against `parts/README.md`.** 600x900
viewBox; white rect first; ink `#111111`; one weight throughout, no accent
weight; `fill="none"` on every open path; no colour, no shading; no text but the
caption; the caption is the page's last sentence verbatim, *"What it reaches,
opens."*, at x=300, 17px Georgia italic, baseline 730, the same as plates 1, 2, 4
and 5; nothing domestic, nothing human, no marriage vocabulary, no numbers, no
quotation, no em-dash.

The generator is kept beside the others so the plate can be re-tuned rather than
re-invented: `runs/parts/gen-plate-3-r2.py`. It imports the shared helpers from
`gen-plates-345.py` and writes only plate 3.

**Checker output, verbatim:**

```
$ python3 runs/design/svgcheck.py runs/parts/plate-3-warm-sun.svg

runs/parts/plate-3-warm-sun.svg
  clean
```

As in round one, "clean" means the checker found no classed `<text>` to measure;
the caption was verified by eye against `parts/part-3-warm-sun.md`.

**What the renders showed.** Two rounds. The first version parted along straight
arms and read as two symmetric blocks of lines; the parting was legible but the
whole was static. The parting was reshaped to open slowly low down and fast near
the top, and the lift at the inner ends was made sharper and more local, which
is what makes the lines read as leaning rather than merely stopping. At page
size and at phone width the opening is unmissable, which was the panel's whole
complaint.

**For the author to rule on.**

1. **It can be read as an open book.** A symmetrical field parting down the
   middle with lifted inner edges is close to the shape of a book lying open,
   and this is a book. It is not domestic and not human, so it breaks no rule in
   `parts/README.md`, and every reader I can simulate sees *opening* first. If
   you see the book and it bothers you, the fix is to make the two sides
   unequal, and I would want your word before breaking the symmetry, because the
   symmetry is what makes the opening read.
2. **The irregularity now carries a different sentence** from the Part III page
   than round one's did. Both are on the page; this is a choice about which
   sentence the plate is for.

---

# Part plates 1 and 2 — Designer's notes, round 3

2026-09-21 12:48. Three instructions from the author, quoted in the dispatch:
titles on both plates; the oak's rings made to say growth rather than age; the
river's canyon tied to something positive. Drafts written to
`runs/parts/plate-1-steady-river.svg` and `runs/parts/plate-2-sturdy-oak.svg`.
**Nothing under `books/` was written or altered.** The generators are kept
beside the others so either plate can be re-tuned rather than re-invented:
`runs/parts/gen-plate-1-r2.py`, `runs/parts/gen-plate-2-r2.py`.

## 1. The titles

`THE STEADY RIVER` and `THE STURDY OAK`, matching `parts/part-N-*.md` and
`03-outline.md` lines 38 and 125 word for word. *Adaptive* was not used: the
author ruled for the book's own word after being asked, and a plate that
contradicts the page it closes is a defect the reader can see in one flip.

Set in the chapter plates' display idiom, read off `design/plates/*.svg`, which
all carry the identical rule:

| | Chapter plates | These two |
|---|---|---|
| class | `.ttl{font:600 17px Georgia,serif;letter-spacing:.20em;text-anchor:middle}` | same rule, `21px`, with the `"Times New Roman"` fallback the Part captions already carry |
| case | full caps | full caps |
| position | `x` = canvas centre, `y=40` on a 430-tall canvas | `x=300`, `y=150` on a 900-tall canvas |
| `role`/`aria-label` | `role="img" aria-label="<title>"` | added, same form |

**Why 21px and not 17.** A Part plate is a full trim page and its caption is
17px italic where a chapter plate's is 12px; the Part set has already scaled
type up by about 1.4. Holding the chapter ratio exactly would give 24px, which
rendered louder than the drawing. 21px is a 1.24 ratio to the caption: clearly
the title, clearly subordinate to the image. One number, two files, the
author's call if he wants it nearer the chapter ratio.

**Why `y=150`.** The ink block then runs from the title's cap height (~138) to
the caption's last baseline (756), centred on 447 against a page centre of 450,
and leaves 40px between the title and the top of the drawing box at y=190.

**A markup change worth naming.** Both files now carry a `<style>` block, so
the captions moved from `text-anchor="middle" font-family=... font-size="17"
font-style="italic"` attributes to `class="cap"` with the same values. Nothing
about the render changes; what changes is that `plate_check.py`'s `anchor-attr`
row goes from WARN to ok, and the captions are now counted as italic lines
(2 against a cap of 2). Reject it in one word if you would rather the drafts
differed from the landed files in the drawing only.

## 2. The oak, and the rings

**The finding, restated.** Thirty near-circular rings with a clean outer edge,
isolated on white, is the end of a cut log. It argues age and felling at a
reader who is being told about a man still standing.

**What was kept.** The rings themselves, the pith dot at the centre, two bands
of tight years, one scar the later rings closed over, the ink, both weights
(1.05 field, 1.35 accent), the drawing box, the caption and its position.

**How the rings were made to say strength rather than age.** Three changes, and
all three are about the same thing:

1. **No outer edge.** The rings run off all four sides of the drawing box. The
   outermost ring is at radius 322; the box corner is 307.6 from the pith, so
   nothing closes anywhere in frame. There is no bark line, no silhouette, no
   round of timber: the reader is looking at part of something bigger that is
   still going outward. This is the change that kills the felled-tree read, and
   rendering confirmed it does so immediately.
2. **The rings widen outward.** Radii 14, 23, 33, 43, 54, 66, 78, 82, 86, 91,
   106, 121, 138, 155, 172, 178, 184, 190, 211, 232, 253, 276, 298, 322. Early
   years lay down 9 or 10px; the last years lay down 22 to 24. The field
   accelerates away from the centre, so what the eye reads is *more every year*,
   not *older every year*.
3. **The two hard bands are grown past, and the ring after each one is the
   heaviest line on the plate.** Rings 7 to 9 (radii 78 to 91) and 15 to 17
   (172 to 190) barely widen at all and kink; the ring immediately after each
   band, at 106 and at 211, is drawn at 1.35 where everything else is 1.05.
   That is the same logic plate 4 uses for the two layers bounding its winter
   band. It means: the year after the hard one, it laid down more.

**The scar.** A wound taken in year 11, upper right, pinching that ring toward
the one inside it and closing over across the next four rings until no trace is
left. It is never drawn deeper than 85% of that year's own growth, so no ring
crosses the ring inside it — the first attempt did, and rendered as a tear
through the wood rather than a dent grown over. The scar is the single
irregularity `parts/README.md` asks for, and it carries the caption: *"The
storm comes through, and in the morning the oak is still there."*

**Two smaller decisions.** Every ring carries the same low-order lumps, so they
all belong to one trunk rather than to a target or a ripple; and the section is
5% taller than it is wide, because a trunk's cross-section never is round.

## 3. The river, and the canyon

**What the drawing does now.** The canyon still cuts down through all twenty
layers, but it is a channel with the river running in it rather than an empty
notch with a thread of water floating underneath. From y=405 to the bottom of
the field the cut is full of water, drawn as wave lines on a 15px pitch — a
tighter texture than the 23.7px rock layers, so it reads as a different
substance and not as more strata. The surface line spans wall to wall and
touches both walls. The water runs off the bottom edge of the drawing box: it
goes on.

**Why that is the tie, as far as a drawing can make it.** The landed plate's
strongest shape was a white wedge widening upward between two striped blocks,
and on a page in a marriage book that is a gap opening between two sides. The
canyon now holds something. The two walls are joined at the waterline instead
of standing apart, and the thing that made the cut is visibly still in it. The
canyon reads as a course, not a wound.

**The canyon profile was reshaped to allow it**: half-width 96 at the top
falling to 46 at the floor on a 0.62 exponent, so the shoulders fall away early
and the gorge below is close to sheer. The landed profile closed to a 20px slot
at the bottom, which no legible amount of water fits into.

### The words, and what I could not source

**The caption is unchanged and verbatim**: *"It's patient enough to cut a
canyon out of rock, one ordinary day at a time."*

I searched the book for language that ties the canyon to something the marriage
gained. It is not there. `canyon` appears in exactly one place in the whole
corpus — the Part I page's last sentence, the caption itself. The Introduction's
"River: Calm and Adaptable" section and `okf/frameworks/the-river-the-oak-and-
the-sun.md` give the river's vocabulary as *accepts the landscape*, *keeps
flowing in the same direction*, *governs yourself before the moment*, *steady
enough that his marriage can move through difficulty without being damaged by
his reaction to it* — all of it about adapting and holding, none of it about
what the patience built. `04-archetype.md` adds nothing on the river beyond the
Part titles.

So per the brief I wrote nothing. **The sentence I would want, for the author to
write, reject or replace:**

> The canyon is not the damage. It is what the ordinary days built.

Two notes on it. It carries no marriage vocabulary, so it does not break the
Part pages' hard rule, and *built* is already the book's word in this register
(Part V's "Stand in the summer you built", Ch23's "The Marriage You Build Every
Day"). But it would be a **second caption line under the first**, which is a
second break in "the caption is the opening page's last sentence, verbatim. The
plate reprints the book's own words; it adds none." If he wants it, the natural
home is the Part I page itself — added there, it becomes the page's last
sentence and the caption rule stands unbroken.

## Checker output, verbatim

```
$ python3 scripts/plate_check.py runs/parts/plate-1-steady-river.svg --part 1
runs/parts/plate-1-steady-river.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      600x900
  [ ok ] captions    2 italic lines against a cap of 2 (0 labels + subtitle + closing line)
  [ ok ] alignment   3 centred texts on the axis or a shared column; 0 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 60px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})

$ python3 scripts/plate_check.py runs/parts/plate-2-sturdy-oak.svg --part 2
runs/parts/plate-2-sturdy-oak.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      600x900
  [ ok ] captions    2 italic lines against a cap of 2 (0 labels + subtitle + closing line)
  [ ok ] alignment   3 centred texts on the axis or a shared column; 0 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 60px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```

For comparison, the two landed plates were run first and both return
`[WARN] anchor-attr` on their captions and `0 italic lines` on the captions row;
every other row is identical. That WARN is what the `<style>` block clears.

**Rows that do not apply to a Part plate, and why.** `plate_check.py` was built
around chapter plates, so `--part` skips two rows by design and a third is
vacuous here:

- **title** — only runs under `--chapter`, where it compares the `.ttl` text to
  the chapter's `distillation.md` Mechanism line. Part plates have no
  distillation; the Part page and `03-outline.md` are the authority, and both
  titles were checked against them by hand and match.
- **grounded** — only runs under `--chapter`, where it looks for every
  three-word run in the chapter corpus. Checked by hand instead: both captions
  appear verbatim in their Part page, and both titles appear verbatim in the
  Part page heading and `03-outline.md`.
- **alignment / drawing blocks** — reports `0 drawing blocks` on all four
  files. Plate 1 has no `<g>` at all; plate 2's single `<g>` spans the canvas
  once its unclipped path coordinates are measured, so the checker treats it as
  the white ground. Nothing is being verified by that half of the row on either
  plate. The centred-text half does run, and passes: three texts on x=300.

Additional checks run by hand, since nothing counts them:

```
plate-1-steady-river   title 'THE STEADY RIVER'  caption verbatim in page: True
                       em-dash False  colours ['#111111', '#ffffff']
                       open paths without fill="none": none
                       strokes ['1.1', '1.4', '1.6']   40 lines, 18 polylines
plate-2-sturdy-oak     title 'THE STURDY OAK'    caption verbatim in page: True
                       em-dash False  colours ['#111111', '#ffffff']
                       open paths without fill="none": none
                       strokes ['1.05', '1.35']        24 paths
```

## What the renders showed

Everything was rasterised with `scripts/chapter_pdf_local.py:svg_to_png`, at
full size and at 0.65 scale for phone width, and looked at beside renders of
the two landed plates. Five compositions were drawn and three were thrown away;
none of the defects was visible in the markup.

**Rejected, plate 1, first attempt — the canyon widened to a 100px floor with
the river drawn across it.** Rendered, the white wedge got *bigger*. Widening
the bottom to make room for water made the void the dominant shape on the page,
which is the exact fault being repaired.

**Rejected, plate 1, second attempt — the strata carried on straight through
the rock and went wavy where they crossed the cut.** Sound in principle and it
did unify the field, but because the waves sat at the same twenty baselines as
the rock layers, the eye joined each wave to the straight line either side of
it and read the water as a wobble in the stone. The water has to be on its own
pitch to be water. That is why the final plate puts it on 15px against the
rock's 23.7px.

**Rejected, plate 1, third attempt — a narrow slot full of water top to
bottom.** Unified and rather handsome, but there was no canyon in it at all: a
striped field with a wavy seam down the middle, which the caption then
contradicts.

**Rejected, plate 2, first attempt — rings with the wobble applied at full
amplitude near the pith.** At radius 9 a 4px wobble is 40% of the radius, and
the core rendered as a spiky rosette. The wobble is now absolute and low
frequency, and the first ring starts at radius 14 as the landed plate's does.

**Rejected, plate 2, second attempt — the scar cut 26px deep regardless of the
year's growth.** Where the growth that year was 15px, the scarred ring crossed
inside the ring before it and rendered as a tear across the wood. Capped at 85%
of the year's own growth.

**At phone width.** Plate 1: the title is legible, the gorge and the body of
water in it are unmistakable, and the tighter pitch of the water still reads as
a different substance at 0.65 scale. Plate 2: the title is legible, the
widening outward is the first thing the eye gets, the two hard bands read as
dense rings, and the scar is still visible though it is the first thing to
soften. Nothing in either plate depends on detail that disappears.

## For the author to rule on

1. **The title breaks a rule in `parts/README.md`.** "No marriage vocabulary,
   same as the opening pages" and the caption rule both survive, but *"The
   caption is the opening page's last sentence, verbatim. The plate reprints
   the book's own words; it adds none"* now has a second kind of text above it.
   The README is a book file and only the Publisher edits it on your word; it
   needs a line saying a Part plate carries its Part's title, set in the chapter
   plates' `.ttl` idiom. Until that line exists the set has an undocumented rule.
2. **Plates 3, 4 and 5 have no titles.** The drafts in `runs/parts/` predate
   this instruction. Furniture that stops at Part II reads as an accident, the
   same lesson as parking-lot #27 and the reason this set exists at all. Say the
   word and they get `THE WARM SUN`, `FALL TO WINTER` and `SPRING TO SUMMER` in
   the same idiom, plus the `<style>` block that clears their `anchor-attr`
   WARN. I did not do it unasked because you named two plates.
3. **The river sentence above.** Write it, replace it, or leave the plate
   carrying the tie in the drawing alone. If you write it, my preference is that
   it goes on the Part I page rather than only on the plate, so the caption rule
   stays intact and the page and the plate keep saying the same last thing.
4. **21px titles.** Named above; the chapter-plate ratio would put them at 24.
5. **Plate 2 now needs a clip path.** It is the first plate in the set with
   `<defs>` and a `<g clip-path>`. `chapter_pdf.py` renders it correctly here,
   but if any downstream tool flattens or re-serialises the SVG, that is the one
   feature that could be dropped, and dropping it restores the cut log. Worth
   one look at the compiled PDF before this lands.
