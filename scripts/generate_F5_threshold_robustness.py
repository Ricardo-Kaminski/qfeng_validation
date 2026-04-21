"""
F5 — Threshold Robustness: STAC/CB Classification Stability Across Parameter Grid
===================================================================================
Paper 1 (Applied Intelligence): Empirical Validation of the Q-FENG C1 Pipeline

Source data: outputs/e5_results/threshold_robustness.parquet  (245 evaluations,
             no hard-coded values — all regime classifications come from the parquet)

Representation:
  A 7-scenario × 7-threshold classification matrix showing, for each (scenario,
  theta_block) pair at fixed theta_stac = 30° (the paper value), the regime that
  the Q-FENG pipeline classifies. Cells are colour-coded by regime (CB red-brown,
  HITL goldenrod, STAC deep blue), with a heavy black border on any cell where
  matches_paper = False (i.e., where the regime classification differs from the
  paper-reported value).

  A vertical dashed frame highlights the paper-value column (theta_block = 120°).

  Right-panel "Robustness summary" reports the three key statistics that support
  the paper's §6.1 robustness claim:
    - Global correct classification rate (240/245 = 97.96%)
    - 100% correctness for theta_block ≤ 125° (210/210)
    - The empirical theta gap [max STAC theta, min CB theta] between the bimodal
      clusters — approximately 120° — which justifies the 120° threshold choice.

Typography and palette consistent with F2, F3, F4.

Usage:
    python scripts/generate_F5_threshold_robustness.py

Output (in outputs/figures/):
    F5_threshold_robustness.pdf
    F5_threshold_robustness.png   (300 dpi)
    F5_threshold_robustness.svg

Author: Ricardo S. Kaminski
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyBboxPatch, Patch, Rectangle

# --------------------------------------------------------------------
# 1. PATHS
# --------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_PARQUET = PROJECT_ROOT / 'outputs' / 'e5_results' / 'threshold_robustness.parquet'
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
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'axes.linewidth': 0.8,
})

# --------------------------------------------------------------------
# 3. SEMANTIC PALETTE (aligned with F2/F3/F4)
# --------------------------------------------------------------------
C_CB    = '#8b2e2e'
C_STAC  = '#1f4e79'
C_HITL  = '#b8860b'
BG_CB   = '#f6e8e8'
BG_STAC = '#eaf2f8'
BG_HITL = '#faf4e6'
C_FAIL  = '#000000'

# Canonical scenario ordering for the matrix (CB block first by theta desc,
# then STAC block by theta desc). This keeps "regime homogeneity" visually clean.
SCENARIO_ORDER = ['C3', 'C7', 'C2', 'T-CLT-01', 'T-CLT-02', 'T-CLT-04', 'T-CLT-03']

# Fixed theta_stac value for the matrix display (matches paper)
THETA_STAC_FIXED = 30


# --------------------------------------------------------------------
# 4. DATA LOADING AND VALIDATION
# --------------------------------------------------------------------
def load_and_validate(path: Path) -> pd.DataFrame:
    df = pd.read_parquet(path)
    required = {'scenario_id', 'theta_deg', 'theta_stac', 'theta_block',
                'regime', 'matches_paper'}
    missing = required - set(df.columns)
    if missing:
        raise RuntimeError(f"Missing required columns: {missing}")
    expected = 5 * 7 * 7  # 5 theta_stac × 7 theta_block × 7 scenarios
    if len(df) != expected:
        raise RuntimeError(
            f"Expected {expected} rows (5 × 7 × 7), got {len(df)}"
        )
    for sid in SCENARIO_ORDER:
        if sid not in df['scenario_id'].unique():
            raise RuntimeError(f"Scenario {sid} missing from parquet")
    return df


def build_matrix(df: pd.DataFrame, theta_block_values: list[int]) -> tuple:
    """Build the 7×7 regime/match matrices for the fixed theta_stac value."""
    n_rows, n_cols = len(SCENARIO_ORDER), len(theta_block_values)
    matrix_regime = np.empty((n_rows, n_cols), dtype=object)
    matrix_match  = np.empty((n_rows, n_cols), dtype=bool)
    matrix_theta  = np.empty(n_rows, dtype=float)
    for i, sid in enumerate(SCENARIO_ORDER):
        sub = (df[(df['scenario_id'] == sid) & (df['theta_stac'] == THETA_STAC_FIXED)]
               .sort_values('theta_block'))
        matrix_theta[i] = sub['theta_deg'].iloc[0]
        for j, tb in enumerate(theta_block_values):
            row = sub[sub['theta_block'] == tb].iloc[0]
            matrix_regime[i, j] = row['regime']
            matrix_match[i, j]  = row['matches_paper']
    return matrix_regime, matrix_match, matrix_theta


# --------------------------------------------------------------------
# 5. FIGURE COMPOSITION
# --------------------------------------------------------------------
def compose_figure(df: pd.DataFrame) -> plt.Figure:
    theta_block_values = sorted(df['theta_block'].unique())
    matrix_regime, matrix_match, matrix_theta = build_matrix(df, theta_block_values)

    total = len(df)
    correct = int(df['matches_paper'].sum())
    correct_pct = correct / total * 100
    correct_safe = int(df[df['theta_block'] <= 125]['matches_paper'].sum())
    total_safe = int((df['theta_block'] <= 125).sum())
    correct_safe_pct = correct_safe / total_safe * 100

    theta_min_cb   = float(df[df['regime'] == 'CIRCUIT_BREAKER']['theta_deg'].min())
    theta_max_stac = float(df[df['regime'] == 'STAC']['theta_deg'].max())

    # Layout
    fig = plt.figure(figsize=(12.0, 6.0))
    gs = fig.add_gridspec(nrows=1, ncols=2, width_ratios=[3.2, 1.0],
                          left=0.10, right=0.97, top=0.78, bottom=0.22,
                          wspace=0.10)

    # ---- LEFT: matrix ----
    ax = fig.add_subplot(gs[0, 0])

    color_of_regime = {'CIRCUIT_BREAKER': BG_CB, 'HITL': BG_HITL, 'STAC': BG_STAC}
    text_of_regime  = {'CIRCUIT_BREAKER': 'CB',  'HITL': 'HITL',  'STAC': 'STAC'}
    fg_of_regime    = {'CIRCUIT_BREAKER': C_CB,  'HITL': '#8a6f1a', 'STAC': C_STAC}

    n_rows, n_cols = len(SCENARIO_ORDER), len(theta_block_values)
    for i in range(n_rows):
        for j in range(n_cols):
            regime = matrix_regime[i, j]
            match  = matrix_match[i, j]
            ax.add_patch(Rectangle((j, n_rows - 1 - i), 1, 1,
                                   facecolor=color_of_regime[regime],
                                   edgecolor='white', linewidth=1.0, zorder=2))
            ax.text(j + 0.5, n_rows - 1 - i + 0.5,
                    text_of_regime[regime],
                    fontsize=9.5, ha='center', va='center',
                    color=fg_of_regime[regime], fontweight='bold', zorder=3)
            if not match:
                # Heavy outline to mark regime flips
                ax.add_patch(Rectangle((j + 0.03, n_rows - 1 - i + 0.03), 0.94, 0.94,
                                       facecolor='none', edgecolor=C_FAIL,
                                       linewidth=2.3, zorder=4))

    ax.set_xticks(np.arange(n_cols) + 0.5)
    ax.set_xticklabels([f'{v}°' for v in theta_block_values])
    y_labels = [f"{SCENARIO_ORDER[i]}\n$\\theta$ = {matrix_theta[i]:.1f}°"
                for i in range(n_rows)]
    ax.set_yticks(np.arange(n_rows) + 0.5)
    ax.set_yticklabels(y_labels[::-1], fontsize=8.5)

    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$\theta_{\mathrm{block}}$  (CB threshold, degrees)', fontsize=10)
    ax.set_ylabel('Scenario', fontsize=10)

    # Paper-value dashed frame
    paper_idx = theta_block_values.index(120)
    ax.add_patch(Rectangle((paper_idx, 0), 1, n_rows,
                           facecolor='none', edgecolor='#1a1a1a',
                           linewidth=1.8, linestyle=(0, (3, 2)), zorder=6))
    ax.text(paper_idx + 0.5, n_rows + 0.20,
            'paper value', fontsize=8.2, ha='center', va='bottom',
            fontweight='bold', color='#1a1a1a', zorder=7)

    # Subtitle below x-axis label
    ax.text(0.5, -0.14,
            rf'$\theta_{{\mathrm{{stac}}}} = {THETA_STAC_FIXED}\degree$ fixed  ·  '
            'Cell colour = regime; heavy border = regime flip vs. paper',
            fontsize=8.8, ha='center', va='top', style='italic',
            color='#555555', transform=ax.transAxes)

    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(axis='both', length=0, pad=4)

    # ---- RIGHT: summary panel ----
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis('off')

    ax2.add_patch(FancyBboxPatch(
        (0.00, 0.00), 1.0, 1.0,
        boxstyle='round,pad=0.02', linewidth=0.7,
        edgecolor='#aaaaaa', facecolor='#fafafa',
        transform=ax2.transAxes, zorder=0))

    ax2.text(0.5, 0.955, 'Robustness summary',
             fontsize=10.5, ha='center', va='center',
             fontweight='bold', color='#222222',
             transform=ax2.transAxes)

    ax2.text(0.5, 0.87, f'{correct_pct:.2f}%',
             fontsize=20, ha='center', va='center',
             fontweight='bold', color='#1a1a1a',
             transform=ax2.transAxes)
    ax2.text(0.5, 0.79,
             f'{correct}/{total} evaluations\ncorrectly classified\n'
             '(5 × 7 thresholds × 7 scenarios)',
             fontsize=8.3, ha='center', va='center',
             color='#555555', transform=ax2.transAxes)

    ax2.plot([0.08, 0.92], [0.70, 0.70], color='#cccccc',
             linewidth=0.6, transform=ax2.transAxes)

    ax2.text(0.5, 0.63,
             r'At  $\theta_{\mathrm{block}} \leq 125\degree$',
             fontsize=9, ha='center', va='center',
             style='italic', color='#2a5a2a',
             transform=ax2.transAxes)
    ax2.text(0.5, 0.555, f'{correct_safe_pct:.0f}%',
             fontsize=16, ha='center', va='center',
             fontweight='bold', color='#2a5a2a',
             transform=ax2.transAxes)
    ax2.text(0.5, 0.48, f'{correct_safe}/{total_safe}',
             fontsize=8, ha='center', va='center',
             color='#555555', transform=ax2.transAxes)

    ax2.plot([0.08, 0.92], [0.42, 0.42], color='#cccccc',
             linewidth=0.6, transform=ax2.transAxes)

    ax2.text(0.5, 0.36, r'Empirical $\theta$ gap',
             fontsize=9, ha='center', va='center',
             fontweight='bold', color='#444444',
             transform=ax2.transAxes)
    ax2.text(0.5, 0.295,
             f'[{theta_max_stac:.1f}°,  {theta_min_cb:.1f}°]',
             fontsize=10, ha='center', va='center',
             color='#1a1a1a', fontweight='bold',
             transform=ax2.transAxes)
    ax2.text(0.5, 0.22,
             'gap ≈ 120° between\nSTAC and CB clusters',
             fontsize=7.8, ha='center', va='center',
             color='#555555', transform=ax2.transAxes)

    ax2.plot([0.08, 0.92], [0.15, 0.15], color='#cccccc',
             linewidth=0.6, transform=ax2.transAxes)

    n_failures = total - correct
    ax2.text(0.5, 0.095,
             f'{n_failures} failures  (T-CLT-02)\n'
             r'all at  $\theta_{\mathrm{block}} = 130\degree$',
             fontsize=7.8, ha='center', va='center',
             style='italic', color=C_FAIL,
             transform=ax2.transAxes)
    ax2.text(0.5, 0.025,
             '(boundary case, §6.1)',
             fontsize=7.2, ha='center', va='center',
             color='#777777', transform=ax2.transAxes)

    # ---- Legend ----
    legend_elements = [
        Patch(facecolor=BG_CB,   edgecolor='white', linewidth=0.5,
              label='CB  —  Circuit-Breaker'),
        Patch(facecolor=BG_HITL, edgecolor='white', linewidth=0.5,
              label='HITL  —  Human-in-the-Loop'),
        Patch(facecolor=BG_STAC, edgecolor='white', linewidth=0.5,
              label='STAC  —  Stable alignment'),
        Patch(facecolor='white', edgecolor=C_FAIL, linewidth=1.8,
              label='Regime flip vs. paper'),
    ]
    fig.legend(handles=legend_elements,
               loc='lower center', bbox_to_anchor=(0.5, 0.015),
               ncol=4, frameon=True, edgecolor='#bbbbbb',
               fancybox=False, fontsize=8.5)

    # ---- Title ----
    fig.suptitle(
        r'Figure 5.  Threshold Robustness  —  STAC/CB Classification Stability Across Parameter Grid',
        fontsize=12.5, fontweight='bold', y=0.955, x=0.05, ha='left'
    )
    fig.text(0.05, 0.915,
             r'Grid search over  $\theta_{\mathrm{stac}} \in \{20, 25, 30, 35, 40\}\degree$  '
             r'and  $\theta_{\mathrm{block}} \in \{100, 105, \ldots, 130\}\degree$  '
             r'(5 × 7 = 35 combinations × 7 scenarios = 245 evaluations).',
             fontsize=9.5, ha='left', va='top', style='italic', color='#333333')

    return fig


# --------------------------------------------------------------------
# 6. MAIN
# --------------------------------------------------------------------
def main() -> None:
    print(f"[F5] Loading {INPUT_PARQUET}")
    df = load_and_validate(INPUT_PARQUET)
    print(f"[F5] Loaded {len(df)} threshold evaluations")

    total = len(df)
    correct = int(df['matches_paper'].sum())
    print(f"[F5] Global correctness: {correct}/{total} = {correct / total * 100:.2f}%")
    safe_mask = df['theta_block'] <= 125
    print(f"[F5] At theta_block <= 125°: "
          f"{int(df[safe_mask]['matches_paper'].sum())}/{int(safe_mask.sum())}")

    failures = df[~df['matches_paper']]
    if len(failures) > 0:
        fail_scen = failures['scenario_id'].unique().tolist()
        fail_tb = sorted(failures['theta_block'].unique().tolist())
        print(f"[F5] Failures concentrated in scenarios {fail_scen} "
              f"at theta_block in {fail_tb}")

    print("[F5] Composing figure...")
    fig = compose_figure(df)

    for ext, dpi in [('pdf', None), ('png', 300), ('svg', None)]:
        out_path = OUTPUT_DIR / f'F5_threshold_robustness.{ext}'
        kwargs = {'bbox_inches': 'tight', 'facecolor': 'white'}
        if dpi is not None:
            kwargs['dpi'] = dpi
        fig.savefig(out_path, **kwargs)
        print(f"[F5] wrote  {out_path}")

    plt.close(fig)
    print("[F5] Done.")


if __name__ == '__main__':
    main()
