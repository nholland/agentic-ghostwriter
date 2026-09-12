#!/usr/bin/env bash
# Prints the real clock, the resolved book, and the inbox at every session
# start. The clock line exists because of Rule 9: an invented date passes
# every format check and looks correct forever.
ROOT="${CLAUDE_PLUGIN_ROOT:-${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}}"
[ -z "$ROOT" ] && exit 0
cd "$ROOT" || exit 0
{
  echo "=== The House ==="
  echo "Real clock: $(date '+%Y-%m-%d %H:%M %Z') - use this for every dated artifact. Never supply a plausible date."
  python3 scripts/resolve_book.py 2>&1 | sed 's/^/  /'
  python3 scripts/inbox.py 2>&1 | head -20 | sed 's/^/  /'
} 2>/dev/null
exit 0
