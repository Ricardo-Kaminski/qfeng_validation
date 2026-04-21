"""
F4 — Governance Suppression Percentage by Scenario
===================================================
Paper 1 (Applied Intelligence): Empirical Validation of the Q-FENG C1 Pipeline

Source data: outputs/e5_results/validation_results.parquet
  (same parquet used by F3; no hard-coded values)

Representation:
  Diverging horizontal bar chart (lollipop-style) with GSP = 0 as central axis.
  - Right side (GSP > 0, red-brown):   Destructive interference — Circuit-Breaker
  - Left side  (GSP < 0, deep blue):   Constructive interference — STAC (positive control)

  Rows grouped by domain (Health Governance, Labour Law) with subtle backgrounds.
  Within each group, rows ordered by GSP descending.

  Each CB row carries an inline annotation with P_q and P_cl, explicitly showing
  the Born-rule vs. classical Bayesian probabilities whose ratio defines GSP.

  Formula box (Equation 10 of paper) positioned at bottom-right for formal
  continuity with F3 (Equation 1 box).

Typography and palette consistent with F2 (Manaus time series) and F3 (Hilbert
decision space).

Usage:
    python scripts/generate_F4_gsp.py

Output (in outputs/figures/):
    F4_governance_suppression.pdf
    F4_governance_suppression.png   (300 dpi)
    F4_governance_suppression.svg

Author: Ricardo S. Kaminski
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyBboxPatch, Patch

# --------------------------------------------------------------------
# 1. PATHS
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
    'axes.labelsize': 10,
    'xtick.labelsize': 8.5,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'axes.linewidth': 0.8,
    'lines.linewidth': 1.3,
})

# --------------------------------------------------------------------
# 3. SEMANTIC PALETTE (aligned with F2 and F3)
# --------------------------------------------------------------------
C_CB        = '#8b2e2e'    # destructive interference — Circuit-Breaker
C_STAC      = '#1f4e79'    # constructive interference — STAC
C_HEALTH_BG = '#f8f5f0'    # subtle warm background — health group
C_LABOUR_BG = '#f4f6f0'    # subtle cool background — labour group


# --------------------------------------------------------------------
# 4. DATA LOADING
# --------------------------------------------------------------------
def load_data(path: Path) -> pd.DataFrame:
    """Load validation parquet and order rows by domain, then by GSP desc."""
    df = pd.read_parquet(path)
    df_health = (df[df['corpus'] == 'saude']
                 .sort_values('governance_suppression_pct', ascending=False)
                 .reset_index(drop=True))
    df_labour = (df[df['corpus'] == 'trabalhista']
                 .sort_values('governance_suppression_pct', ascending=False)
                 .reset_index(drop=True))
    return pd.concat([df_health, df_labour]).reset_index(drop=True), len(df_health)


# --------------------------------------------------------------------
# 5. FIGURE COMPOSITION
# --------------------------------------------------------------------
def compose_figure(df_ordered: pd.DataFrame, n_health: int) -> plt.Figure:
    n = len(df_ordered)
    y_positions = np.arange(n)[::-1]

    fig, ax = plt.subplots(figsize=(11.5, 5.4))
    fig.subplots_adjust(left=0.18, right=0.97, top=0.83, bottom=0.18)

    # ---- Group backgrounds ----
    y_health_top    = y_positions[0] + 0.5
    y_health_bottom = y_positions[n_health - 1] - 0.5
    y_labour_top    = y_positions[n_health] + 0.5
    y_labour_bottom = y_positions[-1] - 0.5
    ax.axhspan(y_health_bottom, y_health_top, color=C_HEALTH_BG,
               alpha=0.55, zorder=0)
    ax.axhspan(y_labour_bottom, y_labour_top, color=C_LABOUR_BG,
               alpha=0.55, zorder=0)

    # ---- Central zero line ----
    ax.axvline(0, color='#444444', linewidth=0.9, zorder=2)

    # ---- Bars with lollipop markers and labels ----
    for y_pos, (_, row) in zip(y_positions, df_ordered.iterrows()):
        gsp = row['governance_suppression_pct']
        is_cb = (row['interference_regime'] == 'CIRCUIT_BREAKER')
        color = C_CB if is_cb else C_STAC

        ax.barh(y_pos, gsp, height=0.52,
                color=color, edgecolor='white', linewidth=0.8,
                alpha=0.88, zorder=3)
        ax.scatter(gsp, y_pos, s=48, color=color,
                   edgecolors='white', linewidths=1.2, zorder=5)

        # Numerical label at tip
        ha = 'left' if gsp >= 0 else 'right'
        offset = 0.4 if gsp >= 0 else -0.4
        ax.text(gsp + offset, y_pos, f"{gsp:+.2f}%",
                fontsize=9, color=color, ha=ha, va='center',
                fontweight='bold', zorder=6)

        # P_q / P_cl annotation (only for CB, to the right of numerical label)
        if is_cb:
            p_q = row['born_p_violation']
            p_cl = row['classical_p_violation']
            label_width = 4.5
            ax.text(gsp + offset + label_width, y_pos,
                    f"$P_q$ = {p_q:.3f}   $P_{{cl}}$ = {p_cl:.3f}",
                    fontsize=7.8, color='#666666', ha='left', va='center',
                    style='italic', zorder=6)

    # ---- Y tick labels: scenario ID + failure_type ----
    yticklabels = []
    for _, row in df_ordered.iterrows():
        sid = row['scenario_id']
        ftype = row['failure_type']
        if pd.isna(ftype) or ftype is None:
            ftype_str = "(STAC — positive control)"
        else:
            ftype_str = f"({ftype.replace('_', '-')})"
        yticklabels.append(f"{sid}\n{ftype_str}")
    ax.set_yticks(y_positions)
    ax.set_yticklabels(yticklabels, fontsize=8.8)

    # ---- X axis ----
    ax.set_xlim(-4, 42)
    ax.set_xlabel(r'Governance Suppression Percentage  GSP (%)', fontsize=10)

    # In-plot interpretive labels (constructive/destructive)
    ax.text(0.02, 0.02, 'Constructive\ninterference',
            fontsize=8, color=C_STAC, ha='left', va='bottom',
            style='italic', transform=ax.transAxes,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.75, pad=2))
    ax.text(0.98, 0.02, 'Destructive\ninterference',
            fontsize=8, color=C_CB, ha='right', va='bottom',
            style='italic', transform=ax.transAxes,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.75, pad=2))

    # ---- Group labels (rotated, left margin) ----
    ax.text(-0.22, (y_health_top + y_health_bottom) / 2,
            'Health\nGovernance', fontsize=10, fontweight='bold',
            ha='center', va='center', rotation=90,
            transform=ax.get_yaxis_transform(), color='#5a3e2a')
    ax.text(-0.22, (y_labour_top + y_labour_bottom) / 2,
            'Labour\nLaw', fontsize=10, fontweight='bold',
            ha='center', va='center', rotation=90,
            transform=ax.get_yaxis_transform(), color='#3a5a2a')

    # ---- Spines and grid ----
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='y', length=0, pad=6)
    ax.tick_params(axis='x', length=3)
    ax.grid(axis='x', linestyle=':', linewidth=0.5, color='#cccccc', zorder=1)
    ax.set_axisbelow(True)

    # ---- Title / subtitle ----
    fig.suptitle(
        r'Figure 4.  Governance Suppression Percentage  —  Born-rule Quantum vs. Classical Bayesian',
        fontsize=12.5, fontweight='bold', y=0.965, x=0.05, ha='left'
    )
    fig.text(0.05, 0.925,
             r'GSP quantifies the suppression of the norm-violating action probability '
             r'by the quantum interference formalism, relative to a classical Bayesian mixture model.',
             fontsize=9.5, ha='left', va='top', style='italic', color='#333333')

    # ---- Formula box (bottom-right, Equation 10) ----
    # Box expanded (0.68→0.66 left, 0.28→0.32 width) and formula fontsize reduced
    # (11.5→10.5) so that P_cl subscripts no longer overflow the rounded border.
    formula_ax = fig.add_axes([0.66, 0.005, 0.32, 0.115])
    formula_ax.axis('off')
    formula_ax.add_patch(FancyBboxPatch(
        (0.02, 0.05), 0.96, 0.90,
        boxstyle='round,pad=0.02', linewidth=0.6,
        edgecolor='#aaaaaa', facecolor='#fafafa',
        transform=formula_ax.transAxes, zorder=0))
    formula_ax.text(0.5, 0.72,
                    r'$\mathrm{GSP} = \dfrac{P_{\mathrm{cl}} - P_{q}}{P_{\mathrm{cl}}} \times 100\%$',
                    fontsize=10.5, ha='center', va='center',
                    transform=formula_ax.transAxes)
    formula_ax.text(0.5, 0.28,
                    r'Equation 10  ·  $P_q$: Born-rule   ·   $P_{\mathrm{cl}}$: classical',
                    fontsize=7.8, ha='center', va='center',
                    style='italic', color='#555555',
                    transform=formula_ax.transAxes)

    # ---- Legend (bottom-left) ----
    legend_elements = [
        Patch(facecolor=C_CB, edgecolor='white', linewidth=0.8,
              label=r'Circuit-Breaker  (destructive interference, $\theta \geq 120\degree$)'),
        Patch(facecolor=C_STAC, edgecolor='white', linewidth=0.8,
              label=r'STAC  (constructive interference, $\theta < 30\degree$)'),
    ]
    fig.legend(handles=legend_elements,
               loc='lower left', bbox_to_anchor=(0.05, 0.01),
               ncol=1, frameon=True, edgecolor='#bbbbbb',
               fancybox=False, fontsize=8.8)

    return fig


# --------------------------------------------------------------------
# 6. SANITY CHECK — recompute GSP from P_q, P_cl and compare to parquet
# --------------------------------------------------------------------
def validate_gsp(df: pd.DataFrame, tol: float = 0.01) -> None:
    """Raise if GSP column does not match (P_cl − P_q)/P_cl × 100 within tolerance."""
    recomp = (df['classical_p_violation'] - df['born_p_violation']) \
             / df['classical_p_violation'] * 100.0
    delta = (recomp - df['governance_suppression_pct']).abs()
    if (delta > tol).any():
        bad = df.loc[delta > tol, 'scenario_id'].tolist()
        raise RuntimeError(
            f"GSP mismatch (> {tol}% tolerance) in scenarios: {bad}"
        )


# --------------------------------------------------------------------
# 7. MAIN
# --------------------------------------------------------------------
def main() -> None:
    print(f"[F4] Loading {INPUT_PARQUET}")
    df_ordered, n_health = load_data(INPUT_PARQUET)
    print(f"[F4] Loaded {len(df_ordered)} scenarios "
          f"({n_health} health, {len(df_ordered) - n_health} labour)")

    print("[F4] Validating GSP = (P_cl − P_q) / P_cl × 100 ...")
    validate_gsp(df_ordered)
    print("[F4] GSP validated for all scenarios (|Δ| < 0.01%)")

    # Report key anchors
    max_row = df_ordered.loc[df_ordered['governance_suppression_pct'].idxmax()]
    min_row = df_ordered.loc[df_ordered['governance_suppression_pct'].idxmin()]
    print(f"[F4] Max destructive: {max_row['scenario_id']} "
          f"(GSP = {max_row['governance_suppression_pct']:.2f}%)")
    print(f"[F4] Max constructive: {min_row['scenario_id']} "
          f"(GSP = {min_row['governance_suppression_pct']:.2f}%)")

    print("[F4] Composing figure...")
    fig = compose_figure(df_ordered, n_health)

    for ext, dpi in [('pdf', None), ('png', 300), ('svg', None)]:
        out_path = OUTPUT_DIR / f'F4_governance_suppression.{ext}'
        kwargs = {'bbox_inches': 'tight', 'facecolor': 'white'}
        if dpi is not None:
            kwargs['dpi'] = dpi
        fig.savefig(out_path, **kwargs)
        print(f"[F4] wrote  {out_path}")

    plt.close(fig)
    print("[F4] Done.")


if __name__ == '__main__':
    main()
