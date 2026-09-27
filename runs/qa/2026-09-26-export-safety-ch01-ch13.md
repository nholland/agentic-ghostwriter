# Export safety: Chapters 1–13

Recorded 2026-09-26 17:30, Publisher in session. No cold desk ran.

Authority: the author approved Inbox #062, #063, #072, #081, #082, #088 and #103, adding: “I'm comfortable with our scripts getting more complex, but I am wary of making the agent part more complex.” Changes are in production scripts, tests and generated exports. No agent definitions, skills, hooks or house instructions changed. No manuscript or plate source was edited or approved.

## Changes

- #062: exercise land.py's actual pre-copy geometry gate with clean, failing and explicit-force cases. Pass the resolved book/run roots through to the checker. Discover the existing DejaVu metrics on this Mac, preserving the conservative font measurements.
- #063: capture a bottom-band SVG at 2× and 3×; assert both dimensions and actual ink. Chromium now waits for fonts before capture.
- #072: inspect decoded visible HTML text for leaked pagebreak tokens and escaped markup, including split text nodes. Remove obsolete pagebreak narration.
- #081: grounding accepts chapter prose, distillation fields and timestamped Author additions; rejects generated brief boilerplate, provenance tags and unrelated sections. Grounding remains a warning.
- #082: compare decoded preview pixels against a fresh capture at the preview's own scale. Exercise current, changed and checker-caller cases. Missing/changed previews warn; rendering errors report unchecked. Export paths render fresh art and skip unrelated historical preview caches.
- #088: report the exact selected SVG's checks, including rendered ink in PDF builds. No-PDF assembly explicitly marks ink unchecked. FAIL is reported without blocking export. Current collection builds use that same checked compiler path.
- #103: full chapter distillations follow prose and plate in whole-book and individual exports. Each new chapter starts fresh, with number and title together. The artifact checker accepts explicit chapter bundles while rejecting prose after a bundle's distillation.

## Evidence

`python3 tests/run.py`:

```text
191/191 fixtures pass
```

`python3 tests/export_safety_cases.py --render` (Chromium permitted):

```text
25/25 export cases pass.
```

`tests/verify_reader_exports.py` uses pypdf to read current PDFs against the source paths and hashes in the manifest. It checks complete prose and distillation text, including numbered practices, chapter order, headings on one page, fresh chapter starts, a plate immediately before each distillation, and blank pages. Normalization ignores whitespace, punctuation and typographic ligature differences; this is supplemented by visual review.

```text
13/13 chapter PDFs and book sequences pass; full prose/distillations preserved, headings together, plates before distillations.
Book: 123 pages; 16 plate pages; no blank pages.
```

Visual review: rendered every page of the whole book, distillation collection and plate collection to PNG and inspected contact sheets; inspected opening, plate and closing distillation pages from all thirteen chapter PDFs. The first review caught chapter numbers orphaned on preceding distillation pages; bundle breaks and heading keep-together fixed that. Revised sheets show those transitions correctly. No new crop or overlap was seen. This is export QA, not a cold editorial/design verdict.

Final checked-compiler rebuild: re-rendered all 274 PDF pages and compared them with the reviewed build. Exact pixel comparison found seven changed plate pages; inspected all seven again, with no visible layout or content defect. The other 267 pages matched. Exact pixel equality was not claimed for the entire rebuild. Source/text/order validation above passed again on the final files.

Artifacts: `output/compiled/book.pdf`, thirteen chapter PDFs, `distillations.pdf`, `plates.pdf`; HTML/images and source manifest under `output/compiled/`. Chapter 13 remains explicitly unapproved; draft plate status remains in the manifest.

## Findings retained for plate review

- Chapter 3: rendered ink enters the left 40px margin band (`left=461`); the new reporting exposes this without stopping the export. Source art was left unchanged.
- Chapter 12: “THE ONE THING FOR HER” has no three-word match in the narrowed grounding corpus. Attribution/content review remains open; no source was invented to make it pass.
- Chapters 1 and 5: title/Mechanism mismatches remain (existing #065 and #070).
- Part plates: bare text-anchor attributes remain warnings.
- Chapter 13: the existing alignment warnings remain.

The seven technical closures do not certify all plate rows clean, approve draft artwork, or settle those content decisions. Historical preview files were not rewritten.
