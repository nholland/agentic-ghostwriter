---
id: 083
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 12:43
applied_by: ! grep -q 'the one place words from the author' scripts/plate_brief.py && grep -q 'put his name to' scripts/plate_brief.py
resolved: 2026-09-26 13:18
---

# plate_brief.py generates 'The Author additions section is the one place words from the author's own mouth are recorded' directly above eleven briefs whose additions are another model's sentences. The per-line tag is honest; the generated sentence above them is not. Reword it to describe what the section now holds?

The brief is the artifact a cold Designer reads to learn what it may quote. It currently mis-describes its own contents in every chapter.

**Recommendation:** Reword to: 'The Author additions section records words the author has put his name to: his own, or copy from elsewhere he endorsed, each tagged with where it came from. plate_check.py's grounded row reads it, so anything here is legal plate copy.'

**Checked:**

```
wc -w: current sentence 24 words, proposed 40, net +16. Eleven briefs (ch01-06, 08-12) carry '[reader feedback, endorsed by the author 2026-09-21]' beneath the current sentence; ch07 has none.
```

**What unblocks this:** Whether endorsed third-party copy is a recognised category in the brief or an undocumented exception

**Resolution (2026-09-26 13:18):** Author: "Approved" to distinguishing the author’s words from outside wording he endorsed while preserving attribution. Corrected scripts/plate_brief.py and all 13 existing runs/chNN/plate-brief.md explanations. Every Author additions section compared byte-for-byte with HEAD and preserved. Existing dates, copy and source tags retained; no manuscript or visual changes. Validation limitation: python3 tests/run.py stops in the existing plate checker on missing /usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf; no full-suite pass claimed.

**Not applied yet.** This ruling lands outside this repo. It closes when `! grep -q 'the one place words from the author' scripts/plate_brief.py && grep -q 'put his name to' scripts/plate_brief.py` exits 0.

**Applied, confirmed 2026-09-26 13:18:** `! grep -q 'the one place words from the author' scripts/plate_brief.py && grep -q 'put his name to' scripts/plate_brief.py` now exits 0.
