"""
Generate Diagram2 v2 SVG from Python (avoids MCP write_file content corruption).
"""
from pathlib import Path

SVG = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="700" height="860" viewBox="0 0 700 860" xmlns="http://www.w3.org/2000/svg" style="background:white">
<style>
  text { font-family: 'Cambria','Times New Roman',serif; }
  .label { font-size: 10px; fill: #1a1a1a; }
  .label-b { font-size: 10px; fill: #1a1a1a; font-weight: 600; }
  .label-sm { font-size: 9px; fill: #555; }
  .label-it { font-size: 9px; fill: #555; font-style: italic; }
  .label-tech { font-size: 8.5px; fill: #777; font-style: italic; }
  .math { font-family: 'Cambria Math','Cambria',serif; font-size: 10px; fill: #333; font-style: italic; }
  .math-b { font-family: 'Cambria Math','Cambria',serif; font-size: 10.5px; fill: #1a1a1a; font-style: italic; font-weight: 600; }
  .box { fill: #fff; stroke: #1a1a1a; stroke-width: 0.8; }
  .box-shaded { fill: #f0f0f0; stroke: #1a1a1a; stroke-width: 0.8; }
  .box-dark { fill: #e0e0e0; stroke: #1a1a1a; stroke-width: 0.8; }
  .box-dashed { fill: none; stroke: #666; stroke-width: 0.6; stroke-dasharray: 5 3; }
  .box-section { fill: #fafafa; stroke: #999; stroke-width: 0.5; stroke-dasharray: 2 2; }
  .arr { stroke: #1a1a1a; stroke-width: 1; fill: none; }
  .arr-thick { stroke: #1a1a1a; stroke-width: 1.4; fill: none; }
  .arr-dashed { stroke: #666; stroke-width: 0.8; fill: none; stroke-dasharray: 5 3; }
  .arr-feedback { stroke: #555; stroke-width: 1; fill: none; stroke-dasharray: 8 4; }
  .arr-prob { stroke: #444; stroke-width: 0.8; fill: none; }
  .world { fill: #f5f5f5; stroke: #333; stroke-width: 0.8; }
  .world-sov { fill: #d0d0d0; stroke: #1a1a1a; stroke-width: 1.2; }
  .world-x { fill: #fff; stroke: #999; stroke-width: 0.8; stroke-dasharray: 2 2; }
</style>
<defs>
  <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M0 1L8 5L0 9Z" fill="#1a1a1a"/>
  </marker>
  <marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M0 1L8 5L0 9Z" fill="#555"/>
  </marker>
  <marker id="ahp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto">
    <path d="M0 1L8 5L0 9Z" fill="#444"/>
  </marker>
</defs>

<rect x="268" y="20" width="164" height="36" rx="4" class="box-shaded"/>
<text class="label-b" x="350" y="35" text-anchor="middle">Input data</text>
<text class="label-sm" x="350" y="47" text-anchor="middle">Features, context</text>

<rect x="450" y="20" width="200" height="40" rx="4" class="box-dashed"/>
<text class="label-sm" x="550" y="36" text-anchor="middle">S5 knowledge base</text>
<text class="label-it" x="550" y="48" text-anchor="middle">Sovereign + elastic predicates</text>
<line x1="550" y1="60" x2="550" y2="80" class="arr-dashed" marker-end="url(#ahg)"/>

<line x1="350" y1="56" x2="350" y2="76" class="arr" marker-end="url(#ah)"/>

<rect x="80" y="82" width="200" height="62" rx="4" class="box"/>
<text class="label-b" x="180" y="100" text-anchor="middle">S1 : Neural / ML predictor</text>
<text class="label-sm" x="180" y="114" text-anchor="middle">LLM, time-series, ensemble</text>
<text class="label-tech" x="180" y="126" text-anchor="middle">e.g. LSTM (Manaus SIH), LightGBM (CEAF), GPT</text>
<text class="label-it" x="180" y="138" text-anchor="middle">produces |psi_N&gt;</text>

<rect x="450" y="82" width="200" height="62" rx="4" class="box"/>
<text class="label-b" x="550" y="100" text-anchor="middle">S5 : Normative engine</text>
<text class="label-sm" x="550" y="114" text-anchor="middle">Clingo (ASP) solver</text>
<text class="label-tech" x="550" y="126" text-anchor="middle">probabilistic annotations; sovereign vs. elastic rules</text>
<text class="label-it" x="550" y="138" text-anchor="middle">produces |psi_S&gt;</text>

<path d="M350 76 L180 76 L180 82" class="arr" fill="none" marker-end="url(#ah)"/>
<path d="M350 76 L550 76 L550 82" class="arr" fill="none" marker-end="url(#ah)"/>
<text class="label-sm" x="350" y="115" text-anchor="middle">||</text>

<rect x="120" y="170" width="460" height="80" rx="8" class="box-dashed"/>
<text class="label-sm" x="136" y="185">S3* : Quantum audit channel</text>

<rect x="240" y="190" width="220" height="44" rx="4" class="box-dark"/>
<text class="label-b" x="350" y="208" text-anchor="middle">theta = arccos( &lt;psi_N | psi_S&gt; )</text>
<text class="label-sm" x="350" y="224" text-anchor="middle">Ontological friction measurement</text>

<line x1="180" y1="144" x2="180" y2="212" class="arr-thick"/>
<path d="M180 212 L238 212" class="arr-thick" marker-end="url(#ah)"/>
<text class="math" x="184" y="180">|psi_N&gt;</text>

<line x1="550" y1="144" x2="550" y2="212" class="arr-thick"/>
<path d="M550 212 L462 212" class="arr-thick" marker-end="url(#ah)"/>
<text class="math" x="510" y="180">|psi_S&gt;</text>

<line x1="350" y1="250" x2="350" y2="286" class="arr-thick" marker-end="url(#ah)"/>
<text class="math" x="358" y="274">theta</text>

<polygon points="350,290 410,330 350,370 290,330" class="box-shaded"/>
<text class="label-b" x="350" y="326" text-anchor="middle">Circuit</text>
<text class="label-b" x="350" y="339" text-anchor="middle">breaker</text>

<text class="label-sm" x="210" y="324" text-anchor="end">theta &lt; theta_crit</text>
<text class="label-sm" x="488" y="324" text-anchor="start">theta &gt; theta_crit</text>

<path d="M290 330 L130 330 L130 390" class="arr-thick" fill="none" marker-end="url(#ah)"/>
<rect x="50" y="394" width="160" height="56" rx="4" class="box"/>
<text class="label-b" x="130" y="414" text-anchor="middle">STAC</text>
<text class="label-sm" x="130" y="426" text-anchor="middle">Authorized execution</text>
<text class="label-it" x="130" y="438" text-anchor="middle">P(Action) amplified</text>

<path d="M410 330 L570 330 L570 390" class="arr-thick" fill="none" marker-end="url(#ah)"/>
<rect x="490" y="394" width="160" height="56" rx="4" class="box"/>
<text class="label-b" x="570" y="414" text-anchor="middle">Block + HITL audit</text>
<text class="label-sm" x="570" y="426" text-anchor="middle">Decision routed to human</text>
<text class="label-it" x="570" y="438" text-anchor="middle">P(Action) suppressed</text>

<path d="M650 422 L666 422 L666 110 L632 110" class="arr-feedback" marker-end="url(#ahg)"/>
<text class="label-sm" x="672" y="266" transform="rotate(90,672,266)" text-anchor="middle">Algedonic signal (S4 bypass)</text>

<line x1="350" y1="370" x2="350" y2="484" class="arr-dashed" marker-end="url(#ahg)"/>
<text class="label-sm" x="358" y="434">log theta, psi_N, psi_S</text>

<rect x="100" y="488" width="500" height="92" rx="6" class="box-shaded"/>
<text class="label-b" x="350" y="506" text-anchor="middle">Ontological Feature Store</text>
<text class="label-sm" x="350" y="520" text-anchor="middle">Logs: theta(t), psi_N(t), psi_S(t), active predicates, regime classification</text>

<line x1="115" y1="530" x2="585" y2="530" stroke="#999" stroke-width="0.4" stroke-dasharray="2 2"/>
<text class="math-b" x="350" y="547" text-anchor="middle">L_Global = L_Perf + lambda . max(0, -cos theta)</text>
<text class="label-it" x="350" y="561" text-anchor="middle">cybernetic loss; gradient propagated to S1 for progressive weight adjustment</text>
<text class="label-tech" x="350" y="573" text-anchor="middle">[Eq. 11]   d L_Global / d w_S1 -&gt; continuous training</text>

<path d="M130 450 L130 508 L98 508" class="arr-dashed" fill="none" marker-end="url(#ahg)"/>
<path d="M570 450 L570 508 L602 508" class="arr-dashed" fill="none" marker-end="url(#ahg)"/>

<path d="M100 539 L34 539 L34 110 L78 110" class="arr-feedback" marker-end="url(#ahg)"/>
<text class="label-sm" x="30" y="320" transform="rotate(-90,30,320)" text-anchor="middle">Continuous training (gradient from L_Global)</text>

<line x1="40" y1="602" x2="660" y2="602" stroke="#999" stroke-width="0.5"/>

<rect x="40" y="618" width="620" height="200" rx="8" class="box-section"/>
<text class="label-b" x="350" y="638" text-anchor="middle">Markovian horizon of possible worlds</text>
<text class="label-sm" x="350" y="651" text-anchor="middle">Clingo (ASP) stable models weighted by Boltzmann distribution; sovereign worlds shielded; theta_eff(t) navigates the horizon over time</text>

<circle cx="350" cy="725" r="22" class="world-sov"/>
<text class="math-b" x="350" y="729" text-anchor="middle">omega*</text>
<text class="label-tech" x="350" y="755" text-anchor="middle">sovereign anchor</text>
<text class="label-tech" x="350" y="767" text-anchor="middle">w -&gt; +infinity</text>

<circle cx="270" cy="710" r="14" class="world"/>
<text class="math" x="270" y="714" text-anchor="middle">omega_1</text>
<text class="label-tech" x="270" y="735" text-anchor="middle">P high</text>

<circle cx="430" cy="710" r="14" class="world"/>
<text class="math" x="430" y="714" text-anchor="middle">omega_2</text>
<text class="label-tech" x="430" y="735" text-anchor="middle">P high</text>

<circle cx="190" cy="735" r="11" class="world"/>
<text class="math" x="190" y="739" text-anchor="middle">omega_3</text>
<text class="label-tech" x="190" y="758" text-anchor="middle">P mid</text>

<circle cx="510" cy="735" r="11" class="world"/>
<text class="math" x="510" y="739" text-anchor="middle">omega_4</text>
<text class="label-tech" x="510" y="758" text-anchor="middle">P mid</text>

<circle cx="115" cy="760" r="10" class="world-x"/>
<text class="math" x="115" y="764" text-anchor="middle">omega_5</text>
<text class="label-tech" x="115" y="783" text-anchor="middle">P -&gt; 0</text>

<circle cx="585" cy="760" r="10" class="world-x"/>
<text class="math" x="585" y="764" text-anchor="middle">omega_6</text>
<text class="label-tech" x="585" y="783" text-anchor="middle">P -&gt; 0</text>

<path d="M340 710 L284 703" class="arr-prob" marker-end="url(#ahp)" stroke-width="1.4"/>
<path d="M360 710 L416 703" class="arr-prob" marker-end="url(#ahp)" stroke-width="1.4"/>
<path d="M331 723 L201 732" class="arr-prob" marker-end="url(#ahp)" stroke-width="0.9"/>
<path d="M369 723 L499 732" class="arr-prob" marker-end="url(#ahp)" stroke-width="0.9"/>
<path d="M329 734 L125 758" class="arr-prob" marker-end="url(#ahp)" stroke-width="0.5" stroke-dasharray="3 2"/>
<path d="M371 734 L575 758" class="arr-prob" marker-end="url(#ahp)" stroke-width="0.5" stroke-dasharray="3 2"/>

<path d="M115 800 Q 200 745, 350 790 T 585 800" stroke="#888" stroke-width="0.8" fill="none" stroke-dasharray="2 3"/>
<text class="label-it" x="350" y="810" text-anchor="middle">theta_eff(t) trajectory: adaptive memory over the horizon  [Eq. 5]</text>

<path d="M260 580 L260 615" class="arr-dashed" marker-end="url(#ahg)"/>
<text class="label-sm" x="265" y="600">P(omega | t) updated</text>

<path d="M440 615 L440 580" class="arr-dashed" marker-end="url(#ahg)"/>
<text class="label-sm" x="445" y="600">active worlds -&gt; S5</text>

</svg>
'''

out = Path(r"C:\Workspace\academico\qfeng_validacao\artefatos\figuras_paper1\Diagram2_QFENG_Engineering_v2.svg")
out.write_text(SVG, encoding="utf-8")
print("WROTE", out, "size:", out.stat().st_size, "bytes")
