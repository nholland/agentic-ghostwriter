---
id: 052
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 15:23
---

# Should inbox.py --add refuse an --applied-by that already exits 0 at filing time? #051 was filed with --applied-by 'true' - the only tautological proof among ~50 inbox items - and inbox.py's reconcile step runs the proof the moment an item is ruled, so a yes would have stamped it 'confirmed applied' with nothing landed. Already fixed in #051 itself by dropping the line; this asks whether to guard the general case.

'true' passed every existing guard: the plain non-empty check, and the tests/run.py-specific proof-freshness check (which only fires when tests/run.py appears in the string). This is a measurement (does the command already exit 0 before any work happens), not the semantic judgment ('is this fixture about this proposal') that FINDINGS 2026-09-19 07:11 declined to keep hardening - but it is adjacent, and the Archivist itself is not certain the line holds. Recommend against building it, but the case for it is real, so leaving the call to you rather than deciding either way myself.

**Recommendation:** lean no - this is the eighth layer on a lineage the house already chose to stop hardening, and the one live instance is already fixed by hand

**Checked:**

```
grep -h '^applied_by:' inbox/*.md | sort | uniq -c -> 'applied_by: true' appeared exactly once (inbox/051), now removed
```

**What unblocks this:** whether a ruling can ever again be auto-confirmed by a proof that was green before the work started
