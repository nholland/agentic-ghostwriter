# Plate kit: the book's plate style of record

The author's "Engraved Line" plate system, built in another thread and brought
into the book on 2026-11-10 with his words: "I actually want to update all of my
plates and interludes with work I did in another thread ... incorporate into the
design system, book, etc." `STYLE.md` is his grammar; `plates.css` the tokens;
`platekit.py` the primitives; each `plate_NN_*.py` / `interlude_N_*.py` one drawing.

## His rulings on arrival (2026-11-10)

- Chapter 8: the pebble-pile version (`plate_08_the_tipping_scale_alt.py`). The
  balance-scale version is kept in `rejected/`.
- Typeface: plates in Georgia, the body face. `plates.css` sets `--plate-font`
  to the body's exact stack (`Georgia, 'Liberation Serif', serif`, from
  `scripts/chapter_pdf_local.py`), not the kit's EB Garamond.
- The Part I closing page's last line is to be rewritten to suit the new Part I
  drawing (stones in a current, no longer the canyon).

## Build

    cd books/the-stoic-husband/design/plate-kit
    python3 plate_01_the_gap.py          # or any plate / interlude script

Each script writes to `out/`: the kit's standalone `.svg` and `.figure.html`
(as he designed them), and `.book.svg`, the single file the house prints.

## What the house added, and why

`platekit.book_svg()` composes the figure's title, deck, rule and caption around
the art as SVG text, because the book's pipeline (`plate_check.py`, `land.py`,
`compile.py`, `plate_packet.py`, the EPUB tool) takes one SVG per plate. It keeps
STYLE.md's proportions: art at 86% of the width (78% on a Part page, to clear the
page margin bands), furniture at the sizes `plates.css` gives the HTML figure.
Two consequences, recorded rather than hidden:

- The book rasterises plates at 3x for print (`scripts/chapter_pdf_local.py`),
  so they print as high-resolution images, not as the vectors STYLE.md asks for.
  Changing that is a renderer decision the kit does not make on its own.
- Furniture lines are wrapped with `plate_check.py`'s DejaVu metrics, which run
  wider than the Liberation Serif that actually prints, so titles wrap a little
  earlier than in his HTML figures. Ch3, Ch9 and Ch13 each carry a label the
  check measures as too wide or touching; rendered at print size they do not
  touch.

## Where the book takes them

| Output | Copied to |
|---|---|
| `out/plate-NN-*.book.svg` | `runs/chNN/plate.svg` and `design/plates/<title-slug>.svg` |
| `out/interlude-N-*.book.svg` | `parts/plate-N-<slug>.svg` (Part closing plates I-III) |
| `out/frontispiece.book.svg` | `design/plates/frontispiece.svg` (own page before the Prologue; added with his second upload, 2026-11-10) |

Rebuild and recopy together; `compile.py` reports a chapter plate as approved
only when `runs/chNN/plate.svg` and its `design/plates/` copy are identical.

A drawing that spills past its 324-unit canvas (the frontispiece's river, the
Part II oak's lower limb) is shrunk and re-centred on its real extent by
`book_svg()`; drawings inside the canvas keep the standard scale.
