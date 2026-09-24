---
name: gw-compile
description: Compile current chapter, book, distillation, and plate PDFs with the one approved format. Replace stable exports under output/compiled/.
---

# /gw-compile — current reader copies

Run `python3 scripts/resolve_book.py` and `python3 scripts/okf_gate.py` first.
Structural failures block; unverified citations remain reported, not invented or
silently upgraded.

## One format

`scripts/chapter_pdf_local.py` is the single Chromium rendering implementation;
`scripts/chapter_pdf.py` is a compatibility entry point, not an alternate style.
`pdf_chapter_style.py` supplies chapter/subsection structure. Use the approved
6-by-9-inch Georgia format: ordinary Chapter N label, bold separate title,
subsection headings on their own lines, flush-left paragraphs with zero indent.
Raster plates keep diagram labels out of audiobook narration. No running headers.
Never copy CSS into a chapter-specific builder or restore the retired WeasyPrint
layout. Set CHROME and NODE_PATH when automatic runtime discovery is insufficient.

## Current outputs

`python3 scripts/compile_current.py --chapters 11 12` refreshes those chapter
packets and all three collections. A chapter packet includes prose, plate, and
full distillation at the back. Collections are full available manuscript with
plates/practices, distillations only, and plates with plain-language explanations.

Use `--include-run N` only when the author has requested an unlanded chapter.
For the current author review through Chapter 13:

```
python3 scripts/compile_current.py --chapters 11 12 13 --include-run 13
```

Landed chapter prose/distillations come from books/; explicit unlanded inputs
come from runs/. `compile.py` assembles the manuscript, preserving precursor and
Arc openings, chapter order, and practice fields. Compilation never constitutes
a chapter verdict or permission to land prose.

Keep one current PDF per chapter at `output/compiled/chapters/chNN.pdf`, and
`book.pdf`, `distillations.pdf`, `plates.pdf` in `output/compiled/`. Stable names
are replaced, not timestamped. `manifest.json` records coverage, source hashes,
and unapproved chapters. Generated HTML and assets are supporting build files.
Remove superseded exported PDFs only after replacements pass checks; preserve
source manuscript, reviews, and design work. Git retains historical tracked exports.

## Verify delivery

Run `package_check.py` on chapter and manuscript HTML; standalone collections
have their own intended structure and do not open on chapter prose. Run
`tests/check_pdf_opening.py` for chapter PDFs. Extract text to check reading order,
full distillation content, and absence of editorial notes. Render every page and
inspect headings, paragraph alignment, plate edges, overflow, and blank pages.
Report actual checks and scope, including any unavailable or unapproved material.

For the plate review document, maintain `runs/design/plate-briefs.md` and run
`python3 scripts/plate_packet.py`. It replaces `output/compiled/plates.pdf`,
showing each image before its explanation. The general compile uses this same
brief and renderer; it never regenerates brief prose from distillations.
