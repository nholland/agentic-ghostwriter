---
id: 021
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 04:59
resolved: 2026-09-18 18:34
---

# voice_rules_check.py crashes on its own NUMBER-UNCHECKED state, and one MISMATCH prints three advice paragraphs, the last of them false.

A rule declaring spec_number null - the state the code's own comment invites - raises KeyError from the mark dict on the text path. Latent today because all eight declare a number; it fires the first time a ninth rule is added, and okf_gate then blocks every prose desk. Separately, a single MISMATCH prints the advice block twice and then a DRIFT paragraph saying the spec no longer contains the wording, when the wording is present. Acting on that paragraph means updating the probe, which hides the mismatch: the gate's most important failure path prints advice that defeats the gate. Net deletion - one dict key added, seven duplicated lines removed.

**Recommendation:** Add the mark key, delete the duplicated block, gate the DRIFT text on real drift.

**Checked:**

```
spec_number removed from em_dash_max -> Traceback, KeyError: 'NUMBER-UNCHECKED'.
```

**What unblocks this:** Whether the gate Rule 8(e) rests on survives its ninth rule.

**Resolution (2026-09-18 18:34):** Fixed. Author: 'Fix both and commit!' The NUMBER-UNCHECKED mark key is added so the honest state prints instead of crashing, the duplicated MISMATCH advice block is deleted, and the DRIFT paragraph is gated on actual drift so it can no longer tell the author to update a probe in a way that would hide a mismatch. The null-spec_number case is a stored fixture.
