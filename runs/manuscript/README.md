# Compiled manuscripts

Built by `python3 scripts/compile.py`. Filenames carry coverage and date per
CLAUDE.md Rule 15.

| File | Coverage | Source | Pages | Words |
|---|---|---|---|---|
| `the-stoic-husband-prologue-ch11-2026-09-15.pdf` | Prologue, Introduction, PART I and PART II openings, Ch1-11 | the **book pipeline's** `refined.md` — the shipped chapters, not this engine's `runs/` | 72 | 22,301 |

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
