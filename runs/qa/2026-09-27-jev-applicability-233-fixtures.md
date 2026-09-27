# Jev applicability to agentic-ghostwriter

Research date: 2026-09-27, clock read 16:04 America/Chicago. Repository examined at `edb57b397ab9eee818145fe012c9c3f3ea63cf90`. Scope: the 233 fixtures reached by `tests/run.py`, their production checks, and relevant editorial contracts. This is platform research by the Publisher in session, not a cold desk review. No Jev inference was run. Recommendations below are proposals, not adopted house rules.

**Recommendation.** Retain all 233 software regression fixtures. Pilot Jev as an additional, advisory evaluator of meaning, starting with Stoic-term explanations and plate-copy support. Its larger opportunity is inexpensive, repeated editorial screening between desk passes. It is not a replacement for executing Python tests, inspecting rendered pages, or obtaining the author's editorial verdict.

The proposed replacement/deletion count is **zero existing fixtures, zero production checks, zero desk contracts**. A pilot adds measurements; any later reduction in desk work must be justified by measured performance and a separately scoped decision.

**What the 233 tests actually do.** I ran `python3 tests/run.py`; it exited 0 and printed:

```
233/233 fixtures pass
```

The full output is preserved beside this report in `2026-09-27-jev-applicability-233-fixtures-tests.txt`. This count covers that runner, not every standalone test program or optional rendering mode in the repository. I inspected the runner, all emitted case names, relevant fixture implementations, and the production code described below. I did not independently audit every assertion or run the separate raster suite.

| Existing coverage | Examples actually exercised | Jev recommendation |
|---|---|---|
| Completion and knowledge receipts | Missing receipts refuse completion; committed edits invalidate stale hashes; force cannot waive reconciliation | Keep deterministic enforcement. Semantic completeness is a separate potential Jev job. |
| Git, session history, and review windows | Wrong ancestry, lost log entries, retained unreviewed ranges, proof against historical code | Keep execution-based tests. A model's reading of code is not proof that the behavior occurred. |
| Document assembly | Missing distillation fields, prose after distillation, escaped or fragmented markup, renderer errors | Keep exact assertions and actual renderer checks. |
| Voice thresholds and state | Changed config values, missing spec wording, stale reviews, wrong book resolution | Keep literal comparisons, counts, and hashes. |
| Knowledge indexing and citations | Preserved annotations, status drift, staged links, chapter slugs | Keep structural checks. Add meaning review only where structure cannot answer. |
| Plate checks and source selection | Geometry, CSS anchor precedence, title matching, permitted grounding corpus, text overlap | Keep existing coverage; evaluate semantic support alongside the grounding heuristic. |

Source: [test runner](../../tests/run.py), [export fixtures](../../tests/export_safety_cases.py), [reconciliation fixtures](../../tests/okf_reconcile_cases.py). Several fixtures test heuristics about text, but their purpose is still to prove that a specified algorithm behaves as intended. Replacing the assertion with an AI judgment would change what is being tested.

