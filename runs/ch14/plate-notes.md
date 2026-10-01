# Chapter 14 plate notes

Current status: the recognition redraw has received a cold Panel PASS and final Designer raster inspection; no corrective edit is required. The author verdict remains pending. The earlier draft and check records below are historical and are superseded by the final readiness review at the end of this file.

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


## Recognition redraw, 2026-09-30 23:22 CDT

This redraw supersedes the previous plate and its review conclusions above. Draft mode, selected concept A. The author's recorded complaint is “current version is awful. It's unrecognizable.” The redraw has now received final raster inspection and a new cold standalone Panel PASS. See the final readiness review below for current status; the author's verdict remains pending.

### What changed and why

Replaced the small rectangular vessel with a large tilted can: open loop handle, sloping rim, curved base, long spout and dark sprinkler head. Replaced the three unbroken connector-like curves with discrete drops descending into grass. Removed the intervening text bands and three-column list. Put “a kinder answer” immediately beside the falling water as the Panel requested. Appreciation is held in the can; the kindness is the watering; the grass is the shared life. These physical connections carry the mechanism instead of leaving grass as a decorative footer.

Kept the selected concept's five text elements, mechanically counted as 18 words including the exact three-word Mechanism title. Copy is inherited from A and its recorded source mapping. The distillation supplies attention, appreciation and care; the concepts record supplies the grounded concrete action and shared-life phrases. The checker confirms grounding against the permitted copy. No quotation, number, technical Stoic term or second metaphor appears. Read only the metaphor_family line from Draft Notes; did not read chapter prose, interview or research.

The one-moment image does not depict improved growth, repayment, or a required response. It also does not explicitly print the previous response caveat. The Panel's transactional misreading remains a question for the independent read, rather than a reason to restore a text band across the watering action.

### House style

Matched tipping-scale.svg's rounded monochrome linework and Georgia/serif typography; matched the-muscle-you-stopped-using.svg's explicit #1a1a1a ink and white background. Retained the selected concept's 640x500 canvas, 17px letterspaced title, 18px action/instruction labels and 16px italic captions. Main contours use 2.4px strokes for phone recognition, close to the 2.2px icon strokes in incomplete-husband.svg. Existing conventions are in design/plates/README.md, so no new style file is proposed.

### Full format checklist

- [x] One plate, one carrier, one chapter anchor image.
- [x] Centered text on x=320; internal/action labels use explicit left alignment in CSS.
- [x] Single drawing block centered as confirmed by the check.
- [x] Canvas 640 wide and 500 high.
- [x] Two italic lines within the computed cap of three.
- [x] No bare text-anchor attributes; anchors live in classes.
- [x] Explicit fill on every shape and text.
- [x] Web-safe serif fallback, house palette and line-based construction.
- [x] Exact Mechanism title and matching aria-label.
- [x] No invented statistics, quotes, em dashes or unglossed terminology.
- [x] Updated only Chapter 14's maintained explanation, preserving unrelated entries.
- [x] Final raster visually inspected by the Designer in the final readiness pass. The Publisher supplied the fresh `pdf/plate.png`; the earlier local rendering limitation and stale-preview warning are superseded.

### Checks and limitation

The first check found a five-pixel right-margin excess on “a kinder answer.” Shifted that label ten pixels left. Reported the failure to the Publisher for the runtime attempt record; this desk's commission permits only the three assigned apparatus files.

First command: `python3 scripts/plate_check.py runs/ch14/plate.svg --chapter 14`

```text
runs/ch14/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [FAIL] geometry    MARGIN  y=263.0 'a kinder answer' 443..605
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x500
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    2 italic lines against a cap of 3 (1 labels + subtitle + closing line)
  [ ok ] alignment   3 centred texts on the axis or a shared column; 1 drawing blocks centred or mirrored
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=94781] <process di
  [WARN] raster-current unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=94796] <process did exit: exitCode=null, signal=SIGABRT>[
```

Same command after the label adjustment:

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
  [ ok ] captions    2 italic lines against a cap of 3 (1 labels + subtitle + closing line)
  [ ok ] alignment   3 centred texts on the axis or a shared column; 1 drawing blocks centred or mirrored
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=94812] <process di
  [WARN] raster-current unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=94821] <process did exit: exitCode=null, signal=SIGABRT>[
```

Exact renderer fallback result: `ModuleNotFoundError: No module named 'cairosvg'`.

No FAIL rows remain in the second check. Rendering warnings are unchecked, not passes. This desk does not grade its own image; the Publisher must obtain a fresh raster, inspect it, independently rerun the checker and commission the standalone read. Recognition and transactional interpretation remain for that read and the author.


## Final Designer readiness review, 2026-09-30

Inspected the current `plate.svg` and the fresh `pdf/plate.png`, then compared the format findings with the current `plate-read.md` and the historical checks in these notes. No SVG changes were needed or made. The raster clearly shows a can, separated falling drops and receiving grass; the action label has clear space to its right and does not collide with the drops. The slight overlap of the lowest drops and grass establishes contact and does not obscure either form.

### Completed format checklist

- [x] Canvas is 640×500 in the SVG; the supplied raster preserves that aspect ratio.
- [x] All three centered texts use x=320. The two other labels use CSS left alignment and sit clearly within or beside their referents.
- [x] Can, falling water and grass form one balanced drawing block, with open margin space on both sides.
- [x] Two italic text lines fit the recorded caption cap of three.
- [x] Text anchors are defined in CSS classes; no bare text-anchor attributes occur.
- [x] Every shape and text has an explicit fill; the background is white and ink is #1a1a1a through currentColor.
- [x] Georgia has a serif fallback. Title, labels and drawing remain visually distinct, with no clipping or unintended text collisions in the fresh raster.
- [x] Title and aria-label are identical: “Appreciation becomes care.” Exact agreement with the distillation is recorded by the supplied source check, rather than independently re-read in this restricted pass.
- [x] Five text elements contain 18 words including the title; no on-plate quotation, statistic, em dash or technical term requires a gloss.
- [x] Final raster inspection is complete. Earlier unavailable-render and pending-read statements are historical limitations, not the current status.
- [x] The independent cold Panel read is complete and PASS, as recorded in `plate-read.md`; no corrective edit was requested.

The Panel's takeaway is that noticing what he values in his wife helps him answer more kindly and care for their shared life. This is the reported reader result, not a new Designer grade. Preserve the residual transactional risk: a defensive reader could infer that kinder answers promise marital growth. The drawing depicts his conduct without a pictured reward or required response from her; the Panel judged this risk insufficient to require a redraw. Author verdict remains pending.

This pass read only the five commissioned artifacts. It did not re-read the house plates or chapter sources; style provenance and grounding above remain the prior desk's recorded evidence. Only this notes file was edited, so the maintained visual explanation requires no change.


### Publisher final check of the recognition redraw

Exact result supplied by the Publisher during this final pass, superseding the earlier 13-text / three-block plate check and the redraw's local rendering warnings. Command: `python3 scripts/plate_check.py runs/ch14/plate.svg --chapter 14`.

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
  [ ok ] captions    2 italic lines against a cap of 3 (1 labels + subtitle + closing line)
  [ ok ] alignment   3 centred texts on the axis or a shared column; 1 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
  [ ok ] raster-current preview matches source pixels at its own scale
```

All Publisher check rows pass for the current redraw, including rendered ink margins and current raster identity. Together with the completed Designer format inspection and cold Panel PASS, the plate is ready for the author's verdict. No remaining rendering or independent-read blocker is recorded.
