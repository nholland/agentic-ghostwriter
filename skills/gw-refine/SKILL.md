---
description: The Line Editor desk refines a cold draft into finished prose plus a distillation, gated by the counted voice script and the clean-room conformance checker. Writes into this repo's runs/ tree only. Use after /gw-draft for the shadow run of a chapter.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-refine/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-refine — refine a cold draft, gated

Argument: a chapter number, optionally `--distill-only` or `--distill-all`. `$ARGUMENTS`

`--distill-only NN` regenerates only `distillation.md` and the chapter's
practice-guide section from the current `refined.md` (after an edit, or a
chapter that predates auto-distillation). `--distill-all` does it for every
chapter in `runs/` — the refresh after a bulk editing pass. Both skip Steps
1–3 and run Step 4 with its voice check.

## Step 0 — paths

```
python3 scripts/resolve_book.py
python3 scripts/okf_gate.py
```

**Both are blocking.** Stop on either failure: the first means no book, the
second a broken citation bundle. `/book-chapter-refine` in the book repo runs the
same citation gate before writing prose, and this pipeline must not be the laxer
of the two.

Require `runs/chNN/draft.md`. Output
`runs/chNN/refined.md` and `runs/chNN/distillation.md`. **Never write inside
`{bookRoot}`.**

## Step 1 — refine

Dispatch `gw-lineeditor` against the draft, the voice constitution, the outline
section, and the draft's Draft Notes. It runs passes 0–4 and runs the counted
script itself as pass 4.

Name the desk when you report.

## Step 2 — counted gate, independently

Do not take the editor's word for it. Run the script yourself on the output:

```
python3 scripts/voice_check.py runs/chNN/refined.md --metaphor-family "<declared>"
```

Compare against what the editor reported. **A discrepancy between the editor's
reported counts and the script's is itself a finding** — that is precisely the
failure that happened on Ch9, Ch10 and the Prologue in the old pipeline, and the
reason this gate is duplicated rather than trusted once. Record any discrepancy.

On HARD failure: back to `gw-lineeditor` with the script output. Two rounds, then
the inbox: `python3 scripts/inbox.py --add ... --raised-by gw-lineeditor --chapter NN
--context ... --unblocks ...`.

## Step 2.5 — the Anti-Slop Reader (the half no script can count)

Dispatch `gw-slopreader` on the refined prose. `voice_check.py` owns the counted
rules; this desk owns the qualitative ones - invented foils, indirection, windup
sentences, the wife cast as a threat, scene-from-outside. The two do not overlap
and neither substitutes for the other.

Its findings are not automatically applied. Plainly-correct fixes go back to
`gw-lineeditor`; anything that changes what the chapter argues goes to the inbox
for the author. A judgement call silently applied by a cold desk is the failure
the inbox exists to prevent.

## Step 3 — conformance gate

Dispatch `gw-specchecker` on the *refined* prose — refinement can break
conformance that the draft satisfied. Two inputs only, plus the script's word
count; pipeline identity withheld. Write `runs/chNN/conformance-refined.md`.
On a FAIL row: two rounds back to `gw-lineeditor`, then the inbox. Nothing is
reported as refined while a FAIL row is open and unruled.

## Step 4 — distillation and the practice guide

`gw-lineeditor` produces two things here:

- `runs/chNN/distillation.md` — in the exact field format of
  `.claude/EDITORIAL-STANDARDS.md` section 4 (Mechanism, Conversation sentence,
  distillation, Lesson, Challenge, Practice). Compile reads the **fields**.
- this chapter's section appended to `runs/appendix/practice-guide.md` — the
  accumulating, reader-facing field guide. Confirm the append did not rewrite
  another chapter's section: the guide is shared across chapters, and the old
  pipeline lost ten Practice sections once because a generator looked for the
  wrong heading and nothing errored.

## Step 5 — report, then the bake-off

Report as in `/gw-draft` Step 5, plus any editor-vs-script discrepancy.

Then, if the old pipeline has a refined chapter at
`{bookRoot}/chapters/chNN/refined.md`, offer the comparison:

```
python3 scripts/bakeoff.py --chapter NN \
  --control {bookRoot}/chapters/chNN/refined.md \
  --variant runs/chNN/refined.md \
  --metaphor-family "<declared>"
```

Do not run it without saying what it does first: it writes two neutrally-named
variants and a sealed mapping, and the author reads them blind before learning
which is which.
