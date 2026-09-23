# Archivist review: Chapter 11 plain-language revision

Review window: 5de2ad0705bdbbd8eed06c9d3d049690021b855e through the Chapter 11 session artifacts and landing commit 2fd4df0. Explicit session bounds supersede any old hook window. Status: proposals only; no rule, skill, or constitution change applied.

## Proposed FINDINGS entry — 2026-09-22 22:48

The author's examples diagnosed a meaning problem that counted voice checks cannot detect: the chapter asked the reader to complete expressions, decode metaphor labels, and supply unnamed actions. The replacement explains what the husband does, avoids, and needs to discuss. Author feedback produced the improvement. The existing voice constitution already prohibited making the reader infer something the writer could name.

The first independent conformance review found 13 of 19 composite requirements met. Subsequent edits restored omitted meanings; that first result is not a final passing verdict. The author then caught another instance of the original problem, the seagull passage, after the plain-language review. Removing its label and explaining the two behaviors worked. This repeats the 2026-08-23 finding: reading for plausible rhythm and reading for actual meaning are different jobs.

The PDF introduced a separate recurrence. Its first version omitted the distillation; the author had to request its inclusion. The initial output citation also required a follow-up for a useful download link. Missing practices were already recorded on 2026-07-27 and 2026-09-10. compile.py now checks practice completeness, but this draft's ad hoc PDF assembly bypassed that path. Comparing rendered text with incomplete input can prove faithful rendering while missing part of the requested package.

What worked: the author approved the revised chapter and complete PDF; the rewrite preserved personal material and quotation wording, explained the distinctions without their old labels, and documented judgment calls. Counted checks were rerun. The permanent voice patch remained a proposal, separately from approval of the chapter.

Recommendation: keep the successful before/after examples as editorial evidence, replace the Line Editor's weak clarity instruction rather than expanding three rule files, and treat reusable draft-package assembly as an open implementation item. No recursive review round is needed.

## Suggestions, not applied

### 1. Rule edit: replace the existing Line Editor Clarity paragraph

Proposed exact replacement:

> **2 — Clarity.** One idea per paragraph. Name actions, fears, choices, and consequences. State distinctions explicitly; explain or remove metaphors. In Editor's Notes, show representative before/after repairs and flag meaning you cannot establish without invention. Apply 01-voice.md's plain-meaning rule separately from counted checks.

Archivist's wc -w measurement: 43 words replacing 26; net +17. The existing three-file proposal patch measures 1,072 added and 626 removed; net +446. The smaller replacement puts the instruction at the review stage and leaves the existing voice constitution authoritative. It does not mechanically certify semantic clarity.

Implementation proof, if authorized: compare the Clarity paragraph exactly with the proposed text, then run scripts/sync_plugin_layout.py --check. That proves installation and mirror consistency, not literary effectiveness. Do not also apply the larger pending patch. No proposal was installed or filed as approved.

### 2. Open item: reusable draft-package assembly

Unmeasured. Reuse or extend the existing assembler for explicitly requested draft packages, including full distillation when requested. Replace the ad hoc input assembly, not the established renderer. Closure requires a fixture that fails when requested distillation is absent and passes with the complete package, exercised through the actual assembly caller. No implementation or honest executable closure proof exists yet; do not file it as an implemented check or use a tautological proof.

## Reviewed and clean within scope

- The final seagull replacement directly explains both behaviors.
- Draft, distillation, and proposed practices express compatible practical distinctions.
- Generic dialogue is not presented as autobiography.
- Research descriptions are narrowed; the notes do not claim renewed source verification.
- Proposed voice changes remain unapplied.
- Existing compile completeness logic is present; another generic presence check would duplicate it.

The Archivist read FINDINGS.md and .claude/LEARNINGS.md in full, the revision artifacts, and relevant assembly code. Canonical synchronization, final PDF verification, and landing were concurrent Publisher work, not independently certified by this review. The Archivist changed no files or inbox items.

## Publisher's landing checks

Voice: all HARD checks passed on canonical Chapter 11. Practice sync: all three practices match in both runs and book trees. OKF gate: PASS. Canonical PDF: eight pages, extracted words match the complete canonical prose plus distillation in order, both existing Marcus quotation strings preserved verbatim. The PDF layout was rendered and visually reviewed during delivery. Permanent rules and the staged plate were not changed.

The whitespace checker reports blank context lines in the stored unified-diff proposal; these are patch syntax, not whitespace changes applied to the rules. The patch itself passes git apply --check and remains unapplied.
