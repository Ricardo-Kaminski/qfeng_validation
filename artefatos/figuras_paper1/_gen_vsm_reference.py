"""
Generates the VSM Reference Diagram for Paper 1 Q-FENG.
Canonical Beer (1972/1979) Viable System Model with S3* explicit audit channel.
Neutral white background, no embedded title/caption (caption goes in DOCX).
Output: VSM_Reference_clean.svg + .png 300dpi
"""

from pathlib import Path

OUT_DIR = Path(r"C:\Workspace\academico\qfeng_validacao\artefatos\figuras_paper1")
SVG_PATH = OUT_DIR / "VSM_Reference_clean.svg"
PNG_PATH = OUT_DIR / "VSM_Reference_clean.png"

# Canvas: 1100 x 800 — proportions tuned for portrait reading flow
SVG = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 800" width="1100" height="800" font-family="Arial, Helvetica, sans-serif">

  <!-- ============= Defs: arrow markers ============= -->
  <defs>
    <marker id="arrow-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a1a"/>
    </marker>
    <marker id="arrow-dashed" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#777"/>
    </marker>
    <marker id="arrow-algedonic" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#b8860b"/>
    </marker>
  </defs>

  <!-- ============= External Environment (left ellipse) ============= -->
  <ellipse cx="120" cy="430" rx="95" ry="280" fill="none" stroke="#666" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="120" y="170" text-anchor="middle" font-size="13" font-weight="600" fill="#444">External</text>
  <text x="120" y="187" text-anchor="middle" font-size="13" font-weight="600" fill="#444">Environment</text>
  <text x="120" y="215" text-anchor="middle" font-size="11" fill="#555" font-style="italic">(regulatory,</text>
  <text x="120" y="231" text-anchor="middle" font-size="11" fill="#555" font-style="italic">institutional,</text>
  <text x="120" y="247" text-anchor="middle" font-size="11" fill="#555" font-style="italic">social)</text>

  <!-- ============= S5 — Policy / Identity (top right) ============= -->
  <rect x="640" y="50" width="380" height="90" rx="6" ry="6" fill="#fafafa" stroke="#1a1a1a" stroke-width="2"/>
  <text x="830" y="78" text-anchor="middle" font-size="15" font-weight="700" fill="#1a1a1a">System 5  —  Policy &amp; Identity</text>
  <text x="830" y="100" text-anchor="middle" font-size="12" fill="#333">Constitutive grounding; defines what the</text>
  <text x="830" y="116" text-anchor="middle" font-size="12" fill="#333">organisation is and what it is for</text>
  <text x="830" y="133" text-anchor="middle" font-size="11" fill="#0066a0" font-style="italic">(Q-FENG: ScopeConfig + sovereignty hierarchy)</text>

  <!-- ============= S4 — Intelligence / Adaptation ============= -->
  <rect x="640" y="180" width="380" height="90" rx="6" ry="6" fill="#fafafa" stroke="#1a1a1a" stroke-width="2"/>
  <text x="830" y="208" text-anchor="middle" font-size="15" font-weight="700" fill="#1a1a1a">System 4  —  Intelligence &amp; Adaptation</text>
  <text x="830" y="230" text-anchor="middle" font-size="12" fill="#333">Prospective monitoring of the environment;</text>
  <text x="830" y="246" text-anchor="middle" font-size="12" fill="#333">detection of trajectory changes; projection</text>
  <text x="830" y="263" text-anchor="middle" font-size="11" fill="#0066a0" font-style="italic">(Q-FENG: Markovian θ_eff + institutional BI)</text>

  <!-- ============= S3 — Operational Control ============= -->
  <rect x="640" y="310" width="380" height="90" rx="6" ry="6" fill="#fafafa" stroke="#1a1a1a" stroke-width="2"/>
  <text x="830" y="338" text-anchor="middle" font-size="15" font-weight="700" fill="#1a1a1a">System 3  —  Operational Control</text>
  <text x="830" y="360" text-anchor="middle" font-size="12" fill="#333">Direct command authority over S1;</text>
  <text x="830" y="376" text-anchor="middle" font-size="12" fill="#333">resource allocation; operational targets</text>
  <text x="830" y="393" text-anchor="middle" font-size="11" fill="#0066a0" font-style="italic">(Q-FENG: Circuit Breaker θ ≥ 120°)</text>

  <!-- ============= S2 — Coordination (lateral right triangle) ============= -->
  <polygon points="525,330 615,310 615,400 525,380" fill="#fafafa" stroke="#1a1a1a" stroke-width="2"/>
  <text x="570" y="348" text-anchor="middle" font-size="13" font-weight="700" fill="#1a1a1a">System 2</text>
  <text x="570" y="365" text-anchor="middle" font-size="12" fill="#333">Coordination</text>
  <text x="570" y="381" text-anchor="middle" font-size="9" fill="#0066a0" font-style="italic">(Q-FENG: cross-corpus)</text>

  <!-- ============= S1 — Operational Units (four horizontal pairs) ============= -->
  <!-- S1 unit 1 -->
  <rect x="290" y="450" width="180" height="55" rx="6" ry="6" fill="#fafafa" stroke="#1a1a1a" stroke-width="1.8"/>
  <text x="380" y="475" text-anchor="middle" font-size="12" font-weight="600" fill="#1a1a1a">Operational Unit 1</text>
  <text x="380" y="492" text-anchor="middle" font-size="10" fill="#555" font-style="italic">(local sub-environment)</text>

  <rect x="500" y="450" width="180" height="55" rx="6" ry="6" fill="#fafafa" stroke="#1a1a1a" stroke-width="1.8"/>
  <text x="590" y="475" text-anchor="middle" font-size="12" font-weight="600" fill="#1a1a1a">Decision / Operation</text>
  <text x="590" y="492" text-anchor="middle" font-size="10" fill="#555" font-style="italic">(produces output)</text>

  <!-- S1 unit 2 -->
  <rect x="290" y="525" width="180" height="55" rx="6" ry="6" fill="#fafafa" stroke="#1a1a1a" stroke-width="1.8"/>
  <text x="380" y="550" text-anchor="middle" font-size="12" font-weight="600" fill="#1a1a1a">Operational Unit 2</text>
  <text x="380" y="567" text-anchor="middle" font-size="10" fill="#555" font-style="italic">(local sub-environment)</text>

  <rect x="500" y="525" width="180" height="55" rx="6" ry="6" fill="#fafafa" stroke="#1a1a1a" stroke-width="1.8"/>
  <text x="590" y="550" text-anchor="middle" font-size="12" font-weight="600" fill="#1a1a1a">Decision / Operation</text>
  <text x="590" y="567" text-anchor="middle" font-size="10" fill="#555" font-style="italic">(produces output)</text>

  <!-- S1 unit 3 -->
  <rect x="290" y="600" width="180" height="55" rx="6" ry="6" fill="#fafafa" stroke="#1a1a1a" stroke-width="1.8"/>
  <text x="380" y="625" text-anchor="middle" font-size="12" font-weight="600" fill="#1a1a1a">Operational Unit 3</text>
  <text x="380" y="642" text-anchor="middle" font-size="10" fill="#555" font-style="italic">(local sub-environment)</text>

  <rect x="500" y="600" width="180" height="55" rx="6" ry="6" fill="#fafafa" stroke="#1a1a1a" stroke-width="1.8"/>
  <text x="590" y="625" text-anchor="middle" font-size="12" font-weight="600" fill="#1a1a1a">Decision / Operation</text>
  <text x="590" y="642" text-anchor="middle" font-size="10" fill="#555" font-style="italic">(produces output)</text>

  <!-- S1 envelope label -->
  <text x="395" y="430" text-anchor="middle" font-size="14" font-weight="700" fill="#1a1a1a">System 1  —  Operational Units</text>
  <text x="395" y="685" text-anchor="middle" font-size="11" fill="#0066a0" font-style="italic">(Q-FENG: algorithmic predictor producing ψ_N)</text>

  <!-- Dotted boundary around the four S1 pairs -->
  <rect x="280" y="442" width="408" height="225" rx="8" ry="8" fill="none" stroke="#888" stroke-width="1.2" stroke-dasharray="3,3"/>

  <!-- ============= S3* Audit Channel — long dashed line bypassing S2 ============= -->
  <!-- Path from S3 directly down to S1 area -->
  <line x1="700" y1="400" x2="600" y2="450" stroke="#b8860b" stroke-width="2" stroke-dasharray="9,5" marker-end="url(#arrow-algedonic)"/>
  <line x1="730" y1="400" x2="600" y2="525" stroke="#b8860b" stroke-width="2" stroke-dasharray="9,5" marker-end="url(#arrow-algedonic)"/>
  <line x1="760" y1="400" x2="600" y2="600" stroke="#b8860b" stroke-width="2" stroke-dasharray="9,5" marker-end="url(#arrow-algedonic)"/>

  <!-- S3* label -->
  <rect x="765" y="430" width="200" height="45" rx="4" ry="4" fill="#fff8e7" stroke="#b8860b" stroke-width="1.5"/>
  <text x="865" y="450" text-anchor="middle" font-size="12" font-weight="700" fill="#8b6508">S3*  —  Audit Channel</text>
  <text x="865" y="466" text-anchor="middle" font-size="10" fill="#8b6508" font-style="italic">(Q-FENG: Clingo SAT/UNSAT)</text>

  <!-- ============= Vertical communication channels (S5↔S4↔S3) ============= -->
  <line x1="830" y1="140" x2="830" y2="178" stroke="#1a1a1a" stroke-width="2" marker-end="url(#arrow-solid)"/>
  <line x1="810" y1="178" x2="810" y2="140" stroke="#1a1a1a" stroke-width="2" marker-end="url(#arrow-solid)"/>

  <line x1="830" y1="270" x2="830" y2="308" stroke="#1a1a1a" stroke-width="2" marker-end="url(#arrow-solid)"/>
  <line x1="810" y1="308" x2="810" y2="270" stroke="#1a1a1a" stroke-width="2" marker-end="url(#arrow-solid)"/>

  <!-- ============= S3 ↔ S2 horizontal coordination ============= -->
  <line x1="640" y1="345" x2="615" y2="350" stroke="#1a1a1a" stroke-width="1.8" marker-end="url(#arrow-solid)"/>
  <line x1="615" y1="365" x2="640" y2="370" stroke="#1a1a1a" stroke-width="1.8" marker-end="url(#arrow-solid)"/>

  <!-- ============= S2 ↔ S1 coordination (anti-oscillation) ============= -->
  <line x1="525" y1="350" x2="500" y2="475" stroke="#1a1a1a" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrow-solid)"/>
  <line x1="525" y1="365" x2="500" y2="550" stroke="#1a1a1a" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrow-solid)"/>
  <line x1="525" y1="380" x2="500" y2="625" stroke="#1a1a1a" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrow-solid)"/>

  <!-- ============= S3 → S1 command (operational control) ============= -->
  <line x1="700" y1="400" x2="680" y2="475" stroke="#1a1a1a" stroke-width="2" marker-end="url(#arrow-solid)"/>
  <line x1="720" y1="400" x2="680" y2="550" stroke="#1a1a1a" stroke-width="2" marker-end="url(#arrow-solid)"/>
  <line x1="740" y1="400" x2="680" y2="625" stroke="#1a1a1a" stroke-width="2" marker-end="url(#arrow-solid)"/>

  <!-- ============= S1 → S3 reporting (dashed, lighter) ============= -->
  <line x1="685" y1="465" x2="700" y2="400" stroke="#777" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow-dashed)"/>
  <line x1="685" y1="540" x2="720" y2="400" stroke="#777" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow-dashed)"/>
  <line x1="685" y1="615" x2="740" y2="400" stroke="#777" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow-dashed)"/>

  <!-- ============= External Environment ↔ S1 (operational interaction) ============= -->
  <line x1="215" y1="475" x2="285" y2="475" stroke="#666" stroke-width="1.5" marker-end="url(#arrow-solid)"/>
  <line x1="215" y1="550" x2="285" y2="550" stroke="#666" stroke-width="1.5" marker-end="url(#arrow-solid)"/>
  <line x1="215" y1="625" x2="285" y2="625" stroke="#666" stroke-width="1.5" marker-end="url(#arrow-solid)"/>

  <!-- ============= External Environment ↔ S4 (environmental scanning) ============= -->
  <path d="M 200 250 Q 400 230 640 220" fill="none" stroke="#666" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#arrow-dashed)"/>

  <!-- ============= Algedonic channel S1 → S5 (long dashed, gold) ============= -->
  <path d="M 470 470 Q 280 280 640 95" fill="none" stroke="#b8860b" stroke-width="1.8" stroke-dasharray="12,4" marker-end="url(#arrow-algedonic)"/>
  <text x="290" y="265" font-size="10" fill="#8b6508" font-style="italic" font-weight="600">algedonic</text>
  <text x="290" y="278" font-size="10" fill="#8b6508" font-style="italic" font-weight="600">signal</text>

  <!-- ============= Legend (bottom) ============= -->
  <g transform="translate(50, 730)">
    <line x1="0" y1="6" x2="35" y2="6" stroke="#1a1a1a" stroke-width="2" marker-end="url(#arrow-solid)"/>
    <text x="42" y="10" font-size="10" fill="#333">command / inference</text>

    <line x1="200" y1="6" x2="235" y2="6" stroke="#777" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arrow-dashed)"/>
    <text x="242" y="10" font-size="10" fill="#333">reporting / data flow</text>

    <line x1="395" y1="6" x2="430" y2="6" stroke="#b8860b" stroke-width="2" stroke-dasharray="9,5" marker-end="url(#arrow-algedonic)"/>
    <text x="437" y="10" font-size="10" fill="#333">audit / algedonic channel</text>

    <line x1="635" y1="6" x2="670" y2="6" stroke="#1a1a1a" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrow-solid)"/>
    <text x="677" y="10" font-size="10" fill="#333">anti-oscillatory coordination</text>

    <text x="950" y="10" font-size="10" fill="#0066a0" font-style="italic">blue: Q-FENG mapping</text>
  </g>

</svg>
'''

# Write SVG
SVG_PATH.write_text(SVG, encoding='utf-8')
print(f"SVG written: {SVG_PATH} ({SVG_PATH.stat().st_size} bytes)")

# Render PNG via cairosvg
try:
    import cairosvg
    cairosvg.svg2png(
        url=str(SVG_PATH),
        write_to=str(PNG_PATH),
        output_width=1650,  # 300dpi at 5.5 inches wide
        output_height=1200
    )
    print(f"PNG written: {PNG_PATH} ({PNG_PATH.stat().st_size} bytes)")
except ImportError:
    print("cairosvg not installed; skipping PNG render. SVG-only output.")
except Exception as e:
    print(f"PNG render failed: {e}")
    print("SVG is available; PNG can be rendered separately if needed.")
