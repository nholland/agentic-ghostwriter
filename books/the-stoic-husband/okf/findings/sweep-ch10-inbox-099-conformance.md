---
type: QA Finding
title: Existing Chapter 10 conformance questions surfaced after inbox 099
provenance: 'Isolated gw-specchecker read of the Chapter 10 outline and edited prose, 2026-10-02; Publisher triage against the pre-edit snapshot.'
audit: sweep
severity: significant
status: open
chapter: 10
chapter_slugs: [boundaries-are-strength]
timestamp: 2026-10-02
---

# Finding status

These are provisional review findings, not an author-approved request to rewrite.
Inbox 099's two approved local replacements are applied. The cold review at
runs/ch10/conformance-inbox-099.md returned 21/25 PASS. It marked four rows FAIL:

- Whether the existing “Mine are simple” list of agreements counts as an
  additional personal story. The checker explicitly calls this uncertain.
- The existing Pillemer attribution does not name the Cornell Marriage Advice
  Project commissioned in the outline.
- It could not establish word count. The Publisher's counted script resolves
  this row: 2,584 prose words against the outline's 2,400–2,700 target.
- The existing ending does not supply the commissioned bridge to unchosen
  burdens and necessary speech.

It also records five attribution questions about the existing Epictetus biography,
Brown formulation/account, Pillemer study identification and Tawwab guidance.
These need comparison with the citation apparatus; the clean-room checker had
only outline and prose, not the OKF or source record. No source status is changed.

# Triage and scope

The personal agreements, Pillemer material, ending and attribution passages
are present in the pre-edit snapshot, runs/ch10/refined-before-inbox-099.md.
The reader-facing closing paragraph is byte-identical before and after the two
replacements. The reviewed application of Enchiridion 30 passed. These concerns
are separate from the approved local corrections and remain for later author
scope review in the earlier-book backlog, inbox 101. No wider rewrite is authorized.
The unsuccessful overall conformance attempt is recorded in runtime handoff.

# Related

- [Boundary vs. Preference](/frameworks/boundary-vs-preference.md)
