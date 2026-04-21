"""
F2 — Manaus Markovian theta_efetivo Dual-Axis Time Series
==========================================================
Paper 1 (Applied Intelligence): Empirical Validation of the Q-FENG C1 Pipeline

Source data:
  - outputs/e5_results/theta_efetivo_manaus.parquet  (12-month series: theta_t,
    theta_efetivo, alpha_t, hospital_occupancy_pct, data_source)
  - outputs/e5_results/manaus_bootstrap_ci.parquet   (95% bootstrap CIs per month)

NO hard-coded values. All numerical content is read from the parquets.

Representation:
  - X axis: 12 months (Jul 2020 – Jun 2021)
  - Left Y axis: interference angle theta (theta_t dashed, theta_efetivo solid)
                 with 95% bootstrap CI band as gray shading
  - Right Y axis: hospital occupancy (%) as bars behind the theta lines
  - Regime bands: CB zone (theta >= 120, red-brown), HITL (yellow), STAC (blue)
  - Marker differentiation: filled squares for SIH/DATASUS months,
                            open circles for literature-estimated months
  - Annotations: CB onset (Oct 2020, alpha=0.909, THREE months before collapse),
                 peak (Feb 2021, theta_eff=130.9), Portaria 69/2021 (Jan 2021)

Typography: serif family, consistent with Kaminski (2026a) monograph acervo
           and Figure 3 (Hilbert decision space).

Usage:
    python scripts/generate_F2_manaus.py

Output (in outputs/figures/):
    F2_manaus_theta_efetivo.pdf
    F2_manaus_theta_efetivo.png  (300 dpi)
    F2_manaus_theta_efetivo.svg

Author: Ricardo S. Kaminski
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# --------------------------------------------------------------------
# 1. PATHS (resolved relative to project root)
# --------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_TS  = PROJECT_ROOT / 'outputs' / 'e5_results' / 'theta_efetivo_manaus.parquet'
INPUT_CI  = PROJECT_ROOT / 'outputs' / 'e5_results' / 'manaus_bootstrap_ci.parquet'
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
    'ytick.labelsize': 8.5,
    'legend.fontsize': 8.5,
    'axes.linewidth': 0.8,
    'lines.linewidth': 1.3,
})

# --------------------------------------------------------------------
# 3. SEMANTIC PALETTE (aligned with F3)
# --------------------------------------------------------------------
C_THETA_T    = '#4a4a4a'   # mid-gray — instantaneous theta
C_THETA_EFF  = '#1a1a1a'   # near-black — Markovian theta (main signal)
C_CB_ZONE    = '#f6e8e8'   # light red-brown — CB zone
C_HITL_ZONE  = '#faf4e6'   # light goldenrod — HITL zone
C_STAC_ZONE  = '#eaf2f8'   # light blue — STAC zone
C_OCCUP_LIT  = '#c8dcc8'   # pale green — literature-estimated occupancy
C_OCCUP_SIH  = '#7fa07f'   # saturated green — SIH/DATASUS occupancy
C_THRESHOLD  = '#8b2e2e'   # dark red-brown — 120° threshold line
C_PORTARIA   = '#5a3e8b'   # purple — Portaria 69/2021 marker
C_CALLOUT    = '#8b2e2e'   # CB red-brown for callouts


# --------------------------------------------------------------------
# 4. DATA LOADING
# --------------------------------------------------------------------
def load_manaus_data(ts_path: Path, ci_path: Path) -> pd.DataFrame:
    """Load time-series and bootstrap CI parquets, merge on 'competencia'."""
    df = pd.read_parquet(ts_path).reset_index(drop=True)
    ci = pd.read_parquet(ci_path).reset_index(drop=True)
    df = df.merge(
        ci[['competencia', 'theta_ci_lower_95', 'theta_ci_upper_95', 'theta_bootstrap_std']],
        on='competencia', how='left'
    )
    return df


# --------------------------------------------------------------------
# 5. FIGURE COMPOSITION
# --------------------------------------------------------------------
def compose_figure(df: pd.DataFrame) -> plt.Figure:
    x = np.arange(len(df))
    month_labels = pd.to_datetime(df['competencia'], format='%Y%m').dt.strftime('%b\n%Y')

    fig, ax1 = plt.subplots(figsize=(11.5, 6.0))
    fig.subplots_adjust(left=0.06, right=0.94, top=0.84, bottom=0.22)

    # ---- Regime bands (left axis, theta space) ----
    ax1.axhspan(120, 170, color=C_CB_ZONE, alpha=0.95, zorder=0)
    ax1.axhspan(30, 120, color=C_HITL_ZONE, alpha=0.95, zorder=0)
    ax1.axhspan(0, 30, color=C_STAC_ZONE, alpha=0.95, zorder=0)
    ax1.axhline(120, color=C_THRESHOLD, linewidth=1.0, linestyle=(0, (4, 2)),
                zorder=1, alpha=0.75)

    # Threshold and zone labels
    ax1.text(-0.25, 122, r'$\theta = 120\degree$   CB threshold',
             fontsize=8.5, color=C_THRESHOLD, ha='left', va='bottom',
             fontweight='bold', zorder=6,
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.75, pad=1.5))
    ax1.text(len(df) - 0.3, 155, r'Circuit-Breaker zone  ($\theta \geq 120\degree$)',
             fontsize=9, color=C_THRESHOLD, ha='right', va='center',
             style='italic', zorder=6,
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=2))
    ax1.text(len(df) - 0.3, 95, r'HITL zone  ($30\degree \leq \theta < 120\degree$)',
             fontsize=9, color='#8a6f1a', ha='right', va='center',
             style='italic', zorder=6,
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=2))

    # ---- Right axis: hospital occupancy bars ----
    ax2 = ax1.twinx()
    bar_colors = [C_OCCUP_SIH if s == 'sih_datasus' else C_OCCUP_LIT
                  for s in df['data_source']]
    bar_edge = ['#4d6a4d' if s == 'sih_datasus' else '#a0b5a0'
                for s in df['data_source']]
    ax2.bar(x, df['hospital_occupancy_pct'],
            color=bar_colors, edgecolor=bar_edge, linewidth=0.6,
            width=0.62, alpha=0.72, zorder=1, label='_nolegend_')
    ax2.set_ylim(0, 170)
    ax2.set_ylabel('Hospital occupancy  (%)', color='#4d6a4d', fontsize=10)
    ax2.tick_params(axis='y', labelcolor='#4d6a4d')
    ax2.set_yticks([0, 25, 50, 75, 100])
    ax2.spines['right'].set_color('#4d6a4d')
    ax2.spines['top'].set_visible(False)

    # ---- Left axis: bootstrap CI band, theta_t, theta_efetivo ----
    ax1.fill_between(x, df['theta_ci_lower_95'], df['theta_ci_upper_95'],
                     color='#b0b0b0', alpha=0.22, zorder=2,
                     label=r'95% bootstrap CI ($\theta$)')
    ax1.plot(x, df['theta_t'], color=C_THETA_T, linewidth=1.3,
             linestyle=(0, (4, 2)), marker='o', markersize=5,
             markerfacecolor='white', markeredgecolor=C_THETA_T,
             markeredgewidth=1.2, zorder=3,
             label=r'$\theta_t$  (instantaneous)')

    # theta_efetivo markers differentiated by data_source
    for is_sih, marker, mfc, label in [
        (True,  's', C_THETA_EFF, r'$\theta_{\mathrm{eff}}$  (SIH/DATASUS)'),
        (False, 'o', 'white',      r'$\theta_{\mathrm{eff}}$  (literature est.)'),
    ]:
        mask = (df['data_source'] == 'sih_datasus') == is_sih
        ax1.scatter(x[mask], df.loc[mask, 'theta_efetivo'],
                    marker=marker, s=55, facecolors=mfc,
                    edgecolors=C_THETA_EFF, linewidths=1.3,
                    zorder=5, label=label)
    ax1.plot(x, df['theta_efetivo'], color=C_THETA_EFF, linewidth=1.8,
             zorder=4, label='_nolegend_')

    # ---- Portaria 69/2021 marker (January 2021) ----
    x_portaria = int(df[df['competencia'] == '202101'].index[0])
    ax1.axvline(x_portaria, color=C_PORTARIA, linewidth=1.0,
                linestyle=(0, (2, 2)), alpha=0.65, zorder=2)
    ax1.text(x_portaria, 167,
             'Portaria 69/2021\n(ICU collapse declared)',
             fontsize=8, color=C_PORTARIA, ha='center', va='top',
             fontweight='bold', zorder=6,
             bbox=dict(facecolor='white', edgecolor=C_PORTARIA,
                       linewidth=0.6, pad=2.0, boxstyle='round,pad=0.25'))

    # ---- CB onset callout (Oct 2020) ----
    x_onset = int(df[df['competencia'] == '202010'].index[0])
    y_onset = float(df.loc[x_onset, 'theta_efetivo'])
    alpha_onset = float(df.loc[x_onset, 'alpha_t'])
    ax1.annotate(
        f"CB onset  Oct 2020\n"
        f"θ$_\\mathrm{{eff}}$ = {y_onset:.1f}°\n"
        f"α(t) = {alpha_onset:.3f}  (crisis memory)\n"
        f"Three months before collapse",
        xy=(x_onset, y_onset),
        xytext=(x_onset - 1.5, 162),
        fontsize=8, color=C_CALLOUT, ha='center', va='top',
        fontweight='bold',
        bbox=dict(facecolor='white', edgecolor=C_CALLOUT,
                  linewidth=0.7, pad=3.0, boxstyle='round,pad=0.3'),
        arrowprops=dict(arrowstyle='-|>', color=C_CALLOUT, linewidth=0.9,
                        connectionstyle='arc3,rad=-0.15'),
        zorder=8,
    )

    # ---- Peak callout (Feb 2021) ----
    x_peak = int(df[df['competencia'] == '202102'].index[0])
    y_peak = float(df.loc[x_peak, 'theta_efetivo'])
    ax1.annotate(
        f"Peak  Feb 2021\n"
        f"θ$_\\mathrm{{eff}}$ = {y_peak:.1f}°",
        xy=(x_peak, y_peak),
        xytext=(x_peak + 1.6, 143),
        fontsize=8, color=C_CALLOUT, ha='center', va='top',
        fontweight='bold',
        bbox=dict(facecolor='white', edgecolor=C_CALLOUT,
                  linewidth=0.7, pad=3.0, boxstyle='round,pad=0.3'),
        arrowprops=dict(arrowstyle='-|>', color=C_CALLOUT, linewidth=0.9,
                        connectionstyle='arc3,rad=0.2'),
        zorder=8,
    )

    # ---- Axes cleanup ----
    ax1.set_xlim(-0.5, len(df) - 0.5)
    ax1.set_ylim(85, 170)
    ax1.set_xticks(x)
    ax1.set_xticklabels(month_labels, fontsize=8.5)
    ax1.set_ylabel(r'Interference angle  $\theta$  (degrees)', fontsize=10)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.tick_params(axis='x', length=3, pad=2)

    # ---- Title and subtitle ----
    fig.suptitle(
        r'Figure 2.  Markovian $\theta_{\mathrm{eff}}$ Trajectory — '
        r'Manaus COVID-19 Health Crisis (Jul 2020 – Jun 2021)',
        fontsize=12.5, fontweight='bold', y=0.97, x=0.06, ha='left'
    )
    fig.text(0.06, 0.925,
             r'Circuit-Breaker activated in October 2020 — three months before '
             r'the January 2021 ICU collapse declared by Portaria MS 69/2021.',
             fontsize=9.5, ha='left', va='top', style='italic', color='#333333')

    # ---- Legend (bottom, single row) ----
    legend_elements = [
        Line2D([0], [0], color=C_THETA_EFF, lw=1.8, marker='s', markersize=6,
               markerfacecolor=C_THETA_EFF, markeredgecolor=C_THETA_EFF,
               label=r'$\theta_{\mathrm{eff}}$ Markovian  (SIH/DATASUS)'),
        Line2D([0], [0], color=C_THETA_EFF, lw=1.8, marker='o', markersize=6,
               markerfacecolor='white', markeredgecolor=C_THETA_EFF,
               label=r'$\theta_{\mathrm{eff}}$ Markovian  (literature est.)'),
        Line2D([0], [0], color=C_THETA_T, lw=1.3, linestyle=(0, (4, 2)),
               marker='o', markersize=5, markerfacecolor='white',
               markeredgecolor=C_THETA_T,
               label=r'$\theta_t$  (instantaneous)'),
        Patch(facecolor='#b0b0b0', alpha=0.35,
              label='95% bootstrap CI'),
        Patch(facecolor=C_OCCUP_SIH, edgecolor='#4d6a4d', alpha=0.72,
              label='Occupancy — SIH/DATASUS'),
        Patch(facecolor=C_OCCUP_LIT, edgecolor='#a0b5a0', alpha=0.72,
              label='Occupancy — literature est.'),
    ]
    fig.legend(handles=legend_elements,
               loc='lower center', bbox_to_anchor=(0.5, 0.02),
               ncol=3, frameon=True, edgecolor='#bbbbbb',
               fancybox=False, fontsize=8.5)

    return fig


# --------------------------------------------------------------------
# 6. SANITY CHECKS (raise if parquet structure is unexpected)
# --------------------------------------------------------------------
def validate_data(df: pd.DataFrame) -> None:
    required = {
        'competencia', 'theta_t', 'theta_efetivo', 'alpha_t',
        'interference_regime', 'hospital_occupancy_pct', 'data_source',
        'theta_ci_lower_95', 'theta_ci_upper_95',
    }
    missing = required - set(df.columns)
    if missing:
        raise RuntimeError(f"Missing required columns: {missing}")

    if len(df) != 12:
        raise RuntimeError(
            f"Expected 12 months in Manaus series, got {len(df)}"
        )

    # Key months used for callouts must be present
    for cmp in ('202010', '202101', '202102'):
        if cmp not in df['competencia'].values:
            raise RuntimeError(f"Missing required competencia: {cmp}")


# --------------------------------------------------------------------
# 7. MAIN
# --------------------------------------------------------------------
def main() -> None:
    print(f"[F2] Loading {INPUT_TS}")
    print(f"[F2] Loading {INPUT_CI}")
    df = load_manaus_data(INPUT_TS, INPUT_CI)

    print("[F2] Validating parquet structure...")
    validate_data(df)
    print(f"[F2] Loaded {len(df)} months — all required columns present")

    # Report the key numerical anchors (self-check against paper Table 3)
    oct_2020 = df[df['competencia'] == '202010'].iloc[0]
    feb_2021 = df[df['competencia'] == '202102'].iloc[0]
    print(f"[F2] CB onset (Oct 2020): theta_eff = {oct_2020['theta_efetivo']:.2f}°, "
          f"alpha = {oct_2020['alpha_t']:.3f}")
    print(f"[F2] Peak (Feb 2021): theta_eff = {feb_2021['theta_efetivo']:.2f}°")

    print("[F2] Composing figure...")
    fig = compose_figure(df)

    for ext, dpi in [('pdf', None), ('png', 300), ('svg', None)]:
        out_path = OUTPUT_DIR / f'F2_manaus_theta_efetivo.{ext}'
        kwargs = {'bbox_inches': 'tight', 'facecolor': 'white'}
        if dpi is not None:
            kwargs['dpi'] = dpi
        fig.savefig(out_path, **kwargs)
        print(f"[F2] wrote  {out_path}")

    plt.close(fig)
    print("[F2] Done.")


if __name__ == '__main__':
    main()
