#!/usr/bin/env bash
# Stop: commit the work, log the session, then ask whether a retrospective is due.
# Order matters: the commit must land before retro-check counts commits.
#
# Only WORK paths are committed automatically. Rule files (.claude/skills,
# .claude/agents, CLAUDE.md, the docs) are not - editing the rules is a
# deliberate act the author should see as its own commit, and auto-committing
# them is how a rule change slips in unreviewed.
ROOT="${CLAUDE_PLUGIN_ROOT:-${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}}"
[ -z "$ROOT" ] && exit 0
cd "$ROOT" || exit 0

WORK="runs/ bakeoff/ inbox/ FINDINGS.md .claude/state/"

# Write the session log FIRST, so it rides in the same commit as the work.
# The first version committed the work, then wrote the log, then ran
# `git commit --amend` to fold it in - which amends whatever HEAD is. In a
# session that only edited rule files (committed deliberately, possibly already
# pushed), that rewrote the author's own commit and folded runs/log.md into it,
# rewriting pushed history - the one thing sync.py promises never to do. Order
# the steps instead; never amend.
python3 scripts/session_log.py 2>/dev/null || true

changed=$( (git diff --name-only -- $WORK; git ls-files --others --exclude-standard -- $WORK) 2>/dev/null )
if [ -n "$changed" ]; then
  git add -- $WORK 2>/dev/null
  git commit -q -m "auto: house artifacts updated $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || true
fi

# Push the session branch so nothing is ever stranded locally (a rule once sat
# unpushed for five weeks). Only a session/ branch, only in a remote session -
# main moves on the author's word alone, via sync.py --land.
cur=$(git symbolic-ref --short HEAD 2>/dev/null)
case "$cur" in
  session/*) [ "${CLAUDE_CODE_REMOTE:-}" = "true" ] && git push -u origin "$cur" --quiet 2>/dev/null || true ;;
esac

exec bash .claude/hooks/retro-check.sh
