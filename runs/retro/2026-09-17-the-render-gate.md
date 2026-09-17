# Archivist Review — 2026-09-17 — the author is the render gate

Scope: since `runs/retro/2026-09-16-second-renderer.md`. PROPOSALS ONLY (Rule 17).

## The four defects are one finding

Blank plate, overlapping letters, three formatting defects already fixed in the
book's own renderer, and a PDF opening on the distillation. **All four were found
by the author opening the artifact**, because **no script in this repo reads a
rendered artifact.** Verified: every `scripts/*.py` that touches `.html` or `.pdf`
*writes* one; none reads one back to check it. `gw-specchecker` has no match for
`manuscript|PDF|package|render`.

`gw-compile/SKILL.md:10` states the stake — *"Nothing else in the house matters to
a reader"* — and nothing executable stands behind that sentence.

The distillation case sharpens it. The answer was **already executable in this
repo**: `compile.py:126` lifts only `practice()` out of `distillation.md` and
`strip_apparatus()` drops the rest. The house's compiler and the house's renderer
disagreed about what a reader receives, and nothing compared them. Third instance
of the shape: the rule existed, was correct, and was invisible when needed.

**Proposal: `scripts/package_check.py`**, drafted and run — 208 words. Asserts on
the emitted HTML that the package never opens on apparatus, that a distillation is
marked and labelled, and that no apparatus heading reached the reader. It **fails
the pre-fix HTML on three counts and passes the fix**. Deletes `gw-compile`'s
71-word *"One renderer, not two"* section, which is now **false**: it forbids a
second renderer the house wrote, is using, and shipped this defect from. Retires
the prior retro's `pdf_format_check.py` rather than adding alongside it.

Honest limit: catches 1 of the 4. Ordering and apparatus are checkable in HTML;
the blank plate is cheap to add; **overlapping letters needs raster inspection and
stays with the author.**

## Carried, re-proved, not restated

**`voice_rules_check.py` is unfixed and Rule 8(e) rests on it.** Last touched
before the retro that proved the holes. Re-mutated, `house.json` md5-verified
identical after: `em_dash_max=9`, `bold_max_per_piece=7`,
`you_density_min_per_1000=1` all print `[ok]` with the wrong number beside the
pass, exit 0. **Highest-severity open item.**

**0 of 9 proposals applied — 0 of 16 across two retros.** Confirmed: one file
changed outside `runs/`. Only changes the author approves live ever land. The fix
is not new machinery: **`inbox.py --applied-by` already exists** and closes an item
when the change lands. Route accepted proposals through it and a proposal becomes a
ruling that closes itself. Deletes the retro's standalone proposals list as system
of record.

## The fix repeated the defect's shape

`build()` now has two distillation paths, 7 transform lines each, **5 identical**.
A defect caused by two copies of one stylesheet, fixed by making two copies of one
transform. Extract `distillation_html(md, kicker)`; deletes ~16 lines, adds none.

## What worked

`--distillation-at` carries its own reason in `--help`, quoting the
shipped-manuscript fact, so the mistake cannot be re-made without reading why.
The inbox auto-close remains the only self-closing loop in the house.

## Unexecuted

`pdftotext`/`pdfinfo` absent, so the rendered PDF's page order was not verified
visually; the ordering claim rests on the emitted HTML.
