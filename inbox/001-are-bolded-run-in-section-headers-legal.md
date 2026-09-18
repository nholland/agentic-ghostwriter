---
id: 001
status: resolved
raised_by: gw-lineeditor
chapter: 0
opened: 2026-09-12 21:12
resolved: 2026-09-14 12:33
applied_by: grep -qi 'run-in' /home/user/playground-260420/books/the-stoic-husband/01-voice.md
---

# Are bolded run-in section headers legal?

voice_check.py flags every numbered chapter: ch01 5, ch05/ch10/ch11 5, ch09 4 bolded run-in headers on their own line. 01-voice.md caps bold at one genuine pull-quote. Prologue and Introduction use none.

**What unblocks this:** A ruling: either the cap allows run-in headers as structure, or the chapters need a pass.

**Resolution (2026-09-14 12:33):** legalize them

**Reopened as RULED (2026-09-15).** The ruling above was recorded and never applied: the voice spec states the run-in header exemption voice_check.py already enforces is still not true on disk. Closing an item cannot mean the author said something; it has to mean the thing is true.

**Applied, confirmed 2026-09-18 19:24:** `grep -qi 'run-in' /home/user/playground-260420/books/the-stoic-husband/01-voice.md` now exits 0.
