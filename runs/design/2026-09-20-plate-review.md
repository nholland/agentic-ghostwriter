# Plate review, the whole set as it stands

**Desk:** the Designer · **Date:** 2026-09-20 16:23 · **Branch:** `claude/gateway-45bnh4` at `14cf389`
**Coverage:** the 10 plates in `books/the-stoic-husband/design/plates/` and the 2 Part
closing plates in `books/the-stoic-husband/parts/`. Twelve files, all read, all
checked, all rendered and looked at. Nothing was modified.

**Headline:** four keep, seven redraw, one reassign, none retire. Two of the seven
redraws are structural (a diagram that argues the opposite of its own caption; a
label sitting half off the artboard). Five are text or margin fixes of a few lines
each. Separately, **the checker the house uses on plates has a rule backwards**, and
that is what let the two structural defects through.

---

## 1. Counted evidence first

### `runs/design/svgcheck.py`, run on all twelve, verbatim

```
books/the-stoic-husband/design/plates/four-ds.svg
  MARGIN  y=278.0 'Argue the intensity, not the messa' 196..683
  MARGIN  y=342.0 'Move the responsibility somewhere ' 196..708

books/the-stoic-husband/design/plates/four-horsemen.svg
  clean

books/the-stoic-husband/design/plates/incomplete-husband.svg
  clean

books/the-stoic-husband/design/plates/river-oak-sun.svg
  MARGIN  y=250.0 'Self-command that moves.' 30..210
  MARGIN  y=270.0 'The river doesn't fight every' 11..229
  MARGIN  y=290.0 'stone in its path. It accepts' 11..229
  MARGIN  y=310.0 'the landscape and keeps' 34..206
  MARGIN  y=330.0 'flowing in the same direction.' 7..233
  MARGIN  y=250.0 'A house can be structurally' 439..641
  MARGIN  y=270.0 'sound and still feel cold.' 442..638
  MARGIN  y=290.0 'Warmth isn't weakness.' 457..623
  MARGIN  y=310.0 'It's what gives strength' 450..630
  COLLIDE y=270.0 'The river doesn't fight ev' [11..229] x 'It's revealed when weight ' [225..435]  overlap 4px
  COLLIDE y=290.0 'stone in its path. It acce' [11..229] x 'placed on it. To possess t' [225..435]  overlap 4px
  COLLIDE y=270.0 'It's revealed when weight ' [225..435] x 'sound and still feel cold.' [442..638]  overlap -7px

books/the-stoic-husband/design/plates/small-rocks-big-rocks.svg
  MARGIN  y=354.0 'Countable. Citable in an argument.' 36..280
  MARGIN  y=354.0 'Too many and too small to count.' 368..598

books/the-stoic-husband/design/plates/the-muscle-you-stopped-using.svg
  clean

books/the-stoic-husband/design/plates/the-operating-system.svg
  MARGIN  y=170.0 'AUTOMATIC RESPONSE' 468..634
  MARGIN  y=226.0 'the inherited pattern' 479..623

books/the-stoic-husband/design/plates/three-second-window.svg
  clean

books/the-stoic-husband/design/plates/tipping-scale.svg
  clean

books/the-stoic-husband/design/plates/virtue-question.svg
  clean

books/the-stoic-husband/parts/plate-1-steady-river.svg
  clean

books/the-stoic-husband/parts/plate-2-sturdy-oak.svg
  clean
```

**Read that output with two corrections in hand**, both established below:

- The `river-oak-sun` MARGIN and COLLIDE rows are **false alarms**. The checker
  measures against a single page margin and one shared baseline band; that plate is
  three centred columns, and the render shows clean gutters. Its widest line reaches
  x=7 on a 660 canvas, which is tight but is a three-column artboard, not an overflow.
- `the-muscle-you-stopped-using` and `three-second-window` report **clean and are not**.
  Both have a label that renders outside the artboard. The checker cannot see it
  because of the precedence bug in section 2.

### Render check

Every plate was rasterised and looked at. **The render helper named in the task
truncates.** `scripts/chapter_pdf_local.svg_to_png` passes `--window-size=W,H` to
headless Chrome, and Chrome gives back a viewport roughly 80 percent of the
requested height, so everything below about `0.80 × canvas height` is silently
dropped from the PNG while the PNG's pixel dimensions still look correct.

