#!/usr/bin/env bash
# PreToolUse guard on writes under any okf/ bundle.
#
# WHY A HOOK
#   Every wrong date in the book's record was typed by hand; the validator can
#   only catch a date that has not happened yet, and a date stamped a few days
#   early looks ordinary forever. This runs on every Write/Edit that touches an
#   okf/**/*.md concept, without anyone remembering it:
#
#     - a NEW concept file written by hand is refused: use scripts/okf_new.py,
#       which reads the clock and runs the validator;
#     - a `timestamp:` line in new content must be TODAY, unless it is the
#       unchanged timestamp the file already carries (rewriting an existing
#       concept keeps its history; only a fresh stamp must be honest).
#
#   Exit 2 blocks the tool call and shows the reason. Anything else lets it through.
#   The reserved files (index.md, log.md, README.md) are exempt.
set -u
INPUT=$(cat)
python3 - "$INPUT" <<'PY'
import json, os, re, subprocess, sys
try:
    data = json.loads(sys.argv[1])
except Exception:
    sys.exit(0)
ti = data.get("tool_input") or {}
path = ti.get("file_path") or ti.get("path") or ""
if not re.search(r"(^|/)okf/[^/]+/[^/]+\.md$", path.replace("\\", "/")):
    sys.exit(0)
base = os.path.basename(path)
if base in ("index.md", "log.md", "README.md"):
    sys.exit(0)
tool = data.get("tool_name", "")
new_text = ti.get("content") if tool == "Write" else (ti.get("new_string") or "")
if tool == "MultiEdit":
    new_text = "\n".join(e.get("new_string", "") for e in ti.get("edits", []))
if not new_text:
    sys.exit(0)
today = subprocess.run(["date", "+%Y-%m-%d"], capture_output=True, text=True).stdout.strip()
exists = os.path.isfile(path)
existing_stamp = None
if exists:
    try:
        m = re.search(r"^timestamp:\s*['\"]?(\d{4}-\d{2}-\d{2}[^'\"\n]*)", open(path, encoding="utf-8").read(), re.M)
        existing_stamp = m.group(1) if m else None
    except OSError:
        pass
if tool == "Write" and not exists and new_text.lstrip().startswith("---"):
    print("okf-timestamp-guard: BLOCKED. A new OKF concept is created with "
          "`python3 scripts/okf_new.py --type ... --title ...` (which reads the clock and runs the "
          "validator), never written by hand. Use --dry-run to propose it first.", file=sys.stderr)
    sys.exit(2)
for m in re.finditer(r"^timestamp:\s*['\"]?(\d{4}-\d{2}-\d{2})", new_text, re.M):
    stamp = m.group(1)
    if existing_stamp and existing_stamp.startswith(stamp):
        continue  # unchanged history
    if stamp != today:
        print(f"okf-timestamp-guard: BLOCKED. timestamp {stamp} is not today ({today}). "
              f"Read the clock: date '+%Y-%m-%d %H:%M'. A plausible date passes every format check "
              f"and looks correct forever; that is why this runs on every write.", file=sys.stderr)
        sys.exit(2)
sys.exit(0)
PY
