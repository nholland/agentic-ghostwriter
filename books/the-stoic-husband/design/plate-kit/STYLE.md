# Plate style: Engraved Line

The three interlude drawings (canyon, oak rings, river mouth) are already the best images in the book. This style makes every mechanism plate belong to the same hand.

## Where the style lives

| Layer | File | Holds |
|---|---|---|
| Tokens | `plates.css` | Ink, the three line weights, lettering sizes, plate furniture (title, deck, caption) |
| Primitives | `platekit.py` | Hand-tremor strokes, measures, rings, labels. Seeded, so builds are identical |
| Grammar | this file | The rules a plate must follow |
| Plates | `plate_NN_name.py` | Geometry only. No colours, weights or font sizes |

A plate never states a colour, a stroke width or a font size. It names a class (`line`, `bold`, `hair`, `dotted`, `caps`, `ital`) and the CSS decides what that means.

## Grammar

1. **One ink.** No greys, no opacity. Tone comes from how closely lines are packed. Solid ink is for small marks only (a hole, a knob).
2. **Three weights.** `hair` for measures and ticks, `line` for the body, `bold` for the one thing the plate is about. One bold element per plate.
3. **Readable before clever.** A reader should get the idea from the drawing in a few seconds, without the caption. If an abstraction needs explaining, draw the thing itself (a door, a board, a man).
4. **Drawn from the book's world.** Currents, channels, banks, rings, grain, roots, light. No boxes, bars, or arrows with heads. If the idea needs a box, find the natural object that does the same job.
5. **Dotted means not yet.** Anything latent, unsaid or undecided is dotted. Solid means it happened.
6. **Lettering follows old map convention.** Spaced caps for what is given (her words, the week, the day). Italic for what moves or is chosen. No bold lettering inside the art.
7. **Few labels in the art.** Five at most, or one caps and one italic per row when a plate has rows. Title, deck and closing line sit outside the drawing as real page text. Plates are not numbered.
8. **Open paper is a material.** The most important area is usually the emptiest.
9. **Lines tremble slightly, shapes do not.** Tremor comes from `platekit`, never from SVG filters (filters get rasterised in the PDF).

## Build notes

- Plates go into the book as inline `<svg>` inside `<figure class="plate-fig">`, not as `<img>`, so they print as vectors and take the book's typeface.
- Plates are drawn on a 324-unit canvas and printed at 86% of the text block, so no drawing reaches the text margins. The hairline prints at 0.4 pt, which is the floor for print; do not go thinner.
- `--plate-font` should be the same face as the body text.

## Interludes and frontispiece

- The frontispiece and the three interludes are full-page drawings with no title or deck: the image, then one closing line set slightly larger than on the mechanism plates.
- They follow the same grammar as the plates. The oak, the sun and the river current are drawn by shared code (`scenery.py` and the interlude files), so the opening scene uses the same three drawings the reader meets later.
- Each interlude closes its Part. Its line should be a sentence from that Part's opener.
