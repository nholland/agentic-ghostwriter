---
id: 093
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-22 23:19
applied_by: python3 -c "import os,re,collections,sys;ids=[re.match(r'(\\d+)-',f).group(1) for f in os.listdir('inbox') if re.match(r'\\d+-',f)];sys.exit(1 if [k for k,v in collections.Counter(ids).items() if v>1] else 0)"
---

# inbox IDs 053 collided for real: this merge brought inbox/053-log-check-s-union-invariant-the-one-its-own-docs.md onto a branch already holding inbox/053-inbox-py-s-tests-run-py-proof-guard-was-widened-.md. inbox.py now lists two #053 items, so --close 053 is ambiguous. Which of the two is renumbered, and does the duplicate-ID guard land with it?

Two open items share one ID after the merge from main. Any --close 053 acts on an ambiguous target, and the ledger's own addressing scheme can no longer name one of its two entries.

**Recommendation:** Renumber inbox/053-log-check-s-union-invariant-the-one-its-own-docs.md to the next free ID and add a duplicate-ID guard in the same commit, so the repair and its regression check land together

**Checked:**

```
python3 -c "import os,re,collections;ids=[re.match(r'(\\d+)-',f).group(1) for f in os.listdir('inbox') if re.match(r'\\d+-',f)];print(dict((k,v) for k,v in collections.Counter(ids).items() if v>1))" -> {'053': 2}; ls inbox/053-*.md -> two files.
```

**What unblocks this:** Which file is renumbered (the log_check one arrived second, on main, independently of this branch's own #053), and whether a duplicate-ID check lands in the same commit as the repair
