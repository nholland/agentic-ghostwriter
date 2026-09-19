---
id: 038
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 06:29
applied_by: python3 tests/run.py
resolved: 2026-09-19 06:29
---

# GAPS.md carried the ttfwidth hardcoded-path bug only as a sentence telling the next reader to check before assuming - replace it with a fixture that catches the pattern generally (a hardcoded absolute literal in sys.path.insert)?

The prose note relies on memory; a fixture doesn't. 10 tracked scripts already use the HERE-based idiom (sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))) that replaced the bug in runs/design/svgcheck.py.

**Recommendation:** grep every tracked .py file for sys.path.insert(0, '<absolute literal>'); mutation-test against both the exact old bug (must catch) and the HERE-based fix (must not flag)

**Checked:**

```
python3 tests/run.py -> sys_path_hardcode_cases(): 3/3 pass, including reintroducing svgcheck.py's old '/tmp/claude-0' line into a string and confirming the pattern flags it
```

**What unblocks this:** the next hardcoded-path import is caught by tests/run.py instead of relying on a reader noticing the sentence in GAPS.md

**Resolution (2026-09-19 06:29):** Approved by the author, applied directly.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-19 06:29:** `python3 tests/run.py` now exits 0.
