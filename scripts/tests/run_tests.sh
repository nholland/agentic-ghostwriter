#!/usr/bin/env bash
# The engine's test harness. Every script is run against a fixture where the
# right answer is already known, and the answer is asserted.
#
# WHY THIS EXISTS
#   FINDINGS.md records eight defects in one week that shared a single shape: a
#   plausible number, no error, caught only by running the script where the
#   right answer was known. This makes that catch mechanical. The book repo had
#   one such test (test_citation_axes.sh) and it found real regressions; the
#   engine had none for ten scripts. A check that calls itself enforcement must
#   have a caller, and a script that calls itself correct must have a test.
#
# Usage: bash scripts/tests/run_tests.sh        (exit 0 = all green)
set -uo pipefail
cd "$(dirname "$0")/../.."
ENGINE="$(pwd)"
FIX="$ENGINE/scripts/tests/fixtures"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Point every script at the fixture book and a scratch state tree. Discovery is
# off so a real book repo next door cannot rescue a deliberately broken fixture.
cp -r "$FIX/book" "$TMP/book"
export GW_BOOK_REPO="$TMP/book" GW_NO_DISCOVERY=1 GW_STATE_ROOT="$TMP/state"
mkdir -p "$GW_STATE_ROOT"
unset GW_BOOK_SLUG

pass=0; fail=0
ok()   { pass=$((pass+1)); echo "  ok   $1"; }
bad()  { fail=$((fail+1)); echo "  FAIL $1"; [ -n "${2:-}" ] && echo "       $2"; }
expect_exit() { # name expected actual
  if [ "$2" = "$3" ]; then ok "$1"; else bad "$1" "expected exit $2, got $3"; fi; }
expect_grep() { # name pattern text
  if echo "$3" | grep -qE "$2"; then ok "$1"; else bad "$1" "missing /$2/ in: $(echo "$3" | head -5)"; fi; }
expect_nogrep() {
  if echo "$3" | grep -qE "$2"; then bad "$1" "unexpected /$2/"; else ok "$1"; fi; }

echo "== resolve_book"
out=$(python3 scripts/resolve_book.py 2>&1); rc=$?
expect_exit "fixture resolves" 0 $rc
expect_grep "reports the active book" "Test Book" "$out"
expect_grep "reports the design layer" "design layer: 1 marks, 0 concept plates, 0 Part closing plates, candidate register present" "$out"
mv "$TMP/book/books/test-book/design" "$TMP/design.bak"
out=$(python3 scripts/resolve_book.py 2>&1)
expect_grep "an absent design layer is said, not assumed" "design layer: ABSENT" "$out"
mv "$TMP/design.bak" "$TMP/book/books/test-book/design"
out=$(python3 scripts/resolve_book.py --list-books 2>&1); rc=$?
expect_grep "lists the registry" "test-book .*1/3 refined" "$out"
out=$(GW_BOOK_SLUG=nope python3 scripts/resolve_book.py 2>&1); rc=$?
expect_exit "unknown --book slug is a problem" 1 $rc
mv "$TMP/book/books/test-book/01-voice.md" "$TMP/voice.bak"
out=$(python3 scripts/resolve_book.py 2>&1); rc=$?
expect_exit "missing voice spec fails" 1 $rc
expect_grep "names the missing file" "REQUIRED missing: books/test-book/01-voice.md" "$out"
mv "$TMP/voice.bak" "$TMP/book/books/test-book/01-voice.md"
out=$(GW_BOOK_REPO="$TMP/nowhere" python3 scripts/resolve_book.py 2>&1); rc=$?
expect_exit "an explicit override that points nowhere is exit 2, never a fallback" 2 $rc
expect_grep "and it says so" "explicit override is never silently replaced" "$out"

echo "== okf_gate"
out=$(python3 scripts/okf_gate.py 2>&1); rc=$?
expect_exit "gate passes with the stub validator and matching voice probes" 0 $rc
mv "$TMP/book/scripts/okf_validate.py" "$TMP/val.bak"
out=$(python3 scripts/okf_gate.py 2>&1); rc=$?
expect_exit "gate FAILS CLOSED without a validator" 1 $rc
mv "$TMP/val.bak" "$TMP/book/scripts/okf_validate.py"
sed -i 's/at most one per piece/at most one per chapter/' "$TMP/book/books/test-book/01-voice.md"
out=$(python3 scripts/okf_gate.py 2>&1); rc=$?
expect_exit "gate blocks when a voice threshold's wording drifts" 1 $rc
expect_grep "names the drifted rule" "bold_max_per_piece" "$out"
sed -i 's/at most one per chapter/at most one per piece/' "$TMP/book/books/test-book/01-voice.md"

