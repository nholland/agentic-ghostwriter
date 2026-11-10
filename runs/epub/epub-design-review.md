# ePub design review: book-draft.epub (Prologue to Chapter 16)

Designer desk, review mode. 2026-11-07 14:44. Nothing in the book or the build was changed.

**What I checked:** `output/compiled/book-draft.epub` (1.88 MB, EPUBCheck 0/0 per the brief; not re-run here). I unzipped it to the scratchpad and rendered every `EPUB/text/*.xhtml`, plus the title page and the nav, in Chromium with the book's stylesheet. I used a 16px reader margin at 390x844 (phone) and 768x1024 (tablet). That gave 136 screenshots: the opening of each file, every plate, and every "Putting into Practice" section. I compared them against `books/the-stoic-husband/design/plates/README.md` and pages 1, 12, 13, 21 and 52 of `output/compiled/book.pdf`.

**Caveat:** Chromium in scroll mode is not a real e-reader. It shows the CSS and the markup faithfully, but not how pages break. Page-break findings come from reading the markup.

**Screenshots** (in `runs/epub/epub-review-shots/`):
- `phone-*`, `tablet-*`: the ePub as built.
- `fix-phone-ch004-*`: the same chapter with the fixes in items 1 to 5 applied to a scratch copy.
- `print-reference-strip.png`: the approved print pages.

## Ranked findings

### 1. The practice page lost its look, and its kicker sits in the wrong section (all 16 chapters)
`prep.py` removes every `<div>` and `<section>`, which takes the classes `kicker`, `rule`, `runin`, `dist` and `distback` with them. Then pandoc splits sections at the demoted `h2`. The result:
- "Putting into Practice" becomes a plain left-aligned `<p>` stranded at the end of the chapter's last beat section, *before* the practice heading (`<p>Putting into Practice</p>` then `</section>`). Screen readers and the EPUB structure treat it as part of the chapter's closing prose.
- The title is a large bold left `h2`. In print it is a smaller, centred 14pt title.
- The short centred rule is now a full-width grooved `<hr>`.
- "Practice" is a bold heading as big as the beat headings. In print it is a grey spaced small-caps label with a hairline under it.
- Nothing starts the practice section on a fresh page. In print, `.distback` does.

**Fix:** in `prep.py`, before flattening, rewrite `<p class="kicker">Putting into Practice</p><h1>` as `<h2 class="dist-title"><span class="kicker">Putting into Practice</span>`. Pandoc keeps header classes and spans. Then add to `epub.css`:

```css
section.dist-title{page-break-before:always;break-before:page}
h2.dist-title{text-align:center;font-size:1.2em;font-weight:600;margin:0 0 .3em}
h2.dist-title .kicker{display:block;font-style:italic;font-weight:normal;font-size:.75em;letter-spacing:.06em;color:#5a5a5a;margin-bottom:.4em}
h2.dist-title + hr{width:40%;margin:.4em auto 1em}
section.dist-title p{margin:0 0 .5em}
section.level2:not(.beat-heading):not(.dist-title) > h2{font-size:.8em;letter-spacing:.16em;text-transform:uppercase;color:#5a5a5a;border-bottom:1px solid #ddd;padding-bottom:.2em}
```

Verified in `fix-phone-ch004-practice.png`: it now matches the print page.

### 2. Plates are drawn 23% narrower than the screen on phones, and ch1 to ch11 are not readable there even at full width
Pandoc wraps each plate in `<figure>`. The stylesheet never resets the browser's default figure margin (`1em 40px`), so on a 390 phone every chapter plate renders at **262 CSS px** inside a 342 px text column (`phone-ch004-plate0.png`). On the tablet they render at 640 px, which is fine. Sharpness is fine everywhere: the PNGs are 1920 px wide, three times the display size.

**Fix:**
```css
figure{margin:0}
figure.plate{page-break-before:always;break-before:page;page-break-inside:avoid;text-align:center}
figure.plate img{width:100%;max-height:95vh;margin:0 auto}
```
This is what print does: a plate is a page of its own. Verified in `fix-phone-ch004-plate.png`: the plate goes from 262 to 342 px.

