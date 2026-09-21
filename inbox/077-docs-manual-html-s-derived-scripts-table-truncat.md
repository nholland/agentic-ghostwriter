---
id: 077
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 01:14
applied_by: test -d tests/fixtures/docstrings
---

# docs/manual.html's derived scripts table truncates each cell at the first PHYSICAL line of the module docstring, not the first sentence, so three live rows publish mid-sentence and ttfwidth.py's row publishes a closing triple-quote as prose. Should manual.py extract the first sentence and refuse to publish a purpose that does not end in terminal punctuation, in the same block that already refuses to publish an invented gate?

manual.py exists because hand-written facts 'were right on the day they were typed', and it declares this table unable to drift. But derived describes where the text came from, not whether it is intact. A truncation is hashed into inputs-digest, so --check reports 'in sync' over it forever - the same close-over-your-own-defect shape that forced #071's proof from a grep to a fixture. This session repaired the fourth instance (plate_packet.py) by hand at the source; the extractor was not touched, so the next wrapped docstring reintroduces it silently.

**Recommendation:** Parse with ast.get_docstring, take text up to the first sentence terminator, and add truncated-purpose to the existing pre-publish refusal at manual.py:1205 - no new script, no new caller, no corpus word

**Checked:**

```
python3 -c "import sys;sys.path.insert(0,'scripts');import manual;print([s['purpose'] for s in manual.read_scripts() if not s['purpose'].endswith(('.','!','?'))])" -> 3 of 32 non-terminal: land.py, toolcheck.py, ttfwidth.py. Published now at docs/manual.html lines 556, 573, 574. Extractor is scripts/manual.py:326 m = re.search(r'"""\s*(.+)', body) - '.' does not match a newline. python3 scripts/manual.py --check -> 'in sync' while all three are live.
```

**What unblocks this:** Whether the manual's scripts table is checked for intactness or only for provenance, and whether the three live defects are repaired at the extractor or one docstring at a time forever
