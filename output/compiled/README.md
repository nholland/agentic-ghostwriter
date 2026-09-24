# Current compiled copies

Coverage: Prologue, Introduction, Chapters 1–13, relevant Arc openings and 16 chapter/Arc plates. This is the available book, not all 29 planned chapters. Chapter 13 remains an author-review draft; plate approval status is in manifest.json. Older-book editorial findings remain deferred.

- [Book](book.pdf): 122 pages, prose, plates, and practices.
- [Distillations](distillations.pdf): 13 pages, Chapters 1–13.
- [Plates](plates.pdf): 16 plates, each followed by its intent, visual explanation, and validation question.
- [Chapter 11](chapters/ch11.pdf): 11 pages, current prose, corrected plate, distillation.
- [Chapter 12](chapters/ch12.pdf): 7 pages, prose, plate, distillation.
- [Chapter 13](chapters/ch13.pdf): 7 pages, prose, plate, distillation.
- [Chapter 9](chapters/ch09.pdf) and [Chapter 10](chapters/ch10.pdf): sole existing exports, relocated unchanged; not reformatted this session.

Rebuild: `python3 scripts/compile_current.py --chapters 11 12 13 --include-run 13`.
One approved format, stable filenames. Source text lives in books/ or explicitly selected runs/. Supporting generated HTML/images live in assets/. Source hashes and scope are in manifest.json. Superseded PDF inventory is in cleanup.json.

Validation: 126/126 existing fixtures passed with the local font path; actual chapter-opening and alignment checks passed for 11–13; all six newly rendered PDFs inspected page by page using rendered contact sheets. Ordered chapter/practice counts, precursor/Arc openings, 13 complete distillations, and 16 raster plate pages checked. No editorial apparatus found. Chapter wording unchanged. Designer and Reader Panel checked the refreshed Chapter 11 plate.

Maintained plate explanations: [plate-briefs.md](../../runs/design/plate-briefs.md). Edit this source, then run `python3 scripts/plate_packet.py` to replace the plates PDF. Show each image before revealing the explanation.

Plates review packet updated: 32 pages (16 image/explanation pairs). All explanation text checked against the maintained Markdown, all source references resolved, all pages visually inspected, and text margins checked. Rendering preserves the brief byte-for-byte.