**Author ruling needed (not an ePub fix).** Even at full width, the ch1 to ch11 plates set captions at 12 to 13.5px on a 640 canvas. On a phone that is about 6.4 CSS px, below legible: "he becomes small without deciding to" on ch5 cannot be read (`phone-ch008-plate0.png`). The ch12 to ch16 plates use 19 to 24px type and read fine. The Designer's own standard is "legible at phone width". The options are:
- (a) accept tap-to-zoom (Apple Books and Kindle both support it) for ch1 to ch11;
- (b) re-set those plates' type to the ch12 to ch16 sizes, which is a revision through `/gw-plate`.

### 3. The chapter openings do not match the house format
Print sets a small grey "Chapter 1" label, then the bold title on its own line. `prep.py` merges them into one heading, "Chapter 1: The Three-Second Window", which on a phone wraps to two ragged lines (`phone-ch004-open.png`).

**Fix:** keep the label as a span:
```
<h1 class="chapter-heading"><span class="num">Chapter 1<span class="sep">: </span></span>The Three-Second Window</h1>
```
with:
```css
h1.chapter-heading .num{display:block;font-size:.55em;font-weight:normal;color:#444;margin-bottom:.5em}
h1.chapter-heading .sep{display:none}
```
The contents list keeps "Chapter 1: The Three-Second Window". Verified in `fix-phone-ch004-open.png`. Beat headings (`h2.beat-heading`) should also drop to `1em` bold to match print's 11pt run, since they now compete with the chapter title.

### 4. Section rules are full-width grooved lines
Every beat ends with an `<hr />` (61 in total). Print draws them as a 1.1in hairline. Here they are the browser default: a full-width, two-tone, inset rule.

**Fix:**
```css
hr{border:0;border-top:1px solid #cfcfcf;width:30%;margin:1.6em auto}
```
There are no empty headings and no doubled rules, but in all 16 chapters a rule sits directly before the plate. Once the plate has its own page, that rule is harmless.

### 5. The Part closing plates can overflow a tablet page and do not get a page of their own
The three 600x900 closing plates (end of ch5, ch11 and ch16) sit in a bare `<p>` directly under the last practice item. On a 768x1024 tablet they render 900 px tall with 1.5em margins, which leaves no room for reader chrome (`tablet-ch008-plate1.png`). Print bounds them by height and isolates them.

**Fix:** have `prep.py` give that paragraph a class (`p.closing-plate`), then:
```css
p.closing-plate{page-break-before:always;text-align:center;margin:0}
p.closing-plate img{max-height:95vh;width:auto}
```

### 6. The title page is bare, and no author is named anywhere
The title page is a left-aligned h1 with the subtitle as body text (`phone-title_page-open.png`). The OPF has no `dc:creator`, so stores and libraries will list the author as "Unknown". `book-manifest.json` does not record the author's name either, and I have not supplied one.

**Fix:** centre `.titlepage`, which pandoc emits but `epub.css` never styles:
```css
.titlepage{text-align:center;margin-top:30%}
.titlepage h1{text-align:center}
```
Pass `--metadata author="..."` once the author gives his name as it should appear (ruling). The title also needs a ruling: both cover candidates read "RIVER. OAK. SUN. / THE STOIC HUSBAND", while the ePub and the manifest say "River, Oak, Sun: The Stoic Husband".

### 7. There is no cover
**Is one needed?** Yes, for anything beyond review copies:
- Apple Books and Kindle show a generic grey tile without one.
- KDP requires a separate cover upload.
- Send-to-Kindle uses the first image if there is no cover, which here would be the Chapter 1 plate.

For a draft passed between readers it is optional.

**What it should be.** The author has two candidate directions in `books/the-stoic-husband/design/covers/`. Neither is ratified: per `source-prompt.md`, "Feedback split; both directions retained as candidates".
- **design-one:** the brown-leather "Heirloom Field Manual", gold-stamped RIVER. OAK. SUN., an oak leaf.
- **design-two:** black cloth, debossed type.

Both are 1254x1254 mock-up composites, not usable cover art. An ePub cover is a portrait image of about 1600x2560. Its type has to stay readable as a thumbnail.

I did not make one. The author needs to pick a direction first. Until he does, the honest interim is no cover, or a plain typographic cover he approves.

