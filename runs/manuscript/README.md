# Compiled manuscripts

Built by `python3 scripts/compile.py`. Filenames carry coverage and date per
CLAUDE.md Rule 15.

| File | Coverage | Source | Renderer | Words |
|---|---|---|---|---|
| `the-stoic-husband-prologue-ch11-2026-09-15.pdf` | Prologue, Introduction, PART I and PART II openings, Ch1-11 | the **book pipeline's** `refined.md` — the shipped chapters, not this engine's `runs/` | `chapter_pdf.py` (weasyprint) | 22,301 |
| `the-stoic-husband-prologue-ch12-2026-09-20.pdf` | Prologue, Introduction, PART I/II/III openings, Ch1-12 | this house's `books/the-stoic-husband/chapters/*/refined.md` | `chapter_pdf_local.py` (headless Chromium fallback — weasyprint unavailable, GAPS.md) | 23,932 |
| `the-stoic-husband-prologue-ch12-plates-draft-2026-09-20-1952.pdf` | As above; round 3: Ch8 and Ch12 through `/gw-plate` (concepts, cold pick, draft, check, cold read, one revision), Ch7 and Ch9 on the author's words. Filenames carry the clock from here (Rule 15: two same-day compiles once shared a name). | `compile.py --plates` | `chapter_pdf_local.py`; plates rasterised via Playwright and checked by `plate_check.py` | 24,067 |
| `the-stoic-husband-prologue-ch12-plates-draft-2026-09-20.pdf` | As above, plus 15 plates: one per chapter Ch1-12 after its prose, Part I/II/III closing plates on their own pages. **13 of 15 are drafts** (`runs/chNN/plate.svg`, `runs/parts/`); only the Part I/II plates are landed. Rebuilt 17:56 after the Reader Panel's round-2 edits (`runs/design/2026-09-20-plate-reader-review.md`). | `compile.py --plates` | `chapter_pdf_local.py`, plates rasterised via Playwright | 24,067 |

## Why this is a script and not a checklist

The first compile, on 2026-09-15, was assembled by following the skill's prose
and **dropped both Part opening pages**. Nothing caught it: the only mechanical
check was a word-count delta against the previous compile, the two pages are
~120 words, and it was the first compile so there was no previous one. The
incumbent pipeline's `manuscript.md` had both pages — the replacement was
quietly less complete than the thing it replaces.

`compile.py` now asserts, before it reports success, that every Part opening the
range crosses is present, that there is one Practice section per in-range
distillation, that no apparatus leaked, and that chapters are in order. Those are
absolute checks against the outline and the files on disk, because a delta is
relative and cannot see a defect already in the baseline.
