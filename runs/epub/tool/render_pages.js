// node pages.js DIR OUTDIR prefix file1 file2 ...  -> paginated (CSS columns) phone render on sepia, one PNG per page
const { chromium } = require('playwright');
const [dir, out, prefix, theme, ...files] = process.argv.slice(2);
const W = 390, H = 844;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  const res = {};
  for (const f of files) {
    await p.goto('file://' + dir + '/' + f);
    await p.evaluate(([W, H, theme]) => {
      const night = theme.startsWith('night'); const bg = night ? '#000' : '#f0dfc6', fg = night ? '#ccc' : '#5b4636';
      if (theme === 'night') document.documentElement.setAttribute('__ibooks_internal_theme', '__NightTheme');
      const s = document.createElement('style');
      s.textContent = `html{background:${bg}!important;margin:0;height:${H}px;overflow:hidden}
        body{color:${fg};margin:0;padding:40px 20px;box-sizing:border-box;height:${H}px;
        column-width:${W - 40}px;column-gap:40px;column-fill:auto}`;
      document.head.appendChild(s);
      // emulate the e-reader's page: Chromium's multicol honours column breaks, not page breaks
      for (const el of document.body.querySelectorAll('*')) {
        const c = getComputedStyle(el);
        if (c.breakBefore === 'page' || c.pageBreakBefore === 'always') el.style.breakBefore = 'column';
      }
    }, [W, H, theme]);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(150);
    const n = await p.evaluate((W) => Math.round(document.body.scrollWidth / W), W);
    res[f] = n;
    for (let i = 0; i < n; i++) {
      await p.evaluate(([i, W]) => { document.body.style.transform = `translateX(${-i * W}px)`; }, [i, W]);
      await p.screenshot({ path: `${out}/${prefix}${f.replace(/\W+xhtml$/, '').replace(/.*\//, '')}-p${String(i + 1).padStart(2, '0')}.png` });
    }
    await p.evaluate(() => { document.body.style.transform = ''; });
  }
  console.log(JSON.stringify(res));
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
