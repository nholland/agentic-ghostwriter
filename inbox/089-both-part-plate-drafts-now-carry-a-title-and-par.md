---
id: 089
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 13:05
applied_by: python3 -c "
import re,subprocess,sys,tempfile,os
base=open('books/the-stoic-husband/parts/plate-1-steady-river.svg',encoding='utf-8').read()
def make(title):
 ttl='<text class=\"ttl\" x=\"300\" y=\"90\" text-anchor=\"middle\" font-family=\'Georgia, \"Times New Roman\", serif\' font-size=\"26\" font-weight=\"600\" fill=\"#111111\">%s</text>'%title
 return re.sub(r'(<svg[^>]*>)',r'\1\n'+ttl,base,count=1)
def run(svg):
 f=tempfile.NamedTemporaryFile('w',suffix='.svg',delete=False,encoding='utf-8');f.write(svg);f.close()
 r=subprocess.run(['python3','scripts/plate_check.py',f.name,'--part','1'],capture_output=True,text=True)
 os.remove(f.name);return r.stdout
def status(out):
 m=re.search(r'\[([^\]]+)\]\s+title\s',out)
 return m.group(1).strip() if m else None
sg,sb=status(run(make('THE STEADY RIVER'))),status(run(make('SOME OTHER TITLE')))
print('matching:',sg,'mismatched:',sb)
sys.exit(0 if (sg=='ok' and sb not in (None,'ok')) else 1)"
---

# Both Part plate drafts now carry a title, and parts/README.md's Form rules have no line permitting one - its caption rule says the plate reprints the book's own words and adds none. Add the title line to README.md and extend plate_check's title row to --part, so a Part plate whose title does not match its Part page heading fails?

**Correction, 2026-09-22 (gw-retro).** The original applied_by below greped plate_check's own output for a title row using `\[[^]]+\]` - a pattern matching `[ ok ]` and `[FAIL]` equally - and ran it against the landed plate, which has no title at all. A title row that prints `[ ok ]` on a title-less plate would have closed this green: the exact half-fix shape FINDINGS.md already records, a check passing the defect it exists to catch. Replaced with a mutation proof: it builds two copies of the landed plate, one titled to match the Part page heading and one titled to mismatch it, and requires the row to exist and print `ok` on the first and something other than `ok` on the second. Verified red today for the honest reason - no title row exists under `--part` at all yet, so both copies show `None`.

The drawn plates exceed their own written contract. plate_check's title row only runs under --chapter, where it compares against the distillation's Mechanism line, so both Part titles were checked by hand and nothing counts them. A README line alone would be invisible to the stage that needs it. Parking lot #37 carries the prose half of this question; this is the mechanical half. Adjacent to #065 (chapter plate titles = the distillation's Mechanism line) - the `--part` title row and the `--chapter` title row are the same row, just against a different reference (the Part page's H1 rather than the Mechanism line).

**Recommendation:** One README bullet stating a Part plate carries its Part's title in the chapter plates' .ttl idiom, plus a title row under --part comparing .ttl to the Part page H1

**Checked:**

```
parts/README.md Form rules list black line on white, one abstract image, caption verbatim, no marriage vocabulary, 6x9 - and no title. plate_check.py on the landed title-less plate-1 with --part 1 exits 0 with all rows ok and no title row present.
```

**What unblocks this:** Whether either draft can land, and whether Parts III-V inherit the title rule mechanically rather than by memory
