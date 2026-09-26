---
id: 077
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 01:14
retired_applied_by: test -d tests/fixtures/docstrings
applied_by: python3 tests/manual_description_cases.py && python3 scripts/manual.py --check
resolved: 2026-09-26 13:18
---

# docs/manual.html's derived scripts table truncates each cell at the first PHYSICAL line of the module docstring, not the first sentence, so three live rows publish mid-sentence and ttfwidth.py's row publishes a closing triple-quote as prose. Should manual.py extract the first sentence and refuse to publish a purpose that does not end in terminal punctuation, in the same block that already refuses to publish an invented gate?

manual.py exists because hand-written facts 'were right on the day they were typed', and it declares this table unable to drift. But derived describes where the text came from, not whether it is intact. A truncation is hashed into inputs-digest, so --check reports 'in sync' over it forever - the same close-over-your-own-defect shape that forced #071's proof from a grep to a fixture. This session repaired the fourth instance (plate_packet.py) by hand at the source; the extractor was not touched, so the next wrapped docstring reintroduces it silently.

**Recommendation:** Parse with ast.get_docstring, take text up to the first sentence terminator, and add truncated-purpose to the existing pre-publish refusal at manual.py:1205 - no new script, no new caller, no corpus word

**Checked:**

```
python3 -c "import sys;sys.path.insert(0,'scripts');import manual;print([s['purpose'] for s in manual.read_scripts() if not s['purpose'].endswith(('.','!','?'))])" -> 3 of 32 non-terminal: land.py, toolcheck.py, ttfwidth.py. Published now at docs/manual.html lines 556, 573, 574. Extractor is scripts/manual.py:326 m = re.search(r'"""\s*(.+)', body) - '.' does not match a newline. python3 scripts/manual.py --check -> 'in sync' while all three are live.
```

**What unblocks this:** Whether the manual's scripts table is checked for intactness or only for provenance, and whether the three live defects are repaired at the extractor or one docstring at a time forever

**Resolution (2026-09-26 13:18):** Author: "Approved" to repairing and testing the manual descriptions. Implemented AST-based module-docstring extraction, whitespace normalization, first-sentence selection, and refusal of incomplete purposes before generation or freshness checks. Regenerated docs/manual.html. All nine focused regression cases fail on the pre-fix extractor and pass on the repaired code. The completion condition now executes those cases and checks the generated manual, replacing the empty-directory test. Validation limitation: python3 tests/run.py stops in the existing plate checker on missing /usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf; no full-suite pass claimed.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/manual_description_cases.py && python3 scripts/manual.py --check` exits 0.

**Applied, confirmed 2026-09-26 13:18:** `python3 tests/manual_description_cases.py && python3 scripts/manual.py --check` now exits 0.