**What Jev contributes.** The API accepts a state and typed questions. Choice selects among declared alternatives; Score evaluates ordered criteria; Noul returns a yes-probability. Questions are evaluated independently against shared state. This supports small, explicit judgments whose consequences are handled in ordinary code. It does not provide the prose explanations or rewritten sentences our desks produce. [TypeSafe introduction](https://docs.typesafe.ai/introduction)

Current documentation lists `jev-1.13.0`, text-only inputs, 64k tokens per request and 32k for state plus the longest question. Input costs $0.042 per million tokens; outputs are free. Pin the model version for experiments. These are published specifications, not measurements made here. [Models](https://docs.typesafe.ai/models)

TypeSafe's limitation notes explicitly identify unreliable counting, numerical precision, date comparisons, complex indirection, distracting long inputs, and susceptibility to adversarial content. This strongly supports keeping our numerical and structural checks in code and giving Jev short, relevant passages. It cannot inspect a plate's rendered pixels. [Known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)

**What the evidence establishes.** The headline speed and cost comparisons come from vendor-designed workflows, with reference answers based on other models rather than independently established truth. Type safety constrains possible outputs; it does not establish that a selected answer is factually correct. Treat those comparisons as motivation for a trial, not expected savings for this platform. [Launch methodology](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

An independent classification experiment reports roughly 5–6x median speedups, with accuracy and calibration varying by task. Its 500-example comparisons and smaller 130-example frontier comparisons used public spam and banking datasets, one configuration, and a gateway. They are useful evidence for affordable triage, not evidence of editorial competence. [PavelRavvich experiment](https://github.com/PavelRavvich/jev-bench/blob/main/article/jev-article.md)

A separate retrieval experiment reports improved ranking over its unranked baseline, but no universal advantage over a dedicated reranker. Its measured Jev reranking latency was about four seconds. The important implication is to measure the entire retrieval-and-review workflow rather than extrapolate from a tiny classification call. Some downstream analyses were exploratory. [Retrieval experiment](https://github.com/emretheus/jev-rag-benchmark)

An independent audit found that removing the unknown option from ambiguous Korean questions could leave confident wrong selections. That particular result does not transfer numerically to this book; it demonstrates why our answer vocabulary must allow insufficient evidence. [Calibration audit](https://github.com/jujumilk3/jev-calibration-audit/blob/main/FINDINGS.md)

A September 24 preprint evaluates Jev as a detector across 44 alignment benchmarks. Its abstract reports promising discrimination but notes the importance of supplied context, including fields that encode labels. I reviewed its abstract, not a full methodological reproduction. It supports investigating automated review, not replacing our editorial evaluations. [RLCDAlignBench preprint](https://arxiv.org/abs/2609.29429)

I did not reproduce these external studies. None of the evidence reviewed establishes performance on this author's voice, Stoic interpretation, or manuscript continuity.

**Where it fits, in implementation order.**

| Priority | Current limitation | Proposed atomic Jev question | Output and owner |
|---|---|---|---|
| 1 | `voice_check.py:check_stoic_glosses` accepts punctuation or gloss-like words within a character window | Does the first-use passage actually explain this term in plain language? | Explained / named only / ambiguous, with a passage ID; Line Editor reviews. |
| 2 | `plate_check.py` grounding accepts any three-word overlap for a text run | Does the permitted source passage support this plate statement, including its qualifiers? | Supported / contradicted / not established / insufficient context; Designer reviews meaning. |
| 3 | Conformance Checker must judge each outline requirement | Does the supplied prose actually fulfill this one requirement? | Fulfilled / missing / contradicted / insufficient context, with source IDs; checker retains final verdict. |
| 4 | OKF reconciliation validates coverage but explicitly cannot establish semantic completeness | Does this changed passage add or alter a claim relative to this retrieved concept? | Equivalent / added claim / contradiction / insufficient evidence; Publisher reconciles. |
| 5 | Anti-Slop Reader handles repeatable local categories | Does this paragraph contain one specifically defined problem, such as an invented foil? | Candidate finding and exact passage; reader explains and proposes correction. |
| 6 | Reader feedback needs category and source matching | Which existing routing category fits this response? | Suggested category plus unknown/mixed; Publisher follows existing feedback gates. |

The first two are the cleanest pilot because inputs and observable defects are small. The fourth could have the highest eventual value, but missing retrieval can masquerade as missing knowledge. Start it later.

Specific local evidence: [voice checker](../../scripts/voice_check.py), [plate checker](../../scripts/plate_check.py), [reconciliation checker](../../scripts/okf_reconcile.py), [conformance contract](../../.claude/agents/gw-specchecker.md), [anti-slop contract](../../.claude/agents/gw-slopreader.md), [feedback routing](../../.claude/skills/gw-signal/SKILL.md).

For gloss screening, enumerate every first occurrence of the configured terms, not only the existing REVIEW candidates: punctuation is precisely how an unexplained term can currently escape. Add sentence-boundary handling and neighboring context before asking Jev. A punctuation-free explanation and an unrelated comma are essential counterexamples.

For plate copy, preserve the existing allowed-source selection. Exclude boilerplate and unapproved proposals before inference. A label with familiar words can still reverse a claim; a faithful paraphrase can have no three-word match. Jev's advisory result should be separate from the existing `grounded` result so neither silently changes meaning.

For conformance, preserve the checker's deliberately restricted inputs: outline requirement and prose. Do not feed it the writer's assurance that the requirement was met. A model-generated decomposition can omit a requirement, so freeze and inspect the requirement inventory. Jev cannot generate the required evidence quote: let it select an existing passage ID and have code reproduce that passage exactly. A missing candidate is not proof the entire chapter lacks evidence.

TypeSafe demonstrates source-line selection with declared IDs and a separate answer-existence question. Its Choice ranking alone can select the closest irrelevant line. This is a useful pattern for traceable findings, provided we distinguish locating possible evidence from deciding that it satisfies a requirement. [Semantic search cookbook](https://docs.typesafe.ai/cookbooks/semantic_find)

For citations, the useful task is whether a retrieved source supports the manuscript's claim. TypeSafe's example combines string matching with semantic judgment, but its eight-case demonstration is small and its label `verified` conflicts with our author-only status. Here the output would be `support_assessment`; it must never promote citation status. A quote missing from one extracted text should be reported as not found there, not declared fabricated: editions, omissions, and OCR can explain a mismatch. [Citation cookbook](https://docs.typesafe.ai/cookbooks/citation_check)

Whole-book continuity, emotional progression, disputed interpretations, metaphor coherence across an arc, and deciding what the book should argue still require broader editorial reasoning. Retrieval could shortlist passage pairs for Jev, but neither an unexamined pair nor an absent match can become a whole-book pass. Rewriting, interviewing, explaining a criticism, and visual QA remain outside the proposed Jev job.

**A concrete pilot design.** Build an opt-in evaluator outside the normal Stop hook. Proposed flow: code selects a permitted excerpt and rule; Jev classifies it; code attaches exact evidence and metadata; the existing desk independently assesses it. During the pilot Jev has no power to clear gates, edit prose, suppress findings, close inbox items, or write accepted knowledge.

Start with two rubrics and about 100 labeled examples per rubric, expanded if real diversity is insufficient. Include clean passages, actual approved historical defects, repaired passages, and controlled mutations. Mark synthetic examples explicitly. Keep unresolved inbox rulings out of gold labels. A current published chapter is not automatically a clean example. Label from explicit author rulings where available; otherwise record independent reviewer decisions and adjudicate ambiguity.

Split development and held-out evaluation by chapter or source family. Keep a defect and its repaired version in the same split. Freeze the rubric, example IDs, and thresholds before the held-out run. Include hard negatives, missing context, negated claims, changed qualifiers, reordered options, distracting text, and instructions embedded in source material. Count abstentions separately from correct decisions.

Compare four conditions on the same inputs: the current heuristic, Jev, a small generative classifier, and the existing full editorial review. Preserve the latter's judgment before revealing Jev's answer. Measure defect recall, false alarms, false clearances, abstention, evidence selection accuracy, end-to-end latency, token cost, and reviewer time. Report per rubric and include uncertainty intervals; a pooled accuracy score can hide failures on a rare serious defect.

TypeSafe's `confidence` is derived from the distribution over answers; it is not a separately measured probability that our editorial verdict is correct. Noul has no separate confidence field. Thresholds need local evaluation, and Choice and Noul thresholds should not be interchanged. [Confidence documentation](https://docs.typesafe.ai/confidence)

Suggested pilot targets, not existing policy: at least 95% recall on labeled defects and at most 10% false alarms on clean cases, with reviewer effort demonstrably reduced. A small sample meeting those point estimates earns continued advisory use, not automatic acceptance. Before skipping any desk work, require a larger representative held-out evaluation with a predeclared bound on false clearances. Confidence scores alone do not authorize skipping.

Log input file hashes, exact source IDs, rubric version, requested and returned model IDs, full probabilities, disposition, token use, timing, and errors. Cache only by all those inputs, including relevant context and rule changes. On timeout or unavailable evidence report UNCHECKED and preserve the existing review path. Offline tests can prove this wrapper's routing and cache behavior; only separate live evaluations can establish model quality. Replaying recorded responses does not prove the current service still performs the same way.

Batch questions that share a relevant excerpt. The vendor recommends parallel questions to reduce repeated calls, but its own large-state caveats argue against stuffing the entire book and every rule into one request. Dependent judgments require a subsequent step or must be independently formulated. [Batching pattern](https://docs.typesafe.ai/patterns/fan-out)

**Economics.** At the documented input price, an illustrative 233 calls of 2,000 tokens each cost $0.019572 in Jev input fees. A 10,000-token shared passage plus 233 questions of 100 tokens each costs $0.001398, if the complete serialized request fits the limits. These are arithmetic scenarios, not a quote or a measured workload; options, criteria, repeated contexts, retries, and reviewer time must be included in actual costing. Even cheap calls offer no savings over a local exact assertion. The financial case depends on reducing expensive model review or human rework without increasing missed defects.

The initial advisory pilot adds review, so it should be budgeted as an experiment. If Jev never permits less expensive review or catches valuable new defects, its low API price does not make it useful.

**Open implementation questions.** Editorial accuracy, stable thresholds, retrieval coverage, actual workload latency, and reviewer savings remain unmeasured. Account access has not been tested. Before sending private interviews, establish the selected account's retention terms: TypeSafe states that customer data is not used for training and offers enterprise zero retention, which is not the same as saying every account has zero retention. No manuscript or interview text was sent to TypeSafe during this research. [Data handling](https://docs.typesafe.ai/legal)

This research changes no book facts or accepted meanings. Knowledge disposition: `no-knowledge-change`; the report records platform findings and proposed experiments only. No house rule, test, or manuscript was modified.
