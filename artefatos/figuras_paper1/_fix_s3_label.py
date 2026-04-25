"""
Patch Diagram2_QFENG_Engineering_v2.svg:
centralize the S3* label inside the dashed rectangle and move it away
from the |psi_N> arrow.

Original line:
  <text class="label-sm" x="136" y="185">S3* : Quantum audit channel</text>

New line (centered on rect x=120 width=460 -> cx=350; y moved up to 165
to sit just above the box top at y=170):
  <text class="label-sm" x="350" y="165" text-anchor="middle">S3* : Quantum audit channel</text>
"""
from pathlib import Path

p = Path(r"C:\Workspace\academico\qfeng_validacao\artefatos\figuras_paper1\Diagram2_QFENG_Engineering_v2.svg")
txt = p.read_text(encoding="utf-8")

old = '<text class="label-sm" x="136" y="185">S3* : Quantum audit channel</text>'
new = '<text class="label-b" x="350" y="165" text-anchor="middle">S3* : Quantum audit channel</text>'

if old in txt:
    new_txt = txt.replace(old, new)
    p.write_text(new_txt, encoding="utf-8")
    print("OK: S3* label centered and lifted above the dashed box")
    print("   from x=136 y=185 (left, overlapping psi_N) -> x=350 y=165 (centered, above box)")
else:
    print("FAIL: old line not found exactly")
    # Show occurrences of S3* for debug
    import re
    for m in re.finditer(r'<text[^>]*>[^<]*S3\*[^<]*</text>', txt):
        print("  match:", m.group()[:200])
