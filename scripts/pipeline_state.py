#!/usr/bin/env python3
"""Single source of truth for pipeline NEXT_ACTION and current phase.

Used by /book-resume and /book-status (and /book-next) instead of inline
heredocs, so the chapter-iteration and phase-inference logic only exists in
one place. --mode next tracks the linear writing/QA/launch pipeline;
--mode next-marketing and --mode next-feedback track the concurrent
Phase 5 publishing loop (Substack/social posting, then reader feedback).

Usage:
    python3 scripts/pipeline_state.py --mode next
    python3 scripts/pipeline_state.py --mode phase --update-phase
    python3 scripts/pipeline_state.py --mode next-marketing
    python3 scripts/pipeline_state.py --mode next-feedback
    python3 scripts/pipeline_state.py --manifest /dev/stdin --mode next
"""

import argparse
import json
import os
import subprocess
import sys

FOUNDATION_ORDER = [
    ("spark", "/book-spark"),
    ("archetype", "/book-archetype"),
    ("voice", "/book-voice"),
    ("audience", "/book-audience"),
    ("outline", "/book-outline"),
]

CHAPTER_STAGES = [
    ("research", "/book-chapter-research {n}"),
    ("draft", "/book-chapter-draft {n}"),
    ("refined", "/book-chapter-refine {n}"),
    ("distill", "/book-distill {n}"),
]

# Order matches CLAUDE.md Phase 3: sweep is the final whole-book coherence
# pass, run after the other four audits — not first.
QA_ORDER = [
    ("human", "/book-human"),
    ("argue", "/book-argue"),
    ("beta", "/book-beta"),
    ("tension", "/book-tension"),
    ("sweep", "/book-sweep"),
]

LAUNCH_ORDER = [
    ("callouts", "/book-callouts"),
    ("marketing", "/book-marketing"),
    ("pitch", "/book-pitch"),
]

PHASE_LABELS = {
    "foundation": "Phase 1: Foundation",
    "writing": "Phase 2: Writing",
    "qa": "Phase 3: QA",
    "publishing-prep": "Phase 4: Publishing Prep",
    "publishing-loop": "Phase 5: Publishing Loop",
}

# Shared sentinel for the marketing/feedback tracks — /book-resume and
# /book-status detect this exact string to omit a track's line entirely
# rather than printing "nothing pending" as prose.
NOTHING_PENDING = "Nothing pending — all published chapters are fully processed."


def load_book(manifest_path):
    with open(manifest_path) as f:
        manifest = json.load(f)
    root = manifest["bookRoot"]
    return manifest, root, manifest["books"][root]


def compute_next(stages, chapter_count):
    foundation = stages.get("foundation", {})
    for key, cmd in FOUNDATION_ORDER:
        if foundation.get(key, "pending") != "complete":
            return cmd

    chapters = stages.get("chapters", {})
    for n in range(1, chapter_count + 1):
        nn = "{:02d}".format(n)
        chapter = chapters.get(nn, {})
        for key, cmd_template in CHAPTER_STAGES:
            if chapter.get(key, "pending") != "complete":
                return cmd_template.format(n=n)

    qa = stages.get("qa", {})
    for key, cmd in QA_ORDER:
        if qa.get(key, "pending") != "complete":
            return cmd

    launch = stages.get("launch", {})
    for key, cmd in LAUNCH_ORDER:
        if launch.get(key, "pending") != "complete":
            return cmd

    return "Pipeline complete — all stages done."


def compute_phase(stages, chapter_count):
    foundation = stages.get("foundation", {})
    if any(foundation.get(k, "pending") != "complete" for k, _ in FOUNDATION_ORDER):
        return "foundation"

    chapters = stages.get("chapters", {})
    for n in range(1, chapter_count + 1):
        nn = "{:02d}".format(n)
        chapter = chapters.get(nn, {})
        if any(chapter.get(k, "pending") != "complete" for k, _ in CHAPTER_STAGES):
            return "writing"

    qa = stages.get("qa", {})
    if any(qa.get(k, "pending") != "complete" for k, _ in QA_ORDER):
        return "qa"

    launch = stages.get("launch", {})
    if any(launch.get(k, "pending") != "complete" for k, _ in LAUNCH_ORDER):
        return "publishing-prep"

    return "publishing-loop"


def compute_next_marketing(stages, chapter_count):
    """First refined chapter with outstanding Substack/social work.

    A chapter with no "publishing" key at all (true for any chapter that
    hasn't started the publishing track yet) resolves via .get(..., {})
    to "not identified" — no manifest migration required.

    "Done" for this track means identified + fully written, not fully
    posted: whether a drafted concept has actually been published on
    Substack is something only the author can confirm (the Substack MCP
    integration can push drafts but can't read publish status back), and
    self-reported "posted" tracking drifts in practice. concepts_posted
    still feeds compute_next_feedback below — it just no longer blocks
    this track from reporting a chapter's marketing work as complete.
    """
    chapters = stages.get("chapters", {})
    for n in range(1, chapter_count + 1):
        nn = "{:02d}".format(n)
        chapter = chapters.get(nn, {})
        if chapter.get("refined") != "complete":
            continue
        pub = chapter.get("publishing", {})
        if not pub.get("concepts_identified", False):
            return "/book-substack {n} — identify and write Substack/social concepts for Chapter {n}".format(n=n)
        total = pub.get("concepts_total", 0)
        written = pub.get("concepts_written", 0)
        if written < total:
            return "/book-substack {n} — finish writing Chapter {n}'s concepts ({written}/{total} written)".format(
                n=n, written=written, total=total
            )
    return NOTHING_PENDING


