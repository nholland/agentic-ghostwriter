#!/usr/bin/env bash
# Batch at three new work commits; dispatch never consumes pending coverage.
ROOT="${CLAUDE_PLUGIN_ROOT:-${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}}"
[ -z "$ROOT" ] && exit 0
SCRIPT_ROOT=$(cd "$(dirname "$0")/../.." && pwd)
exec python3 "$SCRIPT_ROOT/scripts/retro_window.py" --repo "$ROOT" --dispatch
