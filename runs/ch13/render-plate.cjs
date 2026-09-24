// Artifact renderer: the repository's Chromium renderer targets Linux;
// use bundled Sharp/librsvg on this Mac without changing production scripts.
const sharp = require('/Users/nholland/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const fs = require('fs');
(async()=>{
  const [src,dest]=process.argv.slice(2);
  if(!src||!dest) throw Error('Usage: node render-plate.cjs input.svg output.png');
  await sharp(fs.readFileSync(src),{density:216}).png().toFile(dest);
  console.log(dest);
})();
