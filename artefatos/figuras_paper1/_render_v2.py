import cairosvg
from pathlib import Path
ROOT = Path(r"C:\Workspace\academico\qfeng_validacao\artefatos\figuras_paper1")
src = ROOT / "Diagram2_QFENG_Engineering_v2.svg"
dst = ROOT / "Diagram2_QFENG_Engineering_v2.png"
cairosvg.svg2png(url=str(src), write_to=str(dst), output_width=1400)
print("OK", dst, "size:", dst.stat().st_size, "bytes")
