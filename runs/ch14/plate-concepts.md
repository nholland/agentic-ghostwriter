# Chapter 14 plate concepts

Mode: concepts. Three roughs for the Reader Panel; no concept selected and no finished plate produced.

## A: Appreciation poured into care

**A stranger sees this and takes away:** Noticing what you value in your wife becomes small acts that tend the life you share.

**Carrier:** One watering can distributes its contents into three streams, each landing above the same continuous grass. The can holds appreciation; its streams name the concrete forms of care. This is a transformation with several expressions, not three kinds of wife or three alternative marriages.

**Chapter image:** “The grass is greener where you water it” and “Keep tending the life you share”. These are source references in these notes only; neither quotation appears on the plate.

**Copy:** Title: “Appreciation becomes care”. Labels: “what you value in your wife”; “appreciation”; “a kinder answer”; “a sincere compliment”; “enjoying her company”; “the life you share”. Mechanically counted from SVG text: 23 words including the three-word title, 9 text elements, 1 italic caption line. The first phrase comes from the distillation's Conversation sentence; the others appear in the refined chapter. The two longer action labels wrap across two text elements each.

**Skeptic's misreading:** Pouring in care guarantees an improved relationship. The drawing deliberately has no before/after grass or guaranteed return, but the watering metaphor still carries that risk.

Thumbnail: `concepts/A.svg`.

## B: Appreciation supports concrete care

**A stranger sees this and takes away:** Appreciating your wife gives the ordinary care of your shared life something to grow from.

**Carrier:** A grass cross-section connects three visible groups of blades, named with concrete caring acts, to a joined root system named appreciation. Unlike A's act of pouring, this is a structural relationship between the often unseen appreciation and the visible conduct it supports.

**Chapter image:** “The grass is greener where you water it” and “The appreciation matters because it can become a kinder answer, a sincere compliment, or time spent enjoying her company.” The roots are a drawn part of the declared grass image, not a second metaphor. The prose does not itself mention roots; the Panel should weigh whether that extension makes the mechanism clearer or merely more abstract.

**Copy:** Title: “Appreciation becomes care”. Labels: “the life you share”; “a kinder answer”; “a sincere compliment”; “enjoying her company”; “appreciation”; “what you value in your wife”. Mechanically counted: 23 words including title, 9 text elements, 0 italic caption lines. Sources as for A.

**Skeptic's misreading:** The wife is the grass and the husband grows or manages her. The grass is explicitly named “the life you share”; no human figure is depicted as gardener, owner or plant. That label must survive any draft.

Thumbnail: `concepts/B.svg`.

## C: Tending is repeated

**A stranger sees this and takes away:** Keep noticing, enjoying and expressing what you value in your wife, and let it shape your answers on ordinary days.

**Carrier:** Four directional arcs surround one patch of grass, making repeated attention and caring conduct an ongoing practice around the same shared life. It is recurrence, unlike A's distribution or B's supporting structure. The arrows connect his own practices; her response is not a node and there is no promised reciprocal arrow from her.

**Chapter image:** “Keep doing that on ordinary days, before dissatisfaction makes it feel urgent” and “Keep tending the life you share, including on the days it gives you nothing new to admire.”

**Copy:** Title: “Appreciation becomes care”. Labels: “Notice what you value”; “in your wife”; “tell her”; “enjoy it”; “the life you share”; “a kinder answer”; “on ordinary days”. Mechanically counted: 24 words including title, 9 text elements, 1 italic caption line. All copy comes from the refined chapter or distillation. Wife and shared-life phrases wrap across two lines.

**Skeptic's misreading:** This is a compulsory sequence or a self-reinforcing emotional loop. The chapter offers practices, not a validated protocol. The Panel must judge whether arrows overstate the sequence.

Thumbnail: `concepts/C.svg`.

## Style and boundaries

Read the existing plates before the brief. Matched the 640-wide chapter canvas, Georgia with serif fallback, dark `currentColor` stroke work, white background, lightly spaced 17px title, 1.8px rounded drawing strokes, centered labels and spare italic captions. Specific models were `tipping-scale.svg` for the drawn relationship and `the-muscle-you-stopped-using.svg` for explicit dark ink on white. Body labels use 16px for phone reading. The existing `design/plates/README.md` supplies written conventions; no new style file is proposed.

All titles exactly match the Mechanism line. Every shape specifies fill; all text anchoring is in CSS. No quotation, statistic, external claim or Stoic technical term appears on the thumbnails. Grass refers to shared life throughout. No book files were changed. These are first-pass roughs with no polishing pass.

## Mechanical notes

The checks below were run on the three roughs, not on a nonexistent `plate.svg`. Isolated labels produce alignment WARNs: A/B use mirrored columns at x=160 and x=480; C uses mirrored x=130 and x=510. Geometry reports no collisions. These are review inputs, not a declaration of standalone success.

Rendering through `chapter_pdf_local.svg_to_png` failed with Playwright SIGABRT and kill EPERM. The attempted PNG destination was temporary storage. No visual inspection or successful ink/raster check is claimed. The Publisher needs a working renderer for the cold visual pick.

Command: `python3 scripts/plate_check.py runs/ch14/concepts/A.svg runs/ch14/concepts/B.svg runs/ch14/concepts/C.svg --chapter 14`

```text
runs/ch14/concepts/A.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x460
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    1 italic lines against a cap of 3 (1 labels + subtitle + closing line)
  [WARN] alignment   centred text on no shared axis: 'a kinder answer' x=160
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=26489] <process di
  [WARN] raster-current preview missing or differs from source at its own scale
runs/ch14/concepts/B.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x460
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    0 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [WARN] alignment   centred text on no shared axis: 'a kinder answer' x=160
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=26491] <process di
  [WARN] raster-current preview missing or differs from source at its own scale
runs/ch14/concepts/C.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x460
  [ ok ] title       title 'Appreciation becomes care' / aria-label 'Appreciation becomes care' vs Mechanism 'Appreciation becomes care'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    1 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [WARN] alignment   centred text on no shared axis: 'tell her' x=510, 'enjoy it' x=130
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed: le trying to kill process: Error: kill EPERM[22m
[2m  - [pid=26493] <process di
  [WARN] raster-current preview missing or differs from source at its own scale
```
