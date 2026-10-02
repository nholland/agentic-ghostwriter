---
id: 114
status: open
raised_by: Publisher
chapter: 14
opened: 2026-10-02 08:40
---

# Check Chapter 14's unverified details, then give the verdict?

Chapter 14 (She Is Enough) is at review in runs/ch14/refined.md (not yet landed). Before the verdict, only you can confirm: (1) the Emmons and McCullough sentence ('Across three studies, people who listed things they were grateful for reported better well-being on several, though not all, measures than comparison groups, most clearly a better mood.') against the paper at greatergood.berkeley.edu/pdfs/GratitudePDFs/6Emmons-BlessingsBurdens.pdf, including 'psychologists' and the 'most clearly a better mood' clause (search-level only); (2) the Seneca Letter 16 quotation ('Natural desires are limited; but those which spring from false opinion can have no stopping-point.') and the Letter 123 detail (poor bread, waiting for hunger) against your Gummere copy; (3) Marcus VI.48: the chapter ends the quote at 'thee.' but George Long continues after a semicolon, so keep the period as house style or end on 'thee;' with an ellipsis; (4) that you said 'we live like hoarders' to her directly; (5) 'thrifty' or 'frugal'; (6) whether to keep her line 'the best meals are the ones you don't have to cook'. Nothing is marked verified.

**Recommendation:** Read the paper and your Gummere copy, answer (3) to (6), then say 'verdict: land it' or send changes.

**Checked:**

```
$ python3 scripts/citations.py --chapter 14 | head -4
citations: chapter 14 (she-is-enough) - 21 total
   21 open        not confirmed yet. Normal; never blocks a chapter.
    0 overclaim   the status stands above the evidence.
    0 settled     your own copy, or superseded.
```

**What unblocks this:** The Chapter 14 verdict, then landing it in the book as its own commit (Rule 8).
