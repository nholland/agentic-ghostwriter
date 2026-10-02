---
id: 056
status: resolved
raised_by: gw-designer
chapter: 1
opened: 2026-09-20 16:33
resolved: 2026-10-01 22:59
applied_by: python3 -c "from pathlib import Path; paths=['books/the-stoic-husband/design/plates/three-second-window.svg','runs/ch01/plate.svg']; assert all('aria-label=\"The Gap\"' in Path(p).read_text() and '>THE GAP</text>' in Path(p).read_text() for p in paths); s=Path('books/the-stoic-husband/design/plates/README.md').read_text(); assert '**The Operating System** is an inline visual.' in s"
okf_receipt: runs/reconciliation/2026-10-01-inbox-056.json
---

# Chapter 1 has two plates that both draw The Gap (three-second-window, the-operating-system). Which is Ch1's plate, and what becomes of the other?

The one-plate-per-chapter rule. Inbox #015 and #019 raised it; #019's resolution answered only the Ch12 half. Today's PDF carries three-second-window as Ch1's plate (its subtitle is the conversation sentence verbatim). the-operating-system draws the route the impression takes, overflows its right margin and carries an em-dash; its concept's chapter_slugs name three chapters.

**Recommendation:** Ch1 = the window; reclassify the-operating-system as a framework explainer and fix its margin and em-dash when it is next touched.

**Checked:**

```
runs/design/2026-09-20-plate-review.md R1; runs/ch01/plate-notes.md. python3 runs/design/svgcheck.py books/the-stoic-husband/design/plates/the-operating-system.svg -> MARGIN y=170.0 'AUTOMATIC RESPONSE' 468..634 (right bound 616).
```

**What unblocks this:** Which file lands as Ch1's plate; whether the-operating-system is retired, redrawn, or reclassified as a framework explainer.

**Resolution (2026-10-01 22:59):** Approved

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 -c "from pathlib import Path; paths=['books/the-stoic-husband/design/plates/three-second-window.svg','runs/ch01/plate.svg']; assert all('aria-label=\"The Gap\"' in Path(p).read_text() and '>THE GAP</text>' in Path(p).read_text() for p in paths); s=Path('books/the-stoic-husband/design/plates/README.md').read_text(); assert '**The Operating System** is an inline visual.' in s"` exits 0.

**Applied, confirmed 2026-10-01 22:59:** `python3 -c "from pathlib import Path; paths=['books/the-stoic-husband/design/plates/three-second-window.svg','runs/ch01/plate.svg']; assert all('aria-label=\"The Gap\"' in Path(p).read_text() and '>THE GAP</text>' in Path(p).read_text() for p in paths); s=Path('books/the-stoic-husband/design/plates/README.md').read_text(); assert '**The Operating System** is an inline visual.' in s"` now exits 0.
