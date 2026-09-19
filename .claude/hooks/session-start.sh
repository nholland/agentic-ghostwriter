#!/usr/bin/env bash
# SessionStart: branch hygiene first, then the board.
#
# Branch hygiene is ported from the book repo's proven hook, because every git
# failure in that repo's incident archive was a model following rule text, and
# every fix was a check that ran on its own:
#   - a session ran from a clone 13 commits behind main and bypassed the
#     freshness guard by hand;
#   - a rule sat on an unpushed branch for five weeks while chapters were
#     written without it;
#   - a branch scan that reasoned about commit counts misreported four branches
#     until it diffed actual trees.
# So this is a hook, not a desk. It runs whether or not anyone remembers it.
ROOT="${CLAUDE_PLUGIN_ROOT:-${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}}"
[ -z "$ROOT" ] && exit 0
cd "$ROOT" || exit 0

branch_msg=""
# A repo cloned while empty has no fetch refspec, so no fetch ever creates
# origin/* and every ahead/behind comparison silently errors. Write the standard
# refspec if it is missing before fetching. (Found when sync.py reported
# "0 ahead, 0 behind" against a ref that did not exist.)
git config --get remote.origin.fetch >/dev/null 2>&1 || git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ] && git fetch origin --quiet 2>/dev/null; then
  cur=$(git symbolic-ref --short HEAD 2>/dev/null || echo "")
  if [ -n "$cur" ] && git diff --quiet && git diff --cached --quiet; then
    if [ "$cur" = "main" ]; then
      nb="session/$(date +%Y%m%d-%H%M%S)"
      if git checkout -b "$nb" origin/main >/dev/null 2>&1; then
        branch_msg="On main at start - created and switched to '$nb' from origin/main. Work lands on main only when the author says so."
      fi
    else
      behind=$(git rev-list --count "$cur..origin/main" 2>/dev/null || echo 0)
      ahead=$(git rev-list --count "origin/main..$cur" 2>/dev/null || echo 0)
      if [ "$behind" -gt 0 ] && [ "$ahead" -eq 0 ]; then
        git merge origin/main --ff-only --quiet 2>/dev/null && branch_msg="'$cur' was $behind behind main - fast-forwarded."
      elif [ "$behind" -gt 0 ]; then
        branch_msg="'$cur' has DIVERGED from main ($ahead ahead, $behind behind). Not touched. Run: python3 scripts/sync.py --merge-main"
      fi
    fi
  fi
fi
git rev-parse HEAD > .claude/state/session-start-sha 2>/dev/null || true

{
  echo "=== The House ==="
  echo "Real clock: $(date '+%Y-%m-%d %H:%M %Z') - use this for every dated artifact. Never supply a plausible date."
  [ -n "$branch_msg" ] && echo "Branch: $branch_msg"
  python3 scripts/resolve_book.py 2>&1 | sed 's/^/  /'
  python3 scripts/next.py 2>&1 | sed 's/^/  /'
  # Non-blocking (Rule 4's spirit): report once at the door, never fail the
  # session over it. chapter_pdf_local.py already covers the gap this reports.
  tc=$(python3 scripts/toolcheck.py 2>&1)
  [ "$tc" != "toolcheck: all optional tools present." ] && echo "$tc" | sed 's/^/  /'
} 2>/dev/null
exit 0
