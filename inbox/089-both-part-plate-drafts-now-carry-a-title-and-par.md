---
id: 089
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 13:05
applied_by: git show 3a7ac88:books/the-stoic-husband/parts/plate-1-steady-river.svg > /tmp/p1.svg && python3 scripts/plate_check.py /tmp/p1.svg --part 1 2>&1 | grep -qE "^[[:space:]]*\[[^]]+\][[:space:]]+title[[:space:]]"
---

# Both Part plate drafts now carry a title, and parts/README.md's Form rules have no line permitting one - its caption rule says the plate reprints the book's own words and adds none. Add the title line to README.md and extend plate_check's title row to --part, so a Part plate whose title does not match its Part page heading fails?

The drawn plates exceed their own written contract. plate_check's title row only runs under --chapter, where it compares against the distillation's Mechanism line, so both Part titles were checked by hand and nothing counts them. A README line alone would be invisible to the stage that needs it. Parking lot #37 carries the prose half of this question; this is the mechanical half.

**Recommendation:** One README bullet stating a Part plate carries its Part's title in the chapter plates' .ttl idiom, plus a title row under --part comparing .ttl to the Part page H1

**Checked:**

```
parts/README.md Form rules list black line on white, one abstract image, caption verbatim, no marriage vocabulary, 6x9 - and no title. plate_check.py on the landed title-less plate-1 with --part 1 exits 0 with all rows ok and no title row present.
```

**What unblocks this:** Whether either draft can land, and whether Parts III-V inherit the title rule mechanically rather than by memory
