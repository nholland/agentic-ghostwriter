---
id: 056
status: open
raised_by: gw-designer
chapter: 1
opened: 2026-09-20 16:33
---

# Chapter 1 has two plates that both draw The Gap (three-second-window, the-operating-system). Which is Ch1's plate, and what becomes of the other?

The one-plate-per-chapter rule. Inbox #015 and #019 raised it; #019's resolution answered only the Ch12 half. Today's PDF carries three-second-window as Ch1's plate (its subtitle is the conversation sentence verbatim). the-operating-system draws the route the impression takes, overflows its right margin and carries an em-dash; its concept's chapter_slugs name three chapters.

**Recommendation:** Ch1 = the window; reclassify the-operating-system as a framework explainer and fix its margin and em-dash when it is next touched.

**Checked:**

```
runs/design/2026-09-20-plate-review.md R1; runs/ch01/plate-notes.md. python3 runs/design/svgcheck.py books/the-stoic-husband/design/plates/the-operating-system.svg -> MARGIN y=170.0 'AUTOMATIC RESPONSE' 468..634 (right bound 616).
```

**What unblocks this:** Which file lands as Ch1's plate; whether the-operating-system is retired, redrawn, or reclassified as a framework explainer.
