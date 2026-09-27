# Jev: meaning preservation after revision

Date: 2026-09-27; clock read 16:27 America/Chicago. Status: proposed design, no API key, no live inference, no integration installed. Scope: idea 1 in the author's Explore JEV parking-lot section. Prepared by the Publisher in session, not a cold editorial desk.

**The proposed job.** After an editorial revision, detect whether the writing has lost, added, or altered meaning, then distinguish intended changes from unexplained ones. Report the exact passages to the reviewer. Jev would supply bounded judgments; existing code and editorial authority would determine what happens next.

Do not ask whether the revised prose is better. A polished sentence can make a different claim. Do not assume the old prose is correct either: an author may explicitly ask us to correct it. Meaning preservation, factual correctness, author fidelity, and voice quality are distinct questions.

This proposal deletes zero tests, checks, rules, or desk responsibilities. It adds an optional advisory experiment. The parking-lot entry is authorized; adopting this integration is not implied by recording it.

**Research basis.** TypeSafe accepts named state fields and independent questions against that state. Its Choice primitive fits a small set of interpretable verdicts, with explicit uncertainty. We can compare short passages without asking Jev to generate prose or reconstruct an entire book. [State documentation](https://docs.typesafe.ai/concepts/state), [Choice documentation](https://docs.typesafe.ai/primitives/choice)

The underlying evaluation idea is established outside Jev: compare meaning in both directions. Babakov and colleagues investigate bidirectional entailment for content preservation. Agrawal and Carpuat evaluate preservation through reading-comprehension questions with document context. These sources motivate the design; neither establishes that Jev performs it reliably. The abstracts were reviewed for this design, not a reproduction of either study. [ACL 2022](https://aclanthology.org/2022.acl-srw.23/), [TACL 2024](https://aclanthology.org/2024.tacl-1.24/)

TypeSafe's citation example also separates literal source matching from judging whether a source supports a claim. It is a useful design analogue, not a ready-made manuscript-editing solution. [Citation checking](https://docs.typesafe.ai/cookbooks/citation_check)

**Start at one existing handoff.** The lowest-complexity initial location is after the Line Editor produces `runs/chNN/refined.md` from `runs/chNN/draft.md`, alongside the independently run counted checks and before the existing conformance review. A later extension can inspect each section revision in `/gw-edit`. Do not call Jev on every file save or keystroke: start with one completed revision batch and immutable input snapshots.

Local contracts: [refinement](../../.claude/skills/gw-refine/SKILL.md), [interactive editing](../../.claude/skills/gw-edit/SKILL.md). These files were read as architectural references, not invoked or changed.

**Build a small comparison packet.**

| Field | How to obtain it | Why it matters |
|---|---|---|
| Baseline prose | Snapshot the actual file before this edit, with a content hash | Never reconstruct the old wording from the editor's recollection |
| Revised prose | Snapshot the proposed result, with a content hash | The judgment applies to these bytes only |
| Matched passages | Code identifies changed paragraphs; preserve headings and neighboring sentences | Negation, pronouns, conditions, and qualifications often cross sentence boundaries |
| Accepted anchor | Relevant approved author wording or knowledge concept, with path, status, and version | Repeated small edits can drift away from the original intent |
| Edit instruction | Exact author instruction or explicit scope of the editorial task | Distinguish polishing from a requested substantive correction |
| Coverage record | All changed ranges, mappings, unresolved moves, and excluded apparatus | An omitted comparison must not look like a clean result |

Use both the immediately previous version and the accepted anchor where one exists. The former locates the edit; the latter guards against cumulative drift. A draft is a baseline, not automatically an authoritative author statement. Missing anchors are reported as a coverage limitation. If approved records conflict, refer that conflict to the Publisher rather than selecting whichever makes the revision pass.

Paragraph alignment is a material part of the problem. A paragraph can move, split, or merge. Start with a known section and manually inspect its before/after alignment for the pilot. The eventual implementation can use exact matching and candidate retrieval, but uncertain mappings remain UNCHECKED. Search for apparently deleted claims elsewhere in the revised section before alleging omission. A move is not deletion.

Separate prose from editor notes using the existing boundary conventions. Do not put the revising agent's explanation of why its edit is good into the semantic comparison. Treat text being compared as evidence, not instructions. This separation helps but does not prove immunity to injected instructions; adversarial text is a documented Jev weakness. [Known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)

**Ask two core questions, then targeted ones.**

1. Does the revised passage still communicate the substantive assertions in the baseline passage? This direction detects omissions and weakened claims.
2. Does the baseline passage support the substantive assertions in the revision? This direction detects added or strengthened claims.

For each direction, use `supported`, `contradicted`, `not_established`, and `insufficient_context`. An unsupported addition is different from a contradiction. The two questions are distinct checks; do not assume their probabilities are complements or multiply them as if errors were independent.

For a short passage this is a useful first screen. For a paragraph with several claims, split into specific questions about actors, qualifiers, causality, conditions, timing, attribution, or reader action. A single verdict over many assertions can hide a changed detail. A question can reference a selected source sentence directly, avoiding an invented paraphrase of the author's meaning.

The hardest design issue is deciding what the claims are. Jev cannot write a claim inventory. Initially, the Publisher selects a small number of explicit source spans and writes the comparison questions for a few examples. This costs reviewer time but allows us to inspect the rubric before testing it. Later, a larger model might propose a claim inventory once per section; that inventory would itself require evidence and completeness checks. Do not assume a perfect, free claim extractor in the business case.

A useful complementary technique is to ask the same reading-comprehension question of each version separately, with the same answer options and a not-stated option. For example, ask whether an action guarantees a result, only makes it possible, or has no stated effect. Different answers expose a change that topic similarity can miss. Keep these separate-state calls distinct from paired-text comparison and evaluate which approach catches more meaningful defects. [Reading-comprehension research](https://aclanthology.org/2024.tacl-1.24/)

**Handle permission to change meaning separately.** Detect the textual relationship first. Then compare each detected change with the recorded edit instruction and accepted anchor. The author may authorize one correction while expecting everything else to remain intact. A general instruction to improve flow must not excuse a new factual claim.

During the pilot, the Publisher makes the authorization decision. An eventual second Jev call could suggest `within_requested_change`, `outside_requested_change`, or `scope_unclear`; it would not confer authority. Keep an authorized correction visible in the audit instead of relabeling it as unchanged. Independent questions in a single TypeSafe call cannot consume each other's outputs; a follow-up that needs the detected issue must be another step. [Parallel-question pattern](https://docs.typesafe.ai/patterns/fan-out)

**Examples to design against.** All sentences below are invented technical examples, not manuscript quotations, author beliefs, or measured Jev outputs. Expected interpretations are design hypotheses for human review.

| Before | After | What the check should notice |
|---|---|---|
| The switch can stop the motor. | The switch stops the motor. | Possibility has become an unqualified assertion |
| Use the switch only when the cover is closed. | Use the switch. | A condition has disappeared |
| The operator checks the latch. | The supervisor checks the latch. | Responsibility changed |
| The delay followed the repair. | The repair caused the delay. | Sequence became causality |
| The technician believes the sensor failed. | The sensor failed. | An attributed belief became an asserted fact |
| Close the cover before starting the motor. | Before starting the motor, close the cover. | A harmless reorder should remain clear |
| The inspector checks the seal. | The seal is checked by the inspector. | Active/passive change preserves the actor and action |
| The alarm is optional. | The alarm is required. | Contradiction; acceptable only if the instruction explicitly requests that correction |
| A limitation appears in paragraph 2. | The same limitation moves to paragraph 3. | Inspect the section before flagging a deletion |
| He checks it before use. | She checks it before use. | Without antecedents, request context rather than guessing identities |

We should also include a faithful, vivid paraphrase with low word overlap, a bland paraphrase that preserves facts but loses voice, an intentional removal of redundant prose, and a changed metaphor that shifts the argument. The bland example should demonstrate a limit: factual meaning preservation does not certify literary quality. A metaphor's ambiguous implication may require the full editorial reader.

**A reviewable request, without a key.** The companion [example JSON request](2026-09-27-jev-meaning-preservation-request.json) uses TypeSafe's documented HTTP shape, with fabricated motor-switch text. It is a design specimen only: no request was sent. The question IDs are bookkeeping; all necessary instructions appear in the question body because the API does not expose those IDs to the model. [API reference](https://docs.typesafe.ai/api)

The example asks whether the revision preserves the modal strength of `can`, whether the revision is supported by the baseline, and whether the actor changed. It demonstrates atomic questions, not a complete evaluator. Do not let its three questions create an illusion that every possible semantic difference has been inspected.

**Report evidence, not a mysterious score.** A local report should display the before and after text, affected dimension, returned category, full probability distribution, model ID, input hashes, and coverage. The reviewer should see the exact word or source span where possible. Jev can select from provided passage IDs; code prints the text associated with that ID. If localization requires the first answer, use a second call. Never ask Jev to invent an explanatory quote.

Initial output states would be `POTENTIAL_DRIFT`, `NO_DRIFT_DETECTED`, and `UNCHECKED`, plus a separate Publisher disposition such as intended change, unintended change, or unresolved. No numerical chapter-quality score. Confidence is a summary of the answer distribution, not a guarantee of correctness on our editorial domain. Thresholds remain unset until local calibration. [Confidence documentation](https://docs.typesafe.ai/confidence)

Contradictory answers, missing passages, unknown categories, timeouts, or stale hashes produce review or UNCHECKED. Do not transform low confidence into a pass. Do not transform a flag into an automatic rewrite. One bounded context expansion may resolve an uncertain reference; continued ambiguity goes to the existing reviewer instead of an indefinite retry loop.

**How to explore this before an API key.** First, inspect the example packet and agree on the distinctions worth protecting. Then assemble a small, offline set from historical edits whose author intent is explicit. Pair benign edits with controlled harmful variants and intended corrections. Store the instruction separately from the prose, with provenance for every expected judgment. Unresolved author decisions are not gold labels.

Twenty or so diverse cases would be enough to improve the design, not to establish deployment safety. Freeze a development set and a separate evaluation set by chapter/source family; keep each original and its variants together. A later live trial measures false clearances, false alarms, abstentions, evidence accuracy, reviewer time, and behavior across repeated calls. Compare with the current review and a simple generative-model classifier. Label results before showing reviewers Jev's predictions.

For the first trial, do not give Jev feedback to the writer automatically. Otherwise we cannot tell whether it protects meaning or merely trains the writer to satisfy its preferences. The claimed quality benefit fails if reviewers spend more effort rejecting alarms, if important meaning changes are confidently cleared, or if faithful stylistic variety is penalized.

**Cost and scope.** The current documented price is $0.042 per million input tokens with free outputs; version `jev-1.13.0` is documented, with 64k total request tokens and 32k for state plus the longest question. Pin the tested version and recheck availability before a live trial. [Models](https://docs.typesafe.ai/models)

Illustration, not a measured bill: 20 changed-passage packets at 2,500 input tokens each would cost $0.0021 per revision batch. That estimate must include question text and criteria; actual costs also include context preparation, claim selection, any second calls, and reviewer effort. A million cheap judgments can still create expensive false alarms. Savings require fewer full reviews or less repair work; the initial advisory experiment adds work.

A later request cache should include baseline, revision, neighboring context, approved-anchor version, edit-instruction version, rubric, and model. A new instruction can invalidate a judgment even when the revised prose is unchanged. Exact quote comparison, number differences, and file integrity remain deterministic checks. A detected numerical difference still needs interpretation: formatting a number differently is not necessarily a meaning change.

**Current conclusion.** This is plausible as a second reader focused on semantic drift at revision handoffs. Its value depends at least as much on selecting the right source, context, and instruction as on the model. We can design those inputs now. Accuracy, calibration, latency, and savings on this platform remain untested.

Knowledge disposition: no-knowledge-change. This is a platform proposal; no accepted book meaning or manuscript was changed. Source-access gap: TypeSafe's how-to-build page failed to load twice, so this design relies on its accessible State, Choice, API, Confidence, Models, limitations, and cookbook pages instead.