def compute_next_feedback(stages, chapter_count):
    """First posted chapter with feedback or signal work outstanding."""
    chapters = stages.get("chapters", {})
    for n in range(1, chapter_count + 1):
        nn = "{:02d}".format(n)
        pub = chapters.get(nn, {}).get("publishing", {})
        if pub.get("concepts_posted", 0) <= 0:
            continue
        if not pub.get("feedback_received", False):
            return "Check for reader feedback on Chapter {n} (posted, awaiting response)".format(n=n)
        if not pub.get("signal_run", False):
            return "/book-signal {n} — process received feedback for Chapter {n}".format(n=n)
    return NOTHING_PENDING


def phase_label(phase, stages, chapter_count):
    if phase == "writing":
        chapters = stages.get("chapters", {})
        # Only count zero-padded numeric keys ("01", "02", ...) — non-numeric
        # keys like "prologue" and "introduction" share this dict for storage
        # but aren't part of the numbered chapter count.
        refined_count = sum(
            1 for k, v in chapters.items()
            if k.isdigit() and v.get("refined") == "complete"
        )
        return "{} — {}/{} chapters refined".format(
            PHASE_LABELS[phase], refined_count, chapter_count
        )
    return PHASE_LABELS.get(phase, phase)


def check_freshness():
    """Refuse to answer from a stale clone.

    Every pipeline answer this script gives is computed from book-manifest.json
    in the working tree. If the clone is behind origin/main, that manifest
    describes the past, and the answer will be confidently wrong -- on
    2026-08-14 it reported `/book-chapter-research 8` for a book whose
    chapters 8 and 9 were both finished on origin/main, because the clone was
    79 commits behind. `/book-next` is a thin dispatcher that invokes the
    answer immediately, and CLAUDE.md Rule 10 forbids the caller from
    second-guessing it, so the check has to live here, before the answer
    exists. `/book-resume` Step 1.5 already ran this exact comparison; it was
    simply invisible to the other caller.

    Fails closed: stderr plus a nonzero exit, which both callers' documented
    error handling already stops on. Never fails on network trouble alone --
    an unreachable remote leaves the last-known ref in place and the
    comparison still runs against it.
    """
    def git(*args, timeout=10):
        return subprocess.run(
            ["git", *args], capture_output=True, text=True, timeout=timeout
        )

    try:
        if git("rev-parse", "--git-dir").returncode != 0:
            return  # not a git repo; nothing to be stale against
        try:
            git("fetch", "origin", "main", "--quiet", timeout=20)
        except subprocess.TimeoutExpired:
            pass  # offline or slow: fall through to the last-known ref
        probe = git("rev-parse", "--verify", "--quiet", "origin/main")
        if probe.returncode != 0:
            return  # no origin/main to compare against
        behind = git("rev-list", "--count", "HEAD..origin/main")
        if behind.returncode != 0:
            return
        n = int(behind.stdout.strip() or 0)
    except (OSError, ValueError, subprocess.SubprocessError):
        return  # never let the guard itself break the pipeline

    if n:
        sys.stderr.write(
            f"pipeline_state: refusing to answer -- this clone is {n} commit(s) "
            "behind origin/main, so book-manifest.json describes an older state "
            "of the book and any answer computed from it may point at work that "
            "is already finished.\n"
            "Fix: `git fetch origin main && git merge origin/main` (or `git reset "
            "--hard origin/main` if this branch has no unsaved work), then re-run.\n"
            "Override only if you know the clone is intentionally behind: "
            "--skip-freshness-check\n"
        )
        sys.exit(2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default="book-manifest.json")
    parser.add_argument(
        "--skip-freshness-check",
        action="store_true",
        help="Answer even if the clone is behind origin/main (see check_freshness)",
    )
    parser.add_argument(
        "--mode",
        choices=["next", "phase", "next-marketing", "next-feedback"],
        required=True,
    )
    parser.add_argument(
        "--update-phase",
        action="store_true",
        help="Write the computed phase back to book-manifest.json (mode=phase only)",
    )
    args = parser.parse_args()

    if not args.skip_freshness_check:
        check_freshness()

    manifest, root, book = load_book(args.manifest)
    stages = book.get("stages", {})
    chapter_count = book.get("chapter_count", len(stages.get("chapters", {})))

    if args.mode == "next":
        print(compute_next(stages, chapter_count))
        return

    if args.mode == "next-marketing":
        print(compute_next_marketing(stages, chapter_count))
        return

    if args.mode == "next-feedback":
        print(compute_next_feedback(stages, chapter_count))
        return

    phase = compute_phase(stages, chapter_count)
    print(phase_label(phase, stages, chapter_count))

    if args.update_phase:
        book["currentPhase"] = phase
        if os.path.exists(args.manifest) and args.manifest not in ("/dev/stdin", "-"):
            with open(args.manifest, "w") as f:
                json.dump(manifest, f, indent=2)


if __name__ == "__main__":
    main()
