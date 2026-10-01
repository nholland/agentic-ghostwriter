---
id: 105
status: resolved
raised_by: gw-slopreader
chapter: 13
opened: 2026-09-27 20:11
resolved: 2026-09-27 22:18
applied_by: grep -q 'Word count target:\*\* 1,500–1,800' books/the-stoic-husband/03-outline.md
okf_receipt: runs/reconciliation/2026-09-27-inbox-105.json
---

# Chapter 13's outline entry still prescribes the bridge you told me to cut, and a 1,000-1,300 word target you asked to exceed. Rewrite both?

On 9/24 you said: remove the noticing-other-women passage and do not use it as a transition; and the chapter felt short. The outline (03-outline.md, Ch13) still says the transition is 'the same brain that used to chase her is capable of chasing someone else instead', and targets 1,000-1,300 words. The revised chapter is 1,501 and the Reader Panel wants ~1,700. The prose already obeys you; only the outline disagrees.

**Recommendation:** Transition: 'Pursuit keeps a man reaching for his wife. What it can't settle is what happens when the reaching stops feeling urgent. Chapter 14 takes on contentment as something practiced rather than waited for.' Word target: 1,500-1,800.

**Checked:**

```
python3 scripts/voice_check.py runs/ch13/refined.md -> '1501 words of prose, 124 sentences'; runs/ch13/coherence-refined.md E8 quotes 03-outline.md lines 278-279
```

**What unblocks this:** 03-outline.md Ch13 transition and word target match your 9/24 ruling

**Resolution (2026-09-27 22:18):** I'm good with the updates to the outline.

**Not applied yet.** This ruling lands outside this repo. It closes when `grep -q 'Word count target:\*\* 1,500–1,800' books/the-stoic-husband/03-outline.md` exits 0.

**Applied, confirmed 2026-09-27 22:18:** `grep -q 'Word count target:\*\* 1,500–1,800' books/the-stoic-husband/03-outline.md` now exits 0.
