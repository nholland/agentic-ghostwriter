# Archivist review — Chapter 13 author-review package

Proposed record only. No house rules, FINDINGS ledger, manuscript, or inbox items changed by this desk.

## Scope and evidence limits

Neither `.claude/state/retro-window` nor `.claude/state/retro-last-sha` exists in this checkout. The prescribed hook window and its fallback therefore cannot be recovered. This is an explicitly scoped review of the six Chapter 13 commits **d8d3dfa..63cdffb**, supplemented by the author exchanges supplied to the desk. It is not a claim that the automatic retrospective hook ran. `runs/log.md` ends with a Chapter 11 entry and contains no derived Chapter 13 session entry; git history is the evidence for this window.

Read the complete `FINDINGS.md` and `.claude/LEARNINGS.md`, the scoped `git log --stat`, substantive chapter/outline/helper/inbox diffs, current chapter review artifacts, plate history and final gates, and the chapter/refine/plate/QA instructions. Inbox #093 is resolved in the author's words; #094–#102 preserve his explicit decision to defer earlier-book consistency work. No independent new source audit or complete reread of Chapters 1–12 was performed for this retrospective.

## Proposed FINDINGS entry

### 2026-09-23 07:39 — Chapter 13 completed; the author still had to manage the review boundary

Chapter 13 reached an author-reading package with refined prose, practices, a revised plate, source audit, conformance, and final persona and qualitative reads. It has no author verdict and has not landed. The useful finding is that the author had to ask whether the Designer had been consulted and whether the personas and cross-book coherence review had happened. Those questions should have been answered by the Publisher's account of completed work and remaining scope.

**What broke, with the distinction that matters.** The first plate work was prepared before dispatching the Designer; the Publisher acknowledged that and then ran the desk. The design workflow already called for that desk. No new desk was missing. Likewise, a plate-only Panel pass could never stand for a chapter persona review. However, chapter personas and cross-book review are not actually stages in the current `gw-chapter` sequence: `gw-qa` owns them separately. Calling their absence a violation of a mandatory chapter gate would rewrite the evidence. The author exposed an orchestration and expectation gap, and the requested reviews then found real older-book issues. The initial plate delivery was explicitly provisional, so this record does not falsely turn that delivery into a claim that the whole chapter was ready. It was too early for an all-work-complete reading handoff; the later readiness report properly says why.

This matches **FINDINGS, 2026-09-13, “Five questions, one finding about the visuals”**: cross-chapter coherence existed but the author could not tell where it happened. It also matches the **2026-09-01 LEARNINGS** account of artifacts serving the builder instead of the person operating through chat. The cost was author attention and extra coordination, not missing capability.

**What was too hard.** A draft-stage plate needed a manual provisional brief because the ordinary generator correctly required refined prose and distillation. The chapter had an unresolved outline ranking, and the author independently requested the plate. Keeping that prototype visibly provisional was an honest exception; inventing refinement artifacts would have been a false completion. The final package later regenerated the brief from real refined sources and replaced the draft-only takeaway. Local font and rendering paths also required helpers. The PDF renderer wrote a file but timed out during shutdown. The readiness report distinguishes that nonzero command result from the separately inspected artifact. This is environment friction, not evidence of a clean renderer run.

**What the checks missed.** The first cold-reviewed plate still felt visually right-heavy to the author and needed arrowheads and the house-style takeaway separator. Mathematical centering and a stranger's semantic read did not establish visual balance or the author's preferred carrier. The explicit author revision fixed those points and received another independent read. That does not make the earlier checks fraudulent; it defines their practical limit. The existing plate instructions already require comparison with the house style and a visual inspection. More checklist prose is not the remedy demonstrated here.

**What worked.** Conformance did not quietly certify the unsupported “most common and costly” ranking. #093 preserved it for a ruling; the author removed the ranking while retaining costly neglect and sustained effort. The outline and refined chapter now reflect that distinction. The reviewer roles remained separate: counted checks, clean-room conformance, qualitative reading, source audit, and simulated audience response addressed different questions. Explicitly hypothetical scenes preserved the author-biography boundary. The wider reviews produced actionable findings, and #094–#102 preserve them without forcing unrelated repairs into Chapter 13. This follows the author's direction rather than calling deferred defects fixed.

**Assessment.** The chapter package is ready for author feedback within its stated scope. Whole-book coherence remains open, and the renderer shutdown problem remains real. Preserve those distinctions. No house-rule addition or new desk is proposed from this window; the demonstrated immediate repairs are already in the package or in the author's deferred inbox.

## Suggestions

**None requiring a new ruling or implementation.** Zero proposed rule-corpus words; nothing to price, replace, or delete. No inbox proposal commands are supplied or executed because this review proposes no new work. Requiring a fresh whole-book audit at every chapter would be a substantial workflow choice unsupported by this single scope decision. Adding a new readiness checklist would duplicate existing stage requirements without proving that it prevents the Publisher from reporting too early.

Do not open duplicate items for the older-book findings or redesign the renderer during this chapter wrap-up. Existing #081 already records the grounding check's overbroad brief corpus; its green row is not proof that every possible phrase is chapter language. Final plate provenance was also read against actual chapter prose in this session. Existing #073 concerns renderer portability/parity but does not claim to fix this Mac shutdown timeout. Neither is silently closed here.

## Checked and found clean, and what that means

- The final readiness statement names its review coverage, deferred older-book issues, unverified author-copy status, and renderer timeout. It does not certify the entire book.
- The author-approved outline diff retains “costly mistake” and adds sustained effort; it does not erase his underlying argument.
- Final reports distinguish the mechanical 1,176-word prose count from conformance's 1,183 including headings. This is a declared counting convention, not a hidden disagreement.
- The final conformance artifact contains ten PASS requirement rows. The archived gate output reports `inbox: 0 open, 1 resolved` for Chapter 13; earlier-book deferrals are separately scoped.
- The helper imports the house renderer and assembly functions rather than copying another stylesheet. Its machine-specific paths limit portability, but no production renderer rewrite was smuggled into the chapter work.
- No author verdict or book landing was manufactured. This retrospective reviews the production record; it does not replace the author's reading or repeat the PDF's visual inspection.