Counted: on a 420-unit canvas, a baseline at y=330 rendered, y=354 did not. Decoded
the PNG and counted dark pixels per band: `(320,340) → 6734`, `(344,366) → 0`,
`(366,384) → 0`. Reproduced in a four-line minimal file.

That cost real evidence. On the first pass, `small-rocks-big-rocks` appeared to have
no captions, `four-horsemen` no attribution line, `tipping-scale` no closing caption,
and `river-oak-sun` no closing formula. All four are present in the markup and all
four render fine once the window is padded. **Every render finding in the table below
is from a padded re-render** (`window-size = W × 1.35H + 80`), not from the helper.

This is a defect in the review tool, not in the plates, and not in the PDF path:
`scripts/compile.py --plates` embeds each SVG as `<img src="...svg">` and the PDF
renderer lays it out natively, so the truncation does not reach a reader copy. It
reaches **the desk that is checking the plate**, which is worse in a different way.

---

## 2. The finding that matters most: the checker's precedence rule is inverted

Three plates set `text-anchor` as an attribute on a `<text>` whose CSS class already
sets `text-anchor`:

```
the-muscle-you-stopped-using.svg:51  <text class="cap" x="44" y="340" text-anchor="start" ...>
three-second-window.svg:27           <text class="cap" x="70" y="256" text-anchor="start">
three-second-window.svg:28           <text class="cap" x="590" y="256" text-anchor="end">
```

`.cap` is declared `{...;text-anchor:middle}` in all three files. In SVG a
presentation attribute carries the specificity of no selector at all, so **a class
rule beats it**. The attribute is ignored and the label centres on its x.

`svgcheck.py` does the opposite. Lines 34-35 read the attribute and let it override
the class, so the checker models an alignment the browser never uses:

```python
ia=re.search(r'text-anchor="(\w+)"',attrs)
if ia: anch=ia.group(1)
```

Measured with the checker's own `ttfwidth` against the widest plausible serif fallback:

| Label | Intended | Actual | Result |
|---|---|---|---|
| `no deadline, nobody watching` (Ch12 plate) | starts at x=44 | centred on 44, spans **-44.2 .. 132.2** | 44px hangs off the **left edge of the artboard**; render shows `eadline, nobody watching` |
| `she says something` | starts at x=70 | centred on 70, spans **5.2 .. 134.8** | 39px inside the 44px margin, 5px from the artboard edge |
| `the words are already out` | ends at x=590 | centred on 590, spans **500 .. 680** | 20px hangs off the **right edge** of a 660 canvas |

The first of those is on `the-muscle-you-stopped-using.svg` — the only plate this
house produced, already landed to the book tree, and reported `clean`. A quarter of
a caption is printed off the page and two gates said it was fine.

**The fix is one character per line** (delete the attribute, add `style="text-anchor:start"`
or give the label its own class), plus a one-line correction in `svgcheck.py` so the
class wins. I have written neither; the checker is production tooling and the plates
are in `books/`.

---

## 3. The twelve plates

Canvas, palette, type and stroke figures in the "deviations" column are measured
against the set's own centre of gravity, described in section 4.

