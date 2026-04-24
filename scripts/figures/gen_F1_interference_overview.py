#!/usr/bin/env python3
"""
gen_F1_interference_overview.py
================================
Gera Figure 1 do Paper 1 Q-FENG Validation — overview agregado dos 7
cenarios no espaco angular, como porta de entrada visual da Secao 5
(Results), antes do detalhamento por cenario que Figure 3 fornece.

Paleta canonica herdada de F3_hilbert_decision_space.svg (matplotlib).
Tipografia: serif (Cambria > Libertinus > Times).

Saidas em outputs/figures/:
  F1_interference_overview.svg
  F1_interference_overview.png  (200 DPI)
  F1_interference_overview.pdf

Execucao (Windows PowerShell, environment qfeng):
  conda activate qfeng
  cd C:\\Workspace\\academico\\qfeng_validacao
  python scripts\\figures\\gen_F1_interference_overview.py

Autor: Ricardo S. Kaminski
Data: 2026-04-22
"""
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Wedge
import numpy as np

# ===========================================================================
# PALETA CANONICA (herdada de F3/F4)
# ===========================================================================
CB_DARK      = "#8b2e2e"   # vinho CB
STAC_DARK    = "#1f4e79"   # azul STAC
STAC_BG      = "#eaf2f8"   # azul claro (setor STAC)
HITL_BG      = "#faf4e6"   # bege (setor HITL)
CB_BG        = "#f6e8e8"   # rosa claro (setor CB)
TEXT_DARK    = "#111111"
TEXT_MID     = "#4a4a4a"
GRID_MID     = "#888888"
GRID_LIGHT   = "#bbbbbb"
AXIS_BLACK   = "#111111"
PSI_S_COLOR  = "#111111"
HITL_COLOR   = "#a07a30"   # bronze escuro para HITL

# ===========================================================================
# DADOS DOS CENARIOS (valores validados em validation_results.parquet)
# ===========================================================================
SCENARIOS = [
    ("C2",       "CB",   "Health", 132.36,  16.75),
    ("C3",       "CB",   "Health", 134.67,  25.16),
    ("C7",       "CB",   "Health", 133.74,  10.66),
    ("T-CLT-01", "CB",   "Labour", 134.08,   9.37),
    ("T-CLT-02", "CB",   "Labour", 127.81,  11.23),
    ("T-CLT-03", "STAC", "Labour",   5.65,  -0.28),
    ("T-CLT-04", "STAC", "Labour",   7.05,  -0.44),
]

# ===========================================================================
# CONFIG TIPOGRAFICA
# ===========================================================================
mpl.rcParams.update({
    "font.family":      "serif",
    "font.serif":       ["Cambria", "Libertinus Serif", "DejaVu Serif",
                         "Times New Roman", "serif"],
    "mathtext.fontset": "stix",
    "axes.edgecolor":   AXIS_BLACK,
    "axes.linewidth":   0.8,
    "text.color":       TEXT_DARK,
    "svg.fonttype":     "none",
    "pdf.fonttype":     42,
})

# ===========================================================================
# FIGURA
# ===========================================================================
fig = plt.figure(figsize=(11.5, 6.6), facecolor="white")
gs = fig.add_gridspec(1, 2, width_ratios=[2.0, 1.0], wspace=0.06,
                      left=0.03, right=0.98, top=0.86, bottom=0.10)

ax = fig.add_subplot(gs[0, 0])
ax.set_aspect("equal")
ax.set_xlim(-1.35, 1.35)
ax.set_ylim(-0.42, 1.38)
ax.axis("off")

# ===========================================================================
# SETORES DE REGIME (semicirculo)
# ===========================================================================
R = 1.00
CENTER = (0.0, 0.0)

for w in [Wedge(CENTER, R, 0, 30, facecolor=STAC_BG, edgecolor="none",
                alpha=0.95, zorder=1),
          Wedge(CENTER, R, 30, 120, facecolor=HITL_BG, edgecolor="none",
                alpha=0.95, zorder=1),
          Wedge(CENTER, R, 120, 180, facecolor=CB_BG, edgecolor="none",
                alpha=0.95, zorder=1)]:
    ax.add_patch(w)

# Limites entre setores
for boundary_deg in [30, 120]:
    rad = np.deg2rad(boundary_deg)
    ax.plot([0, R*np.cos(rad)], [0, R*np.sin(rad)],
            color=GRID_MID, lw=0.6, linestyle=(0, (2, 2)), zorder=2)

# Arco externo
theta_arc = np.linspace(0, np.pi, 200)
ax.plot(R*np.cos(theta_arc), R*np.sin(theta_arc),
        color=GRID_LIGHT, lw=0.8, zorder=2)

