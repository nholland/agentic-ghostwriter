---
id: 137
status: resolved
kind: gap
trigger: built
raised_by: Publisher
chapter: -
opened: 2026-09-24 00:00
resolved: 2026-09-24 00:00
---

# PDF rendering consolidated

*Migrated 2026-10-04 from GAPS.md ('built since the audit').*

The author approved one format and stable current exports on 2026-09-24.
`chapter_pdf_local.py` is the only rendering implementation; `chapter_pdf.py`
delegates to it. WeasyPrint and its alternative stylesheet were removed.
`output/compiled/` holds current chapter, book, distillation, and plate PDFs;
its manifest records coverage and source hashes. Historical exported copies are
removed after replacement checks. Manuscript sources and reviews remain intact.

**A fifth name in this list, `ttfwidth`, turned out not to belong here at all -
checked 2026-09-19, not assumed.** `runs/design/svgcheck.py` imports it from a
hardcoded path into one prior session's scratchpad (`/tmp/claude-0/...`), which
only ever worked by accident, in whichever container happened to have a stray
copy sitting there. The module was never missing - `runs/design/ttfwidth.py`
sits right next to the script that imports it. Fixed by importing from the
script's own directory; no install of any kind involved. The shape - a
hardcoded absolute literal in `sys.path.insert()` - is no longer something a
future reader has to remember to watch for: `tests/run.py`'s
`sys_path_hardcode_cases()` greps every tracked script for it, mutation-tested
against both the exact bug (must catch it) and the fix's own `HERE`-based idiom
(must not flag it).

**What is, and is not, "environment setup."** `scripts/toolcheck.py` only ever
checks; it never installs, because there is nothing here it could install past
the network policy. Two things stay off this list on purpose: the personal MCP
connectors (Substack, Buffer) documented below under the publication stack.
Those hold the author's own account credentials - a connector he sets up
through claude.ai's connector settings or his own machine, never a package a
shared environment's startup script should be trying to configure for him.