| File | What it draws | Whose mechanism | svgcheck | Render | Style deviations | Recommendation |
|---|---|---|---|---|---|---|
| `design/plates/four-ds.svg` | Four named defensive moves in a ruled list, each with a one-line definition | **near miss: drawn for ch03's framing but not its mechanism.** Concept `chapter_slugs: [the-discipline-of-not-reacting, how-to-fight-without-becoming-small]` = Ch3 and Ch5. Ch3's Mechanism is *The Closed Door*; this draws the four moves, not the door closing | 2 MARGIN, both real | Clean, legible at phone width. ~22% of the canvas below the last row is empty | Canvas 640x430, on-set. No diagram at all: it is a typeset list, so no stroke weight to compare. Right text column runs to x=683 and x=708 on a 640 canvas | **redraw** — two lines overflow the artboard by 43 and 68 units, and if it stays a list it is a sidebar, not a plate |
| `design/plates/four-horsemen.svg` | The four behaviour names stacked, a subtitle, a closing line and an attribution | **near miss: drawn for ch09's framing but not its mechanism.** Ch9's Mechanism is *The Bottomless Yes*; this draws Gottman's taxonomy, which the chapter cites in one paragraph | clean | Clean. All four names, `Contempt is the one that matters most.` and `After John Gottman` all present once padded | Canvas 640x430, on-set. Names set at 19px via inline `style`, the only inline size override in the set besides the Ch12 plate | **redraw** — see the claim-scope flag in section 5; and four centred words is a contents page, not a mechanism made visible |
| `design/plates/incomplete-husband.svg` | A River/Oak/Sun triangle with six failure modes, each outside its own edge with a `X without Y` gloss | **framework/explainer, no chapter** — concept maps to `the-man-without-a-blueprint`, which is the **Introduction**, not a numbered chapter | clean | Clean and genuinely good. Six modes, one rule, empty interior, matched heights. Readable at phone width | Canvas 700x540, the largest in the set. Own class names (`el`/`fm`/`fs`) and stroke 2.2/1.15/0.9 | **keep** — it is the strongest plate in the book and the only one where the diagram carries an argument the prose alone did not |
| `design/plates/river-oak-sun.svg` | Three marks in three columns, each with a short gloss and a four-line definition, over the closing formula | **framework/explainer, no chapter** — same concept, the **Introduction** | 9 MARGIN + 3 COLLIDE, **all false** (three-column layout, see above) | Clean. Columns well separated, formula present and legible | Canvas 660x470. **Five straight apostrophes** (`doesn't`, `isn't`, `It's`) where `four-ds` uses curly. Only typographic inconsistency in the set | **keep** — one find-and-replace on the apostrophes, nothing else |
| `design/plates/small-rocks-big-rocks.svg` | Three outlined circles against ninety small filled dots, each side captioned | **ch07, The Private Tally.** Concept `chapter_slugs: [the-end-of-scorekeeping]` = Ch7. The subtitle *The ledger can only count what it can see* is Ch7's conversation sentence in miniature | 2 MARGIN, cosmetic (caption starts 8 units inside the left margin) | Clean once padded. The volume argument lands: countable few against uncountable many | Canvas 640x420, on-set. Stroke 1.6 | **reassign** — this is Ch7's chapter plate and nothing on disk says so. Give it the name and the outline pointer, then it is a keep |
| `design/plates/the-muscle-you-stopped-using.svg` | Three full bars (walking, running, reading) over one mostly-dashed bar (romance), with what is left of it filled | **ch12, The Thing With No Deadline.** Byte-identical to `runs/ch12/plate.svg`. The sub-label `no deadline, nobody watching` names the mechanism | **clean, and wrong** | **Defect.** `no deadline, nobody watching` spans -44.2 to 132.2 and prints a quarter off the left edge of the artboard | Canvas 640x460. **The only plate with `style="color:#1a1a1a"` and a white background rect** — the other nine leave `currentColor` unresolved. Ironically this is the more correct behaviour | **redraw** — one-line anchor fix, then it is the best chapter plate in the set |
| `design/plates/the-operating-system.svg` | A timeline: trigger and loaded meaning as one solid span, a dashed gap, then the automatic response | **ch01, The Gap** (shares Ch1 with `three-second-window` — see section 5). Concept maps to Ch1, Ch3 and Ch4 | 2 MARGIN, both real | Clean. The dashed span reads as the gap immediately | Canvas 660x360, the shortest in the set. `AUTOMATIC RESPONSE` ends 25.7 units from the artboard edge against a 44-unit margin | **redraw** — one em-dash, one unglossed Greek term, one margin overflow (section 5) |
| `design/plates/three-second-window.svg` | A three-second bar with the first sixth filled solid and labelled *the window*, the rest open and labelled *already firing* | **ch01, The Gap.** Identical to `runs/ch01/plate.svg` | **clean, and wrong** | Legible, and the proportion argues the point. Both end captions sit outside the margin, one 20 units off the artboard | Canvas 660x380. Uses a `fill="currentColor"` rect, the only filled block outside the Ch12 plate | **redraw** — two anchor fixes. The drawing itself is right |
| `design/plates/tipping-scale.svg` | A beam on a fulcrum: many small weights on the low left pan, one weight on the high right pan | **ch08, The Tipping Scale.** Exact name match to the distillation | clean | **Defect.** The beam tips **away from** the pan labelled `the one that finally tipped it`. A reader sees a single weight failing to tip anything, which is the opposite of the caption *The tip feels sudden. It never is.* | Canvas 640x420, stroke 1.8 | **redraw** — the geometry contradicts the mechanism. Also `Relitigating` (section 5) |
| `design/plates/virtue-question.svg` | Four practical virtue labels, each with a two-line instruction, ruled apart | **framework/explainer, no chapter** — concept `chapter_slugs: [introduction, the-three-second-window, all]`, so it is book-wide furniture | clean | Clean and legible | Canvas 640x430, on-set. Like `four-ds`, a typeset list rather than a diagram | **redraw** — one em-dash at line 18 (section 5). Structurally fine as an explainer |
| `parts/plate-1-steady-river.svg` | Canyon strata in section, cut by one thin irregular channel with water at the base | **Part I closing plate.** Not a chapter mechanism, by design | clean (no classed text to measure) | Clean, striking, works at phone width. Caption is Part I's last sentence verbatim, confirmed against `parts/part-1-steady-river.md` | 600x900, `#111111` on `#ffffff`, stroke 1.1/1.4/1.6, Georgia via `font-family` attributes. A **second visual language** by design, ratified in `parts/README.md` | **keep** |
| `parts/plate-2-sturdy-oak.svg` | Tree rings with two tight bands and one scar the later rings closed over | **Part II closing plate** | clean | Clean. Caption verbatim from `parts/part-2-sturdy-oak.md`. **Risk:** ~30 concentric strokes at 1.05 on a 600 canvas will alias on a phone screenshot; it is fine in print | 600x900, `#111111`, stroke 1.05/1.35. 78KB, 40x the next largest file | **keep** — but see the moiré note in section 5 |

