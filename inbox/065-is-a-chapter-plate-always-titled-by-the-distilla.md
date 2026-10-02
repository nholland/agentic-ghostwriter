---
id: 065
status: resolved
raised_by: gw-panel
chapter: -
opened: 2026-09-20 17:46
resolved: 2026-10-01 16:23
okf_receipt: runs/reconciliation/2026-10-01-inbox-065.json
---

# Is a chapter plate always titled by the distillation's Mechanism? Ten of twelve are; Ch7 (Small Rocks, Big Rocks) and Ch12 (The Muscle You Stopped Using) were not.

The Reader Panel's review (runs/design/2026-09-20-plate-reader-review.md) rates both off the mark and says this one ruling closes two of its top three findings. The Designer raised the same in runs/ch07/plate-notes.md. Round 2 retitles both to the Mechanism as drafts; your word makes it the rule.

**Recommendation:** Yes: the title is the Mechanism line, word for word.

**Checked:**

```
grep -h '^\*\*Mechanism:' books/the-stoic-husband/chapters/ch*/distillation.md against grep -o 'aria-label="[^"]*"' runs/ch*/plate.svg at round 1: 10 match, ch07 and ch12 do not.
```

**What unblocks this:** Whether the Designer's brief says 'title = the distillation's Mechanism line' and whether Ch7 and Ch12 land under their new titles.

**Resolution (2026-10-01 16:23):** yes
