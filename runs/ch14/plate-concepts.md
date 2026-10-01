# Chapter 14 plate concepts

Designer, concepts mode. 2026-09-30 23:16. Three rough thumbnails, one drawing pass each. No concept is approved. The existing plate.svg is unchanged.

## Recognition diagnosis

The brief records the author's words: “current version is awful. It's unrecognizable.” The current vessel is a small upright rectangle with a handle and narrow spout. At phone width its shape is closer to a cup than a watering can. Three uninterrupted curves look like diagram connectors, not falling water. They end above the care labels; a further text band separates them from the grass. The grass therefore reads as a decorative footer. The actual relationship, appreciation becoming care for a shared life, lives mainly in the words.

The alternatives make the anchor image structural: contact between water and grass (A), a visible root-to-shoot dependency (B), or care recurring across ordinary days (C). They are different carriers, not three layouts of the old fan of labels.

## A. Water reaches the grass

**A stranger sees this and takes away:** Noticing what you value in your wife gives you appreciation to turn into everyday care for your shared life.

**Carrier:** A large, recognizable watering can pours discrete falling drops directly onto a single patch of grass. Appreciation is inside the vessel; the kinder answer is the act of tending. The water visibly reaches the grass instead of terminating at a caption.

**Chapter image:** “The grass is greener where you water it” and “Keep tending the life you share”. These source excerpts identify the image here; neither quotation is printed on the thumbnail.

**Copy, counted:** 18 words total, 15 excluding the three-word title. Title: “Appreciation becomes care”. Other text: “Notice what you value in your wife”; “appreciation”; “a kinder answer”; “the life you share”. Two italic lines.

**Skeptic's misreading:** Kindness is a technique for making the wife grow into a more pleasing person. The grass must remain the shared life, not an illustration of her improvement.

**Validation question:** Can a stranger identify a watering can, falling water, and grass without reading, and then locate the husband’s action from the labels?

Thumbnail: `concepts/A.svg`.

## B. Appreciation feeds the care

**A stranger sees this and takes away:** Appreciation for your wife supports the kinder answers and sincere compliments you give her.

**Carrier:** One continuous grass plant extends from roots below the ground to visible shoots above it. Appreciation sits by the roots, care by the shoots. The physical continuity makes their dependency visible without a generic flowchart or vessel.

**Chapter image:** “The grass is greener where you water it”. Roots are the proposed visual extension of that grass image, not a second metaphor. The chapter itself does not name roots; that interpretation needs the Panel’s judgment and the author’s verdict.

**Copy, counted:** 26 words total, 23 excluding the title. Title: “Appreciation becomes care”. Other text: “Notice what you value in your wife”; “the care you give her”; “a kinder answer”; “a sincere compliment”; “appreciation”; “the life you share”. Three italic lines.

**Skeptic's misreading:** Good intentions automatically produce kind behavior. The chapter requires practicing care; this carrier could understate that choice.

**Validation question:** Does the reader see appreciation supporting actual care, or only a generic plant with labels?

Thumbnail: `concepts/B.svg`.

## C. Tending on ordinary days

**A stranger sees this and takes away:** Put appreciation for your wife into small acts of care repeatedly, in the ordinary life you share.

**Carrier:** Three acts of watering recur above three equal grass patches, read across a time arrow. Different care labels name the acts, while equal grass height avoids inventing a growth rate or guaranteed improvement. Repetition, rather than a single transfer or hidden dependency, carries the argument.

**Chapter image:** “Keep doing that on ordinary days” and “Keep tending the life you share”. The recurring watering action is the chapter's practice made visible.

**Copy, counted:** 29 words total, 26 excluding the title. Title: “Appreciation becomes care”. Other text: “Notice what you value in your wife”; “a kinder answer”; “a sincere compliment”; “enjoying her company”; “Keep doing that on ordinary days”; “the life you share”. Two italic lines. The three care labels wrap across two lines each.

**Skeptic's misreading:** These three acts are a prescribed sequence, or three different relationships. The Panel should test whether repetition across time is legible.

**Validation question:** Do the repeated acts read as ordinary sustained care, without implying a wife must repay it?

Thumbnail: `concepts/C.svg`.

## Style and copy sources

All three use a 640 × 500 white canvas; currentColor at #1a1a1a; Georgia with serif fallback; a centred 17px semibold, letterspaced title; quiet italic captions; explicit fills; thin rounded linework. These match the family in `design/plates/small-rocks-big-rocks.svg`, `tipping-scale.svg`, and `the-muscle-you-stopped-using.svg`. Body labels are enlarged to 18px for phone reading. Existing conventions are in `design/plates/README.md`; no new style file is proposed.

Title and opening label: distillation mechanism and refined “Notice what you value” section / opening paragraph. Care labels: refined “Let appreciation become care” paragraph. Shared-life label and tending: refined final sentence. Ordinary-days line: same care paragraph. No Stoic terminology, statistics, or quotations appear in the thumbnails.

Literal word counts were computed from SVG text nodes with Python, splitting on whitespace: A 18, B 26, C 29.

## Rough-thumbnail check

Command: `python3 scripts/plate_check.py runs/ch14/concepts/A.svg runs/ch14/concepts/B.svg runs/ch14/concepts/C.svg --chapter 14`.

The check returned no FAIL rows. Rendering was blocked by the local Playwright process launch/termination permission failure; ink and raster are unchecked. Do not treat these as visually verified. No second drawing pass was made in concepts mode. The final plate check belongs to draft mode; running it against the unchanged, rejected plate would not validate these concepts.

Verbatim checker rows (terminal colour escape codes omitted):

```text
runs/ch14/concepts/A.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x500
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    2 italic lines against a cap of 3 (1 labels + subtitle + closing line)
  [WARN] alignment   centred text on no shared axis: 'appreciation' x=205, 'a kinder answer' x=172; drawing off centre with no mirror and no text on its axis: block -112..126 centred at 7
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM
  - [pid=94058] <process di
  [WARN] raster-current unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM
  - [pid=94060] <process did exit: exitCode=null, signal=SIGABRT>
[
runs/ch14/concepts/B.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x500
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    3 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [WARN] alignment   centred text on no shared axis: 'a kinder answer' x=160, 'a sincere compliment' x=440
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM
  - [pid=94062] <process di
  [WARN] raster-current unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM
  - [pid=94064] <process did exit: exitCode=null, signal=SIGABRT>
[
runs/ch14/concepts/C.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x500
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    2 italic lines against a cap of 2 (0 labels + subtitle + closing line)
  [WARN] alignment   drawing off centre with no mirror and no text on its axis: block -112..126 centred at 7, block -112..126 centred at 7, block -112..126 centred at 7
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM
  - [pid=94066] <process di
  [WARN] raster-current unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM
  - [pid=94068] <process did exit: exitCode=null, signal=SIGABRT>
[
```

The roots interpretation in B is the one metaphor judgment requiring explicit attention. Alignment warnings remain for the selected concept's draft pass. The Publisher owns the maintained finished-plate brief; this commission changed only this concepts document and the three thumbnails.
