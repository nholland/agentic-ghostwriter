---
id: 135
status: resolved
kind: gap
trigger: built
raised_by: Publisher
chapter: -
opened: 2026-10-03 02:00
resolved: 2026-10-03 02:00
---

# `switch`: change the active book

*Migrated 2026-10-04 from GAPS.md ('built since the audit').*

scripts/switch_book.py lists the registry, validates the target and writes bookRoot once. It does not move config/house.json's mirrored voice thresholds, so voice_rules_check.py fails until they match the new book's spec; that is the intended loud failure.
