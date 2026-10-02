# Codex entry to the same house

Read `CLAUDE.md` in full and `.claude/RUNTIME.md`. They are the shared house
instructions; Codex is another runtime for this repository, not another pipeline.
Explicit author instructions take precedence over skill guidelines.

1. Run `python3 scripts/resolve_book.py` and `python3 scripts/inbox.py` at
   session entry. Stop if the book resolver fails. Read
   `python3 scripts/runtime_handoff.py resume` before continuing production.
2. Use `$gw` or the author's `/gw` intent. Skills under `.agents/skills` link to
   canonical `.claude/skills`; follow the selected skill in full, treating the
   words after the invocation as its arguments. Never compute next yourself.
3. Keep Publisher and Developmental Editor in session. Dispatch the named cold
   desks with fresh context and explicit inputs, without the author transcript.
   Use the isolated conformance runner when only two inputs may be visible.
   If cold delegation is unavailable, report it; never call an in-session read cold.
4. Save unfinished work and failed gate attempts through `runtime_handoff.py`.
   Pending concepts and verdicts, knowledge receipts, and retry limits survive
   runtime changes. Do not let chat acknowledgments substitute for files.
5. Stop desks and let the shared Stop hook save the handoff and release ownership
   before switching. Suggest the Archivist when work is ready to commit; a commit
   request includes his pre-commit review. Commits and pushes are explicit.
   If hooks are unavailable, run the equivalent mechanics
   explicitly and report that limitation. `scripts/sync.py --push` saves this
   branch; name it. Never `--land` without the author's explicit instruction.