**Counts: keep 4 · redraw 7 · reassign 1 · retire 0.**

Of the seven redraws, **two are structural** (`tipping-scale`, and `four-ds`/`four-horsemen`
if you want them to be plates rather than lists) and **five are edits of one to three
lines** (`the-muscle-you-stopped-using`, `three-second-window`, `the-operating-system`,
`virtue-question`, and the margin lines in `four-ds`).

### Chapter mapping, all twelve chapters

Derived from each concept's `chapter_slugs` and each chapter's `**Mechanism:**` line,
not from the plate filenames.

| Ch | Mechanism | Plate on disk |
|---|---|---|
| 01 | The Gap | **two candidates**: `three-second-window.svg`, `the-operating-system.svg` |
| 02 | The Mood Mirror | none landed |
| 03 | The Closed Door | none (`four-ds.svg` is Ch3's framing, not its mechanism) |
| 04 | The Hole Maker | none landed |
| 05 | The Remaining Nails | none |
| 06 | The Tally You Don't Read Aloud | none |
| 07 | The Private Tally | `small-rocks-big-rocks.svg` (unlabelled as such) |
| 08 | The Tipping Scale | `tipping-scale.svg` |
| 09 | The Bottomless Yes | none (`four-horsemen.svg` is a Ch9 citation, not its mechanism) |
| 10 | The Undecided Line | none |
| 11 | The Conversation She's Never Heard | none |
| 12 | The Thing With No Deadline | `the-muscle-you-stopped-using.svg` |
| Intro | (no `distillation.md` exists) | `incomplete-husband.svg`, `river-oak-sun.svg` |
| Book-wide | — | `virtue-question.svg` |

**Three of twelve chapters have a plate that draws their mechanism.** One has two.
Eight have none. Two plates belong to the Introduction, which has no distillation
file at all and therefore no stated mechanism for a plate to be measured against.

---

## 4. Proposed style spec, for ratification

Derived from what the twelve files actually do. Offered for the author to ratify or
amend; not written into `books/`, per Rule 8 and per the standing note in inbox #015
that a style file is a constitution artifact.

### 4.1 Two languages, on purpose

The book has **two** visual languages and that is correct, not a defect. Inbox #015
ratified `design/plates/` as the standard for plates; `parts/README.md` independently
sets the Part closing plates as black line on white at 6x9. The rule that resolves
them: **a chapter or framework plate is a diagram in Language A; a Part closing plate
is a full-page image in Language B.** Nothing else uses either.

### 4.2 Language A — chapter and framework plates

**Canvas.** Landscape, roughly 3:2, no background rect unless the plate needs one.
In use: 640x430 (×4), 640x420 (×2), 660x380, 660x470, 660x360, 700x540.
*Proposed rule: **640x430 is the default.** Depart only for a reason you can name
(the triangle needs 700x540; the timeline needs 660x360). Trim the canvas to the
content — `four-ds` and `virtue-question` carry ~22% empty canvas at the foot.*

**Ink.** One colour: `#1a1a1a`, set once as `style="color:#1a1a1a"` on the root, with
every shape drawn in `currentColor`. Tone is carried by `opacity`, never by hue:
`1.0` structure · `.86` body · `.82` filled bars · `.74` subtitle · `.66` caption
· `.62` scatter · `.55` attribution · `.28` rules · `.26` column dividers.
*Proposed rule: **greyscale only, and the root must declare its colour.** Nine of ten
plates leave `currentColor` unresolved, which works only because a viewer's default
`color` happens to be black. `the-muscle-you-stopped-using.svg` is the one that gets
this right and should be the template.*

**Background.** `<rect width="W" height="H" fill="#ffffff"/>` as the first element.
Only the Ch12 plate has one. *Proposed rule: always, so a plate photographed off a
dark-mode screen is still a plate.*

**Type.** `Georgia, serif` throughout, no exceptions, no second family.

| Class | Declaration | Use |
|---|---|---|
| `.ttl` | `600 17px`, `letter-spacing:.20em`, centred | Plate title, caps, one line |
| `.sub` | `italic 13.5px`, centred, `opacity:.74` | The conversation sentence, one or two lines |
| `.el` | `600 15px`, `letter-spacing:.18em`, centred | Element name in a diagram |
| `.lbl` | `600 14px`, `letter-spacing:.16em` | Row label in a list |
| `.txt` | `14px`, `opacity:.86` | Body line in a list |
| `.bd` | `12.5px`, centred, `opacity:.88` | Body line in a column |
| `.cap` | `italic 12px`, centred, `opacity:.66` | Caption or a label attached to a shape |
| `.src` | `11.5px`, centred, `opacity:.55` | Attribution, last line on the plate |
| `.frm` | `600 13px`, `letter-spacing:.10em`, centred | The closing formula only |
| `.rule` | `stroke:currentColor`, `.8`, `opacity:.28` | Horizontal separators |

*Proposed rule: **a class either sets `text-anchor` or it does not, and no `<text>`
overrides its class with an attribute.** A label that needs a different alignment
gets its own class. This is the whole of the bug in section 2, written as a rule.*
Both class sets are already in the files; the ten above are their union. Plates carry
classes they never use — worth pruning at the next redraw.

**Stroke weights.** `2.2` marks · `1.8` heavy diagram · `1.5` connector lines ·
`1.6` outlines · `1.15` triangle edges · `1.2`/`1.4` light diagram · `.9` ticks ·
`.8` rules. *Proposed rule: **at most three weights on one plate**, and the heaviest
is the thing the plate is about.*

**Margins.** 44 units on all four sides at 640 wide, which is what `svgcheck.py`
assumes. Four plates currently break it. *Proposed rule: 44 is the bound and the
checker is authoritative once its precedence bug is fixed.*

**Composition.** Title, then subtitle, then one horizontal band of drawing, then
labels, then at most two caption lines, then attribution if any. Every plate in the
set follows it.

**Accessibility.** `role="img"` plus `aria-label` on the root, matching the title in
title case. **This is load-bearing:** `scripts/land.py` derives the landed filename
from `aria-label`. All ten design plates have it; **neither Part plate does.**

### 4.3 Language B — Part closing plates

Fixed by `parts/README.md` and confirmed by both files: 600x900 (6x9 trim), `#111111`
on `#ffffff`, one to three stroke weights between 1.05 and 1.6, no fill, no colour,
no shading. One abstract image of time laid down in layers, with one irregularity.
Image occupies roughly y=190 to y=700; caption at y=730 and y=756 in `italic 17px`
Georgia, centred, `#111111`, **verbatim the Part opening page's last sentence.** Both
current captions check out verbatim. `font-family` is set per element rather than by
class, which is why `svgcheck` has nothing to measure on them.

*Proposed additions, since the set is meant to reach five:* add `role="img"` and an
`aria-label` to match Language A; hold the ring/stratum count low enough that the
image survives a phone screenshot (Part II is at the edge); and keep the caption
block at exactly two lines so the five sit at the same height on a flip-through.

### 4.4 Rules that are about words, not pictures

`01-voice.md` applies to every character printed on a plate.

- **No em-dashes** (`01-voice.md` line 56). Two plates carry one.
- **Every Stoic or Greek term gets a plain-English gloss on the same plate**
  (lines 35 and 176, which name `phantasia` and `prohairesis` explicitly).
- **Sixth-grade vocabulary** (line 183). `Relitigating` is not.
- **No invented number.** The only numbers in the set are `half a second` /
  `two and a half seconds` on `three-second-window`, which are Ch1's own prose, and
  `Discourses 2.18`, a locator. Clean.
- **No quotation unless its citation is at least `verifiable` with a non-search
  `evidence_source`.** No plate carries a quotation. Two carry paraphrase with
  attribution; `gottman-four-horsemen.md` is `status: verifiable`,
  `evidence_source: page-text`, so that clears the bar.

---

## 5. Prose and accuracy flags on plates

1. **Em-dash, `the-operating-system.svg` line 29:** `an impression — phantasia`.
2. **Em-dash, `virtue-question.svg` line 18:** `Act from genuine care for her and for
   the marriage — not from ego`. Both are plain violations of `01-voice.md` line 56,
   and neither is inside a quotation, so the translator exception does not reach them.
3. **Unglossed Greek, `the-operating-system.svg` line 33:** `prohairesis` sits alone
   under `THE GAP` with no gloss anywhere on the plate. `phantasia` at least has
   `an impression` beside it. The voice spec names both terms by name as the failure
   case. Its own example gloss is available to borrow: *the part of you that chooses
   before you react.*
4. **Vocabulary, `tipping-scale.svg` line 52:** `Relitigating the last one misses
   where the weight came from.` Plainly: *arguing the last one again.*
5. **Claim scope, `four-horsemen.svg` line 19:** the plate says `Contempt is the one
   that matters most.` Ch9's refined prose says `Contempt is the one that matters
   most **here**.` Dropping one word turns a claim scoped to the chapter's argument
   into a universal finding about divorce research, printed under Gottman's name on
   something designed to be photographed. Restore `here`, or rewrite so the scope is
   in the sentence.
6. **Geometry against caption, `tipping-scale.svg`:** the beam tips toward the many
   small weights and away from the single weight labelled `the one that finally
   tipped it`. Whatever the intent, a reader reads a scale as tipping toward the
   weight that tipped it. The plate currently argues that the last straw did nothing.
7. **Moiré risk, `parts/plate-2-sturdy-oak.svg`:** ~30 concentric strokes at 1.05
   over a 600-unit width. Safe in print, likely to shimmer on a phone. The same
   lesson the marks README already records for the river glyph below 28px.

---

## 6. Needs the author's ruling

**R1. Chapter 1 has two plates and the rule says one.** `three-second-window.svg` and
`the-operating-system.svg` both draw *The Gap*, in the same vocabulary, and
`runs/ch01/plate.svg` is now a byte-identical copy of `three-second-window.svg`, which
means the compiler will emit that one as Ch1's plate. Inbox #019 asked this question
and its resolution answered only the Ch12 half; #015 flagged it earlier and it has
never been ruled. I did not decide it cold because the two are not redundant: the
window plate is the reader's experience, the operating-system plate is the mechanism
underneath it, and which is *the* Ch1 plate depends on what the chapter is for.
**Three ways out, and I recommend the third:** pick one and retire the other; fold
them into one plate (the #019 recommendation, still unapplied); or reclassify
`the-operating-system.svg` as a framework explainer belonging to the Stoic-practice
apparatus rather than to a chapter, which is what its concept's three-chapter
`chapter_slugs` already implies.

**R2. Are `four-ds`, `four-horsemen` and `virtue-question` plates or sidebars?** All
three are typeset lists with a rule between rows. They are clean and useful and they
draw nothing. If a plate is a diagram, these are sidebars and should be typeset in
the chapter rather than given a page. If the house wants them as plates, each needs
a drawing. I cannot decide this without knowing whether a plate is meant to earn a
full page in the reader PDF.

**R3. `incomplete-husband` and `river-oak-sun` belong to the Introduction, which has
no `distillation.md`.** Everything else in the set is measured against a stated
mechanism; these two cannot be. Does the Introduction get a distillation, or are
these two formally framework plates that happen to live in the Introduction?

**R4. Ch6 and Ch7 have near-identical mechanisms.** *The Tally You Don't Read Aloud*
and *The Private Tally*. `small-rocks-big-rocks` draws the ledger that can only count
what it can see, which fits both. Before I draw a Ch6 plate I need to know what
distinguishes the two, or this is a finding about the distillations rather than a
drawing problem.

**R5. Nothing records which plate belongs to which chapter, and the compiler can only
see plates under `runs/`.** `scripts/compile.py:82` returns a chapter plate **only** if
`runs/chNN/plate.svg` exists; the `design/plates/` glob is a byte-comparison used to
decide whether it is landed, never a lookup. So `small-rocks-big-rocks.svg` cannot
reach a reader PDF no matter what, because nothing connects it to Ch7. Either the
outline gains a `*Reader-facing chapter plate: ...*` line per chapter, the way it
already carries one per Part, or the manifest gains a plate key per chapter. This is
a Publisher/production call, not mine, but it blocks the reader PDF the review was
commissioned for.

**R6. Ratify or amend section 4**, and say where it should live. I did not write it
into `books/`; inbox #015 left a style file outstanding and it is still outstanding.

---

## 7. What the READMEs do not record

`design/plates/README.md` is careful and mostly accurate. Eight things are new or
have gone stale.

1. **The README says "Nine draft plates." There are ten.**
   `the-muscle-you-stopped-using.svg` landed on 2026-09-18 and was never added to the
   source table, so the book's only house-produced plate is the one the plate index
   does not list.
2. **The Gottman note is out of date.** It says the concept is `unverified` and that
   Ch9's notes and the concept disagree. Inbox #005 resolved that on 2026-09-18: the
   concept is now `status: verifiable`, `evidence_source: page-text`. The README's
   conclusion (no numbers on the plate) still stands; its stated reason no longer does.
3. **The text-anchor precedence trap is not recorded anywhere**, and it is exactly the
   class of defect the README's own closing line is about. It is worse than the two it
   records, because rendering alone did not catch it: the checker said `clean` and the
   clipped render was itself clipped by the render helper.
4. **The render helper truncates the bottom ~20%.** The README says "render every
   plate before committing it." True, and insufficient: the helper the house hands the
   Designer drops the foot of the canvas without erroring, which on this set hides
   four plates' captions, one attribution line and one closing formula.
5. **Only `the-muscle-you-stopped-using.svg` declares a colour or paints a
   background.** The other nine rely on an inherited `color` that nothing in the file
   guarantees. The marks README explains `currentColor` as a feature for inheriting a
   dark or light context; on a plate with no declared context it is an unstated
   dependency instead.
6. **`river-oak-sun.svg` uses straight apostrophes** where the rest of the set uses
   curly. Five occurrences, one file.
7. **Neither Part plate carries `role="img"` or `aria-label`**, and `land.py` derives
   a landed plate's filename from `aria-label`. Part plates do not go through
   `land.py` today, so nothing is broken; it is a trap for whoever wires Parts III to V.
8. **Four-horsemen order.** The plate lists criticism, contempt, defensiveness,
   stonewalling (matching the concept and the canonical order). Ch9's prose lists
   criticism, defensiveness, contempt, stonewalling. Not an error in either, but a
   reader with both in front of him will notice. Worth one deliberate choice.

**One thing outside my twelve, noted because it changes the picture.** While this
review was running, six further plate files appeared under `runs/`, mtimes 16:21 to
16:22 today: `runs/ch02/plate.svg` (aria-label *The Mood Mirror*), `runs/ch03`
(*The Closed Door*), `runs/ch04` (*The Hole Maker*), `runs/ch09` (*The Bottomless
Yes*), and `runs/parts/plate-3-warm-sun.svg`, `plate-4-fall-to-winter.svg`,
`plate-5-spring-to-summer.svg`. None is byte-identical to anything in
`design/plates/`, so none has landed. They were not in this review's brief and I have
not reviewed them; they appear to be a concurrent desk drawing the missing chapters.
Two consequences worth stating: they will need the same precedence and em-dash checks
before landing, and `runs/ch01/plate.svg` being an exact copy of
`three-second-window.svg` quietly answers R1 by file copy rather than by ruling.
