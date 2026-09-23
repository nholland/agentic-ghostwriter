# Chapter 11 revision verdict

Date: 2026-09-22 22:48

The author reviewed the plain-language draft, requested the seagull paragraph be replaced with explicit behavior, then requested the distillation in the PDF. After receiving the complete eight-page PDF, the author said:

> Nice work. Commit to main. Let's see what Archivist thinks

Verdict: approved for landing. Source: plain-language-draft.md (prose before Editor's Notes), plain-language-distillation.md, and the complete PDF delivered in this session.

Scope: replace Chapter 11 prose, distillation, its practice-guide section, and its PDF. Preserve research and citation status. Voice-constitution and desk changes remain proposals; approval of this chapter does not apply them.

Publisher handling: existing land.py re-lands unrelated staged plates and skips replacement of an existing guide section. This revision is therefore copied with unique-section assertions and checked by practice_sync.py and okf_gate.py. Only Chapter 11's section in the book guide is replaced, under gw-edit's explicit refresh instruction; the runs guide gains that section.

The existing runs/ch11/plate.svg has the same mechanism, but still says 'forty times' and 'Kindly. Once.' It was not part of the approved PDF and is not landed with this revision. No new author interview was fabricated.
