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

# NOT .claude/state/: that is per-container scratch, now gitignored. Adding it
# here is what turned every session start into an empty "auto:" commit.
WORK="runs/ bakeoff/ inbox/ FINDINGS.md"
changed=$( (git diff --name-only -- $WORK; git ls-files --others --exclude-standard -- $WORK) 2>/dev/null )
if [ -n "$changed" ]; then
  git add -- $WORK 2>/dev/null
  git commit -q -m "auto: house artifacts updated $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || true
fi

python3 scripts/session_log.py 2>/dev/null || true
# session_log.py writes runs/log.md, which is a work path; fold it into the same commit
if ! git diff --quiet -- runs/log.md 2>/dev/null || git ls-files --others --exclude-standard -- runs/log.md 2>/dev/null | grep -q .; then
  git add -- runs/log.md 2>/dev/null
  # Amend ONLY while HEAD is unpublished. Amending a pushed commit rewrote
  # history on every push of 2026-09-14 (six --force-with-lease in one session,
  # against sync.py's own "never rewrites history"), and orphaned every SHA in
  # runs/log.md: 9 of 9 existed but were no ancestor of HEAD.
  cur_b=$(git symbolic-ref --short HEAD 2>/dev/null)
  if [ -n "$cur_b" ] && git merge-base --is-ancestor HEAD "origin/$cur_b" 2>/dev/null; then
    git commit -q -m "auto: session log $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || true
  else
    git commit -q --amend --no-edit 2>/dev/null || git commit -q -m "auto: session log $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || true
  fi
fi

# Push the working branch so nothing is ever stranded locally (a rule once sat
# unpushed for five weeks). ANY branch but main - the old session/* glob matched
# nothing in a cloud container, which names branches claude/<name>, so the net
# was inert in the one environment that reclaims the disk. main still moves on
# the author's word alone, via sync.py --land.
cur=$(git symbolic-ref --short HEAD 2>/dev/null)
case "$cur" in
  main|"") : ;;
  *) [ "${CLAUDE_CODE_REMOTE:-}" = "true" ] && git push -u origin "$cur" --quiet 2>/dev/null || true ;;
esac

# Derived files must have a deriving script AND the check must have a caller -
# sync_plugin_layout.py's own docstring says so, and until now it had neither.
# Nothing here rewrites anything: they report, the Publisher acts.
# One list, not one line per generated file. Adding the next derived artifact
# should cost an entry here, not another line of shell - a bespoke line per file
# is how the third one quietly never gets added. Each entry is
# script|what is stale|what to do about it.
# The stored fixtures. Two checks written on 2026-09-17 each contained the defect
# they were written to fix, because each was proved by a one-off run nobody kept.
# These are those proofs, kept. Unconditional (#027): a `git diff --quiet HEAD`
# guard here skipped in 5 of 6 real tree states, including the normal end of a
# session - the author commits the very check he edited, then the guard sees a
# clean tree and never runs it. The run is 0.3s; the guard cost more than it saved.
if ! out=$(python3 tests/run.py 2>&1); then
  echo "FIXTURES FAILING: a check no longer catches what it was written to catch." >&2
  echo "$out" | tail -20 >&2
fi

DERIVED="
scripts/sync_plugin_layout.py|the plugin-layout copies under agents/ and skills/|python3 scripts/sync_plugin_layout.py
scripts/manual.py|docs/manual.html - the roster, commands, scripts or thresholds changed|python3 scripts/manual.py, then republish the artifact so the author's link is not stale
scripts/build_diagrams_page.py|docs/diagrams.html - a drawing or caption changed|python3 scripts/build_diagrams_page.py, then republish the artifact
"
drift=""
while IFS='|' read -r script what fix; do
  [ -z "$script" ] && continue
  python3 "$script" --check >/dev/null 2>&1 || drift="${drift}${what} (${fix}). "
done <<EOF
$DERIVED
EOF
[ -n "$drift" ] && echo "DERIVED FILES STALE: ${drift}Regenerate before closing, then tell the author what changed." >&2

exec bash .claude/hooks/retro-check.sh