echo "== voice_check (against independent counts)"
py=$(python3 - <<'PY'
import re, json, subprocess, sys
raw = open("scripts/tests/fixtures/voice-sample.md", encoding="utf-8").read()
prose = raw.split("## Draft Notes")[0]
# independent, deliberately naive counts
bare = 0
for line in prose.split("\n"):
    inq = re.sub(r'"[^"]*"', "", line)
    bare += inq.count("—")
inline = sum(len(re.findall(r"\*\*[^*]+\*\*", l)) for l in prose.split("\n")
             if re.search(r"\*\*[^*]+\*\*", l) and not re.fullmatch(r"\s*\*\*[^*]+\*\*[\s.:]*", l))
words = re.findall(r"[A-Za-z’']+", re.sub(r"^#.*$", "", prose, flags=re.M))
doors = sum(1 for w in words if w.lower().startswith("door"))
you = sum(1 for w in words if w.lower() in ("you", "your", "yours", "you're", "yourself"))
rep = json.loads(subprocess.run([sys.executable, "scripts/voice_check.py", "scripts/tests/fixtures/voice-sample.md",
                                 "--metaphor-family", "door,doors", "--json"], capture_output=True, text=True).stdout)
r = {x["check"]: x for x in rep["results"]}
checks = {
  "em-dash bare count": (r["em-dash"]["value"], bare),
  "em-dash is a FAIL at cap 0": (r["em-dash"]["status"], "FAIL"),
  "inline bold count (run-in header excluded)": (r["bold-as-crutch"]["value"], inline),
  "run-in header counted separately": (r["bold-as-crutch"]["run_in_headers"], 1),
  "metaphor family hits": (round(r["metaphor family"]["value"] * rep["word_count"] / 1000), doors),
  "you-density hits": (round(r["you-density"]["value"] * rep["word_count"] / 1000), you),
  "prose word count excludes apparatus": (rep["word_count"], len(words)),
  "apparatus cut at Draft Notes": (rep["stripped_apparatus"].get("cut_at_heading"), "Draft Notes"),
  "long sentence detected": (r["long-sentence share"]["value"] > 0, True),
}
for k, (got, want) in checks.items():
    print(("ok" if got == want else "FAIL") + "\t" + k + "\t" + f"got {got!r} want {want!r}")
PY
)
while IFS=$'\t' read -r st name detail; do
  [ "$st" = ok ] && ok "$name" || bad "$name" "$detail"
done <<< "$py"
out=$(python3 scripts/voice_check.py "$FIX/voice-sample.md" 2>&1); rc=$?
expect_grep "undeclared family is UNCHECKED, never passed" "UNCHECKED \(not passed\): metaphor family" "$out"
out=$(python3 scripts/voice_check.py "$FIX/voice-sample.md" --short-form --metaphor-family door 2>&1)
expect_grep "short-form says what it does" "short-form: same caps" "$out"

echo "== next (the oracle)"
out=$(python3 scripts/next.py 2>&1); rc=$?
expect_exit "runs on the fixture" 0 $rc
expect_grep "book pipeline's brief for ch02 makes it the shadow candidate" "NEXT_ACTION: /gw 2 --shadow" "$out"
expect_grep "shipped count reads chNN directories" "1 shipped on the book pipeline" "$out"
out=$(python3 scripts/next.py --floor 2>&1)
expect_grep "floor lists the shadow draft" "ch02 +draft .*--shadow" "$out"
mkdir -p "$GW_STATE_ROOT/runs/ch03"; touch "$GW_STATE_ROOT/runs/ch03/interview.md"
out=$(python3 scripts/next.py 2>&1)
expect_grep "in-progress chapter outranks a new one" "NEXT_ACTION: /gw 3" "$out"
expect_grep "next stage after interview is research, cold" "stopped at research" "$out"
out=$(python3 scripts/next.py --floor 2>&1)
expect_grep "floor lists ch03 research as cold" "ch03 +research" "$out"
python3 scripts/inbox.py --add "test question" --raised-by gw-test --chapter 3 --context c --unblocks u >/dev/null
out=$(python3 scripts/next.py 2>&1)
expect_grep "an open inbox item parks the chapter" "NEXT_ACTION: /gw inbox" "$out"
expect_grep "the board names the item" "ch03 parked" "$out"
out=$(python3 scripts/next.py --chapter 3 2>&1)
expect_grep "--chapter shows the parked detail with the item id" "inbox item\(s\) #001" "$out"
python3 scripts/inbox.py --close 1 --resolution "ruled" >/dev/null
out=$(python3 scripts/next.py 2>&1)
expect_grep "closing the item unparks it" "NEXT_ACTION: /gw 3" "$out"
mkdir -p "$GW_STATE_ROOT/bakeoff/ch01"; printf '**Which one would you publish?**  variant-_\n' > "$GW_STATE_ROOT/bakeoff/ch01/verdict.md"
out=$(python3 scripts/next.py 2>&1)
expect_grep "an unread bake-off outranks an in-progress chapter" "NEXT_ACTION: /gw compare 01" "$out"
rm -rf "$GW_STATE_ROOT/bakeoff"

