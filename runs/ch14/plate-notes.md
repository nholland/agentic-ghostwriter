# Chapter 14 plate notes

Draft mode. Panel selection: A, as recorded in `plate-pick.md`. Pending independent check, rendered inspection, standalone read and author verdict.

## What the drawing shows

Appreciation becomes three small forms of care: a kinder answer, a sincere compliment, and enjoyment of her company. The watering can and its three streams carry that transformation. Grass is explicitly named as the life they share. It is neither a picture of the wife nor a picture of the husband's property.

The Panel's concept read identified a risk that one can could make him solely responsible for keeping the entire marriage alive. The draft scopes the streams as “the care you give her”; grass extends past their reach on both sides. The equal grass height, single moment and absence of a returning arrow avoid a promised improvement or reward. “Without requiring a particular response” comes directly from the distillation. These are design decisions for the Panel to test, not a claim that its risk has been eliminated.

## Style matched

Matched `books/the-stoic-husband/design/plates/tipping-scale.svg`: monochrome currentColor, 1.8px rounded strokes, Georgia with serif fallback, centered 17px letter-spaced title. Matched `the-muscle-you-stopped-using.svg`: explicit #1a1a1a ink and white background. Used 16px action labels and 14px italic captions for phone reading. Canvas is 640x500, with the extra height used for the scope and response wording. Existing `design/plates/README.md` conventions were read; no new style file is proposed.

## Copy and sources

Mechanically counted from XML text elements: **34 words, 13 text elements** including the title. No on-plate quotation, number or technical Stoic term.

| Copy | Source |
|---|---|
| Appreciation becomes care | Distillation Mechanism, exact wording |
| Notice what you value / in your wife | Refined section label and distillation Conversation sentence |
| appreciation | Refined chapter, recurring term |
| the care you give her | Refined “Notice what you value” section |
| a kinder / answer | Refined “Let appreciation become care” section |
| a sincere / compliment | Same paragraph |
| enjoying / her company | Same paragraph |
| the life you share | Refined final sentence |
| without requiring a particular response | Distillation Practice 2 |

The declared metaphor family remains grass, greener, water, waters, watered, watering, tend, tends, tending, tended. No secondary image is introduced.

## Format checklist

- [x] Every centered text is on the canvas axis or a shared column: 160, 320, 480.
- [x] Drawing blocks centered or mirrored, as checked below.
- [x] Canvas 640 wide.
- [x] Two caption lines within the computed cap of four.
- [x] No bare text-anchor attribute; CSS classes set anchors.
- [x] Explicit fills on every drawn shape and text.
- [x] Mechanism wording is the title.
- [x] Publisher rendered and visually inspected the final SVG; see Publisher final check below. The Designer’s sandbox rendering failure was resolved by the Publisher’s browser session.

Updated only the Chapter 14 entry by appending to `runs/design/plate-briefs.md`; preserved the existing entries and introductory prose. No book files changed.

## Counted check

Command: `python3 scripts/plate_check.py runs/ch14/plate.svg --chapter 14`

```text
runs/ch14/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x500
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    2 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   13 centred texts on the axis or a shared column; 3 drawing blocks centred or mirrored
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=62156] <process di
  [WARN] raster-current preview missing or differs from source at its own scale
```

The renderer warnings are limitations, not passes. The Publisher should render the SVG and run its independent check before the standalone Panel read. No author-only wording ruling is needed at this draft stage; all copy is grounded. Whether the scoped watering image still suggests sole responsibility is the specific reader question left open.

## Stage 6: final revision and format review

Read `plate-read.md`. The Panel returned PASS for the primary mechanism and found a secondary risk in the response caveat's placement beneath the entire shared-life image. Made one layout revision: placed “without requiring a particular response” directly below the three acts, before the grass. Lowered the grass and its label slightly to preserve whitespace. The caveat now qualifies those acts of appreciation instead of closing the whole marriage diagram. No copy, causal relationship or claim was added. The word count remains 34 and the text-element count remains 13.

Updated only Chapter 14's maintained visual explanation to describe this placement. Preserved all unrelated entries. The Panel must judge the revised image; this note does not award it a second PASS.

Final format checklist:

- [x] All centered text uses x=320 or the shared columns x=160 and x=480.
- [x] All three drawing groups centered or mirrored.
- [x] Canvas 640 wide, 500 high.
- [x] Two italic captions remain within the four-line cap.
- [x] Text anchors specified only in CSS classes.
- [x] Explicit fills, serif fallback, unchanged house palette and stroke weight.
- [x] Title exactly matches the Mechanism; copy remains source-grounded.
- [ ] Revised raster inspection remains for the Publisher: local Playwright rendering fails in this desk's sandbox.

Current source check, after this one revision:

```text
runs/ch14/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x500
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    2 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   13 centred texts on the axis or a shared column; 3 drawing blocks centred or mirrored
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=63118] <process di
  [WARN] raster-current unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=63128] <process did exit: exitCode=null, signal=SIGABRT>[
```

## Publisher final plate check, 2026-09-30 17:48 CDT

Independent command after the single Designer revision and final raster render:
`python3 scripts/plate_check.py runs/ch14/plate.svg --chapter 14`

```text
runs/ch14/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x500
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    2 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   13 centred texts on the axis or a shared column; 3 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
  [ ok ] raster-current preview matches source pixels at its own scale
```

I inspected the final PNG at `runs/ch14/pdf/plate.png` and every page of
`output/compiled/chapters/ch14.pdf`, including the embedded plate and full
distillation. The revised plate's standalone Panel read is PASS; its secondary
one-sided-responsibility risk remains documented in `plate-read.md`.
