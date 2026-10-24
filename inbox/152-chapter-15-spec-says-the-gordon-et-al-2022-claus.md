---
id: 152
status: open
raised_by: gw-specchecker
chapter: 15
opened: 2026-10-24 03:57
---

# Chapter 15 spec says the Gordon et al. 2022 clause is 'relief plus appreciation'. The study as researched says an unfair housework split goes with lower satisfaction except where the partner feels appreciated. Which wording governs?

Row 40 of the round-2 conformance check failed. The outline (03-outline.md, Ch15 research burden) says 'relief plus appreciation (Gordon et al. 2022)'. The draft prints the researched finding, nearly word for word from research.md F1, and says the study was about whoever does the housework, not about a husband who helps. Relief is not Gordon's finding. Same pass: the spec says 'clauses'; each study is one sentence plus his reading.

**Recommendation:** Keep the draft as written and change the outline line to the researched finding at the verdict; 'relief' would put a claim in Gordon's mouth the study does not make.

**Checked:**

```
grep -n 'relief' runs/ch15/draft.md -> no match; outline line 392: 'At most two research clauses: relief plus appreciation (Gordon et al. 2022) and motive (Impett et al. 2005).'; draft line 37: 'A 2022 study by Gordon and colleagues found that doing more of the housework, and feeling the split was unfair, went with lower satisfaction in the relationship, except among people who felt appreciated by their partner.'
```

**What unblocks this:** Whether /gw-revise outline changes the spec wording to the researched finding (recommended), or the draft is changed to say 'relief'
