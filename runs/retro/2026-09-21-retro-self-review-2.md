# Archivist — 2026-09-21 01:14 — the second self-review in one hour

**Window:** `84b79969..0074d6e3` (read from `.claude/state/retro-window`, per #030).
Two commits: `f194db48` "Archivist review of plate_packet.py" and `0074d6e3`
"auto: session log". **No work was done in this window.** It is the prior
retrospective's own output plus Stop-hook bookkeeping — the exact self-referential
shape inbox **#074** already named and proposed a fix for, still open.

Three lines would be the honest report. There is one substantive finding, and it is
about #074's fix rather than about this window, so it follows.

---

## The question asked: would #074's fix have prevented this dispatch?

**Only under one of its two readings — and its close-condition cannot tell them apart.**

`f194db48` touches `inbox/075`, `inbox/076`, and `runs/retro/2026-09-21-plate-packet.md`.
It is a *mixed* commit: a retro's prose **and** the watched `inbox/` filings that are
the Archivist's only durable output. Measured on this window:

```
current rule COUNT           = 1     (dispatches)
(b) pathspec ':!runs/retro/' = 1     (still dispatches — NOT a fix)
(a) commit-level filter      = 0     (skipped — the fix)
```

`retro-check.sh` never watched `runs/` in the first place, so a pathspec exclusion is
a no-op: the commit still counts through `inbox/`. Only dropping the whole commit when
it carries a `runs/retro/` file closes the loop.

#074 *meant* (a) — its evidence windows `908a2ef` and `9332607` are both mixed commits
(inbox + retro), and it reports `new=0` for them, which only (a) produces. Its diagnosis
and its measurements are sound.

**What is not sound is how it closes.** Its `--applied-by` is

```
grep -rq 'retro dispatch skips a commit carrying runs/retro/' tests/
```

a grep for its own sentence. That exits 0 for (b) implemented under an (a)-sounding
fixture name, and for the string sitting in a comment. This is the lens the charter
names outright: *a proposal that adds or fixes a check closes on its fixture, never on
a grep for its own text* — the shape that closed green over two half-fixes before.

**What recurs.** Eight consecutive `gw-retro` items now carry grep-shaped proofs
(#062, #063, #064, #071, #072, #073, #074, and #077/#075 as `test -d` stubs). #074
attributes this to #048 — `prove.py` cannot prove a case that does not exist yet.
That is true of `prove.py`, but it is **not** true here, and the belief is costing
real proof strength:

- `tests/run.py` already contains `retro_window_cases()`, which builds a real temp
  git repo and **runs `retro-check.sh` itself** (line ~1260). The harness #074 needs
  exists; a mixed-commit case is three lines inside it.
- The actual blocker is narrower: `python3 tests/run.py` passes **107/107, exit 0**
  today, so naming it alone as `--applied-by` is tautological (#052's shape). That is
  a reason to write a *discriminating* proof, not a reason to fall back to grep.

## Lenses

- **What broke.** Nothing in this window. No prose, no book, no desk ran.
- **What was missing.** A close-condition on #074 that can distinguish its fix from
  the non-fix that shares its wording. Proposed below.
- **What was too hard.** Filing an honest fixture-backed proof: `inbox.py` requires
  `--prove-file/--prove-at/--prove-case` whenever a `gw-retro` `--applied-by` names
  `tests/run.py`, and `prove.py` refuses a not-yet-existing case (#048). The path of
  least resistance is a grep, and eight items took it.
- **What worked.** The #030 lineage rule earned itself again. The dispatch prose named
  the range as `f194db4c...0074d6e3`; `f194db4c` is not a commit in this repo
  (`git log f194db4c..0074d6e3` → *fatal: ambiguous argument*). Reading
  `.claude/state/retro-window` rather than the dispatch's prose gave the correct bounds
  with no guessing. `retro-window` was also written correctly and matched the dispatch.
- **What recurs.** The retro-reviews-a-retro loop, now third in the last five
  dispatches. Of the last ten commits, four are Archivist reviews and two are real work
  (`83bede5` plate_packet.py, `1543f17` manual republish). State today: 20 dispatch
  markers against 15 retro docs.

## Not proposed

No rule edit. No new desk, skill or check beyond the one fixture. Nothing to delete.
Corpus measured at **18,540 words** (`cat CLAUDE.md .claude/agents/*.md
.claude/skills/*/SKILL.md | wc -w`), up from 17,017 on 2026-09-19 — noted, not acted
on; none of this session's growth is rule text.

I am not re-filing the loop finding. #074 owns it. This asks only that it close on
something that cannot lie.

## Proposal

**Type:** new check with a caller (fixture), replacing #074's grep close-condition.
**Cost:** the hook's rule-text delta is #074's already-measured +17 words (8-word count
line → 25-word block); the fixture case body is **unmeasured** — I have not drafted it.
**What it replaces:** the `grep -rq` proof on #074, and nothing else.

```
python3 scripts/inbox.py --add "#074's fix is right but its proof cannot tell the fix from the non-fix: 'skip commits touching runs/retro/' as a pathspec exclusion still dispatches, because the retro's inbox filings are themselves watched. Should #074 close on a mixed-commit fixture in retro_window_cases() instead of a grep for its own sentence?" \
    --raised-by gw-retro --chapter 0 \
    --context "retro-check.sh never watched runs/, so ':!runs/retro/' is a no-op and the loop continues; only dropping the whole commit works. #074's applied_by greps tests/ for its own wording, which exits 0 over either implementation. Eight consecutive gw-retro items now carry grep-shaped proofs on the belief that #048 forbids fixtures here, but tests/run.py's retro_window_cases() already runs retro-check.sh against a real temp repo." \
    --unblocks "Whether the retro loop's fix is verified by behaviour or by wording, and whether the eight-item grep-proof habit ends where a harness already exists" \
    --recommend "Yes: implement #074 as a commit-level filter, add a mixed commit (inbox/ + runs/retro/ in one commit) to retro_window_cases(), and close both items on the behavioural proof below rather than on grep" \
    --evidence "Window 84b79969..0074d6e3, sole work commit f194db48 touches inbox/075, inbox/076, runs/retro/2026-09-21-plate-packet.md. WATCHED='bakeoff/ inbox/ scripts/ config/ books/ FINDINGS.md'. git rev-list --count 84b79969..0074d6e3 -- \$WATCHED -> 1 (dispatches). Same with ':!runs/retro/' appended -> 1 (still dispatches). Commit-level filter dropping any commit containing a runs/retro/ path -> 0 (skipped). python3 tests/run.py -> 107/107 fixtures pass, exit 0, so tests/run.py alone as applied_by is tautological. tests/run.py:1270 already resolves .claude/hooks/retro-check.sh and runs it via subprocess against a temp git repo." \
    --applied-by "R=\$(git rev-parse --show-toplevel); T=\$(mktemp -d); git -C \"\$R\" worktree add -q --detach \"\$T\" 0074d6e3 >/dev/null 2>&1; mkdir -p \"\$T/.claude/state\"; echo 84b79969b60fbad3f61147b68f4dbbc01b0deeff > \"\$T/.claude/state/retro-last-sha\"; rc=0; CLAUDE_PROJECT_DIR=\"\$T\" bash \"\$R/.claude/hooks/retro-check.sh\" >/dev/null 2>&1 || rc=\$?; git -C \"\$R\" worktree remove --force \"\$T\" >/dev/null 2>&1; test \"\$rc\" -ne 2"
```

The `--applied-by` replays **this exact window** against the current hook in a throwaway
worktree and passes only when the hook stops dispatching on it. Verified red today:
`hook exit=2`, command exit 1. It names no file and greps no text, so it cannot be
satisfied by wording — and because it does not name `tests/run.py`, it does not trip the
`--prove-file` guard that pushed the last eight items to grep. The fixture is still
required by the recommendation; the proof is simply stronger than the fixture.

## Looked at, clean

`retro-window` (correct bounds, matched the dispatch), `retro-last-sha` (advanced to
HEAD as designed), the `runs/log.md` diff (9 lines, Stop hook, accurate), `#071`'s
window-consumption concern (did not recur here), `#075`/`#076` as filed (well-formed,
both carry non-tautological `--applied-by`), `tests/run.py` (107/107 green).
