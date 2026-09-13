---
description: The Publisher runs a whole chapter through the house - interview, research, draft, refine, plate, verdict package - pausing only where the author is needed. The one command for one chapter. Resumable from wherever the chapter stopped. --shadow drafts cold from the book pipeline's existing brief, in parallel with it.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-chapter/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-chapter — one chapter, end to end

Argument: a chapter number, optionally `--from <stage>`, `--shadow`, or `--no-plate`. `$ARGUMENTS`

This is the handle the author actually holds. The desk-level commands
(`/gw-interview`, `/gw-research`, `/gw-draft`, `/gw-refine`) still exist for
re-running one stage; this one chains them and keeps the author out of the loop
everywhere he does not need to be in it. `/gw-floor` runs many chapters' cold
stages at once.

**You are the Publisher for the whole run.** Name every desk you dispatch. Never
dispatch the interview or a check-in to a sub-agent.

## Step 0 — where is this chapter?

```
python3 scripts/resolve_book.py
python3 scripts/okf_gate.py
```

Both blocking. Then ask the oracle where this chapter is — do not work it out
from the directory listing yourself:

```
python3 scripts/next.py --chapter NN
```

It returns the next stage, who runs it, and why. Say which stage you are
starting at. For reference, the rule it applies:

| Present | Start at |
|---|---|
| nothing, and no brief in the book repo | interview |
| nothing, and `{bookRoot}/chapters/chNN/research.md` exists | **draft, `--shadow`** (see below) |
| `interview.md` | research |
| `research.md` | draft (brief-gaps.md, if present, went to the inbox already) |
| `draft.md` | refine |
| `refined.md` | plate, then verdict |

`--from <stage>` overrides, for a deliberate re-run.

## `--shadow` — the parallel run

The book pipeline's research is the author in the room; the brief it produces
is the automation boundary already crossed. When that brief exists, this house
drafts from **the same file**, cold, into `runs/chNN/`, while the book pipeline
drafts its own. Zero extra author time, zero risk to the book, and at the end
`/gw-bakeoff NN` compares the two blind. This is the Chapter 12 plan.

In `--shadow`: skip the interview and research stages; `/gw-draft` reads
`{bookRoot}/chapters/chNN/research.md`; the plan-only brief review still runs
and its gap list is **recorded as a finding, not sent back** (the brief is the
book pipeline's, and if it was thin and their chapter shipped fine, the author
closed those gaps live - which is the measurement). Everything from the draft
onward is identical. The oracle offers `--shadow` on its own when the brief
exists; you never assume the brief is there.

## The three pauses, and no others

| Pause | Why it cannot run cold |
|---|---|
| **1. The interview** | The chapter's ideas come from the author here or they do not exist. (Skipped in `--shadow`.) |
| **2. Content concepts** | A concept capturing what he thinks is a claim only he can confirm (Rule 9). Small: show the `okf_new.py --dry-run` proposals, get a yes or a correction, continue. Gap markers do not pause. (Skipped in `--shadow`: the brief is not this house's.) |
| **3. The verdict** | Only he can say whether it landed. |

Everything else runs cold and gated. If a cold stage fails its gate twice,
stop, write the inbox item, and **tell him the chapter is parked and why** — do
not loop, and do not quietly pick an answer to keep moving:

```
python3 scripts/inbox.py --add "<what is stuck>" --raised-by <desk> --chapter NN \
    --context "<what he needs to answer cold>" --unblocks "<the ruling>"
```

That is the one inbox. `next.py` reads it and reports the chapter as parked;
`/gw-inbox` shows it. Nothing else is written to signal a stuck chapter.

## The sequence

1. **Interview** — follow `/gw-interview` in full. Pause 1.
2. **Research** — follow `/gw-research`: dispatch `gw-researcher`, then the
   Ghostwriter's plan-only review and `term_check.py` as the gates. Pause 2 on
   content concepts.
3. **Draft** — follow `/gw-draft`: `gw-ghostwriter`, then `voice_check.py`,
   then `gw-specchecker` (handed the script's word count).
4. **Refine** — follow `/gw-refine`: `gw-lineeditor`, then `voice_check.py`
   run independently, `gw-slopreader`, `gw-specchecker`, distillation and the
   practice-guide section.
5. **Plate** — first `python3 {bookRepo}/scripts/design_elements.py {bookRoot} --check`
   (regenerate if stale: the candidate register is derived and never reasoned
   around). Then dispatch `gw-designer` on the distillation, the declared
   metaphor family, and the design layer under `{bookRoot}/design/`. Skip with
   `--no-plate`. If this chapter is the last in its Part and the Part has no
   closing plate, the Designer may propose one in the Part idiom; that is a
   second product, offered, never assumed. A plate failure never blocks the
   chapter; it goes to the inbox. If `resolve_book.py` reported the design
   layer ABSENT, the Designer says so and proposes a `design-language.md`
   rather than inventing a style.
6. **Verdict package** — run `/gw-compile NN` to produce the PDF. Then hand him
   the package: the PDF, the plate, the counts as the scripts printed them, the
   conformance rows, and every inbox item raised during the run. Pause 3.

## After the verdict

- If the book pipeline also has this chapter, offer `/gw-bakeoff NN`.
- Record in `FINDINGS.md`: which pauses happened, how many gate rounds each cold
  stage took, every inbox item, and any discrepancy between a desk's
  self-reported count and the script's. One honest entry per chapter.

## What this command never does

Write inside the book repo's constitution or `chapters/` tree. Skip a gate
because the prose read clean. Resolve an inbox item on his behalf. Report a
count from memory. Start a shadow run without saying that is what it is.
