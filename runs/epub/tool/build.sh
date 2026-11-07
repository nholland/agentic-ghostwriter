#!/usr/bin/env bash
# Build the draft ePub from the compiled book HTML, then validate it.
# Usage: bash runs/epub/tool/build.sh   (run from the repo root, after compile_current.py)
set -euo pipefail
ROOT=$(pwd); A=output/compiled/assets; T=$(mktemp -d)
python3 -I runs/epub/tool/prep.py "$A/book.html" "$T/book-epub.html" "$ROOT"
(cd "$A" && pandoc "$T/book-epub.html" -f html -t epub3 --resource-path=. --css="$ROOT/runs/epub/tool/epub.css" \
  --metadata title="River, Oak, Sun: The Stoic Husband" --metadata subtitle="Draft, Prologue to Chapter 16" \
  --metadata lang=en-US --toc --toc-depth=1 --split-level=1 -o "$ROOT/output/compiled/book-draft.epub")
java -jar /opt/epubcheck/epubcheck-5.1.0/epubcheck.jar output/compiled/book-draft.epub 2>&1 | grep -v JAVA_TOOL | tail -3