### 8. Contents list and heading hierarchy
- The structure is correct: Part pages are h1, chapters are h1, beats are h2. The nav has 21 flat entries and so does `toc.ncx`.
- **Issue:** Parts do not nest their chapters, so a phone reader sees one long flat numbered list with blue underlined links (`phone-nav-open.png`).
- **Fix:** add `ol.toc{list-style:none;padding:0}` and `ol.toc a{text-decoration:none;color:inherit}`. Optionally nest chapters under their Part, either by post-processing `nav.xhtml` or by building the Part pages as h1 and the chapters as h2 with `--split-level=2`.
- **Author ruling:** the Part titles "PART I — THE STEADY RIVER" carry an em-dash in the contents list, on the Part pages, and in every practice title ("Chapter 1 — The Three-Second Window"). The house rule bans em-dashes on plates and in prose. Print has the same dashes, so this is not an ePub regression; it is a question for the author.

### 9. Smaller points
- **Body text:** flush left, zero indent, `.8em` paragraph gap. This matches the house format.
- **Italics:** survive everywhere (Part epigraphs, Latin and Greek terms, practice questions).
- **Run-in labels:** "Mechanism:", "The idea in one sentence:", "Lesson:" and "Challenge:" survive as `<strong>`. They read correctly, but at full bold, where print uses 600 weight. That is acceptable.
- **Blockquotes** (ch10, ch12) use the browser default: a 40px indent on both sides, upright text and no rule, which wastes phone width. Print uses italic text with a left hairline. **Fix:** `blockquote{margin:1em 1.2em;padding-left:.8em;border-left:2px solid #d4d4d4} blockquote p{font-style:italic}`. The citation line ("*Discourses* 2.18, Long trans.") should also come out of italics in a class, as print's `cite` does.
- **Plate alt text** is "Plate, Chapter 1". Screen readers will announce nothing useful. **Fix:** alt text = the plate's title plus its one caption line, taken from the SVG.
- **Part pages** match print: left bold caps title, italic epigraph. The book's River, Oak and Sun marks (`design/marks/`) are an option for these pages, but only on the author's word, since print does not use them.
- **Landmarks** list only the title page and the contents, so Kindle's "Go to Beginning" opens on the title page. **Fix:** add a `bodymatter` landmark pointing at `ch001.xhtml`, by post-processing `nav.xhtml` or with pandoc's `epub:type` on the Prologue.
- **Tablet line length** is about 95 characters at 768 px. Readers add their own margins, so leave it.

## Kindle vs Apple Books
- **Fonts:** `com.apple.ibooks.display-options.xml` sets `specified-fonts=true`, so Apple Books honours Georgia until the reader picks another font. Kindle ignores publisher fonts unless "Publisher Font" is chosen, and falls back to Bookerly. Georgia is not embedded, and Android readers have no Georgia, so the serif fallback applies there.
- **Page breaks:** Apple Books paginates each XHTML file separately and honours `page-break-before` inside a file in paginated mode. Kindle (KF8 through Send-to-Kindle or KDP conversion) honours `page-break-before:always`, but not `break-before`, so keep both, as written above. Neither app honours `vh` everywhere. `max-height:95vh` works in Apple Books and current Kindle apps; on older e-ink Kindles it is ignored, and the image is still scaled to the screen.
- **Plates:** both apps let you double-tap a plate to zoom it full screen. On Kindle e-ink this only works for images inside a block, which they are. The thin grey lines in the ch1 to ch11 plates will look washed out on e-ink. The darker ch12 to ch16 line weights survive better.
- **Headings and colour:** Kindle drops `color` on e-ink, which is harmless. Kindle forces a first-line indent on paragraphs only when none is set; ours is set to 0, which is correct.
- **Cover:** KDP takes the cover as a separate upload and ignores an in-book cover page. Apple Books takes it from the OPF `cover-image` property (pandoc `--epub-cover-image`).

## For the author to rule on
1. Plate type size for ch1 to ch11 at phone width: accept tap-to-zoom, or revise the plates (item 2).
2. The author's name as it should appear, and the title form: colon, or "RIVER. OAK. SUN." (item 6).
3. Which cover direction, if any, before a public build (item 7).
4. Em-dashes in Part titles and practice titles (item 8).

---

## 2026-11-10: page breaks, blank pages, and plates on the reader's page

