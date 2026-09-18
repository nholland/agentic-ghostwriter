# Archivist Review — 2026-09-18 — both new checks contain the defect they were written to fix

Scope: since `runs/retro/2026-09-17-the-render-gate.md`. PROPOSALS ONLY (Rule 17).
Filed as inbox **#020–#023** — the first proposals ever routed through
`--applied-by`, each with a fixture rather than a grep.

## The one finding

**`package_check.py` passes a package that opens on the distillation** — the exact
defect it was written for — if the section's class says `distback`. It tests the
class string and never the position. Reproduced by the Publisher:

```
<section class="dist distback">…</section><section><h1>Chapter 12</h1>…</section>
→ [ ok ]  opens on: dist distback   EXIT=0
```

**It prints the failure inside its own PASS line.** Second escape: any extra
attribute on the tag (`<section class="dist" id="d">`) is invisible to its regex,
and it then reports `opens on: chapter` for a package that opens on the
distillation. Third: `<h2><span>Draft Notes</span></h2>` escapes the apparatus scan.

The docstring's stated limit is **understated**. It names rendering as the
boundary — glyphs, blank plates — and claims the package "does not have the three
faults we have already shipped". Fault one is the shipped fault, and it is not
guarded.

`voice_rules_check.py` carries the same shape cheaper: its one honest state
crashes. A rule with `spec_number: null` — the state the code's own comment
invites — raises `KeyError: 'NUMBER-UNCHECKED'` on the text path. Latent today
because all eight declare a number; it fires on the ninth, and `okf_gate` then
blocks every prose desk. **The `failed`-list half of that fix landed; the print
half did not** — the same partial-patch shape that bit mid-work.

**The shape is fourteen retros old.** `LEARNINGS.md:99`: *"a check that existed
only as a comment… the file listed a check that looked like enforcement."*
`distback` means "at the back" as a name only. Nothing enforces it.

**Why it recurred here.** Each check's proof was a one-off run and was never
stored. There is no `tests/`, no fixture directory, nothing that re-runs "fails
the pre-fix HTML on three counts". The Archivist had to construct the pre-fix form
itself — and constructing it is what found the escapes. **A proof that cannot be
re-run is a comment.**

## `--applied-by` is unproven, and carried none of the seven

`inbox/` held 19 items and **not one was created that arc**. The seven landed
because the author said "clean those items up". The mechanism written into
`gw-retro.md` that same arc had never carried a proposal. **7-of-7 is evidence
about the author, not the machinery.**

Sharper: every existing close-condition is a `grep`. It proves text exists, not
that it works. `grep -q 'spec_number'` would have closed green over both half-fixes
found today.

## Verified clean

- **The three mutations are genuinely fixed**, re-run independently of the commit
  message: `em_dash_max 0→9`, `bold_max 1→7`, `you_density 40→1` all MISMATCH,
  exit 1, plus two more the Archivist added. Rule 8(e) rests on something real.
- `package_check.py` does fail the exact pre-fix serialization on three counts and
  pass the live artifact. The claim is true for the form that shipped.
- `distillation_html` extraction clean; `#012`/`#014` auto-closed correctly off
  `--prose-only`; `gw-compile`'s replacement text accurate; `GAPS.md`,
  `gw-designer`, plugin copies all correct.

**Residual, disclosed not fixed:** three rules have digit-free probe spans, so
`spec_number` is hand-transcribed with nothing deriving it. Editing `value` and
`spec_number` together passes clean. Two deliberate edits instead of one; judged
acceptable, not worth machinery.

**Contradiction found:** `voice_rules_check.py`'s docstring still describes the
pre-rewrite behaviour and never mentions `spec_number`. The file was rewritten;
its docstring went false the way `gw-compile`'s section had, in the same arc that
replaced that section.

**Minor:** `gw-compile/SKILL.md:41` documents the check's path unquoted. The only
artifact this house has produced has spaces in its name, so copied as written it
splits into seven arguments and exits 2.

**Unexecuted:** rendered PDF page order (no `pdftotext`); the book's
`chapter_pdf.py` (no weasyprint).
