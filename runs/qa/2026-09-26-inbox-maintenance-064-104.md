# Approved inbox maintenance batch — 2026-09-26

Authority: “Do the three that you approve. Decline and remove the rest.” Implemented by the Publisher in session; no cold desk review was performed.

## Implemented

- #064/#071: `retro_window.py` supplies one review range to manual reviews and the hook. Dispatch changes only the notification boundary. Explicit completion requires an existing report containing the exact reviewed hashes and advances only through that reviewed end. Newer work remains pending. Legacy unconsumed windows preserve their start. Missing valid bounds report an error rather than silently truncating coverage.
- #074/#079: the hook still batches at three new work commits. A commit containing a report and only inbox/FINDINGS review output does not count. A report mixed with substantive watched production changes does count. Merely committing a report does not mark anything reviewed.
- #104: `lost_entries` permits identical nonempty file sets to excuse a missing heading only on the same branch. The real check exposed exactly one missing historical session, restored verbatim from merge parent `273b374356d0cec4b7dc562e09b7f42f1417bf91`: `2026-09-18 18:34 — claude/gateway-tmjrgm`. No legacy exemptions were added.

The old shell implementation was replaced by a wrapper calling the shared script. The Archivist's old 115-word bounds bullet became 36 words plus a 29-word completion instruction; total desk definition decreased from 1,251 to 1,201 words. The derived mirror carries the same replacement: net reduction of 100 words across both desk files. No other desk rules changed. The old hook had 499 whitespace-delimited words; its replacement has 36. The new Python code is production logic, not additional desk instructions.

## Declined

#076, #078, #090 and #091 are resolved with `disposition: declined`, following the author's instruction. Their historical proposals and proof commands are retained as history; those implementations were not performed and their old proof commands were not represented as passing. No generated assets were deleted. #087 remains the visual decision for the Part I illustration.

## Verification

The dedicated suite exercises cross-branch matching in both directions, same-branch restatements, partial/empty file sets, repeated dispatch, manual reads, completion after newer work, rejection of a mismatched report range, report-and-inbox-only commits, mixed substantive commits, and invalid/missing state. The actual shell hook is exercised in disposable repositories.

```text
21/21 maintenance fixtures pass
216/216 fixtures pass
log_check: 197 entries intact - structure ok, union checked against every merge parent.
sync_plugin_layout: in sync
inbox: 26 open, 1 ruled but not yet applied
```

`git diff --check` passed. The five implemented records close on the dedicated behavioral suite, rerun by the inbox command. Review completion remains a reviewer action after writing the report; the tool verifies the report and range, not the intellectual quality of the review. Old dispatch records cannot establish whether a review actually happened, so migration conservatively retains unconfirmed coverage.
