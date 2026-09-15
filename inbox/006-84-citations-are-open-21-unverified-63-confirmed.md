---
id: 006
status: ruled
raised_by: gw-factchecker
chapter: 0
opened: 2026-09-15 10:17
resolved: 2026-09-15 10:17
applied_by: test $(python3 scripts/citations.py --json | python3 -c 'import json,sys;d=json.load(sys.stdin);print(d["counts"]["open"]+d["counts"]["overclaim"])') -eq 0
---

# 84 citations are open - 21 unverified, 63 confirmed but not by you

This does not block anything. The gate reports and the book proceeds. Say 'citations' for where everything stands, or 'citations 12' for one chapter. The manifest is the book repo's generated citation-queue.md. Close them however suits you: your own copy, internet research, or a deep-research pass with another agent. Anything that fits neither, park it.

**Recommendation:** Work them down at your own pace. Nothing waits on this.

**Checked:**

```
python3 scripts/citations.py -> 89 total: 84 open, 1 overclaim, 4 settled. Cross-checks against the book's own generated citation-queue.md (21 unverified, 63 verifiable, 2 verified, 3 superseded).
```

**What unblocks this:** Nothing. A standing count, not a gate. It closes itself when nothing is left open or overclaiming.

**Resolution (2026-09-15 10:17):** Standing item. Citations are tracked, never blocking.

**Not applied yet.** This ruling lands outside this repo. It closes when `test $(python3 scripts/citations.py --json | python3 -c 'import json,sys;d=json.load(sys.stdin);print(d["counts"]["open"]+d["counts"]["overclaim"])') -eq 0` exits 0.
