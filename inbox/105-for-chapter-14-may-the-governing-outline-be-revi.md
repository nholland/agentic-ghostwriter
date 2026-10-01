---
id: 105
status: resolved
raised_by: gw-ghostwriter plan-only gate, second failed attempt
chapter: 14
opened: 2026-09-29 23:20
resolved: 2026-09-30 17:32
applied_by: grep -Fq "Author: Yes, use the newer direction" runs/reconciliation/2026-09-30-ch14-direction.json
okf_receipt: runs/reconciliation/2026-09-30-ch14-direction.json
---

# For Chapter 14, may the governing outline be revised to center practicing enough through appreciation and gratitude, replacing the work-trip highlight-reel story and unsupported universal courtship claim?

The current approved outline conflicts with the author's later Sun-arc direction. See runs/ch14/outline-proposal.md, research.md and brief-gaps.md. The second cold brief gate failed on this unresolved specification; no outline edit or draft is authorized by the screenshot.

**Recommendation:** Revise the outline toward the author's appreciation-and-gratitude direction, retaining comparison as a brief pressure and removing the unconfirmed work-trip story.

**Checked:**

```
python3 scripts/next.py --chapter 14
ch14: next stage is concepts (3 content concept(s) proposed, waiting on your yes (proposed-concepts.md)) -> /gw-chapter 14
Cold gw-ghostwriter plan-only gate (2026-09-29): FAIL — current outline requires highlight-reel/work-trip/Epictetus commission while current brief follows later appreciation/gratitude direction; screenshot addendum introduces no new blocking research gap.
```

**What unblocks this:** Chapter 14 outline/specification and cold-draft gate

**Resolution (2026-09-30 17:32):** Yes, use the newer direction.

**Not applied yet.** This ruling lands outside this repo. It closes when `Updated books/the-stoic-husband/03-outline.md, 05-framework.md and runs/ch14/outline-section.md` exits 0.

**Resolution (2026-09-30 17:33):** Yes, use the newer direction.

**Not applied yet.** This ruling lands outside this repo. It closes when `grep -Fq "Author: Yes, use the newer direction" runs/reconciliation/2026-09-30-ch14-direction.json` exits 0.

**Applied, confirmed 2026-09-30 17:33:** `grep -Fq "Author: Yes, use the newer direction" runs/reconciliation/2026-09-30-ch14-direction.json` now exits 0.
