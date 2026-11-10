---
id: 169
status: resolved
raised_by: Publisher
chapter: 0
opened: 2026-11-10 03:45
resolved: 2026-11-10 04:12
applied_by: python3 tests/run.py
okf_receipt: runs/reconciliation/2026-11-10-inbox-169.json
---

# Fix voice_check.py's sentence splitter so abbreviations like 'al.' and 'No.' only match as whole words?

Found by the batch-5 Line Editor and confirmed by the Archivist's pre-commit review (2026-11-10); filed on the author's 'File it'. voice_check.py applies its ABBREV list with plain str.replace, so 'al.' matches the end of usual./real./signal. and a standalone 'No.' is treated as an abbreviation. Those sentences get merged with the next one, which inflates average sentence length and the long-sentence share (a HARD check). It can only cause false FAILs, never hide a real violation; it did nudge a few batch-5 rewordings.

**Recommendation:** Match ABBREV entries only on word boundaries (regex), and add a regression fixture under tests/ for the sentence below that fails on today's code and passes after the fix.

**Checked:**

```
python3 -c "import sys; sys.path.insert(0,'scripts'); import voice_check as v; print(v.sentences('That was usual. She left. It was real. No. Then he spoke.'))" -> ['That was usual. She left.', 'It was real. No. Then he spoke.'] (2 sentences; expected 5)
```

**What unblocks this:** Accurate sentence statistics and long-sentence counts for every chapter, including the batch-5 register pass

**Resolution (2026-11-10 04:12):** Fixed in d74c090: word-boundary matching for ABBREV, 'No.' only before a number; fixtures in tests/run.py (old code: 2 sentences, new: 5).

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-11-10 04:13:** `python3 tests/run.py` now exits 0.
