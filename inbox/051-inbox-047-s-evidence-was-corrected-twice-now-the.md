---
id: 051
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 15:09
resolved: 2026-09-26 07:47
---

# Inbox #047's evidence was corrected twice now - the first correction (fixing fabricated evidence) itself carried forward a stale SHA and a wrong date, because it reused positional reflog references (@{N}) that shift on every fetch or push, and reused a number without re-running the command. Should inbox.py --add refuse an --evidence block that cites a positional git reference (@{N}, 'the Nth entry') instead of a dated SHA?

This directly conflicts with FINDINGS 2026-09-19 07:11's decision to stop hardening the gw-retro proof-lineage rather than add another guard - so this is not a routine addition, it needs your explicit call rather than mine. The case for it: this is a different lineage (evidence content, not proof mechanics) and the failure just recurred at real cost - I (the Publisher) reproduced the exact anti-pattern while correcting the first instance of it. The case against: it is still a guard on free-text prose, and 'is this SHA actually re-measured or reused from memory' may be as undecidable as 'is this fixture about this proposal' was.

**Recommendation:** your call - I would lean toward not building this (it repeats the shape the house already declined to keep hardening), but the Archivist disagrees and the evidence for disagreement is concrete

**Checked:**

```
inbox/047's first correction (2026-09-20 ~14:24) claimed 'git rev-list --max-parents=0 main -> c74fe66' and 'main@{3}... 2026-09-20' - both wrong by the time they were written (main was d34a3ec-rooted since 2026-09-18 20:58, and the reflog position had already shifted). Corrected a second time with dated SHAs throughout, verified fresh at every line.

Corrected 2026-09-20 - dropped this item's own applied_by: true. The Archivist
found it tautological (the shell builtin true always exits 0), so the moment
this item is ruled, inbox.py's reconcile step would stamp it "confirmed
applied" before anything landed. This item asks a yes/no question with no
code artifact of its own to prove; --close --resolution alone marks it
resolved correctly without a fabricated proof command attached to it.
```

**What unblocks this:** whether inbox.py enforces dated-SHA evidence for future gw-retro items, or whether this specific recurrence is accepted as the residual cost of the 2026-09-19 07:11 decision

**Resolution (2026-09-26 07:47):** Author: "Approved" to closing #051, #052 and #085 as "additional rule declined; existing evidence requirements remain." Decline the proposed automatic restriction on Git-reference wording. Such a restriction cannot establish whether the underlying evidence is correct; existing requirements for fresh, accurate evidence remain.
