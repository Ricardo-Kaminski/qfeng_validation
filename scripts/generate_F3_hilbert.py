"""
F3 — Q-FENG Interference Geometry in the Decision Hilbert Space
================================================================
Paper 1 (Applied Intelligence): Empirical Validation of the Q-FENG C1 Pipeline

Source data: outputs/e5_results/validation_results.parquet  (real experimental data,
             NO hard-coded values — all psi_N, psi_S and theta come from the parquet)

Representation: canonical QDT convention — each scenario is rendered in the 2D
                subspace span(psi_N, psi_S). For health scenarios (psi in R^3),
                the Gram–Schmidt projection preserves the interference angle theta
                exactly (verified: delta < 5e-5 degrees vs. parquet theta_deg).

Layout:
  Upper row (3 subplots): Health Governance — C2, C3, C7
  Upper-right slot:       Legend + Equation 1 (theta definition, §3.1 of paper)
  Lower row (4 subplots): Labour Law — T-CLT-01..04

Typography: serif family; palette in grayscale with two semantic accents
            (CB red-brown, STAC deep blue). Consistent with Kaminski (2026a)
            monograph visual acervo.

Usage:
    python scripts/generate_F3_hilbert.py

Output (in outputs/figures/):
    F3_hilbert_decision_space.pdf
    F3_hilbert_decision_space.png  (300 dpi)
    F3_hilbert_decision_space.svg

Author: Ricardo S. Kaminski
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Wedge

# --------------------------------------------------------------------
# 1. PATHS (resolved relative to project root)
# --------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_PARQUET = PROJECT_ROOT / 'outputs' / 'e5_results' / 'validation_results.parquet'
OUTPUT_DIR = PROJECT_ROOT / 'outputs' / 'figures'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------
# 2. TYPOGRAPHY
# --------------------------------------------------------------------
mpl.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Nimbus Roman', 'Liberation Serif'],
    'mathtext.fontset': 'dejavuserif',
    'axes.titlesize': 11,
    'axes.labelsize': 9.5,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8.5,
    'figure.titlesize': 13,
    'axes.linewidth': 0.8,
    'lines.linewidth': 1.2,
})

# --------------------------------------------------------------------
# 3. SEMANTIC PALETTE
# --------------------------------------------------------------------
C_STAC  = '#1f4e79'   # deep blue  — alignment
C_HITL  = '#b8860b'   # dark goldenrod — graduated friction
C_CB    = '#8b2e2e'   # dark red-brown — destructive interference
C_PSI_S = '#111111'   # near-black — normative vector (solid)
C_PSI_N = '#4a4a4a'   # mid-gray   — predictor vector (dashed)
BG_STAC = '#eaf2f8'
BG_HITL = '#faf4e6'
BG_CB   = '#f6e8e8'

# --------------------------------------------------------------------
# 4. DATA LOADING
# --------------------------------------------------------------------
def load_validation_data(path: Path) -> pd.DataFrame:
    """Load validation_results.parquet and parse JSON psi vectors."""
    df = pd.read_parquet(path)
    df['psi_n'] = df['psi_n_json'].apply(json.loads)
    df['psi_s'] = df['psi_s_json'].apply(json.loads)
    return df


# --------------------------------------------------------------------
# 5. GEOMETRY — Gram–Schmidt projection onto span(psi_N, psi_S)
# --------------------------------------------------------------------
def project_to_plane(psi_n: list[float], psi_s: list[float]) -> tuple[np.ndarray, np.ndarray]:
    """
    Orthonormal projection of two ambient vectors into the 2D subspace they span.

    Returns (psi_n_2d, psi_s_2d) such that:
      - angle(psi_n_2d, psi_s_2d) == angle(psi_n, psi_s)  (exact, up to float ε)
      - psi_s_2d lies along the +e1 axis (convention)
    """
    psi_n = np.asarray(psi_n, float)
    psi_s = np.asarray(psi_s, float)
    e1 = psi_s / np.linalg.norm(psi_s)
    psi_n_perp = psi_n - np.dot(psi_n, e1) * e1
    n_perp = np.linalg.norm(psi_n_perp)
    e2 = psi_n_perp / n_perp if n_perp > 1e-12 else np.zeros_like(e1)
    psi_s_2d = np.array([np.dot(psi_s, e1), np.dot(psi_s, e2)])
    psi_n_2d = np.array([np.dot(psi_n, e1), np.dot(psi_n, e2)])
    return psi_n_2d, psi_s_2d


def theta_of(v: np.ndarray) -> float:
    """Angle of a 2D vector from +x axis, in degrees, range [0, 360)."""
    return np.degrees(np.arctan2(v[1], v[0])) % 360.0


# --------------------------------------------------------------------
# 6. SUBPLOT RENDERER
# --------------------------------------------------------------------
def draw_hilbert_subplot(ax: plt.Axes, row: pd.Series, ambient_label: str) -> None:
    """Render one scenario as a unit-circle Hilbert decision diagram."""
    psi_n_2d, psi_s_2d = project_to_plane(row['psi_n'], row['psi_s'])
    theta_deg = row['theta_deg']
    regime = row['interference_regime']
    sid = row['scenario_id']
    gsp = row['governance_suppression_pct']
    is_stac = (regime == 'STAC')

    # Unit circle
    ax.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor='#888888',
                        linewidth=0.7, zorder=1))

    # Governance regime sectors (wedges centered on psi_S direction)
    ang_s = theta_of(psi_s_2d)
    ax.add_patch(Wedge((0, 0), 1.0, ang_s - 30, ang_s + 30,
                       facecolor=BG_STAC, edgecolor='none', alpha=0.85, zorder=0))
    ax.add_patch(Wedge((0, 0), 1.0, ang_s + 120, ang_s + 240,
                       facecolor=BG_CB, edgecolor='none', alpha=0.85, zorder=0))
    ax.add_patch(Wedge((0, 0), 1.0, ang_s + 30, ang_s + 120,
                       facecolor=BG_HITL, edgecolor='none', alpha=0.85, zorder=0))
    ax.add_patch(Wedge((0, 0), 1.0, ang_s + 240, ang_s + 330,
                       facecolor=BG_HITL, edgecolor='none', alpha=0.85, zorder=0))

    # Cartesian reference (subtle)
    ax.axhline(0, color='#bbbbbb', linewidth=0.5, zorder=1)
    ax.axvline(0, color='#bbbbbb', linewidth=0.5, zorder=1)

    # psi_S vector — solid, near-black
    ax.add_patch(FancyArrowPatch(
        (0, 0), tuple(psi_s_2d),
        arrowstyle='-|>', mutation_scale=14,
        color=C_PSI_S, linewidth=1.6, zorder=4))

    # psi_N vector — dashed, mid-gray
    ax.add_patch(FancyArrowPatch(
        (0, 0), tuple(psi_n_2d),
        arrowstyle='-|>', mutation_scale=14,
        color=C_PSI_N, linewidth=1.6,
        linestyle=(0, (5, 2.5)), zorder=4))

    # Arc indicating theta (in the shorter direction)
    ang_n = theta_of(psi_n_2d)
    a1, a2 = ang_s, ang_n
    diff = (a2 - a1) % 360.0
    if diff > 180:
        a1, a2 = ang_n, ang_s
    arc_r = 0.22
    arc_color = C_CB if not is_stac else C_STAC
    ax.add_patch(Wedge((0, 0), arc_r, a1, a2,
                       width=0.015, facecolor=arc_color,
                       edgecolor='none', alpha=0.9, zorder=5))

    # Theta label
    mid_ang_deg = (a1 + ((a2 - a1) % 360) / 2) % 360
    mid_ang = np.radians(mid_ang_deg)
    label_r = 0.50 if is_stac else arc_r + 0.13
    ax.text(label_r * np.cos(mid_ang), label_r * np.sin(mid_ang),
            f"θ = {theta_deg:.1f}°",
            fontsize=9, ha='center', va='center',
            color=arc_color, fontweight='bold', zorder=6,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.82, pad=1.5))

    # Vector labels — strategy differs between CB (vectors far apart) and STAC
    if not is_stac:
        ax.annotate(r'$|\psi_S\rangle$', xy=psi_s_2d,
                    xytext=(psi_s_2d[0] * 1.16, psi_s_2d[1] * 1.16 - 0.05),
                    fontsize=10, color=C_PSI_S, ha='left', va='center', zorder=7)
        ax.annotate(r'$|\psi_N\rangle$', xy=psi_n_2d,
                    xytext=(psi_n_2d[0] * 1.16 - 0.02, psi_n_2d[1] * 1.16 + 0.05),
                    fontsize=10, color=C_PSI_N, ha='right', va='center', zorder=7)
    else:
        # STAC: near-coincident vectors → external callouts
        ax.annotate(r'$|\psi_S\rangle$',
                    xy=(psi_s_2d[0] * 0.72, psi_s_2d[1] * 0.72),
                    xytext=(0.78, 0.62),
                    fontsize=10, color=C_PSI_S, ha='center', va='center',
                    arrowprops=dict(arrowstyle='-', color=C_PSI_S,
                                    linewidth=0.6, connectionstyle='arc3,rad=0.1'),
                    zorder=7)
        ax.annotate(r'$|\psi_N\rangle$',
                    xy=(psi_n_2d[0] * 0.82, psi_n_2d[1] * 0.82),
                    xytext=(0.78, -0.55),
                    fontsize=10, color=C_PSI_N, ha='center', va='center',
                    arrowprops=dict(arrowstyle='-', color=C_PSI_N,
                                    linewidth=0.6, linestyle='dashed',
                                    connectionstyle='arc3,rad=-0.1'),
                    zorder=7)

    # Subplot title
    ftype = row.get('failure_type')
    ftype_str = '' if (pd.isna(ftype) or ftype is None) else f"  ·  {ftype.replace('_', '-')}"
    regime_str = 'CB' if regime == 'CIRCUIT_BREAKER' else 'STAC'
    ax.set_title(f"{sid}  [{regime_str}]{ftype_str}", fontsize=10, pad=6, loc='left')

    # GSP annotation (lower-left)
    gsp_color = C_CB if not is_stac else C_STAC
    gsp_text = f"GSP  {gsp:+.1f}%" if not is_stac else f"GSP  {gsp:+.2f}%"
    ax.text(-1.28, -1.18, gsp_text, fontsize=8.2, color=gsp_color,
            ha='left', va='bottom', fontweight='bold',
            bbox=dict(facecolor='white', edgecolor=gsp_color,
                      linewidth=0.5, pad=2.0, boxstyle='round,pad=0.25'))

    # Ambient dimension badge (lower-right)
    ax.text(1.28, -1.18, ambient_label, fontsize=7.5,
            color='#666666', style='italic', ha='right', va='bottom')

    # Axes cleanup
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.35)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


# --------------------------------------------------------------------
# 7. FIGURE COMPOSITION
# --------------------------------------------------------------------
def compose_figure(df: pd.DataFrame) -> plt.Figure:
    df_health = df[df['corpus'] == 'saude'].reset_index(drop=True)
    df_labour = df[df['corpus'] == 'trabalhista'].reset_index(drop=True)

    fig = plt.figure(figsize=(11.5, 9.1), constrained_layout=False)
    gs = fig.add_gridspec(
        nrows=2, ncols=4,
        height_ratios=[1.0, 1.0],
        hspace=0.30, wspace=0.10,
        left=0.04, right=0.97, top=0.87, bottom=0.08,
    )

    # Upper row — HEALTH (3 subplots + info slot)
    axes_health = [fig.add_subplot(gs[0, c]) for c in range(3)]
    ax_info = fig.add_subplot(gs[0, 3]); ax_info.axis('off')
    for ax, (_, row) in zip(axes_health, df_health.iterrows()):
        draw_hilbert_subplot(ax, row, r'$\mathbb{R}^3 \to \mathrm{span}(\psi_N, \psi_S)$')

    # Lower row — LABOUR (4 subplots)
    for i, (_, row) in enumerate(df_labour.iterrows()):
        ax = fig.add_subplot(gs[1, i])
        draw_hilbert_subplot(ax, row, r'$\mathbb{R}^2$  (native)')

    # Panel headers
    fig.text(0.04, 0.905, r'Health Governance  —  $\psi$ in $\mathbb{R}^3$  (3 actions)',
             fontsize=11.5, fontweight='bold', ha='left', va='center')
    fig.text(0.04, 0.455, r'Labour Law  —  $\psi$ in $\mathbb{R}^2$  (2 actions)',
             fontsize=11.5, fontweight='bold', ha='left', va='center')
    fig.add_artist(Line2D([0.04, 0.97], [0.478, 0.478],
                          color='#cccccc', linewidth=0.7, transform=fig.transFigure))

    # Title + subtitle
    fig.suptitle(
        'Figure 3.  Q-FENG Interference Geometry in the Decision Hilbert Space',
        fontsize=13, fontweight='bold', y=0.975, x=0.04, ha='left')
    fig.text(0.04, 0.938,
             r'Angle $\theta$ between predictor state $|\psi_N\rangle$ (dashed) and '
             r'normative state $|\psi_S\rangle$ (solid), across seven scenarios and '
             r'two normative regimes.',
             fontsize=9.5, ha='left', va='top', style='italic', color='#333333')

    # Info box (upper-right) — legend + Equation 1
    legend_elements = [
        Line2D([0], [0], color=C_PSI_S, lw=1.8,
               label=r'$|\psi_S\rangle$  normative state'),
        Line2D([0], [0], color=C_PSI_N, lw=1.8, linestyle=(0, (5, 2.5)),
               label=r'$|\psi_N\rangle$  predictor state'),
        mpl.patches.Patch(facecolor=BG_STAC, edgecolor='#888888', linewidth=0.3,
                          label=r'STAC sector  ($\theta < 30\degree$)'),
        mpl.patches.Patch(facecolor=BG_HITL, edgecolor='#888888', linewidth=0.3,
                          label=r'HITL sector  ($30\degree \leq \theta < 120\degree$)'),
        mpl.patches.Patch(facecolor=BG_CB, edgecolor='#888888', linewidth=0.3,
                          label=r'Circuit-Breaker  ($\theta \geq 120\degree$)'),
    ]
    leg = ax_info.legend(handles=legend_elements,
                         loc='upper center', bbox_to_anchor=(0.5, 0.98),
                         fontsize=8.5, frameon=True,
                         edgecolor='#aaaaaa', fancybox=False,
                         title='Governance regime', title_fontsize=9.5)
    leg.get_frame().set_linewidth(0.6)

    ax_info.add_patch(FancyBboxPatch(
        (0.08, 0.05), 0.84, 0.32,
        boxstyle='round,pad=0.02', linewidth=0.6,
        edgecolor='#aaaaaa', facecolor='#fafafa',
        transform=ax_info.transAxes, zorder=0))
    ax_info.text(0.5, 0.30,
                 r'$\theta = \arccos\!\left(\dfrac{\langle\psi_N | \psi_S\rangle}'
                 r'{\|\psi_N\|\,\|\psi_S\|}\right)$',
                 fontsize=12, ha='center', va='center', transform=ax_info.transAxes)
    ax_info.text(0.5, 0.13, r'Equation 1 — interference angle',
                 fontsize=8, ha='center', va='center', style='italic',
                 color='#555555', transform=ax_info.transAxes)

    # Footer (data provenance)
    fig.text(0.04, 0.018,
             'Source: outputs/e5_results/validation_results.parquet  '
             r'|  Projection: Gram–Schmidt into $\mathrm{span}(\psi_N, \psi_S)$  '
             r'|  $\theta$ preserved exactly  |  GSP: governance suppression percentage.',
             fontsize=7.5, color='#555555', ha='left', va='bottom')

    return fig


# --------------------------------------------------------------------
# 8. GEOMETRY SELF-CHECK (runs on execute; raises if projection corrupts theta)
# --------------------------------------------------------------------
def validate_projection(df: pd.DataFrame, tol: float = 1e-3) -> None:
    """Abort execution if Gram–Schmidt projection fails to preserve theta_deg."""
    for _, row in df.iterrows():
        psi_n_2d, psi_s_2d = project_to_plane(row['psi_n'], row['psi_s'])
        cos_t = np.dot(psi_n_2d, psi_s_2d) / (
            np.linalg.norm(psi_n_2d) * np.linalg.norm(psi_s_2d))
        theta_recomp = np.degrees(np.arccos(np.clip(cos_t, -1, 1)))
        delta = abs(theta_recomp - row['theta_deg'])
        if delta > tol:
            raise RuntimeError(
                f"Projection corrupted theta for {row['scenario_id']}: "
                f"parquet={row['theta_deg']:.4f}, recomputed={theta_recomp:.4f}, "
                f"delta={delta:.2e}"
            )


# --------------------------------------------------------------------
# 9. MAIN
# --------------------------------------------------------------------
def main() -> None:
    print(f"[F3] Loading {INPUT_PARQUET}")
    df = load_validation_data(INPUT_PARQUET)
    print(f"[F3] Loaded {len(df)} scenarios")

    print("[F3] Validating Gram–Schmidt projection preserves theta...")
    validate_projection(df)
    print("[F3] Projection validated (all scenarios: |Δθ| < 1e-3°)")

    print("[F3] Composing figure...")
    fig = compose_figure(df)

    for ext, dpi in [('pdf', None), ('png', 300), ('svg', None)]:
        out_path = OUTPUT_DIR / f'F3_hilbert_decision_space.{ext}'
        kwargs = {'bbox_inches': 'tight', 'facecolor': 'white'}
        if dpi is not None:
            kwargs['dpi'] = dpi
        fig.savefig(out_path, **kwargs)
        print(f"[F3] wrote  {out_path}")

    plt.close(fig)
    print("[F3] Done.")


if __name__ == '__main__':
    main()
