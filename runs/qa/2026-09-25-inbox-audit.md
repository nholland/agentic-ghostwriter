# Inbox audit — 57 pending records, 2026-09-25

Prepared by the Publisher in session. This is an Inbox audit, not a cold Archivist review. Scope: the 56 open records and one ruled record reported by inbox.py at the evidence snapshot; both records numbered 053 are included separately. No author rulings were inferred, no records closed, and no manuscript or house rules changed.

## What you need to know

The Inbox mixes old questions, unfinished implementation, policy proposals, and actual author decisions. Four requests have been superseded; three are partly completed. Many remaining records belong to the same repair. The record count is not a count of questions you need to answer.

The easiest next implementation work is duplicate-ID protection (#046), the malformed manual descriptions (#077/#080), and the misleading plate-brief explanation (#083). The most clearly already-authorized work is export consistency (#103). This audit identifies that work; it does not claim those repairs are complete.

Review the current plates together, not the successive versions described by their old Inbox headlines. All twelve current chapter draft SVGs are selected by compile.chapter_plate(), and none has an identical copy in the landed plate directory. That is file identity evidence, not proof that the author never expressed approval elsewhere. Part selection differs: the compiler prefers the landed outline path.

Only the author can supply biography (#094), set the scope of teaching about real unfairness and repeated boundary violations (#098/#099), approve changes to locked prose, and choose visual meaning. Programming details and test implementation can be handled by the Publisher. Earlier-book revisions #094–102 remain explicitly deferred until commissioned.

## Recommended work packages, easiest first

1. **Reconcile stale records.** Retire the obsolete implementation/scheduling requests #057, #069, #073, #075 on their actual replacement evidence; record separately what still needs visual approval. Complete #062’s behavioral verification before closing it. Do not use the ambiguous number 053 to close anything.
2. **Small production repairs.** Duplicate identifiers (#046); manual extraction and its proof (#077/#080); accurate attribution wording (#083). I can prepare and test these without author expertise.
3. **Reader exports.** Complete your existing sequence instruction (#103), with cropped-image and leaked-markup regression cases (#063/#072). Include checks of selected plate files (#088) and repair the local checker’s unavailable-font assumption before claiming geometry is checked.
4. **One plate review.** Present current chapter and Part drawings with plain-language intent and a recommendation. Absorb #054–061, #067–070, #084, #086–087 where relevant. Keep only remaining decisions; do not resurrect labels already removed. Coordinate Chapter 5 with #095 and Chapter 4 with #101.
5. **One concise design contract.** Combine #059/#065/#066/#089 after the visual review. Preserve current deliberate exceptions instead of adopting an old uniform-canvas proposal unchanged.
6. **One maintenance batch.** Review-window handling (#064/#071/#074/#079), new-code proof support (#048), log integrity (the log version of #053), ancestry safety (#047), grounding (#081), and render freshness (#082). These are engineering tasks; their existing proposals are not independently approved by this audit.
7. **Prune policy proposals.** Recommend no additional free-text evidence gate (#051), no universal already-green rejection (#052), keeping the reverted filer scope (the proof version of #053), and no extra command-pasting rule (#085). Consider feedback intake (#045) separately. Keep asset retention (#076) and old external publishing (#078) pending an inventory of what is still used. Avoid a specialized canyon-checker project (#090/#091) until a visual verdict establishes its purpose.
8. **One earlier-book revision commission.** Start with biography, workload fairness and boundary scope; then prepare the coordinated local edits in #094–102. Do not ask you to settle each line without a proposed before/after.

## Complete routing, with explanations

Counts below are classifications of records, not approvals or estimates of implementation time. Links open the original records, which retain their detailed evidence.

### Superseded — 4

| Record | What this means now | Recommendation / who acts |
|---|---|---|
| [#057](../../inbox/057-ch7-reuses-small-rocks-big-rocks-which-draws-wha.md) | Chapter 7’s old rocks illustration has already been replaced by The Private Tally. The current SVG labels YOUR PAGE and HER PAGE. | Retire the old reuse-versus-redraw question; review the current drawing with the other plates. Its final approval is separate. |
| [#069](../../inbox/069-three-plates-fail-the-standalone-read-ch2-ch6-ed.md) | The requested Chapter 2 and 6 edits and Chapter 5 replacement have later PASS records in their plate-read.md files. Current SVGs contain later revisions too. | Retire the scheduling question. Those historical passes do not certify every subsequent edit or author approval. |
| [#073](../../inbox/073-chapter-pdf-py-cannot-be-executed-here-so-its-cs.md) | The two independent PDF stylesheets no longer exist as described. chapter_pdf.py is now a compatibility entry point for the shared Chromium format. | Retire the proposed parity test; test the shared renderer when it changes. |
| [#075](../../inbox/075-plate-packet-py-pins-plate-titles-to-one-hard-co.md) | plate_packet.py now reads maintained runs/design/plate-briefs.md and raises on missing SVGs or briefs. The hard-coded dated title document and silent title fallback are gone. | Retire the old implementation proposal. Preserve the current maintained brief. |

### Partly completed — 3

| Record | What this means now | Recommendation / who acts |
|---|---|---|
| [#054](../../inbox/054-ch8-s-landed-tipping-scale-plate-puts-the-one-th.md) | The complaint concerns the old landed Chapter 8 scale. The current draft is a later replacement; the compiler selects that draft, which has no identical landed copy. | Show the current scale in one plate review. Do not copy it into the book on the authority of this obsolete one-fix description. |
| [#055](../../inbox/055-ch12-s-landed-plate-prints-its-gloss-no-deadline.md) | The old Chapter 12 off-page label is absent from the current replacement drawing. The compiler selects the replacement, which has no identical landed copy. | Fold into approval of the current Chapter 12 plate. The original one-line fix is no longer the whole change. |
| [#062](../../inbox/062-land-py-copies-a-chapter-plate-into-books-with-n.md) | land.py already calls plate_check and refuses FAIL rows unless --force. The requested behavior is present in code; a dedicated behavioral proof was not established in this audit. | Verify the landing behavior with a focused fixture before closing. Do not add a second landing gate. |

### Already authorized — 1

| Record | What this means now | Recommendation / who acts |
|---|---|---|
| [#103](../../inbox/103-align-all-reader-exports-to-the-approved-chapter.md) | You already specified prose, plate, then full distillation. The whole-book compiler still extracts only Practice; individual chapter rendering has adopted the sequence. | Implementation work: update assembly and regenerate affected current reader exports with visual QA. No new editorial decision needed. Not implemented by this audit. |

### Technical work — 16

| Record | What this means now | Recommendation / who acts |
|---|---|---|
| [#046](../../inbox/046-two-branches-can-allocate-the-same-inbox-number-.md) | Two live records share number 053. inbox.py still returns the first matching record when closing by number. | Repair identity handling and preserve both records and their references. Do not use --close 53. No technical choice needs the author. |
| [#047](../../inbox/047-should-sync-py-land-refuse-when-local-main-is-no.md) | The status label now correctly says origin/main, but land() still does not check local-main ancestry before checkout and merge. | Finish the missing ancestry check and prove it in a throwaway repository; no need to reconstruct the disputed historical incident. |
| [#048](../../inbox/048-tests-prove-py-cannot-prove-a-fixture-for-a-new-.md) | prove.py still requires an explicit FAIL line and reads the historical file with git show(check=True); absent new files and missing/crashing cases are not handled as proposed. | Design a focused new-code proof case. Do not accept arbitrary crashes as proof that the intended defect was caught. |
| [#053-log](../../inbox/053-log-check-s-union-invariant-the-one-its-own-docs.md) | log_check still excuses a missing heading whenever its file set survives anywhere, without requiring the same branch. The proposed lost_entries function is absent. | One focused log-integrity repair and fixture, after higher-value reader-facing work. Historical restoration needs its own evidence check. |
| [#063](../../inbox/063-svg-to-png-silently-lost-the-bottom-fifth-of-eve.md) | The request is a regression test for a previously fixed cropped image, not a request to redesign any plate. No bottom-band fixture was located in tests/run.py. | Add the small rendered-image fixture when working on exports; report unavailable rendering as unchecked, not passed. |
| [#064](../../inbox/064-retro-check-sh-overwrites-retro-window-on-every-.md) | The review hook still rewrites the recorded review window at dispatch. Its newer three-commit batching does not itself preserve unreviewed earlier work. | Combine with #071, #074 and #079 into one review-window repair, not four decisions. |
| [#071](../../inbox/071-retro-window-is-never-marked-consumed-so-a-revie.md) | The Archivist brief still tells the desk to read the window file; there is no scripts/retro_window.py oracle. | Combine with #064. Track what was actually reviewed; a newer HEAD alone must not discard an unconsumed window. |
| [#072](../../inbox/072-package-check-py-printed-ok-on-all-four-manuscri.md) | package_check still lacks a visible leaked-markup check. This is a proposed regression guard against earlier literal page-break text, not proof that current exports have that defect. | Include a small known-bad rendered-HTML case in export verification. |
| [#074](../../inbox/074-retro-check-sh-watches-inbox-and-the-archivist-s.md) | The hook batches at three watched-path commits now, but still counts Inbox changes made by retrospectives. Batching reduces frequency without excluding those commits. | Combine with #064/#071/#079; distinguish pure review output from substantive work committed alongside it. |
| [#077](../../inbox/077-docs-manual-html-s-derived-scripts-table-truncat.md) | manual.py still takes the first physical docstring line. Fresh read_scripts() output finds four malformed purposes, including the newer pdf_chapter_style.py row. | Repair extraction and verify generated descriptions. You need not decide how Python parses a docstring. |
| [#079](../../inbox/079-074-s-fix-is-right-but-its-proof-cannot-tell-the.md) | This is a better test for #074, not a separate product decision. Excluding only a directory cannot exclude the other files in the same commit. | Carry its mixed-commit case into the combined review-window repair; do not run its old worktree-mutating proof during a read-only audit. |
| [#080](../../inbox/080-075-and-077-both-close-on-test-d-a-directory-tha.md) | The old directory-exists closure commands remain. #075’s implementation has been superseded; #077’s extractor problem remains. | Use evidence of the replacement to retire #075; give #077 an actual behavior test. No extra global proof-policy guard is needed for these two records. |
| [#081](../../inbox/081-plate-check-py-appends-the-whole-plate-brief-md-.md) | A fresh call confirms plate_check still accepts “the drawing carries the argument” from the generated brief as grounded source language. | Narrow source extraction to approved content and attributed additions; preserve endorsed language. Test allowed and disallowed text. |
| [#082](../../inbox/082-the-panel-s-stale-raster-claim-was-confirmed-by-.md) | plate_check has no raster_current function. This audit did not compare current image pixels; the old report of matching images is historical. | Verify source and cached render at matching scale when preparing the next plate review. Avoid presenting a scale mismatch as staleness. |
| [#083](../../inbox/083-plate-brief-py-generates-the-author-additions-se.md) | plate_brief.py still describes additions as words from the author’s own mouth, although endorsed outside wording is allowed in these briefs. | Correct the generated explanation without changing the underlying permission or authorship tags; preserve existing additions when regenerating. |
| [#088](../../inbox/088-plate-check-only-ever-runs-on-a-source-svg-a-hum.md) | The compiler selects SVGs but does not call plate_check on those selected files. Part plates still prefer the landed outline path over drafts. | Add reporting for the actual selected files. Coordinate with #062; export reporting and landing refusal have different semantics. |

### House-policy decision — 13

| Record | What this means now | Recommendation / who acts |
|---|---|---|
| [#045](../../inbox/045-should-gw-signal-step-0-become-a-stop-condition-.md) | Reader feedback once described a different or stale chapter. Step 0 still asks for a chapter read but does not explicitly preserve the supplied feedback and stop mismatched routing. | Recommend preserving the paste and matching it before proposing edits. Approve a concise replacement to the feedback intake rule, not an entire new checker. |
| [#051](../../inbox/051-inbox-047-s-evidence-was-corrected-twice-now-the.md) | This proposes rejecting certain Git-reference wording in evidence. Its own record recommends against adding another free-text guard. | Decline the extra wording gate. Require fresh evidence in the actual review under existing rules. |
| [#052](../../inbox/052-should-inbox-py-add-refuse-an-applied-by-that-al.md) | This would reject any completion command already passing when filed, including proposals that merely ratify existing work. | Decline the universal gate. Separate evidence of present behavior from evidence that a proposed change has been applied. |
| [#053-proof](../../inbox/053-inbox-py-s-tests-run-py-proof-guard-was-widened-.md) | The proof requirement was widened to all filers and then reverted; current code remains scoped to gw-retro. | Keep the reversion. Its all-tests-pass closure command cannot prove the author ratified that policy; record an actual decision. |
| [#059](../../inbox/059-ratify-the-plate-style-spec-the-review-desk-deri.md) | The old plate README still says design-language.md does not exist. Current chapter draft canvases also differ from the original uniform-canvas proposal. | Combine with #065/#066/#089 into one short design contract based on current approved examples. Do not ratify the old measurements wholesale. |
| [#065](../../inbox/065-is-a-chapter-plate-always-titled-by-the-distilla.md) | A universal plate-title-equals-Mechanism rule remains a choice. Chapter 5 still exposes why title and distillation must be coordinated. | Recommend matching names by default with deliberate exceptions. Resolve Chapter 5 through #070/#095; review Chapter 1’s Gap/window distinction explicitly. |
| [#066](../../inbox/066-the-reader-panel-proposes-three-set-wide-rules-f.md) | This bundles copy limits, consistent visual symbols, and requiring the lesson to be drawn. Those are ongoing design standards, not three isolated corrections. | Fold into the single design contract. Prefer reader comprehension over an absolute requirement that every lesson can be diagrammed. |
| [#076](../../inbox/076-runs-manuscript-commits-29-regenerable-pngs-and-.md) | The snapshot now has 29 tracked legacy manuscript PNGs and no tracked HTMLs there. The original six-HTML count is stale; .gitignore has no matching exclusion. | Do not apply the old blanket deletion blindly. Inventory current references, then choose which generated assets to stop tracking. No files removed in this audit. |
| [#078](../../inbox/078-two-derived-pages-tell-the-author-to-republish-t.md) | config/house.json has no published_artifacts record. The old external artifact URL is historical; this audit did not inspect the remote copy. | First establish whether those external pages are still maintained. If they are, record their canonical links and published versions; otherwise retire that workflow. |
| [#085](../../inbox/085-runs-ch04-plate-notes-md-round-7-asserts-ch05-st.md) | The false Chapter 5 claim already has a Publisher correction in plate-notes. This asks for another evidence-pasting rule, not that repair again. | Keep the correction and decline another blanket rule. Existing requirements already demand opening sources and reporting only checks that ran. |
| [#089](../../inbox/089-both-part-plate-drafts-now-carry-a-title-and-par.md) | Part-plate README still has no title rule; plate_check has no Part title comparison. Draft titles and author-approved form need to agree. | Include the Part-title choice in the combined design contract, then add its check if approved. |
| [#090](../../inbox/090-087-s-corrected-proof-samples-void-and-taper-onl.md) | This proposes a specialized canyon-geometry checker after #087’s inadequate proof. No canyon row exists. Its ink-density definition is itself a design choice. | Combine with #087/#091. First approve the intended picture by looking at it; do not make another bespoke checker a prerequisite to deciding on the art. |
| [#091](../../inbox/091-090-s-own-proof-only-requires-the-canyon-row-to-.md) | This corrects the proposed #090 test: monotonic narrowing alone would favor the defective drawing and could certify an Oak with no canyon. | Retain these counterexamples if a canyon check is later built. This is a test-design dependency, not another author question. |

### Visual decision — 10

| Record | What this means now | Recommendation / who acts |
|---|---|---|
| [#056](../../inbox/056-chapter-1-has-two-plates-that-both-draw-the-gap-.md) | The compiler currently uses the Chapter 1 window drawing. The old operating-system asset has a separate explanatory role, still awaiting disposition. | Recommend keeping the window for Chapter 1 and retaining the other as a framework explainer, outside the one-plate count. |
| [#058](../../inbox/058-are-four-ds-four-horsemen-and-virtue-question-pl.md) | The Four Ds, Four Horsemen, and virtue-question assets are text-led reference material, not the chapter plates currently selected. | Recommend retaining them as reference/sidebar assets. Any insertion into prose needs a concrete placement proposal. |
| [#060](../../inbox/060-part-closing-plates-iii-v-keep-single-line-capti.md) | The question mixes a tiny caption-position preference with whether Parts IV and V should mirror each other. | Review the Part plates as a set once. Keep the mirrored seasonal pair provisionally; no need for the author to choose numerical coordinates. |
| [#061](../../inbox/061-four-label-level-calls-on-the-new-chapter-plates.md) | Several premises are gone: Chapter 5 no longer prints PARRHESIA, Chapter 11 now has an apostrophe and no “forty times,” and Chapter 1 is 640×340, not 660×380. | Retire those old label choices inside the consolidated plate review. Do not ask for blanket approval of the obsolete description. |
| [#067](../../inbox/067-round-2-label-calls-on-the-redrawn-plates-ch9-lo.md) | Later drawings changed these choices too: Chapter 7 now labels HER PAGE and “a ledger you can’t fully read”; Chapter 12 no longer lists the old four tasks. Part III’s open-book reading remains noted in the current brief. | Review current images, particularly Part III. Avoid restoring old text merely because it once appeared in this question. |
| [#068](../../inbox/068-ch8-and-ch12-redrawn-through-gw-plate-four-small.md) | Chapter 8 and Chapter 12 now carry later captions. TONIGHT remains, but the old package of minor calls no longer describes the whole current drawing. | Fold into their current visual verdict, together with #054/#055. |
| [#070](../../inbox/070-ch5-s-new-plate-is-titled-the-courage-to-come-ba.md) | Chapter 5’s plate says The Courage to Come Back while its distillation retains The Remaining Nails. | Recommend the new title, coordinated with #095’s plain-language treatment. This changes book content, so prepare it for the author’s verdict. |
| [#084](../../inbox/084-ch4-row-three-s-caption-the-hole-remains-is-sing.md) | The current Chapter 4 draft still says “The hole remains.” under the accumulating-hole row. | Recommend “It’s full of holes.” as the proposed caption. Review alongside #101 because the same plate also prints “Anger isn’t strength,” a flagged prose claim. |
| [#086](../../inbox/086-runs-parts-plate-2-sturdy-oak-svg-is-the-only-pl.md) | The Oak draft still uses clipPath. The former alternate-renderer premise is stale because rendering has been consolidated. | Do not bake geometry merely to satisfy a grep. Test the intended delivery renderer; flatten only if a demonstrated delivery need justifies it. |
| [#087](../../inbox/087-the-part-i-redraw-was-meant-to-remove-the-empty-.md) | The River draft and landed drawing remain different; the record repeatedly corrected its measurements. The current compiler still prefers the landed Part file. | Show the two pictures together and recommend the converging canyon with the intended river. #090/#091 are supporting test questions, not additional aesthetic votes. |

### Editorial decision — 9

| Record | What this means now | Recommendation / who acts |
|---|---|---|
| [#094](../../inbox/094-align-the-author-marriage-timeline-across-the-pr.md) | The current marriage-duration passages still disagree: over thirty years in the Prologue, twenty-three in Chapter 1, twenty-four last year in Chapter 12. | Only you can supply wedding year, together-since year if different, and which scenes are retrospective. Then I can prepare the corrections. |
| [#095](../../inbox/095-keep-the-nail-metaphor-consistent-between-chapte.md) | Chapter 4 says an apology pulls the nail; Chapter 5 still says an apology ends the fight but the nail stays. | Recommend plain unresolved-hurt language in Chapter 5; coordinate with #070’s distillation title. You approve meaning and final wording. |
| [#096](../../inbox/096-align-prohairesis-hegemonikon-and-the-gap-termin.md) | Chapter 4 still calls prohairesis the governing faculty, while Chapter 2 uses ruling faculty for hegemonikon; Chapter 6 also closes a different “gap.” | Recommend capacity to choose in Chapter 4 and ordinary cooperation wording in Chapter 6. Prepare local edits, preserving the distinct concepts. |
| [#097](../../inbox/097-repair-the-chapter-4-repair-reference-and-chapte.md) | Chapter 4 still points to Chapter 16 for repair; Chapter 8 promises temperament analysis that Chapter 9 claims already happened. | Correct the repair destination and narrow the promise to what the chapters deliver. You decide whether temperament asymmetry needs a separate later treatment. |
| [#098](../../inbox/098-deliver-the-promised-practical-response-to-real-.md) | The detailed review identifies an unfulfilled promise: honest shared accounting of workload, followed by another discussion of gratitude. This is a substantive manuscript proposal, not a mechanical fix. | Recommend a Chapter 8 passage assessing workload, capacity and duration together, followed by a request; qualify Chapter 6’s blanket resentment claim. You approve scope. |
| [#099](../../inbox/099-clarify-chapter-10-boundary-duty-and-its-absolut.md) | Chapter 10’s existing boundary discussion needs to distinguish refusing retaliation from accepting repeated violations; it also still says some damage does not repair. | You decide the intended concrete response to a repeated violation. I can draft a local clarification and soften the absolute repair claim. |
| [#100](../../inbox/100-remove-chapter-12-guaranteed-reciprocity-and-the.md) | Chapter 12 still promises a matching bare-minimum return and says restarting asks nobody’s forgiveness. | Recommend removing guaranteed reciprocity and allowing acknowledgment of hurt, preserving initiative and your chosen trying-to-win-favor wording. |
| [#101](../../inbox/101-schedule-the-earlier-book-repetition-and-qualita.md) | This is a later revision batch for repetition and specific voice problems, supported by detailed excerpts. It was explicitly deferred. | Choose when to commission one earlier-book revision pass. Coordinate overlapping edits with #098/#100/#084; do not launch separate competing rewrites. |
| [#102](../../inbox/102-reconcile-the-introduction-five-mode-framework-w.md) | The Introduction’s five listed failures and the framework’s sixth River-without-Sun pairing need an intentional relationship. | Recommend including the sixth pairing if the Introduction is meant as the complete taxonomy. You decide that scope before a locked-text edit. |

### Standing tracker — 1

| Record | What this means now | Recommendation / who acts |
|---|---|---|
| [#006](../../inbox/006-84-citations-are-open-21-unverified-63-confirmed.md) | Fresh citation counts are 118 open, 0 overclaim, 4 settled. The headline’s 84 is historical. This is already ruled and not a chapter gate. | Continue research toward verifiable; only the author confirms verified against the source. No fresh policy decision is needed. |

## Evidence and limits

Read the full pending records, the Archivist brief, relevant resolved records #092/#093, current routing and validation code, current SVG text/selection, later Chapter 2/5/6 plate review records, the current design and Part READMEs, and relevant current manuscript passages. Ran inbox.py and citations.py; called read_scripts(), chapter_plate(), and the grounding corpus directly. The [evidence snapshot](2026-09-25-inbox-audit-evidence.json) records the source commit, hashes of every pending Inbox file, selected plate text, counts, and the checker failure.

The audit is not a new visual verdict or a fresh full manuscript review. Historical PASS records are identified as such. No old applied_by commands were blindly executed: some create worktrees or regenerate/delete files, and some only grep wording. Source inspection confirms implementation presence or absence; it is not a substitute for a behavioral test.

Current plate geometry verification is **unchecked**: plate_check.rows() failed because this Mac lacks `/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf`. No font substitution was made, and no plate was declared geometrically clean by this audit. The current geometry cannot be certified by the old Linux results.

The old asset-retention proposal has partly aged out: 29 legacy manuscript PNGs remain tracked, but no HTMLs in that directory remain tracked. The current external publishing links were not checked online; first decide whether that service is still in use. No cited research was independently reverified here.

## Should the Archivist do this periodically?

Yes, as triage within its existing batched review. The Publisher should own the understandable Inbox and follow-through; the Archivist can independently check whether records are stale, overlapping, already authorized, or no longer questions for the author. It should recommend closures with evidence, not invent rulings or silently reject unresolved proposals.

Your earlier #092 decision already changed the hook to three watched-path commits, with an end-of-session review route. Keep that cadence. Do not introduce a calendar automation or a second review loop just for the Inbox. Extend the existing Inbox-reading bullet in the desk brief, replacing it rather than creating another desk or another standing list. A [draft replacement with measured word counts](2026-09-25-archivist-inbox-triage-proposal.md) is provided for a concrete later rule decision; it has not been applied.
