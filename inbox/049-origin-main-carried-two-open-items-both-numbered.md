---
id: 049
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 14:54
applied_by: test $(ls inbox/ | cut -c1-3 | sort | uniq -d | wc -l) -eq 0
resolved: 2026-09-20 14:54
---

# origin/main carried two open items both numbered 045 (the tests/prove.py fixture-for-a-new-file proposal, opened 13:56, and the gw-signal Step 0 stop-condition proposal, opened 15:00) - inbox.py printed them with no warning, and --close 045 would have bound any ruling to whichever slug sorts first. Renumber the older one to 048?

Two independent branches (gateway-qve5zb, gateway-brzxoo) each correctly computed next_id() as 045 from what they could see, then merged clean since the inbox is one file per item - no conflict to catch it. Closing #045 today would have recorded the author's ruling against the wrong proposal: 's' (should-gw-signal...) sorts before 't' (tests-prove-py...), so --close 045 binds to the gw-signal item regardless of which one the author meant to rule on.

**Recommendation:** renumber 045-tests-prove-py-cannot-prove-a-fixture-for-a-new-.md to 048 (it is the narrower, self-contained item) and update its id: field; leave 045-should-gw-signal... as the sole 045

**Checked:**

```
git ls-tree --name-only origin/main inbox/ | grep '^inbox/045' -> both files present, both 'id: 045', both status: open. Renamed and updated the id field; ls inbox/ | sort | tail -5 now shows a single 045, 046, 047, 048 with no duplicate. python3 tests/run.py -> 95/95.
```

**What unblocks this:** whether the author's next ruling on an inbox item lands on the item he actually read

**Resolution (2026-09-20 14:54):** Applied directly - a live risk to the author's next inbox ruling on main, verified independently before acting. Renumbered; no duplicate IDs remain.

**Not applied yet.** This ruling lands outside this repo. It closes when `test $(ls inbox/ | cut -c1-3 | sort | uniq -d | wc -l) -eq 0` exits 0.

**Applied, confirmed 2026-09-20 14:54:** `test $(ls inbox/ | cut -c1-3 | sort | uniq -d | wc -l) -eq 0` now exits 0.
