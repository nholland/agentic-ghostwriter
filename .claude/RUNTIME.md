# One house, two runtimes

Claude Code and Codex operate the same repository, branch, book, apparatus,
inbox, and production scripts. `.claude/` remains the canonical instruction
source; edit it from either runtime and run `scripts/sync_plugin_layout.py`.
Codex discovers the same skills through `.agents/skills` links and reads the
generated `.codex/agents/*.toml` desk adapters. Do not install a second copy of
this house's skills globally. A packaged manifest is supplied for distribution;
the working project needs no separate plugin installation.

## Resume and handoff

Start hooks read `runs/handoff.json`; `scripts/next.py` still decides what is
next. Read its referenced chapter and intake files before continuing. Intake is
the author's exact words, not approval inferred by a script. Reconcile relevant
knowledge under `.claude/OKF.md` before completion. Chat transcripts are separate.

During an interview or unfinished edit, save the current chapter and unfinished
work with `python3 scripts/runtime_handoff.py checkpoint --chapter N --note-file
PATH`. Use a note file with the author's words, outstanding questions, assigned
artifact paths, and unfinished work; do not replace the interview record with
this note. Save after meaningful progress, not only at the end of the turn.

When a gate fails, record `python3 scripts/runtime_handoff.py attempt --chapter
N --desk gw-X` before retrying. Count across runtimes; two failures go to the
inbox. The checkpoint is a continuation aid, never a new source of approvals or
evidence. Changed input hashes require fresh checks. Pending concepts and
verdicts remain pending, and existing review.json validation still applies.

Stop all desks before switching. The Stop hook only saves the checkpoint and
releases writer ownership. It does not run checks, tests, commits, logging,
pushes, generated-file checks or retrospective dispatch. Run relevant checks
during the work. Before committing, call the Archivist with
`scripts/archivist_check.py`; session records use its explicit `--record` tool
after the work commit. Commit and push explicitly when asked.
Open this same checkout in the other runtime and say `/gw` (Claude) or `$gw`
(Codex); both accept the same intent after the command. No branch switch is
needed. Never leave one runtime writing while the other resumes.

The hooks reject a second active session. After an interruption the lease stays
held because desks may still run. The Publisher must stop the old desks first;
for a crashed session on the same boot run `python3 scripts/runtime_handoff.py recover
--stopped-session SESSION` with the exact id reported by the hook. This releases
ownership, preserves all files, and does not declare partial work complete.

Writer leases record the local host and operating-system boot identity. After
a confirmed reboot on that host, startup and writer claims automatically retire
the old lease, including desks that could not survive the reboot, and preserve
the old ownership evidence in `.claude/state/runtime-recovery.json`. Unknown
boot identity, a different host, and legacy unmarked leases never permit automatic
takeover. A matching live session upgrades its legacy lease on its next claim.

`SessionEnd` releases its own writer only when no desks remain recorded active
(otherwise the last desk's Stop releases it, unless the main session resumes);
it preserves the last checkpoint and unfinished files without declaring completion
checks passed. `Interrupt` retains ownership because a tool or desk may still run.
Repeated or late Stop/SubagentStop events never acquire ownership or release a
new writer. A failed checkpoint retains ownership until safe session end or
explicit recovery; switching chats alone does not end a session immediately.
Stop and SessionEnd errors retain their cause in ignored
`.claude/state/runtime-hook-failure-<event>.json` diagnostic records.

## Codex desks

Publisher and Developmental Editor stay in the author-facing session. Dispatch
the other named desks with fresh context and explicit artifact inputs. Never
fork the author conversation into a cold desk. Do not launch both writers on
the same output or append shared files concurrently.

The conformance checker must receive only the outline section and prose. Use
`scripts/cold_review.py` for a fresh Codex conformance read with retrieval tools
disabled and only the two text inputs supplied. Other
reviewers' read-only settings and tool hooks are guardrails; do not claim they
are a complete filesystem isolation boundary. If a client cannot preserve cold
context, report it and use the isolated runner, rather than silently reviewing
in the author's session. The Publisher writes read-only reviewers' reports.

Codex project defaults request GPT-6 Astra at low reasoning effort. Check the
effective model in the desktop task because explicit session selection can
override the project default. Live Claude/Codex chapter quality and complete
chapter handoffs require an actual author-supervised production run; fixture
tests alone do not prove literary quality.
