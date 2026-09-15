---
id: 005
status: ruled
raised_by: gw-retro
chapter: 12
opened: 2026-09-14 11:22
resolved: 2026-09-14 14:11
applied_by: grep -q '^status: verifiable' /home/user/playground-260420/books/the-stoic-husband/okf/citations/gottman-four-horsemen.md
---

# gottman-four-horsemen.md is status: verified with evidence_source: page-text, so okf_gate blocks all prose

okf_gate.py exits 1 on okf/citations/gottman-four-horsemen.md. Only you can close a citation, against your physical copy - CLAUDE.md Rule 3. The file is in the book repo, which this engine never writes to, so the fix is yours to apply there.

**What unblocks this:** Either you confirm the quote against your own copy and evidence_source becomes author-copy, or status drops to verifiable until you can. Until one of those, /gw 12 cannot start - no desk may write prose while the gate is red.

**Resolution (2026-09-14 14:11):** Approved: status drops to verifiable. Public-source confirmation is good enough - that is the standard used for every other citation, including ones verified via external deep research. The author-copy pass stays pending.

**Reopened as RULED (2026-09-15).** The ruling above was recorded and never applied: the citation gate passes is still not true on disk. Closing an item cannot mean the author said something; it has to mean the thing is true. This closes itself when `python3 scripts/okf_gate.py` exits 0.

**Proof command corrected 2026-09-15.** It was `python3 scripts/okf_gate.py`, and the gate stopped blocking on unverified work the same day - so the item closed itself while the citation was untouched. A proof command must check the thing the ruling names, not a gate whose meaning can change underneath it.