# Linha base horizontal
ax.plot([-R-0.05, R+0.05], [0, 0], color=AXIS_BLACK, lw=0.9, zorder=3)

# ===========================================================================
# VETOR |psi_S> (referencia horizontal)
# ===========================================================================
ax.annotate("", xy=(R*0.95, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>,head_length=0.5,head_width=0.22",
                            color=PSI_S_COLOR, lw=1.9,
                            shrinkA=0, shrinkB=0),
            zorder=10)
ax.text(R*1.02, -0.09, r"$|\psi_S\rangle$",
        fontsize=12, color=TEXT_DARK, ha="left", va="top",
        style="italic", fontweight="bold")

# ===========================================================================
# CLUSTER CB (5 cenarios, 127.8-134.7 deg)
# Staggering radial + callouts externos ordenados
# ===========================================================================
cb_label_config = [
    # (label, theta_deg, vec_radius, label_theta_deg, label_radius)
    ("T-CLT-02", 127.81, 0.95, 128, 1.23),
    ("C2",       132.36, 0.88, 136, 1.25),
    ("C7",       133.74, 0.81, 146, 1.22),
    ("T-CLT-01", 134.08, 0.74, 158, 1.18),
    ("C3",       134.67, 0.67, 170, 1.02),
]

for label, theta_deg, vec_r, lbl_ang, lbl_r in cb_label_config:
    rad = np.deg2rad(theta_deg)
    lbl_rad = np.deg2rad(lbl_ang)
    x_end = vec_r * np.cos(rad)
    y_end = vec_r * np.sin(rad)
    x_lbl = lbl_r * np.cos(lbl_rad)
    y_lbl = lbl_r * np.sin(lbl_rad)

    ax.annotate("", xy=(x_end, y_end), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>,head_length=0.4,head_width=0.18",
                                color=CB_DARK, lw=1.5, linestyle="--",
                                shrinkA=0, shrinkB=0),
                zorder=8)

    ax.plot([x_end, x_lbl], [y_end, y_lbl],
            color=CB_DARK, lw=0.5, alpha=0.5, zorder=7)

    ha = ("right" if x_lbl < x_end
          else ("left" if x_lbl > x_end + 0.05 else "center"))
    ax.text(x_lbl, y_lbl, label,
            fontsize=9.5, color=CB_DARK,
            ha=ha, va="center", fontweight="bold", zorder=12)

# ===========================================================================
# CLUSTER STAC (2 cenarios, 5.7-7.1 deg)
# Callouts abaixo do eixo horizontal para evitar colisao com |psi_S>
# ===========================================================================
stac_label_config = [
    # (label, theta_deg, vec_radius, label_x_abs, label_y_abs)
    ("T-CLT-03", 5.65, 0.95, 0.40, -0.22),
    ("T-CLT-04", 7.05, 0.82, 0.90, -0.30),
]

for label, theta_deg, vec_r, x_lbl, y_lbl in stac_label_config:
    rad = np.deg2rad(theta_deg)
    x_end = vec_r * np.cos(rad)
    y_end = vec_r * np.sin(rad)

    ax.annotate("", xy=(x_end, y_end), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>,head_length=0.4,head_width=0.18",
                                color=STAC_DARK, lw=1.5, linestyle="--",
                                shrinkA=0, shrinkB=0),
                zorder=8)

    ax.plot([x_end, x_lbl], [y_end, y_lbl],
            color=STAC_DARK, lw=0.5, alpha=0.5, zorder=7)

    ax.text(x_lbl, y_lbl, label,
            fontsize=9.5, color=STAC_DARK,
            ha="center", va="top", fontweight="bold", zorder=12)

# ===========================================================================
# ROTULOS DOS SETORES (dentro das fatias)
# ===========================================================================
# STAC - no angulo 20, raio 0.70
x_stac = 0.70 * np.cos(np.deg2rad(20))
y_stac = 0.70 * np.sin(np.deg2rad(20))
ax.text(x_stac, y_stac + 0.03, "STAC",
        fontsize=10, color=STAC_DARK, ha="center", va="center",
        style="italic", fontweight="bold", zorder=5)
ax.text(x_stac, y_stac - 0.04, r"$\theta < 30°$",
        fontsize=8.5, color=STAC_DARK, ha="center", va="center",
        style="italic", zorder=5)

# HITL - no angulo 75, raio 0.55
x_hitl = 0.55 * np.cos(np.deg2rad(75))
y_hitl = 0.55 * np.sin(np.deg2rad(75))
ax.text(x_hitl, y_hitl, "HITL",
        fontsize=10, color=HITL_COLOR, ha="center", va="center",
        style="italic", fontweight="bold", zorder=5)