echo "== inbox"
out=$(python3 scripts/inbox.py --all 2>&1)
expect_grep "closed item shows as done with the ruling recorded" "#001 \[done\]" "$out"
grep -q "Resolution (" "$GW_STATE_ROOT"/inbox/001-*.md && ok "resolution written into the item" || bad "resolution written into the item"
out=$(python3 scripts/inbox.py 2>&1)
expect_grep "nothing open reads as nothing waiting" "nothing waiting" "$out"

echo "== parked"
out=$(python3 scripts/parked.py --add "q without trigger" 2>&1); rc=$?
expect_exit "refuses a parked question without a trigger" 1 $rc
out=$(python3 scripts/parked.py --add "rename Part IV" --trigger "at the Ch13 interview" 2>&1); rc=$?
expect_exit "parks with a trigger" 0 $rc
expect_grep "count is one" "^1$" "$(python3 scripts/parked.py --count)"
out=$(python3 scripts/next.py 2>&1)
expect_grep "board shows the parked count" "parked: 1 deferred" "$out"
python3 scripts/parked.py --close 1 --resolution "The Desert" >/dev/null
expect_grep "count back to zero" "^0$" "$(python3 scripts/parked.py --count)"
python3 scripts/parked.py --note "keep it" >/dev/null
grep -q "keep it" "$GW_STATE_ROOT/runs/notes.md" && ok "note appended verbatim" || bad "note appended verbatim"

echo "== term_check"
out=$(python3 scripts/term_check.py "$FIX/brief-sample.md" 2>&1); rc=$?
expect_exit "an undefined coinage fails the gate" 1 $rc
expect_grep "Nail Parable resolves to the OKF concept" "Nail Parable +OKF" "$out"
expect_grep "Second Hinge resolves nowhere (FAIL)" "Second Hinge +NONE" "$out"
expect_grep "Ratchet Window is outline-only (WARN)" "Ratchet Window +OUTLINE" "$out"
expect_grep "Quiet Ledger is defined in the text" "Quiet Ledger +DEFINED" "$out"
expect_nogrep "named people are not coinages" "Marcus Aurelius|Gottman" "$out"
out=$(python3 scripts/term_check.py "$FIX/brief-sample.md" --strict 2>&1); rc=$?
expect_exit "--strict fails on outline-only too" 1 $rc

