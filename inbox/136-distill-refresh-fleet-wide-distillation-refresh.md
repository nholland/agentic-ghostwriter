---
id: 136
status: resolved
kind: gap
trigger: built
raised_by: Publisher
chapter: -
opened: 2026-10-03 02:00
resolved: 2026-10-03 02:00
---

# `distill --refresh`: fleet-wide distillation refresh

*Migrated 2026-10-04 from GAPS.md ('built since the audit').*

scripts/distill_status.py finds the chapters to re-read (missing, malformed, or prose changed since the distillation); the Fleet refresh section of /gw-edit re-runs the Line Editor on only those. A flag is "re-read", not "wrong".