Designer desk, 2026-11-10 12:40. **What started it:** the author read `book-draft.epub` on a phone reader in sepia and sent four screenshots. In them, Chapter 1's "Logical.", "Kind." and "Self-controlled." each start a new page, with the rest of the page blank. "You Own This" starts a page too. The book's very first page is fully blank. "The Gap" plate is an opaque white rectangle on the sepia page.

**Changed:** `runs/epub/tool/` only:
- `prep.py`, `epub.css` and `build.sh` were edited.
- `post.py` is new.
- `render_pages.js` is new: the paginated preview harness used below.

No chapter text was changed, and nothing in `books/` was touched.

### Defect 1: in-chapter heads open a new page
**Cause:**
- `epub.css` asks for no break before beat heads. The only page breaks it sets are on the plate, the practice title and the closing plate.
- Pandoc's EPUB writer, however, always wraps every heading and its text in a `<section>`. Chapter 1 alone had nine `section.level2` blocks, one per beat, including one for each virtue.
- The author's reader started a page at each beat. It also ignored at least part of our CSS: the headings are centred, the `hr` is full width, and the plate did not get its own page. So it is breaking on markup, either at every `<section>` or at every `h2`. I cannot tell which from the screenshots, so the fix removes both.

**Fix:** `post.py` runs after pandoc and rewrites the EPUB:
- All 146 `<section>` elements become `<div>`s, keeping the same id, class and `epub:type`. Nav targets still resolve; checked.
- All 92 in-chapter heads become `<p class="beat-heading" role="heading" aria-level="2"><strong>…</strong></p>`, as do the 16 "Practice" labels. That covers 86 `h2.beat-heading` plus the Introduction's 6 unclassed h2s. Screen readers still announce them as level-2 headings, and they still read bold if a reader drops our CSS.
- Chapter and Part titles stay `h1`, and the practice title stays `h2.dist-title`.
- The zip is rewritten with `mimetype` first and stored.

