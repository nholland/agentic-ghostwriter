---
id: 031
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 20:48
resolved: 2026-09-18 20:48
applied_by: python3 tests/run.py
---

# inbox.py --chapter N was accepted on read and silently ignored. Filtered, with a fixture?

render() never received the chapter; --chapter was wired to --add only. A desk asking which items a chapter raised got all items under a header claiming the whole inbox's counts - a plausible answer, no error. This is how Ch12's ledger came to carry three disagreeing counts (19, 11, 12) in one commit.

**Recommendation:** Filter on read (2 lines), fixture it isolated from the real inbox, repoint the skill's two phrases at the command.

**Checked:**

```
Before: python3 scripts/inbox.py --all --chapter 12 returned all 30 items under '27 resolved'. After: returns exactly the 12 chapter-12 items.
```

**What unblocks this:** gw-chapter/SKILL.md's verdict-package and FINDINGS steps run a command instead of recalling a list.

**Resolution (2026-09-18 20:48):** Anything else? (this session's follow-up round)

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-18 20:48:** `python3 tests/run.py` now exits 0.
