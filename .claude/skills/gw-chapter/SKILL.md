---
description: The Publisher runs a whole chapter through the house - interview, research, draft, refine, plate, verdict package - pausing only where the author is needed. The one command for one chapter. Resumable from wherever the chapter stopped.
---

# /gw-chapter — one chapter, end to end

Argument: a chapter number, optionally `--from <stage>` or `--no-plate`. `$ARGUMENTS`

This is the handle the author actually holds. The desk-level commands
(`/gw-interview`, `/gw-research`, `/gw-draft`, `/gw-refine`) still exist for
re-running one stage; this one chains them and keeps the author out of the loop
everywhere he does not need to be in it.

**You are the Publisher for the whole run.** Name every desk you dispatch. Never
dispatch the interview or a check-in to a sub-agent.

## Step 0 — where is this chapter?

```
python3 scripts/resolve_book.py
python3 scripts/okf_gate.py
```

`resolve_book.py` is blocking. The citation gate **reports** and does not stop the run (Rule 4): an unverified citation is unfinished work, not a defect. A structural failure there still blocks.
from the directory listing yourself:

```
python3 scripts/next.py --chapter NN
```

It returns the next stage and why. Say which stage you are starting at. For
reference, the rule it applies:

| Present | Start at |
|---|---|
| nothing | interview |
| `interview.md` | research |
| `research.md` (and no `brief-gaps.md` outstanding) | draft |
| `draft.md` with conformance passed | refine |
| `refined.md` | plate, then verdict |

`--from <stage>` overrides, for a deliberate re-run.

## The three pauses, and no others

| Pause | Why it cannot run cold |
|---|---|
| **1. The interview** | The chapter's ideas come from the author here or they do not exist. |
| **2. Content concepts** | A concept capturing what he thinks is a claim only he can confirm (Rule 9 in `CLAUDE.md`). Small: show, get a yes or a correction, continue. Gap markers do not pause. |
| **3. The verdict** | Only he can say whether it landed. |

Everything else runs cold and gated. If a cold stage fails its gate twice, stop,
write the inbox item, and **tell him the chapter is parked and why** — do not
loop, and do not quietly pick an answer to keep moving. The two-touch design
fails in exactly one hard-to-notice way, and that is it.

## The sequence

1. **Interview** — follow `/gw-interview` in full. Pause 1.
2. **Research** — follow `/gw-research`: dispatch `gw-researcher`, then the
   Ghostwriter's plan-only review as the gate. Pause 2 on content concepts.
3. **Draft** — follow `/gw-draft`: `gw-ghostwriter`, then `voice_check.py`,
   then `gw-specchecker`.
4. **Refine** — follow `/gw-refine`: `gw-lineeditor`, then `voice_check.py`
   run independently, `gw-slopreader`, `gw-specchecker`, distillation.
5. **Plate** — dispatch `gw-designer` on the distillation and the declared
   metaphor family. Skip with `--no-plate`. A plate failure never blocks the
   chapter; it goes to the inbox.
6. **Verdict package** — run `/gw-compile NN` to produce the PDF. Then hand him
   the package: the PDF, the plate, the counts as the scripts printed them, the
   conformance rows, and `python3 scripts/inbox.py --all --chapter NN` for every
   inbox item this chapter raised — run it, don't recall it (a hand-enumerated
   list of Ch12's items disagreed with the script by 7, silently, until a fixed
   `--chapter` filter existed). Pause 3.

## After the verdict

- **Write `runs/chNN/verdict.md`** the moment he actually gives it — his words,
  the real clock. `next.py` treats this file as the chapter's only exit from
  "verdict": without it, the oracle reports this chapter waiting on him forever,
  even once a later chapter is fully refined beside it (inbox #028). Do not
  write it before he has given the verdict, and never on a re-run that only
  reproduces the package.
- If the old pipeline also has this chapter, offer `/gw-bakeoff NN`.
- Record in `FINDINGS.md`: which pauses happened, how many gate rounds each cold
  stage took, `scripts/inbox.py --all --chapter NN`'s count (paste it, don't
  restate it from memory), and any discrepancy between a desk's self-reported
  count and a script's. One honest entry per chapter.

## What this command never does

Write inside the book repo. Skip a gate because the prose read clean. Resolve
an inbox item on his behalf. Report a count from memory.