ax.text(x_hitl, y_hitl - 0.07, r"$30° \leq \theta < 120°$",
        fontsize=8.5, color=HITL_COLOR, ha="center", va="center",
        style="italic", zorder=5)

# CB - no angulo 155, raio 0.48
x_cb = 0.48 * np.cos(np.deg2rad(155))
y_cb = 0.48 * np.sin(np.deg2rad(155))
ax.text(x_cb, y_cb + 0.03, "CIRCUIT-BREAKER",
        fontsize=10, color=CB_DARK, ha="center", va="center",
        style="italic", fontweight="bold", zorder=5)
ax.text(x_cb, y_cb - 0.04, r"$\theta \geq 120°$",
        fontsize=8.5, color=CB_DARK, ha="center", va="center",
        style="italic", zorder=5)

# ===========================================================================
# TICKS ANGULARES EXTERNOS (sem 90 deg para evitar conflito com anotacao)
# ===========================================================================
for tick_deg in [0, 30, 60, 120, 150, 180]:
    rad = np.deg2rad(tick_deg)
    ax.plot([R*np.cos(rad), (R+0.025)*np.cos(rad)],
            [R*np.sin(rad), (R+0.025)*np.sin(rad)],
            color=TEXT_MID, lw=0.7, zorder=3)
    ax.text((R+0.075)*np.cos(rad), (R+0.075)*np.sin(rad),
            f"{tick_deg}°",
            fontsize=8, color=TEXT_MID, ha="center", va="center")

# ===========================================================================
# ANOTACAO "NATURAL GAP"
# ===========================================================================
ax.text(0, 1.30,
        "natural gap — no scenario in the HITL band",
        fontsize=8.5, color=TEXT_MID, ha="center", va="center",
        style="italic", alpha=0.85)
gap_arc_rad = np.linspace(np.deg2rad(12), np.deg2rad(125), 80)
ax.plot(1.15*np.cos(gap_arc_rad), 1.15*np.sin(gap_arc_rad),
        color=TEXT_MID, lw=0.5, alpha=0.4, linestyle=":")

# ===========================================================================
# PAINEL INFORMATIVO (direita)
# ===========================================================================
ax_info = fig.add_subplot(gs[0, 1])
ax_info.axis("off")
ax_info.set_xlim(0, 1)
ax_info.set_ylim(0, 1)

# Header
ax_info.text(0.02, 0.97, "Scenario regime classification",
             fontsize=10.5, fontweight="bold",
             color=TEXT_DARK, ha="left", va="top")

# Tabela
table_data = [
    ("C2",       "132.4°", "CB",   "Health"),
    ("C3",       "134.7°", "CB",   "Health"),
    ("C7",       "133.7°", "CB",   "Health"),
    ("T-CLT-01", "134.1°", "CB",   "Labour"),
    ("T-CLT-02", "127.8°", "CB",   "Labour"),
    ("T-CLT-03", "  5.7°", "STAC", "Labour"),
    ("T-CLT-04", "  7.1°", "STAC", "Labour"),
]

y_header = 0.88
ax_info.text(0.02, y_header, "Scenario",
             fontsize=8.5, fontweight="bold", color=TEXT_DARK, ha="left")
ax_info.text(0.42, y_header, "θ",
             fontsize=8.5, fontweight="bold", color=TEXT_DARK, ha="left",
             style="italic")
ax_info.text(0.60, y_header, "Regime",
             fontsize=8.5, fontweight="bold", color=TEXT_DARK, ha="left")
ax_info.text(0.85, y_header, "Domain",
             fontsize=8.5, fontweight="bold", color=TEXT_DARK, ha="left")

ax_info.plot([0.02, 0.98], [y_header - 0.02, y_header - 0.02],
             color=GRID_LIGHT, lw=0.5, transform=ax_info.transAxes,
             clip_on=False)

row_h = 0.055
for i, (scn, theta, reg, dom) in enumerate(table_data):
    y = y_header - 0.06 - i*row_h
    regime_color = CB_DARK if reg == "CB" else STAC_DARK
    ax_info.text(0.02, y, scn, fontsize=8.5, color=TEXT_DARK, ha="left")
    ax_info.text(0.42, y, theta, fontsize=8.5, color=TEXT_DARK, ha="left",
                 fontfamily="monospace")
    ax_info.text(0.60, y, reg, fontsize=8.5, color=regime_color, ha="left",
                 fontweight="bold")
    ax_info.text(0.85, y, dom, fontsize=8.5, color=TEXT_MID, ha="left")

