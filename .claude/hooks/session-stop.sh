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
changed=$( (git diff --name-only -- $WORK; git ls-files --others --exclude-standard -- $WORK) 2>/dev/null )
if [ -n "$changed" ]; then
  git add -- $WORK 2>/dev/null
  git commit -q -m "auto: house artifacts updated $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || true
fi

python3 scripts/session_log.py 2>/dev/null || true
# session_log.py writes runs/log.md, which is a work path; fold it into the same commit
if ! git diff --quiet -- runs/log.md 2>/dev/null || git ls-files --others --exclude-standard -- runs/log.md 2>/dev/null | grep -q .; then
  git add -- runs/log.md 2>/dev/null && git commit -q --amend --no-edit 2>/dev/null || git commit -q -m "auto: session log $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || true
fi

exec bash .claude/hooks/retro-check.sh
