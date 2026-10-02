---
id: 116
status: resolved
raised_by: gw-factchecker
chapter: 2
opened: 2026-10-02 11:46
resolved: 2026-10-02 22:28
applied_by: ! grep -q "wishes to give calm" books/the-stoic-husband/chapters/ch02/refined.md
okf_receipt: runs/reconciliation/2026-10-02-ch02-seneca-quote-removed.json
---

# Chapter 2 prints a Seneca quotation that is not in De Ira. How do you want the line handled in the chapter?

Ch2 (landed, chapters/ch02/refined.md line 64) prints: "Reason wishes to give calm to our emotions, not to root them out," attributed to Seneca, De Ira. The Fact-Checker read all of De Ira in Latin (Basore, on Perseus) and in Stewart's English (1889) and L'Estrange: the line is in neither. Its only source is a 2025 Psychology Today article by Kruse. Worse, De Ira argues the opposite: I.7 reports 'temper anger, don't remove it' as others' view and rejects it; III.42 ends 'Let us not moderate anger, but get rid of it altogether.' The chapter's real point (governing is not numbness) still stands without it. Nothing from Ch2 has been posted with this line: Substack/social draft 04 uses it and is blocked. Options: A) quote the real Stewart II.3 sentence about anger under reason's control (anger only, not 'emotions'); B) quote the real II.2 'first movement' passage, though Ch4 already leans on De Ira; C) drop the quotation and the attribution and keep 'Not suppress. Not eliminate. Calm.' as your own words. Full report: runs/ch02/seneca-calm-not-root-out-factcheck.md.

**Recommendation:** C: drop the quotation and the Seneca attribution, keep the line as your own words. Lowest risk, needs no new source, and does not add to Seneca's cap across chapters.

**Checked:**

```
runs/ch02/seneca-calm-not-root-out-factcheck.md
```

**What unblocks this:** A ruling on the Ch2 line (a /gw-edit 2 change), then Substack post 04 can be rebuilt and the citation concept and two frameworks repointed.

**Resolution (2026-10-02 22:28):** Author: "C" (drop the quotation and the Seneca attribution; keep the line as his own words). Applied to chapters/ch02/refined.md; concept marked defect/do-not-quote; downstream notes listed in quality/citation-defects.md as still open.

**Not applied yet.** This ruling lands outside this repo. It closes when `! grep -q "wishes to give calm" books/the-stoic-husband/chapters/ch02/refined.md` exits 0.

**Applied, confirmed 2026-10-02 22:28:** `! grep -q "wishes to give calm" books/the-stoic-husband/chapters/ch02/refined.md` now exits 0.
