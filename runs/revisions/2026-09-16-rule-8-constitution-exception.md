# Proposed amendment — Rule 8, the constitution exception
**Artifact:** `CLAUDE.md` (this repo) · **Status:** PROPOSED. Rule 17 — the house does not edit its own rules.
**Raised:** 2026-09-16, from the author's question about updating the voice spec while the playground stays frozen.

## The problem, measured

Four rulings are blocked on book-repo edits: `01-voice.md` (run-in headers; the
metaphor cap), `appendix/practice-guide.md`, `okf/citations/gottman-four-horsemen.md`,
`sources/interview-author-stories.md`. The metaphor cap capped Ch12 at 3 mentions
after the author asked for more. `#018` leaves the book contradicting itself about
its own author's love language.

## Why the current rule is over-broad

Rule 8 reads: *"Never write inside the book repo. Outputs go to `runs/chNN/`.
**This is what lets both pipelines run at once.**"* The stated hazard is this
engine's **output** — drafts, citations, chapters — contaminating a bundle the
other pipeline reads. A constitution change the author has ruled is not output;
it updates both pipelines simultaneously, which is the intent.

"Frozen" should mean *no new chapters ship from the old pipeline*, not *no file
in that repo may change.* The constitution is the book's law, not one pipeline's
property.

## The proposed amendment

```diff
  8. **Never write inside the book repo.** Outputs go to `runs/chNN/`. This is
     what lets both pipelines run at once.
+
+    **One exception, added 2026-09-16: the constitution.** The Publisher — never
+    a desk — may write the book's L4 files when the author has ruled in words,
+    in session, under all five conditions:
+
+    a. **Scope.** Only `00-premise.md`, `01-voice.md`, `02-audience.md`,
+       `03-outline.md`, `04-archetype.md`, `05-framework.md`, `06-sources.md`
+       and `sources/*`. Never `chapters/`, never `okf/`, never `manuscript.md`,
+       never `appendix/`. Those are output, and output is what Rule 8 is for.
+    b. **Authority.** His explicit word this session, quoted verbatim in the
+       commit message. Not an inbox ruling from a previous session, not a desk's
+       recommendation, not an inference.
+    c. **Never cold.** No sub-agent may write there under any circumstances. A
+       desk that believes the constitution should change writes an inbox item.
+    d. **Visible and revertible.** Each write is its own commit on its own branch
+       in the book repo, never on its `main`, so the other pipeline sees it as a
+       proposal it can refuse.
+    e. **The engine follows, never leads.** Where a threshold in
+       `config/house.json` mirrors the spec, the spec changes first and the
+       engine's value changes in the same commit pair. An engine enforcing a
+       number its constitution does not state is the defect this rule exists to
+       prevent.
```

## Blocker — fix this before the amendment, not after

`voice_rules_check.py` verifies that each threshold's **source phrase** still
appears in `01-voice.md`. It does **not** verify that the phrase's **number**
matches the value the engine enforces. Proven by execution (Archivist, 2026-09-16):
with `value` mutated 3→5 while the spec still reads "~3 mentions", it prints
`[ok] metaphor_family_max_per_1000 = 5` and exits 0.

So today, condition (e) cannot be enforced by anything but a model remembering.
**Fix the check first.** Otherwise the first use of this exception is a silent
divergence between engine and constitution — the exact failure the exception is
designed to avoid.

## Sequencing

| When | What | Why |
|---|---|---|
| **Now** | Fix `voice_rules_check.py`; apply this amendment; land the four pending edits. | Unblocks the metaphor cap and stops the book contradicting itself. |
| **After Ch13–14** | Execute the migration in inbox `#007`: book assets move here, playground becomes a read-only archive. | One good chapter is not a proven system. Keep the fallback until a second and third chapter ship clean. |
| **At migration** | Rule 8 loses its reason and this exception with it. Both collapse into "this repo owns the book." | The exception is scaffolding, not architecture. Delete it when it stops earning its place. |

## What this does not change

The engine still never writes chapters, citations, the manuscript or the practice
guide into the book repo. Those stay in `runs/`. `/gw-found` still refuses to
author L4 for a book it did not create. `/gw-revise` still produces a diff rather
than applying one when the author has not ruled.
