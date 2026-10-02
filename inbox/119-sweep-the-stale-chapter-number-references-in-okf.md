---
id: 119
status: open
raised_by: Publisher
chapter: 0
opened: 2026-10-02 08:40
---

# Sweep the stale chapter-number references in OKF notes and logs?

The outline is canonical for chapter numbers and slugs follow titles, so these do not break anything, but many OKF notes say things like 'Ch17 (the sexless marriage)' or 'Chapter 21 (betrayal)' using numbers that were already out of date before the 2026-10-02 restructure. progress.md and parking-lot.md are historical records and would not be touched.

**Recommendation:** Defer until the Chapter 17 research pass, then fix only the notes it reads.

**Checked:**

```
$ grep -rEn '\b(Ch|Chapter )(1[5-9]|2[0-3])\b' books/the-stoic-husband --include=*.md | grep -v '03-outline\|progress.md\|parking-lot.md\|okf/log.md' | wc -l
68
```

**What unblocks this:** Accurate chapter pointers in the OKF for the Desert and Orchard research passes.