echo "== okf_new"
out=$(python3 scripts/okf_new.py --type Citation --title X --status verified --dry-run 2>&1); rc=$?
expect_exit "never writes verified" 1 $rc
out=$(python3 scripts/okf_new.py --type Citation --title X --status verifiable --quote-form verbatim --evidence-source search-synthesis --resource r --dry-run 2>&1); rc=$?
expect_exit "transcription rule refuses verbatim on search" 1 $rc
out=$(python3 scripts/okf_new.py --type Story --title X --chapter-slugs no-such-chapter --dry-run 2>&1); rc=$?
expect_exit "invented chapter slug refused" 1 $rc
out=$(python3 scripts/okf_new.py --type Story --title X --tags ch02 --dry-run 2>&1); rc=$?
expect_exit "chapter number in tags refused" 1 $rc
out=$(python3 scripts/okf_new.py --type Citation --title "Fixture Gap Two" --description d --chapter-slugs the-first-door --status unverified --quote-form none --evidence-source none --gap-type research --by gw-test 2>&1); rc=$?
expect_exit "valid gap marker is written" 0 $rc
today=$(date +%Y-%m-%d)
grep -q "timestamp: \"$today" "$TMP/book/books/test-book/okf/citations/fixture-gap-two.md" && ok "timestamp is today, from the clock" || bad "timestamp is today"
grep -q "fixture-gap-two.md" "$TMP/book/books/test-book/okf/log.md" && ok "log.md appended" || bad "log.md appended"
grep -q "fixture-gap-two.md" "$TMP/book/books/test-book/okf/index.md" && ok "index.md entry added" || bad "index.md entry added"
out=$(python3 scripts/okf_new.py --type Citation --title "Fixture Gap Two" --chapter-slugs the-first-door 2>&1); rc=$?
expect_exit "refuses to overwrite an existing concept" 1 $rc
out=$(python3 scripts/okf_new.py --type "Reader Signal" --title "A reader wrote" --platform reddit --signal-category gift --gift-type supporting --by gw-test 2>&1); rc=$?
expect_exit "signal concept written" 0 $rc
grep -A3 "## Signals" "$TMP/book/books/test-book/okf/index.md" | grep -q "a-reader-wrote" && ok "'None yet' placeholder replaced in index" || bad "'None yet' placeholder replaced in index"

echo "== okf-timestamp-guard hook"
H=.claude/hooks/okf-timestamp-guard.sh
mk() { python3 -c 'import json,sys; print(json.dumps({"tool_name":sys.argv[1],"tool_input":json.loads(sys.argv[2])}))' "$1" "$2"; }
out=$(mk Write "{\"file_path\":\"$TMP/book/books/test-book/okf/citations/brand-new.md\",\"content\":\"---\ntype: Citation\ntimestamp: $today\n---\"}" | bash $H 2>&1); rc=$?
expect_exit "hand-written new concept is blocked (use okf_new)" 2 $rc
out=$(mk Edit "{\"file_path\":\"$TMP/book/books/test-book/okf/citations/existing-gap.md\",\"new_string\":\"timestamp: 2025-01-01 10:00\"}" | bash $H 2>&1); rc=$?
expect_exit "backdated stamp in an edit is blocked" 2 $rc
out=$(mk Edit "{\"file_path\":\"$TMP/book/books/test-book/okf/citations/existing-gap.md\",\"new_string\":\"timestamp: $today 10:00\"}" | bash $H 2>&1); rc=$?
expect_exit "today's stamp passes" 0 $rc
out=$(mk Edit "{\"file_path\":\"$TMP/book/books/test-book/okf/citations/existing-gap.md\",\"new_string\":\"description: reworded\"}" | bash $H 2>&1); rc=$?
expect_exit "edit that does not touch the stamp passes" 0 $rc
out=$(mk Write "{\"file_path\":\"$TMP/book/books/test-book/okf/citations/existing-gap.md\",\"content\":\"---\ntype: Citation\ntimestamp: \\\"2026-01-01 09:00\\\"\n---\"}" | bash $H 2>&1); rc=$?
expect_exit "rewrite keeping the file's own old stamp passes" 0 $rc
out=$(mk Write "{\"file_path\":\"$TMP/book/books/test-book/okf/index.md\",\"content\":\"timestamp: 2020-01-01\"}" | bash $H 2>&1); rc=$?
expect_exit "reserved files are exempt" 0 $rc
out=$(mk Write "{\"file_path\":\"$TMP/somewhere/else.md\",\"content\":\"timestamp: 2020-01-01\"}" | bash $H 2>&1); rc=$?
expect_exit "files outside okf/ are untouched" 0 $rc

echo "== bakeoff"
out=$(python3 scripts/bakeoff.py --chapter 1 --control "$TMP/book/books/test-book/chapters/ch01/refined.md" --variant "$FIX/voice-sample.md" --metaphor-family door --out "$TMP/bakeoff" 2>&1); rc=$?
expect_exit "packet builds" 0 $rc
out=$(python3 scripts/bakeoff.py --unseal "$TMP/bakeoff/ch01" 2>&1); rc=$?
[ "$rc" -ne 0 ] && ok "refuses to unseal before the verdict" || bad "refuses to unseal before the verdict"

echo "== plugin layout"
out=$(python3 scripts/sync_plugin_layout.py --check 2>&1); rc=$?
expect_exit "root mirror in sync with .claude/" 0 $rc

echo
echo "$pass passed, $fail failed"
[ "$fail" -eq 0 ]
