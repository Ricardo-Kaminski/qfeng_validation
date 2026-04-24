"""
F6 — Psi-Weight Sensitivity Analysis
=====================================
Paper 1 (Applied Intelligence): Empirical Validation of the Q-FENG C1 Pipeline

Source data: outputs/e5_results/psi_sensitivity.parquet
  (7 scenarios, ±20% perturbation, n=500 Monte Carlo samples each;
   aggregated statistics: theta_paper, theta_mean, theta_std, theta_p5, theta_p95)

Representation:
  Two-panel strip plot with regime-specific zoom to resolve the 120° gap between
  STAC and CB clusters. Each scenario is rendered as a horizontal range bar spanning
  [p5, p95], with:
    - Whiskers at p5 and p95
    - Filled circle at theta_mean
    - Solid vertical tick at theta_paper (reference from validation_results)
    - Inline numerical annotation (theta_paper, mu, sigma)

  Upper panel:  STAC regime (xlim 0–13°, two positive controls)
  Lower panel:  Circuit-Breaker regime (xlim 119–142°, five CB scenarios)
  Right panel:  Sensitivity summary — perturbation spec, 100% correctness hero,
                max sigma, reference to paper §6.2

  The CB panel includes:
    - Dashed vertical line at theta=120° (CB threshold)
    - Callout on T-CLT-02 highlighting that even its p5 remains above 120°,
      confirming robustness at the regime boundary

Typography and palette consistent with F2, F3, F4, F5.

Usage:
    python scripts/generate_F6_psi_sensitivity.py

Output (in outputs/figures/):
    F6_psi_sensitivity.pdf
    F6_psi_sensitivity.png   (300 dpi)
    F6_psi_sensitivity.svg

Author: Ricardo S. Kaminski
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, Patch

# --------------------------------------------------------------------
# 1. PATHS
# --------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_PARQUET = PROJECT_ROOT / 'outputs' / 'e5_results' / 'psi_sensitivity.parquet'
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
# 3. SEMANTIC PALETTE
# --------------------------------------------------------------------
C_CB    = '#8b2e2e'
C_STAC  = '#1f4e79'
BG_CB   = '#f6e8e8'
BG_STAC = '#eaf2f8'


# --------------------------------------------------------------------
# 4. DATA LOADING AND VALIDATION
# --------------------------------------------------------------------
def load_and_validate(path: Path) -> pd.DataFrame:
    df = pd.read_parquet(path)
    required = {'scenario_id', 'theta_paper_deg', 'theta_mean_deg',
                'theta_std_deg', 'theta_p5_deg', 'theta_p95_deg',
                'perturbation_pct', 'n_samples', 'pct_correct_regime'}
    missing = required - set(df.columns)
    if missing:
        raise RuntimeError(f"Missing required columns: {missing}")
    if len(df) != 7:
        raise RuntimeError(f"Expected 7 scenarios, got {len(df)}")
    return df


# --------------------------------------------------------------------
# 5. PANEL RENDERING
# --------------------------------------------------------------------
def draw_panel(ax: plt.Axes, df_sub: pd.DataFrame, color: str, bg_color: str,
               xlim: tuple[float, float], title: str,
               annot_offset_factor: float = 0.02) -> None:
    """Draw strip plot for one regime group (STAC or CB)."""
    y_positions = np.arange(len(df_sub))[::-1]
    ax.axvspan(*xlim, color=bg_color, alpha=0.45, zorder=0)

    for y_pos, (_, row) in zip(y_positions, df_sub.iterrows()):
        p5, p95 = row['theta_p5_deg'], row['theta_p95_deg']
        mean = row['theta_mean_deg']
        paper = row['theta_paper_deg']
        std = row['theta_std_deg']

        # p5-p95 range bar
        ax.barh(y_pos, p95 - p5, left=p5, height=0.32,
                color=color, alpha=0.25, edgecolor=color, linewidth=0.8,
                zorder=2, label='_nolegend_')
        # Whiskers
        ax.plot([p5, p5], [y_pos - 0.18, y_pos + 0.18],
                color=color, linewidth=1.4, zorder=3)
        ax.plot([p95, p95], [y_pos - 0.18, y_pos + 0.18],
                color=color, linewidth=1.4, zorder=3)
        ax.plot([p5, p95], [y_pos, y_pos],
                color=color, linewidth=1.0, zorder=3, alpha=0.7)
        # Mean
        ax.scatter(mean, y_pos, s=52, color=color,
                   edgecolors='white', linewidths=1.2, zorder=5,
                   label='_nolegend_')
        # theta_paper reference tick
        ax.plot([paper, paper], [y_pos - 0.12, y_pos + 0.12],
                color='#111111', linewidth=2.0, zorder=6)

        # Inline statistics
        annot_x = p95 + (xlim[1] - xlim[0]) * annot_offset_factor
        ax.text(annot_x, y_pos,
                f'$\\theta_{{paper}}$ = {paper:.1f}°    '
                f'$\\mu$ = {mean:.2f}°    '
                f'$\\sigma$ = {std:.2f}°',
                fontsize=8, color='#444444', ha='left', va='center',
                style='italic', zorder=6)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(df_sub['scenario_id'].tolist(), fontsize=9)
    ax.set_xlim(xlim)
    ax.set_ylim(-0.7, len(df_sub) - 0.3)
    ax.set_xlabel(r'Interference angle  $\theta$  (degrees)', fontsize=9.5)
    ax.set_title(title, fontsize=10, loc='left',
                 pad=8, color='#333333', style='italic')
    ax.grid(axis='x', linestyle=':', linewidth=0.5, color='#cccccc', zorder=0)
    ax.set_axisbelow(True)
    for side in ['top', 'right']:
        ax.spines[side].set_visible(False)
    ax.tick_params(axis='y', length=0, pad=6)
    ax.tick_params(axis='x', length=3)


# --------------------------------------------------------------------
# 6. FIGURE COMPOSITION
# --------------------------------------------------------------------
def compose_figure(df: pd.DataFrame) -> plt.Figure:
    df_stac = (df[df['theta_paper_deg'] < 30]
               .sort_values('theta_paper_deg').reset_index(drop=True))
    df_cb = (df[df['theta_paper_deg'] >= 120]
             .sort_values('theta_paper_deg', ascending=False).reset_index(drop=True))

    pert = int(df['perturbation_pct'].iloc[0])
    n_samples = int(df['n_samples'].iloc[0])
    correctness = float(df['pct_correct_regime'].iloc[0])

    fig = plt.figure(figsize=(12.0, 6.2))
    gs = fig.add_gridspec(nrows=2, ncols=2,
                          width_ratios=[3.2, 1.0],
                          height_ratios=[1.0, 1.3],
                          left=0.10, right=0.97, top=0.82, bottom=0.14,
                          hspace=0.48, wspace=0.10)

    ax_stac = fig.add_subplot(gs[0, 0])
    ax_cb   = fig.add_subplot(gs[1, 0])
    ax_info = fig.add_subplot(gs[:, 1])
    ax_info.axis('off')

    # ---- STAC panel ----
    draw_panel(ax_stac, df_stac,
               color=C_STAC, bg_color=BG_STAC,
               xlim=(0, 13),
               title='STAC regime  —  positive controls (constructive interference)')
    # Note: STAC threshold at 30° is outside this zoomed view — annotate in corner
    ax_stac.text(12.85, len(df_stac) - 0.5,
                 r'STAC threshold $\theta = 30\degree$ is further right',
                 fontsize=7.3, color=C_STAC, ha='right', va='top',
                 style='italic', zorder=5,
                 bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1.5))

    # ---- CB panel ----
    draw_panel(ax_cb, df_cb,
               color=C_CB, bg_color=BG_CB,
               xlim=(119, 142),
               title='Circuit-Breaker regime  —  destructive interference')
    # CB threshold line (now visible inside the zoomed area)
    ax_cb.axvline(120, color=C_CB, linewidth=1.3,
                  linestyle=(0, (4, 2)), zorder=1, alpha=0.9)
    ax_cb.text(120.2, len(df_cb) - 0.35,
               r'CB threshold',
               fontsize=7.8, color=C_CB, ha='left', va='top',
               fontweight='bold', zorder=7,
               bbox=dict(facecolor='white', edgecolor=C_CB,
                         linewidth=0.5, pad=1.8, boxstyle='round,pad=0.15'))

    # T-CLT-02 callout — highlights narrow margin from p5 to threshold
    t_clt_02 = df_cb[df_cb['scenario_id'] == 'T-CLT-02'].iloc[0]
    y_t02 = list(df_cb['scenario_id']).index('T-CLT-02')
    y_t02_pos = len(df_cb) - 1 - y_t02
    gap = t_clt_02['theta_p5_deg'] - 120
    ax_cb.annotate(
        f'p5 = {t_clt_02["theta_p5_deg"]:.2f}°\n(gap to CB: {gap:.2f}°)',
        xy=(t_clt_02['theta_p5_deg'], y_t02_pos),
        xytext=(123.5, y_t02_pos + 0.55),
        fontsize=7.3, color='#666666', ha='left', va='bottom',
        style='italic',
        bbox=dict(facecolor='white', edgecolor='#bbbbbb',
                  linewidth=0.5, pad=2, boxstyle='round,pad=0.2'),
        arrowprops=dict(arrowstyle='-', color='#888888',
                        linewidth=0.6, connectionstyle='arc3,rad=0.2'),
        zorder=7,
    )

    # ---- INFO panel ----
    ax_info.add_patch(FancyBboxPatch(
        (0.00, 0.00), 1.0, 1.0,
        boxstyle='round,pad=0.02', linewidth=0.7,
        edgecolor='#aaaaaa', facecolor='#fafafa',
        transform=ax_info.transAxes, zorder=0))

    ax_info.text(0.5, 0.96, 'Sensitivity summary',
                 fontsize=10.5, ha='center', va='center',
                 fontweight='bold', color='#222222',
                 transform=ax_info.transAxes)
    ax_info.text(0.5, 0.88, f'±{pert}%  perturbation',
                 fontsize=11, ha='center', va='center',
                 fontweight='bold', color='#1a1a1a',
                 transform=ax_info.transAxes)
    ax_info.text(0.5, 0.83, r'on each $\psi_N$ component',
                 fontsize=8.5, ha='center', va='center',
                 color='#555555', style='italic',
                 transform=ax_info.transAxes)
    ax_info.text(0.5, 0.77,
                 f'$n$ = {n_samples} Monte Carlo samples\nper scenario',
                 fontsize=8.5, ha='center', va='center',
                 color='#555555', transform=ax_info.transAxes)

    ax_info.plot([0.08, 0.92], [0.68, 0.68], color='#cccccc',
                 linewidth=0.6, transform=ax_info.transAxes)

    ax_info.text(0.5, 0.61, 'Correct regime rate',
                 fontsize=9, ha='center', va='center',
                 fontweight='bold', color='#2a5a2a',
                 transform=ax_info.transAxes)
    ax_info.text(0.5, 0.52, f'{correctness:.0f}%',
                 fontsize=22, ha='center', va='center',
                 fontweight='bold', color='#2a5a2a',
                 transform=ax_info.transAxes)
    ax_info.text(0.5, 0.43,
                 f'across all 7 scenarios\n({n_samples * 7} total samples)',
                 fontsize=8, ha='center', va='center',
                 color='#555555', transform=ax_info.transAxes)

    ax_info.plot([0.08, 0.92], [0.36, 0.36], color='#cccccc',
                 linewidth=0.6, transform=ax_info.transAxes)

    max_std_row = df.loc[df['theta_std_deg'].idxmax()]
    ax_info.text(0.5, 0.30, r'Maximum  $\sigma_\theta$',
                 fontsize=9, ha='center', va='center',
                 fontweight='bold', color='#444444',
                 transform=ax_info.transAxes)
    ax_info.text(0.5, 0.22,
                 f"{max_std_row['theta_std_deg']:.2f}°  ({max_std_row['scenario_id']})",
                 fontsize=10, ha='center', va='center',
                 color='#1a1a1a', transform=ax_info.transAxes)
    ax_info.text(0.5, 0.155,
                 'closest to CB threshold;\neven p5 stays above 120°',
                 fontsize=7.7, ha='center', va='center',
                 color='#555555', style='italic',
                 transform=ax_info.transAxes)

    ax_info.plot([0.08, 0.92], [0.09, 0.09], color='#cccccc',
                 linewidth=0.6, transform=ax_info.transAxes)
    ax_info.text(0.5, 0.04, 'Paper Table 7  ·  §6.2',
                 fontsize=7.5, ha='center', va='center',
                 color='#777777', style='italic',
                 transform=ax_info.transAxes)

    # ---- Legend ----
    legend_elements = [
        Line2D([0], [0], color='#111111', lw=2.0,
               label=r'$\theta_{paper}$  reference'),
        Line2D([0], [0], color=C_CB, marker='o', markersize=7,
               markerfacecolor=C_CB, markeredgecolor='white',
               markeredgewidth=1.0, linestyle='none',
               label=r'$\theta_{\mathrm{mean}}$  (CB)'),
        Line2D([0], [0], color=C_STAC, marker='o', markersize=7,
               markerfacecolor=C_STAC, markeredgecolor='white',
               markeredgewidth=1.0, linestyle='none',
               label=r'$\theta_{\mathrm{mean}}$  (STAC)'),
        Patch(facecolor=C_CB, alpha=0.25, edgecolor=C_CB,
              label='[p5, p95] range (CB)'),
        Patch(facecolor=C_STAC, alpha=0.25, edgecolor=C_STAC,
              label='[p5, p95] range (STAC)'),
    ]
    fig.legend(handles=legend_elements,
               loc='lower center', bbox_to_anchor=(0.5, 0.005),
               ncol=5, frameon=True, edgecolor='#bbbbbb',
               fancybox=False, fontsize=8.3)

    # ---- Title ----
    fig.suptitle(
        r'Figure 6.  $\psi$-Weight Sensitivity Analysis  —  '
        r'Monte Carlo Robustness Under $\pm 20\%$ Perturbation',
        fontsize=12.5, fontweight='bold', y=0.965, x=0.05, ha='left'
    )
    fig.text(0.05, 0.92,
             r'For each scenario, 500 perturbation samples were drawn by adding '
             r'$\mathcal{U}(-\delta, +\delta)$ noise to each component of $\psi_N$ '
             r'(with $\delta = 20\%$), re-normalising, and recomputing $\theta$.',
             fontsize=9.5, ha='left', va='top', style='italic', color='#333333')

    return fig


# --------------------------------------------------------------------
# 7. MAIN
# --------------------------------------------------------------------
def main() -> None:
    print(f"[F6] Loading {INPUT_PARQUET}")
    df = load_and_validate(INPUT_PARQUET)
    print(f"[F6] Loaded {len(df)} scenarios with psi-sensitivity statistics")

    pert = int(df['perturbation_pct'].iloc[0])
    n_samples = int(df['n_samples'].iloc[0])
    correctness = float(df['pct_correct_regime'].iloc[0])
    print(f"[F6] Perturbation: ±{pert}%,  n={n_samples} samples/scenario")
    print(f"[F6] Correct regime rate: {correctness:.1f}% "
          f"(across {n_samples * len(df)} total samples)")

    max_row = df.loc[df['theta_std_deg'].idxmax()]
    print(f"[F6] Max sigma: {max_row['scenario_id']} "
          f"(sigma = {max_row['theta_std_deg']:.2f}°, "
          f"p5 = {max_row['theta_p5_deg']:.2f}°)")

    print("[F6] Composing figure...")
    fig = compose_figure(df)

    for ext, dpi in [('pdf', None), ('png', 300), ('svg', None)]:
        out_path = OUTPUT_DIR / f'F6_psi_sensitivity.{ext}'
        kwargs = {'bbox_inches': 'tight', 'facecolor': 'white'}
        if dpi is not None:
            kwargs['dpi'] = dpi
        fig.savefig(out_path, **kwargs)
        print(f"[F6] wrote  {out_path}")

    plt.close(fig)
    print("[F6] Done.")


if __name__ == '__main__':
    main()
