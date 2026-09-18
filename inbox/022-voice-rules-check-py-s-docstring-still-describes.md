---
id: 022
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 04:59
---

# voice_rules_check.py's docstring still describes the behaviour it had before yesterday's rewrite.

It says the check 'asserts that the phrase each threshold came from is STILL THERE' - true before 2026-09-18, false now that it compares declared numbers. It never mentions spec_number. Same shape as gw-compile's 'One renderer, not two' section that went false and was replaced this same arc: authoritative text that a change quietly invalidated, and it is the first thing a caller reads.

**Recommendation:** Rewrite the third docstring paragraph, and have it state the residual hole: three rules have digit-free probe spans, so their spec_number is hand-transcribed with nothing deriving it.

**Checked:**

```
ast.get_docstring contains no match for spec_number; the behaviour compares numbers.
```

**What unblocks this:** Whether the first thing a caller reads about the gate is true.
