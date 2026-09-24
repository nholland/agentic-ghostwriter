Recorded 2026-09-23T07:45:00.625791-05:00

# Investigation: why the Archivist stopped at diagnosis

Status: investigation and proposed corrections, not applied house changes.

## What can be established

The mandate already empowers the Archivist to improve the system. `.claude/agents/gw-retro.md:47–51` explicitly calls out work the author had to do, missing checks and unnamed stages. Lines 66–70 say recurrent failure should produce a check with a caller. FINDINGS.md:323–339 records the author's earlier expansion from rule audit to system learning. A lack of permission to recommend improvements does not explain this outcome.

The review itself identified the necessary evidence: the author had to ask for review coverage; the persona/coherence capability exists separately from chapter orchestration; prior history contains the same author-coordination problem; additional review found material defects. Its conclusion nevertheless says that immediate repairs are already in the package/inbox and rejects new work. That is the demonstrable reasoning gap: correcting the current artifact was treated as sufficient mitigation of the repeatable process failure.

The review considered a fresh whole-book audit on every chapter and another readiness checklist, then rejected both. Neither is the minimum remedy. Calling an existing focused review before chapter handoff, routing its findings back, and recording its actual completion is a narrower option. Existing capability without a required caller is incomplete orchestration.

## Publisher steering, recorded verbatim from this conversation

Initial brief included: “Avoid inventing new rules just to suggest; distinguish existing gates ignored vs missing workflow.”

Follow-up included: “Please keep recommendations small and report-oriented; no need implementation or broad new rule suite. User needs completed review, not exhaustive redesign. Existing PDF provided and verified latest.”

The original agent received full conversation history rather than a neutral evidence-only packet. These directions did not prohibit recommendations, but emphasized restraint and task closure. That is a plausible contributing pressure, not a measured account of the model's private causal process. Publisher then accepted the no-recommendation conclusion without testing whether the next chapter could fail the same way.

## Instruction imbalance

The role has legitimate safeguards against generating unnecessary rules: “Suggest only if necessary,” warnings about ledger growth, a suggestion requiring a deletion/replacement, measured word costs, and executable closure commands. These are quality constraints, not permission to ignore meaningful gaps. In combination with the Publisher's steering, they made the cost of proposing explicit while there was no equally explicit burden to explain why a recurring unresolved failure was safe to leave unchanged.

The report itself foregrounds “Zero proposed rule-corpus words.” That is evidence that rule volume was salient; it does not prove it was the sole or dominant cause. The proper objective is reducing recurrent author effort and improving manuscript quality, with simplicity as a constraint.

## Concrete reproduction of the opportunity missed

Read-only isolated probe of scripts/next.py, using a temporary directory and its actual STAGES/chapter_state functions:

```text
Files: draft.md, interview.md, refined.md, research.md
State: ('verdict', '/gw-compile', 'refined; no plate yet (optional)')
Persona, coherence, conformance and voice review results: absent
```

This is not a claim that next.py is currently violating its implementation contract; it presently reports artifact-based stage progression. It demonstrates that the existing mechanism cannot enforce the broader review-ready meaning the author expects. A report file's existence alone would also be insufficient: a future solution must bind verdict, scope, unresolved findings and reviewed input revision. Checks verify review completion and freshness, not literary quality.

## Alternative explanations and limits

The user had requested getting Chapter 13 wrapped up and deferring older-book repairs. Avoiding an unrequested rewrite of the system or reopening those content issues was appropriate. It did not preclude proposing a small workflow improvement for author decision. The no-self-modification boundary already protected against unsolicited implementation.

Absent retro-window files and stale runs/log.md reduced automatic session provenance; the Archivist disclosed that and reconstructed an explicit git window. Its report nevertheless identified the core orchestration gap, so missing logs are not supported as the primary explanation for omitting a recommendation here.

No controlled prompt ablation was run. We cannot assign causal weights to role text, briefing, history or sampling from this one outcome. The failed inference and Publisher acceptance are observable; the pressure mechanisms are evidence-based hypotheses. An independent review is a cross-check of reasoning, not a causal experiment.

## Corrections worth proposing

1. Rebalance the Archivist's assessment: every material recurring failure must have either a proportionate preventive recommendation, a linked existing remedy that actually prevents recurrence, or a concrete reason to accept the remaining risk. This replaces the generic dismissal pressure; it does not impose a recommendation quota.
2. Give the Archivist a neutral evidence packet and outcome mandate. Remove Publisher instructions that prejudge the amount or type of recommendations. Keep implementation authority separate from freedom to propose.
3. Wire the existing Reader Panel and cross-chapter reader into a scoped chapter review before author handoff; route actionable current-chapter findings to the owning desk, independently recheck changed work, and preserve explicitly deferred author decisions. Broader milestone review remains useful without requiring a whole-book reread for every edit.
4. Replace artifact-presence-only readiness with review evidence tied to the final input revision and declared scope. A missing, failed or stale required review cannot produce author-ready. Distinguish current-chapter blockers from explicitly deferred older-book issues.
5. Evaluate the Archivist on held-out session cases: recurring unaddressed omission; same incident repaired locally but not prevented; existing working remedy; legitimately clean session; duplicated proposal; and findings with inconclusive evidence. Assess causal specificity, proportionate remedy, owner/caller and restraint. Do not grade by number of recommendations or agreement with Publisher.

Acceptance examples for readiness: refined prose without persona/coherence review stays at review; stale review after substantive edits is invalidated; plate-only read cannot satisfy chapter review; current essential findings require correction or explicit author disposition; deferred old-book findings do not block Chapter 13; current passing reviews permit handoff. These are proposed tests, not implemented or passing tests.

No rules, production code, manuscript or inbox decisions changed during this investigation. The original Archivist report remains preserved so the failure is not erased.

## Independent cross-check

archivist-independent-audit.md agrees that the original no-recommendation conclusion was unsupported, and identifies the same local-repair-versus-recurrence inference. It favors a narrower Publisher-owned coverage decision over an automatic full-book audit; it does not itself establish that every review type must run on every chapter. Publisher recommendation is a required pre-handoff review with an explicitly appropriate scope, not a full-book reread at each edit. The independent audit also notes that calling the original recommendation “failed” in its brief could bias its own review; agreement is corroboration of visible reasoning, not proof of uncontaminated causal attribution.
