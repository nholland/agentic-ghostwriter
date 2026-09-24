"""Run unchanged house checker with this Mac's bundled DejaVu font path."""
import sys
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
repo=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(repo/'scripts'))
import plate_check
import chapter_pdf_local
def local_render(svg_path, png_path, scale=3):
    if scale != 3:
        raise ValueError('Local Sharp helper is configured for 3x rendering')
    subprocess.run(['node', str(repo/'runs/ch13/render-plate.cjs'), str(svg_path), str(png_path)], check=True, capture_output=True)
    box = ET.parse(svg_path).getroot().attrib['viewBox'].split()
    return float(box[2]), float(box[3])
chapter_pdf_local.svg_to_png = local_render
plate_check.D='/Users/nholland/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype/DejaVuSerif%s.ttf'
raise SystemExit(plate_check.main())
