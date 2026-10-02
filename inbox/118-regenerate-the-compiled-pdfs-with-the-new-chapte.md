---
id: 118
status: open
raised_by: Publisher
chapter: 0
opened: 2026-10-02 08:40
---

# Regenerate the compiled PDFs with the new chapter and Part titles?

The compiled book, chapter PDFs and distillations under output/compiled/ still show the old Chapter 3 title ('The Discipline of Not Reacting') and the old Chapter 14 title. /gw-compile regenerates them from the current text.

**Recommendation:** Run /gw-compile after the Chapter 13, 12 and 11 edits, so the PDFs are rebuilt once.

**Checked:**

```
$ grep -c 'Discipline of Not Reacting' output/compiled/assets/manuscript.md
2
```

**What unblocks this:** Reader-facing PDFs that match the outline.