# Caixa da equacao
y_eq_top = y_header - 0.06 - len(table_data)*row_h - 0.04
ax_info.plot([0.02, 0.98], [y_eq_top, y_eq_top],
             color=GRID_LIGHT, lw=0.5, transform=ax_info.transAxes,
             clip_on=False)

eq_box = mpatches.FancyBboxPatch((0.02, y_eq_top - 0.17), 0.96, 0.15,
                                  boxstyle="round,pad=0.012,rounding_size=0.012",
                                  facecolor="#fafafa", edgecolor=GRID_LIGHT,
                                  lw=0.5, transform=ax_info.transAxes,
                                  clip_on=False)
ax_info.add_patch(eq_box)

ax_info.text(0.50, y_eq_top - 0.06,
             r"$\theta\ =\ \arccos\!\left(\dfrac{\langle \psi_N \mid \psi_S\rangle}{\|\psi_N\|\,\|\psi_S\|}\right)$",
             fontsize=13, color=TEXT_DARK, ha="center", va="center")
ax_info.text(0.50, y_eq_top - 0.14,
             "Equation 1 — interference angle",
             fontsize=8, color=TEXT_MID, ha="center", va="center",
             style="italic")

# Legenda de vetores
y_leg = y_eq_top - 0.22
ax_info.plot([0.05, 0.15], [y_leg, y_leg],
             color=PSI_S_COLOR, lw=1.8, transform=ax_info.transAxes,
             clip_on=False, solid_capstyle="round")
ax_info.text(0.17, y_leg, r"$|\psi_S\rangle$   normative reference",
             fontsize=8.5, color=TEXT_DARK, ha="left", va="center",
             transform=ax_info.transAxes)

y_leg -= 0.055
ax_info.plot([0.05, 0.15], [y_leg, y_leg],
             color=CB_DARK, lw=1.5, linestyle="--",
             transform=ax_info.transAxes, clip_on=False)
ax_info.text(0.17, y_leg, r"$|\psi_N\rangle$   predictor — CB",
             fontsize=8.5, color=TEXT_DARK, ha="left", va="center",
             transform=ax_info.transAxes)

y_leg -= 0.055
ax_info.plot([0.05, 0.15], [y_leg, y_leg],
             color=STAC_DARK, lw=1.5, linestyle="--",
             transform=ax_info.transAxes, clip_on=False)
ax_info.text(0.17, y_leg, r"$|\psi_N\rangle$   predictor — STAC",
             fontsize=8.5, color=TEXT_DARK, ha="left", va="center",
             transform=ax_info.transAxes)

# ===========================================================================
# TITULO E RODAPE
# ===========================================================================
fig.text(0.03, 0.955,
         "Figure 1.  Interference angle θ across seven scenarios — "
         "overview of governance regime classification",
         fontsize=12.5, fontweight="bold", color=TEXT_DARK, ha="left")

fig.text(0.03, 0.915,
         "Predictor states |ψN⟩ (dashed) plotted by their angular separation "
         "from the normative reference |ψS⟩ (solid, horizontal).  "
         "Five CIRCUIT-BREAKER scenarios cluster at 127.8°–134.7° "
         "(destructive interference); two positive controls fall within the "
         "STAC band at 5.7°–7.1° (constructive interference).",
         fontsize=9.2, color=TEXT_MID, ha="left", style="italic")

fig.text(0.03, 0.03,
         "Source: outputs/e5_results/validation_results.parquet   |   "
         "Angular separation θ = arccos(⟨ψN|ψS⟩ / ‖ψN‖‖ψS‖)   |   "
         "Regime bands follow Q-FENG C1 pipeline specification "
         "(Kaminski 2026a, §7.4).",
         fontsize=8, color=TEXT_MID, ha="left", style="italic")

# ===========================================================================
# SAIDA (em outputs/figures/)
# ===========================================================================
# Caminho relativo: o script assume execucao a partir da raiz do projeto
# qfeng_validacao. Se executado de outro diretorio, ajuste OUTPUT_DIR.
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # ../../qfeng_validacao/
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

outpath_base = OUTPUT_DIR / "F1_interference_overview"

fig.savefig(str(outpath_base) + ".svg", format="svg",
            bbox_inches="tight", pad_inches=0.10, facecolor="white")
fig.savefig(str(outpath_base) + ".png", format="png",
            bbox_inches="tight", pad_inches=0.10, facecolor="white", dpi=200)
fig.savefig(str(outpath_base) + ".pdf", format="pdf",
            bbox_inches="tight", pad_inches=0.10, facecolor="white")

print(f"[OK] {outpath_base}.svg")
print(f"[OK] {outpath_base}.png")
print(f"[OK] {outpath_base}.pdf")
