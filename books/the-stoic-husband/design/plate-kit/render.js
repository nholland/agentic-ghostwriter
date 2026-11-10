// Render a plate figure on a 6x9in book page, as PNG (preview) and PDF (to confirm it stays vector).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const name = process.argv[2];
const dir = __dirname;
const font = (w, s) => `@font-face{font-family:"EB Garamond";font-weight:${w};font-style:${s};src:url("file://${dir}/node_modules/@fontsource/eb-garamond/files/eb-garamond-latin-${w}-${s}.woff2")}`;
const html = `<!doctype html><meta charset="utf-8"><style>
${[400, 500].flatMap(w => ['normal', 'italic'].map(s => font(w, s))).join('\n')}
${fs.readFileSync(path.join(dir, 'plates.css'), 'utf8')}
@page{size:6in 9in;margin:0} html,body{margin:0}
body{width:6in;height:9in;display:flex;align-items:center;justify-content:center}
.block{width:324pt}
</style><div class="block">${fs.readFileSync(path.join(dir, 'out', name + '.figure.html'), 'utf8')}</div>`;
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 576, height: 864 }, deviceScaleFactor: 3 });
  fs.writeFileSync(path.join(dir,'out',name+'.preview.html'),html); await pg.goto('file://'+path.join(dir,'out',name+'.preview.html')); await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: path.join(dir, 'out', name + '.page.png') });
  await (await pg.$('figure')).screenshot({ path: path.join(dir, 'out', name + '.png') });
  await pg.pdf({ path: path.join(dir, 'out', name + '.pdf'), width: '6in', height: '9in', printBackground: true });
  await b.close();
})();
