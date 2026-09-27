---
id: 075
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 01:10
retired_applied_by: test -d tests/fixtures/plate-names
resolved: 2026-09-25 23:30
---

# plate_packet.py pins plate titles to one hard-coded dated file (runs/design/2026-09-20-plate-names-and-visual-summaries.md) and falls back silently to 'Chapter N' for any chapter missing from it. Should curated_names() take the newest runs/design/*-plate-names-and-visual-summaries.md and refuse a silent fallback, proved by a two-dated-docs fixture?

#065, #069 and #070 are all open proposals to retitle or redraw plates. The next naming pass lands a new dated file beside the old one; the old one still exists and still parses, so the packet keeps yesterday's titles and says nothing. A missing plate prints MISSING; a missing title prints a page headed 'Chapter 5'. This is the one artifact built to go to strangers.

**Recommendation:** Glob newest-wins, and print MISSING-TITLE and exit non-zero rather than falling back - the same loudness chapter_plate() already gets

**Checked:**

```
curated_names() resolves 12/12 today: ch01..ch12 all named, all Mechanism/Conversation/Lesson fields non-empty - so this is latent, not live. The pin is scripts/plate_packet.py:45-46 NAMES_DOC = os.path.join(REPO,'runs','design','2026-09-20-plate-names-and-visual-summaries.md'); the silent fallback is line 186 title = names.get('ch%02d' % n, 'Chapter %d' % n). ls runs/design/ shows four 2026-09-20-* documents already, one naming pass in. curated_names() also already carries one unproven scar: Ch5's extra italic naming-note paragraph broke the first parse, fixed by a last-non-blank-line heuristic with no stored fixture.
```

**What unblocks this:** Whether the packet's titles follow the latest naming pass automatically, or the author has to remember to edit line 45 after every retitle

**Resolution (2026-09-25 23:30):** Author: "Approved" to the recommendation to close #073, #075, #057 and #069 as superseded. scripts/plate_packet.py now reads maintained runs/design/plate-briefs.md and rejects missing SVGs or briefs. The old dated-title lookup and fallback have been replaced; the original newest-dated-file proposal is not claimed implemented. Evidence: runs/qa/2026-09-25-inbox-audit.md; source presence rechecked at closure. The obsolete implementation-specific applied_by command is preserved as retired_applied_by; it is not a completion condition for this author-approved retirement.