**Page starts now:** the CSS breaks before exactly four things:
- `figure` (chapter plate);
- `div.part-closing` (Part I's closing text);
- `div.closing-plate` (Part closing plates);
- `div.dist-title` (the practice page).

The practice page always follows a full-page plate, so its break adds no blank space. The 2026-11-07 decision (print's `distback`) stands.

### Defect 2: fully blank pages, including the first
**Cause:** not reproduced, because Chromium is not the author's reader. Two causes are likely from the markup:
- **(a) A break with nothing before it.** The same section-break behaviour as defect 1 applies at the start of a file. Every spine file, the title page included, opened with a `<section>`. A reader that breaks before a section and does not suppress the break at the top of a file emits an empty page first.
- **(b) Plates taller than the reader's page.** Plates were bounded at `max-height:95vh`. On a phone, the reader's header and footer eat more than 5% of the screen, so a plate after a forced break could be taller than the page. The plate then gets pushed on, leaving a blank page. The screenshot of "The Gap" shows the plate running into the footer.

**Fix:**
- (a) No `<section>` remains anywhere: checked, 0 in 23 files.
- (b) Plates are now bounded at `80vh`. The closing-plate image is `display:block` with `line-height:0`, so no text line box adds height under it.
- A further bug in the same area was fixed: Part closing pages never got their page. `prep.py` step 4 matched a `<p>` wrapper the compiled book never has. The plates are in `<div class="plate">` and the closing text follows `<div class="pb">`, and step 5 deleted both. So the Part I closing text ran straight on from the last practice item. Both now survive as `div.part-closing` (1) and `div.closing-plate` (3).

**Not fixed:** if the reader generates a blank page because the book has **no cover** (inbox #166, no cover yet), only a cover will remove it.

### Defect 3: plates sit on a white box
**Cause:**
- The plate PNGs are the print rasters from `chapter_pdf_local.py`: opaque RGB on white.
- The plate kit's `.knock` shapes (`fill: var(--plate-paper)`, #fff) clear the lines behind them, so transparency alone would still leave white dots.

**Fix:** `prep.py` step 3b derives an ink-only image from each print raster:
- All 19 rasters are greyscale (maximum channel spread 0) and drawn in the kit's one ink, #111. Every pixel is therefore a mix of ink and paper.
- `alpha = (255 - grey) / (255 - 17)` recovers the ink exactly. The output is a grey+alpha PNG with grey fixed at 17.
- Paper, including the knock-outs, becomes transparent. The ring in "The Gap" now shows the reader's page through its centre, and the lines behind it stay cleared.
- On any light page this looks identical to the print plate laid on that page.
- These files exist only in the EPUB. The print rasters and the SVG sources are untouched.

**Why not re-rasterise the SVGs with a transparent background?** It would still paint the knock shapes white, and it would need a second render path that could drift from print. The derived image is exactly the print plate, minus the paper.

**Size:** the EPUB grew from 1.88 MB to 2.48 MB.

### Night themes (decision)
Near-black ink on a black page is close to invisible: `2026-11-10-phone-night-unsignalled-ch01-plate.png`.

**What the build does:**
- Where the reader tells the book its theme, the CSS inverts the plate to light ink. That covers:
  - Apple Books' `__ibooks_internal_theme` attribute (Night, Gray);
  - Readium-based readers' `readium-night-on`.
- See `2026-11-10-phone-night-applebooks-*.png`.
- I did **not** key it to `prefers-color-scheme: dark`. That reports the phone's setting, not the reader's, so a phone in dark mode reading in sepia would get white ink on a sepia page, which is worse than the defect.

**Residual:** a reader in a dark theme that gives no signal will show the plates very faint. That includes the Kindle apps, Google Play Books and most Android readers, as far as I know.
- Kindle e-ink "dark mode" inverts the whole screen, so it is fine there.
- The alternative, a light card behind every plate, is exactly what the author rejected on sepia.

**Author ruling:** accept the residual, or ask for a plate-only light card in dark themes for a specific reader he uses.

### Verified, and how
- **Structure:**
  - All 23 XHTML files parse as XML.
  - Every `<img>` and every internal link and fragment resolves.
  - No XHTML file is empty; the smallest are the Part pages at 69 to 73 words, and the title page at 11.
  - The OPF manifest resolves.
  - `mimetype` is the first zip entry, stored.
- **Visual:** `render_pages.js` lays each file out as phone pages, 390x844 CSS px at 2x on #f0dfc6, with 20 px margins. It uses CSS columns, with every `break-before:page` mapped to a column break.
  - Pages rendered: title, contents, Prologue, Chapter 1 (13 pages), Chapter 5 with Part I closing (11), Chapter 12 (11), plus night renders.
  - A blank-page scan found **no blank page** in any rendered file.
  - The Chapter 1 virtues flow: "Logical." sits mid-page under "The Inward Turn", and "Kind.", "Self-controlled." and "Brave enough…" share the next page.
- **Not verified:**
  - **EPUBCheck: NOT RUN.** `/opt/epubcheck/epubcheck-5.1.0/epubcheck.jar` is not installed and cannot be downloaded here. `build.sh` still ends by calling it and exits 1 on that line. Two new constructs need its confirmation: `role="heading"` with `aria-level` on `<p>`, and `epub:type` on `<div>`.
  - **Real e-reader pagination cannot be fully emulated in a browser.** Chromium honours our CSS; the author's reader evidently does not. These renders prove what the markup and CSS now ask for, not what his app will do. The one real test is the author opening this build in the same app, in sepia and in night.

**Screenshots** (`runs/epub/epub-review-shots/2026-11-10-*`):
- `before-phone-sepia-ch01-plate-white-box`
- `phone-sepia-title-page`
- `phone-sepia-contents`
- `phone-sepia-prologue-p01`
- `phone-sepia-ch01-p06-virtues-start`
- `phone-sepia-ch01-p07-virtues-flow`
- `phone-sepia-ch01-p10-chapter-end`
- `phone-sepia-ch01-p11-plate`
- `phone-sepia-ch01-p12-practice`
- `phone-sepia-ch05-part1-closing-text`
- `phone-sepia-ch05-part1-closing-plate`
- `phone-sepia-ch12-plate`
- `phone-night-applebooks-ch01-plate`
- `phone-night-applebooks-part1-closing-plate`
- `phone-night-unsignalled-ch01-plate`

**Left open:**
1. Night-theme residual in readers that give no theme signal (above).
2. A blank first page caused by the missing cover, if that is what his reader does (inbox #166).
3. "Use it." ends Chapter 1 on a mostly empty page, because the plate that follows takes a page of its own. This is the rule the author set; it is not a defect.
4. The section rule (`hr`) printed just before each plate now sits alone at the foot of that page; the 2026-11-07 review noted it as harmless.
