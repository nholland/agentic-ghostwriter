#!/usr/bin/env bash
# Stop hook, last step: if this SESSION touched the work, ask the Publisher to
# dispatch the Archivist - once per session.
#
# Per session, not every N commits. The old pipeline's threshold existed to stop
# a loop: retrospectives edited rule files, rule-file edits counted toward the
# next retrospective, and the ledger grew 8x in 27 days. That loop is broken at
# the root here - the Archivist never applies, and rule paths are not watched -
# so frequency is no longer the danger, and the author asked to learn from each
# session. The damper that remains is the desk's own: nothing substantive,
# three lines, stop.
ROOT="${CLAUDE_PLUGIN_ROOT:-${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}}"
[ -z "$ROOT" ] && exit 0
cd "$ROOT" || exit 0

STATE=".claude/state"; mkdir -p "$STATE"
START=$(cat "$STATE/session-start-sha" 2>/dev/null)
HEAD_SHA=$(git rev-parse HEAD 2>/dev/null)
[ -z "$HEAD_SHA" ] && exit 0
[ -z "$START" ] && START="$HEAD_SHA~1"
git merge-base --is-ancestor "$START" "$HEAD_SHA" 2>/dev/null || exit 0

# once per session
DONE="$STATE/retro-done-$(echo "$START" | cut -c1-12)"
[ -f "$DONE" ] && exit 0

# The WORK, never the rules. .claude/, CLAUDE.md and the docs are excluded on purpose.
WATCHED="runs/ bakeoff/ inbox/ scripts/ config/ FINDINGS.md"
COUNT=$(git rev-list --count "$START..$HEAD_SHA" -- $WATCHED 2>/dev/null); COUNT=${COUNT:-0}
[ "$COUNT" -ge 1 ] || exit 0

touch "$DONE"
echo "SESSION REVIEW: this session made $COUNT commit(s) touching the work. Before closing, dispatch the Archivist (agent gw-retro) to review it cold - what broke, what was missing, what was too hard, what worked, what recurs - and show the author its suggestions. It proposes; you apply nothing without his yes. If it reports nothing substantive, pass that on in one line and move on. Then tell him where his work is: which branch, whether it is pushed, and whether it is on main." >&2
exit 2
