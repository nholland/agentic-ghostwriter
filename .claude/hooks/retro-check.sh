#!/usr/bin/env bash
# Ported from the book repo's .claude/hooks/retro-check.sh, with the paths and
# the questions adapted to this house. The mechanism is unchanged and the
# reasoning behind it is worth keeping verbatim:
#
#   Watch the WORK, not the rules that govern it. When rule-file paths were
#   watched, editing the ruleset counted toward the threshold that triggered
#   the next rule-editing retrospective - a loop with no damping and no
#   deletion path. LEARNINGS.md went from 739 to 6,026 words in 27 days, and
#   five of nine consecutive sessions were spent on pipeline maintenance
#   rather than on the book. A retrospective should be triggered by writing,
#   not by its own output.
#
# Fires at the hook layer so it survives context compaction and does not
# depend on which skill the author happened to run.

ROOT="${CLAUDE_PLUGIN_ROOT:-${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}}"
[ -z "$ROOT" ] && exit 0
cd "$ROOT" || exit 0

STATE_DIR=".claude/state"
MARKER_FILE="$STATE_DIR/retro-marker.txt"
THRESHOLD_FILE="$STATE_DIR/retro-threshold.txt"
DEFAULT_THRESHOLD=12
mkdir -p "$STATE_DIR"

THRESHOLD="$DEFAULT_THRESHOLD"
if [ -f "$THRESHOLD_FILE" ]; then
  READ_THRESHOLD=$(cat "$THRESHOLD_FILE" 2>/dev/null)
  case "$READ_THRESHOLD" in
    ''|*[!0-9]*) ;;
    *) THRESHOLD="$READ_THRESHOLD" ;;
  esac
fi

HEAD_SHA=$(git rev-parse HEAD 2>/dev/null)
[ -z "$HEAD_SHA" ] && exit 0

if [ ! -f "$MARKER_FILE" ]; then
  echo "$HEAD_SHA" > "$MARKER_FILE"
  exit 0
fi
MARKER_SHA=$(cat "$MARKER_FILE" 2>/dev/null)

# The marker must be an ancestor of HEAD, not merely an existing object, or a
# squash-merge cycle makes rev-list compare two unrelated points.
if [ -z "$MARKER_SHA" ] || ! git merge-base --is-ancestor "$MARKER_SHA" "$HEAD_SHA" 2>/dev/null; then
  echo "$HEAD_SHA" > "$MARKER_FILE"
  exit 0
fi

# The work: shadow-run outputs, bake-offs, the inbox, and the production
# scripts. NOT .claude/, CLAUDE.md, README.md, ARCHITECTURE.md, FLOW.md.
WATCHED_PATHS="runs/ bakeoff/ inbox/ scripts/ config/"
COUNT=$(git rev-list --count "$MARKER_SHA..$HEAD_SHA" -- $WATCHED_PATHS 2>/dev/null)
COUNT=${COUNT:-0}

if [ "$COUNT" -ge "$THRESHOLD" ] 2>/dev/null; then
  echo "$HEAD_SHA" > "$MARKER_FILE"
  echo "RETRO CHECK: $COUNT commits have touched the work ($WATCHED_PATHS) since the last retrospective. Before continuing, dispatch the Archivist (agent gw-retro) to run it cold, then show the author its proposals - do not apply them yourself. It answers THREE questions, in this order:

(1) WHICH EXISTING RULES DID WE VIOLATE OR IGNORE, AND WHY? Answer this first and honestly. A rule that is routinely bypassed is mis-placed (the stage that needs it cannot see it), mis-specified, or dead. This is usually the more valuable question, and on the old pipeline it was never asked: a stage that could not check a chapter against its own spec was visible for six chapters and no retrospective surfaced it, because every retrospective only looked for rules to add.

(2) DID A COLD DESK DECIDE SOMETHING SILENTLY THAT SHOULD HAVE GONE TO THE INBOX? This is the failure mode specific to this house. The two-touch design works only if everything a cold desk could not decide reaches the author. Look for judgement calls resolved inside a desk's output that he never saw. Also: did the script's count and the desk's self-reported count ever disagree? That discrepancy is a finding.

(3) What is worth promoting into a rule? Content-quality patterns, mechanics gaps, framework drift.

RETROSPECTIVES ARE NET-ZERO BY DEFAULT. A proposed rule must name the rule it replaces or a deletion candidate. If you cannot name one, propose it as an open item instead. The instruction corpus here is ~9,900 words against ~82,800 on the old pipeline; the whole point of this house is that it does not grow for free.

Prefer fixing a rule's PLACEMENT over adding a rule. Most failures have been a rule that existed but was invisible to the stage that needed it.

Propose concrete file updates to the author; do not apply them without asking. If nothing substantive surfaced, say so and move on. Log findings to FINDINGS.md, an incident ARCHIVE, not a ruleset: durable rules belong in the desk or skill that enforces them. Tune .claude/state/retro-threshold.txt (currently $THRESHOLD) if this fires too often or too rarely." >&2
  exit 2
fi
exit 0
