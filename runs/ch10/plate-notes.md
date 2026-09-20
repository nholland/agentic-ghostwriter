# Ch10 plate notes — The Undecided Line

**Date:** 2026-09-20
**File:** `runs/ch10/plate.svg` (aria-label, and so the landed filename: *The Undecided Line*)

## What it shows, and why that is the mechanism

`chapters/ch10/distillation.md` names the mechanism **The Undecided Line** and the
conversation sentence: *"He had rules he'd defend without thinking and had never
said what any of them were for, so they folded the first time somebody pushed."*

The plate is one rule, drawn twice, under the same lean.

- **Top, UNDECIDED.** The rule as a line. An arrow presses down on it and the line
  folds at the middle, because the box underneath it is empty: *this protects
  ________*, captioned *"nobody ever finished the sentence."* Gloss in the left
  gutter, in the chapter's own vocabulary: *a preference, and preferences fold*.
- **Bottom, DECIDED.** The same rule, the same lean, and this time a solid footing
  under the line carrying one finished sentence: *this protects the savings and
  the big calls we make together*. It holds. Gloss: *a boundary, and it holds*.
- **Under the rule**, the second half of the mechanism, which the distillation
  says naming also buys: *"Now the argument is about what you are protecting, not
  about the rule."*

The chapter's three domains (what you do to each other, money, how you run your
family) and its three pressures (anger, company, the night she does not hold it)
are not on the plate. They are the chapter's coverage, not its mechanism. One
named example carries the test; the rest would turn a mechanism into a contents
page.

## The anchor image, and the prose it comes from

The chapter's one image is **the line itself, with or without something
underneath it**: *"A line, decided ahead of time, that holds when somebody leans
on it"*, and *"that's exactly why the rule folds when somebody leans on it hard
enough. There was nothing underneath it."* The drawing is that sentence and its
negative, nothing more. Two other images in the chapter, the friend's picture of
your wife as a cup and Epictetus on a father, are deliberately left off: each
would be a second image on the one page a reader takes in at a glance.

The money example is the chapter's own (*"an amount above which neither of us
spends without talking first"*), and what it protects is the chapter's own answer
(*"the savings, or the house you're working toward, or the two of you making big
calls together"*), compressed to fit one line. The concept
`okf/frameworks/boundary-vs-preference.md` states the same test and the same
example, so nothing on the plate leads the book.

## Reuse check

Nothing in `design/plates/` draws this mechanism. `four-ds.svg` is Ch3 and Ch5 by
its concept's `chapter_slugs`; `four-horsemen.svg` is Ch9's citation.
`the-oaks-boundary.md` and the other boundary frameworks have no plate. New plate.

## Style decisions, and what they were matched to

- Canvas 640x430, the canvas of `four-ds.svg`, `four-horsemen.svg` and
  `tipping-scale.svg`, plus the explicit white ground from `runs/ch12/plate.svg`.
- Class block copied from ch12, with one addition, `.capl`, which is `.cap` with
  `text-anchor:start`. See the caution below; the addition is not decorative.
- Two weights of drawn line, as in `tipping-scale.svg`: 1.8 for the object being
  argued about (the rule, the lean), 0.8 at opacity .28 for the hairline base
  under the footing and the divider before the closing caption.
- Dashed outline for the thing that is not there (the unfinished sentence), solid
  fill at opacity .82 for the thing that is (the footing), which is the same
  solid-versus-dashed grammar as ch12 and `the-operating-system.svg`.
- Beat labels in spaced small caps at the left margin with an italic gloss under
  them, which is the `four-ds.svg` row pattern and the ch12 ROMANCE pattern.
- No quotation, no number, no Stoic term on the plate. Epictetus is the chapter's
  authority for deciding in advance, but his words stay in the prose.

## Checks

`python3 runs/design/svgcheck.py runs/ch10/plate.svg`

```
runs/ch10/plate.svg
  clean
```

## What the render showed

Three defects the markup did not show and the checker could not catch.

1. **Captions sitting on top of the lean arrows.** `text-anchor="start"` as an
   attribute on an element whose class sets `text-anchor:middle` did not take:
   the label rendered centred, straight through the arrow, and "so it folds"
   rendered on top of the line's right end. Fixed by adding a `.capl` class.
   Confirmed with an isolated test: a class beats a `text-anchor` attribute, and
   an inline `style="text-anchor:start"` beats the class. **svgcheck.py reads the
   attribute and trusts it**, so this whole family of defects is invisible to it.
   Proposed house rule in the return.
2. **The subtitle overran the right margin** once it grew to name the lean.
   Caught by the checker (`MARGIN y=66.0 ... 36..604`), shortened, re-run clean.
3. **The footing read as a floating block** until a hairline base was added under
   it. Same defect family as the tipping scale's first draft, where the beam
   missed the fulcrum.

## For the author

1. **UNDECIDED / DECIDED as the two labels.** They name the mechanism the
   distillation names. The chapter's own pair is preference / boundary, which is
   on the plate as the gloss under each label. If he wants that pair promoted to
   the labels, it is a two-word change and the glosses come off.
2. **The money example is his.** It is on a page meant to be shared. No figure
   appears, only the rule and what it protects, but he should confirm he is happy
   to have that one in a diagram rather than only in prose.
