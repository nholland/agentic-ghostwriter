---
id: 083
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 12:43
applied_by: ! grep -q 'the one place words from the author' scripts/plate_brief.py && grep -q 'put his name to' scripts/plate_brief.py
---

# plate_brief.py generates 'The Author additions section is the one place words from the author's own mouth are recorded' directly above eleven briefs whose additions are another model's sentences. The per-line tag is honest; the generated sentence above them is not. Reword it to describe what the section now holds?

The brief is the artifact a cold Designer reads to learn what it may quote. It currently mis-describes its own contents in every chapter.

**Recommendation:** Reword to: 'The Author additions section records words the author has put his name to: his own, or copy from elsewhere he endorsed, each tagged with where it came from. plate_check.py's grounded row reads it, so anything here is legal plate copy.'

**Checked:**

```
wc -w: current sentence 24 words, proposed 40, net +16. Eleven briefs (ch01-06, 08-12) carry '[reader feedback, endorsed by the author 2026-09-21]' beneath the current sentence; ch07 has none.
```

**What unblocks this:** Whether endorsed third-party copy is a recognised category in the brief or an undocumented exception
