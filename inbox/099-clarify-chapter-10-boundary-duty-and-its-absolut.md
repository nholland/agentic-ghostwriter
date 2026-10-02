---
id: 099
status: resolved
raised_by: Publisher
chapter: 10
opened: 2026-09-23 06:53
resolved: 2026-10-02 00:29
applied_by: python3 -c 'from pathlib import Path
import re
packet=Path('"'"'runs/qa/2026-09-27-inbox-098-099-proposal/proposal.md'"'"').read_text()
section=packet.split('"'"'## ch10\n'"'"',1)[1].split('"'"'## Scope and review notes'"'"',1)[0]
pairs=re.findall(r'"'"'\*\*Before\*\*\n\n(.*?)\n\n\*\*Proposed\*\*\n\n(.*?)(?=\n\nReplace|\Z)'"'"',section,re.S)
s=Path('"'"'books/the-stoic-husband/chapters/ch10/refined.md'"'"').read_text().split("## Editor'"'"'s Notes",1)[0]
assert len(pairs)==2
assert all(old.strip() not in s and s.count(new.strip())==1 for old,new in pairs)
'
okf_receipt: runs/reconciliation/2026-10-02-inbox-099.json
---

# Clarify Chapter 10 boundary duty and its absolute claim that damage cannot repair?

Affected scope: Ch10; continuity with Prologue, Ch4 and Ch11. User explicitly deferred these findings: "Add the consistency items to the inbox, we can address those later." This is a later author-ruling backlog only. No manuscript changes are authorized now; this item does not block Chapter 13. Evidence below is the exact review-report excerpt, not a claim of a new independent manuscript audit.

**Recommendation:** Clarify that maintaining his own code against retaliation does not require accepting repeated violations; author should supply the intended concrete response and scope. Replace the absolute no-repair claim with trust that may take years to rebuild, consistent with later repair work.

**Checked:**

```
$ sed -n '23,32p' runs/ch13/persona-coherence-ch01-ch13.md
### 2. A boundary holds your conduct; the text sometimes makes that sound like accepting any conduct

**Personas:** skeptic; Paul; continuity editor. **Scope:** older-book/author decision, especially Chapter 10 “What you do to each other.” **Severity:** high.

The chapter names no physical aggression and no name-calling, then says the specific rules matter less than whether a list holds. It next asks what happens when *she* crosses the list, quotes Epictetus on submitting to a father, says the reasoning carries “straight over,” and concludes “You hold it anyway.” The intended instruction is clear in the surrounding philosophy: her wrongdoing does not authorize his. The dangerous alternative reading is also available: being a good husband means continuing to receive mistreatment because the relationship itself fixes his duty.

The Prologue says a marriage takes two and Chapter 11 says refused counseling matters, so the book has not simply endorsed unilateralism. But neither statement supplies the missing distinction here. A personal code against retaliation and a response to another person's repeated violation are different decisions. The current transition skips the second.

**Cost of fixing:** small local clarification that holding his own standard does not require accepting the violation, with one concrete action consistent with the author's intended scope; author should settle the scope before broader treatment. This need not preempt Chapter 23's decision about leaving. No generic disclaimer and no Chapter 13 repair required.

$ sed -n '46,49p' runs/ch13/slop-coherence-ch01-ch13.md
### 8. Medium — repair versus permanence, Ch4 / Ch10 / Ch11

Exact Ch10 lines 98–99: “What the list protects is the part of a marriage that doesn't repair.” Ch4 describes incidents “that were never quite fully repaired”; Ch11 allows apology, repeated conversation, and help. Remembering harm is not the same as being unable to repair it. The absolute makes the book's repair work sound futile. **Fix:** “The list protects trust that can take years to rebuild.” Keep the warning without deciding every damaged marriage's future.
```

**What unblocks this:** Author ruling on boundary-response scope, then separate local Ch10 edits. Deferred; Chapter 13 can proceed.

## Approved revision scope; exact proposal ready — 2026-09-27

The author said “Approved” after the recommendation to prepare focused revisions. Exact proposed wording is in [the review packet](../runs/qa/2026-09-27-inbox-098-099-proposal/proposal.md), with full chapter previews, a patch, and counted-check outputs. This implements the promised review-before-application step; proposed prose is not yet in the book. No cold desk review was performed.

**Resolution (2026-10-02 00:29):** Approved

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 -c 'from pathlib import Path
import re
packet=Path('"'"'runs/qa/2026-09-27-inbox-098-099-proposal/proposal.md'"'"').read_text()
section=packet.split('"'"'## ch10\n'"'"',1)[1].split('"'"'## Scope and review notes'"'"',1)[0]
pairs=re.findall(r'"'"'\*\*Before\*\*\n\n(.*?)\n\n\*\*Proposed\*\*\n\n(.*?)(?=\n\nReplace|\Z)'"'"',section,re.S)
s=Path('"'"'books/the-stoic-husband/chapters/ch10/refined.md'"'"').read_text().split("## Editor'"'"'s Notes",1)[0]
assert len(pairs)==2
assert all(old.strip() not in s and s.count(new.strip())==1 for old,new in pairs)
'` exits 0.

**Applied, confirmed 2026-10-02 00:29:** `python3 -c 'from pathlib import Path
import re
packet=Path('"'"'runs/qa/2026-09-27-inbox-098-099-proposal/proposal.md'"'"').read_text()
section=packet.split('"'"'## ch10\n'"'"',1)[1].split('"'"'## Scope and review notes'"'"',1)[0]
pairs=re.findall(r'"'"'\*\*Before\*\*\n\n(.*?)\n\n\*\*Proposed\*\*\n\n(.*?)(?=\n\nReplace|\Z)'"'"',section,re.S)
s=Path('"'"'books/the-stoic-husband/chapters/ch10/refined.md'"'"').read_text().split("## Editor'"'"'s Notes",1)[0]
assert len(pairs)==2
assert all(old.strip() not in s and s.count(new.strip())==1 for old,new in pairs)
'` now exits 0.
