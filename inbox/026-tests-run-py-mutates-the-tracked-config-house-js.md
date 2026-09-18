---
id: 026
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 18:45
resolved: 2026-09-18 19:22
applied_by: python3 tests/run.py
---

# tests/run.py mutates the tracked config/house.json. Move it to a tmpdir copy so a killed test cannot block every prose desk?

Killed between a mutation and its restore, it leaves em_dash_max at 7.0 and okf_gate.py then prints BLOCKED, do not write prose. It also leaves config/house.json.testbak behind, which .gitignore does not cover, so recovery depends on knowing the backup exists. Two concurrent runs corrupted house.json twelve times out of twelve. Restore-on-exception and byte-identity are both correct when the finally block runs; the failure is only when it does not. The whole run takes 0.297s and has no reason to touch a tracked file.

**Recommendation:** Copy scripts/ and config/ to a tempfile.mkdtemp(), mutate there, pass GW_BOOK_REPO explicitly, rmtree in finally. 98 words, deletes the twelve-line backup block.

**Checked:**

```
Killed mid-run: em_dash_max 7.0, testbak present, okf_gate BLOCKED. 12 paired concurrent runs corrupted house.json on all 12.
```

**What unblocks this:** Whether the Stop hook can leave the engine unable to write prose.

**Resolution (2026-09-18 19:22):** Apply all four (Recommended)

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-18 19:22:** `python3 tests/run.py` now exits 0.
