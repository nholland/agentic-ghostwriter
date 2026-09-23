# For Codex and other non-Claude agents

This house was built for Claude Code. `CLAUDE.md` is the constitution: read it
in full before doing anything, and follow it as written. This file only covers
what Claude Code does automatically and you must do by hand.

1. **Session start** (Claude's SessionStart hook): run
   `python3 scripts/resolve_book.py` and `python3 scripts/inbox.py`. Stop if
   `resolve_book.py` exits non-zero.
2. **Commands.** `/gw`, `/gw-chapter` and the rest are not built in. When the
   author types one, read `.claude/skills/<name>/SKILL.md` and follow it in full.
3. **Desks.** You cannot dispatch sub-agents. Run a desk in session by reading
   `.claude/agents/<desk>.md` and doing its job under its rules. Say which desk
   you are acting as. Say plainly that it did not run cold.
4. **The pauses are files.** Content concepts go to
   `runs/chNN/proposed-concepts.md` (`status: open`) and are shown to the author
   before anything else happens. Gap markers and source findings are written
   immediately (Rule 9). Never hold either in chat.
5. **Session end** (Claude's Stop hook): run `python3 scripts/sync.py --push`
   and name the branch. Never `--land` without the author's word.
