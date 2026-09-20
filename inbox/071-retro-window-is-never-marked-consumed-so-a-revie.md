---
id: 071
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 22:05
applied_by: grep -q retro_window.py .claude/agents/gw-retro.md
---

# retro-window is never marked consumed, so a review dispatched by the Publisher rather than the Stop hook reads a window that was already reviewed. Today it named 4ea3575..980e502 - a span containing f7736f3, the retrospective OF that span - while this session's twelve commits sat outside it. Should scripts/retro_window.py become the single oracle, deriving the bounds as end..HEAD whenever the recorded window's end is not HEAD?

Fourth instance of #030's shape and the second consecutive session where the window was correct only because the Publisher passed it by hand in the dispatch prompt. Distinct from #064, whose fix does not cover this: #064 advances START when a runs/retro/ commit falls inside the window, and f7736f3 is exactly that, so today's window is consumed under #064's own rule and the file still names it. gw-retro.md spends 103 words telling the desk to trust that file. The proposed fixture (retro_window_cases()) does not exist yet, so tests/prove.py cannot discriminate it - same wall #062-#064 hit; filed with a grep proof instead.

**Recommendation:** Yes: add scripts/retro_window.py printing START HEAD, derive end..HEAD when the recorded end is not HEAD, call it from gw-retro.md in place of the paragraph, and prove it in retro_window_cases()

**Checked:**

```
cat .claude/state/retro-window -> '4ea3575994dd9d1ad1523b6f844451fcb91d9743 980e502e2eac0d0498b26966feb681d4ea4acf44'; git log --oneline 4ea3575..980e502 -> '980e502 auto: session log 2026-09-20 19:58 / f7736f3 Archivist: retro of the plate pipeline; #062's proof corrected; #069 routes the three sweep failures / 36baf54 Reader Panel: Ch8 second cold read, PASS'; git log --oneline 980e502..HEAD | wc -l -> 13; sed -n '24,31p' .claude/agents/gw-retro.md | wc -w -> 103
```

**What unblocks this:** Whether the Archivist's bounds are computed or hand-carried, and whether gw-retro.md lines 24-31 drop from 103 words to 62
