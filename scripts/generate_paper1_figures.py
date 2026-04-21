"""
PAPER1 — Publication-quality figures F2 and F3
Run from project root: python scripts/generate_paper1_figures.py
"""
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
from pathlib import Path

OUTPUT_DIR = Path('outputs/figures')
OUTPUT_DIR.mkdir(exist_ok=True)

# ── Typography ────────────────────────────────────────────────────────────────
matplotlib.rcParams.update({
    'font.family':        'serif',
    'font.serif':         ['Times New Roman', 'Palatino', 'DejaVu Serif'],
    'font.size':          10,
    'axes.labelsize':     11,
    'axes.titlesize':     10.5,
    'xtick.labelsize':    9,
    'ytick.labelsize':    9.5,
    'legend.fontsize':    8.5,
    'legend.framealpha':  0.93,
    'legend.edgecolor':   '#CCCCCC',
    'figure.dpi':         150,
    'savefig.dpi':        300,
    'savefig.bbox':       'tight',
    'savefig.pad_inches': 0.08,
    'axes.linewidth':     0.8,
    'xtick.major.width':  0.8,
    'ytick.major.width':  0.8,
    'grid.alpha':         0.22,
    'grid.linestyle':     '--',
    'grid.linewidth':     0.6,
})

# ── Palette (colorblind-safe, publication-ready) ───────────────────────────────
CB_DARK   = '#922B21'   # deep crimson — Circuit-Breaker bars/lines
CB_LIGHT  = '#FADBD8'   # blush — CB background
STAC_DARK = '#1A5276'   # navy — STAC bars/lines
STAC_LIGHT= '#D6EAF8'   # pale blue — STAC background
ALT_DARK  = '#7E5109'   # dark amber — Alert zone text
ALT_LIGHT = '#FEF9E7'   # pale gold — Alert background
OCC_COLOR = '#117A65'   # teal — occupancy
LIT_COL   = '#808B96'   # medium gray — literature data marker
SIH_COL   = '#212F3D'   # near-black — SIH data marker
SEP_COL   = '#AEB6BF'   # separator line


# ═══════════════════════════════════════════════════════════════════════════════
# F2 — Manaus 12-month θ_efetivo trajectory + hospital occupancy
# ═══════════════════════════════════════════════════════════════════════════════
def make_f2():
    df = pd.read_parquet('outputs/e5_results/theta_efetivo_manaus.parquet')

    # Month labels
    xlabels = [
        'Jul\n2020', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
        'Jan\n2021', 'Feb', 'Mar', 'Apr', 'May', 'Jun'
    ]
    x       = np.arange(len(df))
    theta   = df['theta_efetivo'].values
    occ     = df['hospital_occupancy_pct'].values
    src     = df['data_source'].values
    critico = df['evento_critico'].values

    fig, ax1 = plt.subplots(figsize=(11.5, 6.0))

    # ── Regime background shading ─────────────────────────────────────────────
    ax1.axhspan(120, 148, color=CB_LIGHT,  alpha=0.55, zorder=0)
    ax1.axhspan(30,  120, color=ALT_LIGHT, alpha=0.45, zorder=0)
    ax1.axhspan(80,   30, color=STAC_LIGHT,alpha=0.45, zorder=0)

    # ── Threshold dashed lines ────────────────────────────────────────────────
    ax1.axhline(120, color=CB_DARK,   lw=1.3, ls='--', alpha=0.75, zorder=2)
    ax1.axhline(30,  color=STAC_DARK, lw=1.3, ls='--', alpha=0.75, zorder=2)

    ax1.text(11.62, 121.2, 'θ = 120° (CB)',
             color=CB_DARK, fontsize=7.8, ha='right', va='bottom', fontweight='bold')
    ax1.text(11.62, 31.2,  'θ = 30° (STAC)',
             color=STAC_DARK, fontsize=7.8, ha='right', va='bottom', fontweight='bold')

    # ── Continuous θ_efetivo line ─────────────────────────────────────────────
    ax1.plot(x, theta, color=SIH_COL, lw=2.0, alpha=0.92, zorder=4,
             solid_capstyle='round')

    # ── Data-source markers ───────────────────────────────────────────────────
    for i in range(len(x)):
        if src[i] == 'literature':
            ax1.plot(x[i], theta[i], 'o', ms=7.5, zorder=5,
                     mfc='white', mec=LIT_COL, mew=1.8)
        else:
            mc = CB_DARK if theta[i] >= 120 else SIH_COL
            ax1.plot(x[i], theta[i], 's', ms=7.0, zorder=5,
                     mfc=mc, mec=mc, alpha=0.9)

    # ── CB onset annotation (Oct 2020, index 3) ───────────────────────────────
    ax1.annotate(
        'CB onset\nOct 2020',
        xy=(3, theta[3]), xytext=(3.6, 143.5),
        fontsize=7.8, color=CB_DARK,
        ha='center', va='top',
        arrowprops=dict(arrowstyle='->', color=CB_DARK, lw=1.1,
                        connectionstyle='arc3,rad=-0.2'),
        bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=CB_DARK,
                  alpha=0.88, lw=0.8)
    )

    # ── Peak annotation (Feb 2021, index 7) ──────────────────────────────────
    ax1.annotate(
        'Peak  Feb 2021\nθ_eff = 130.9°',
        xy=(7, theta[7]), xytext=(8.9, 143.5),
        fontsize=7.8, color=CB_DARK,
        ha='center', va='top',
        arrowprops=dict(arrowstyle='->', color=CB_DARK, lw=1.1,
                        connectionstyle='arc3,rad=0.2'),
        bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=CB_DARK,
                  alpha=0.88, lw=0.8)
    )

    # ── Portaria 69/2021 vertical marker (Jan 2021, index 6) ─────────────────
    ax1.axvline(5.85, color='#6C3483', lw=1.3, ls=':', alpha=0.85, zorder=3)
    ax1.text(5.73, 107.0,
             'Portaria 69/2021\n(emergency decree)', fontsize=7.5,
             color='#6C3483', ha='right', va='center',
             bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='#6C3483',
                       alpha=0.80, lw=0.7))

    # ── Secondary axis — hospital occupancy bars ──────────────────────────────
    ax2 = ax1.twinx()
    ax2.spines['top'].set_visible(False)
    bw = 0.32
    for i in range(len(x)):
        col   = '#CB4335' if critico[i] else OCC_COLOR
        alpha = 0.40      if critico[i] else 0.22
        ax2.bar(x[i] + bw/2, occ[i], width=bw,
                color=col, alpha=alpha, zorder=1, linewidth=0)

    ax2.set_ylabel('Hospital occupancy (%)', fontsize=10.5,
                   color=OCC_COLOR, labelpad=8)
    ax2.set_ylim(0, 148)
    ax2.tick_params(axis='y', labelcolor=OCC_COLOR, labelsize=9)
    ax2.spines['right'].set_edgecolor(OCC_COLOR)
    ax2.spines['right'].set_visible(True)
    ax2.spines['right'].set_linewidth(0.8)
    ax2.yaxis.set_minor_locator(MultipleLocator(10))

    # ── Data source separators ────────────────────────────────────────────────
    for xv in [2.5, 8.5]:
        ax1.axvline(xv, color=SEP_COL, lw=0.9, ls=':', alpha=0.65, zorder=2)

    # ── Data source shading labels (subtle, inside zones) ─────────────────────
    ax1.text(1.0, 86.5, 'lit.', ha='center', fontsize=7.0,
             color=LIT_COL, style='italic', alpha=0.7)
    ax1.text(5.5, 86.5, 'SIH/DATASUS', ha='center', fontsize=7.0,
             color=SIH_COL, style='italic', alpha=0.7)
    ax1.text(9.75, 86.5, 'lit.', ha='center', fontsize=7.0,
             color=LIT_COL, style='italic', alpha=0.7)

    # ── Regime zone labels (right side, clear of annotations) ────────────────
    ax1.text(11.65, 136.0, 'Circuit-Breaker\nzone  (θ ≥ 120°)',
             fontsize=7.5, color=CB_DARK, fontweight='bold', style='italic',
             ha='right', va='center')
    ax1.text(11.65, 110.0, 'Alert zone',
             fontsize=7.5, color=ALT_DARK, style='italic',
             ha='right', va='center')

    # ── Left axis setup ───────────────────────────────────────────────────────
    ax1.set_xlim(-0.55, 11.7)
    ax1.set_ylim(83, 148)
    ax1.set_xticks(x)
    ax1.set_xticklabels(xlabels, fontsize=9)
    ax1.set_ylabel('Interference angle θ_eff (degrees)', fontsize=11)
    ax1.set_xlabel('Month  ·  Jul 2020 – Jun 2021', fontsize=11, labelpad=5)
    ax1.yaxis.set_minor_locator(MultipleLocator(5))
    ax1.grid(axis='y', which='major')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # ── Legend (placed below plot, horizontal) ────────────────────────────────
    leg_elems = [
        Line2D([0], [0], color=SIH_COL, lw=2.0,
               label='θ_eff (Markovian)'),
        Line2D([0], [0], marker='s', ls='none', ms=6.5,
               mfc=CB_DARK, mec=CB_DARK, label='SIH/DATASUS (CB)'),
        Line2D([0], [0], marker='o', ls='none', ms=6.5,
               mfc='white', mec=LIT_COL, mew=1.8, label='Literature est.'),
        mpatches.Patch(facecolor=OCC_COLOR, alpha=0.25,
                       label='Occupancy (%)'),
        mpatches.Patch(facecolor='#CB4335', alpha=0.40,
                       label='Occupancy — emergency'),
        Line2D([0], [0], color='#6C3483', lw=1.3, ls=':',
               label='Portaria 69/2021'),
    ]
    ax1.legend(handles=leg_elems, loc='upper center',
               bbox_to_anchor=(0.42, -0.14),
               ncol=3, fontsize=8.0, framealpha=0.93,
               handlelength=1.8, columnspacing=1.2)

    # ── Title ─────────────────────────────────────────────────────────────────
    ax1.set_title(
        'Figure 2.  Q-FENG Normative Alignment Trajectory — Manaus Health Crisis (Jul 2020 – Jun 2021)\n'
        'Markovian θ_eff with hospital occupancy overlay; Circuit-Breaker activated Oct 2020, '
        'two months before the January 2021 collapse peak.',
        fontsize=9.5, pad=9, loc='left', color='#1C2833'
    )

    plt.tight_layout()
    for ext in ('png', 'pdf'):
        fig.savefig(OUTPUT_DIR / f'F2_manaus_timeseries.{ext}')
    plt.close(fig)
    print('OK F2 saved -> outputs/figures/F2_manaus_timeseries.{png,pdf}')


# ═══════════════════════════════════════════════════════════════════════════════
# F3 — Seven-scenario θ bar chart with GSP annotations
# ═══════════════════════════════════════════════════════════════════════════════
def make_f3():
    df = pd.read_parquet('outputs/e5_results/validation_results.parquet')

    # Ordered display sequence
    ORDER = ['C2', 'C3', 'C7', 'T-CLT-01', 'T-CLT-02', 'T-CLT-03', 'T-CLT-04']
    df = df.set_index('scenario_id').loc[ORDER].reset_index()

    labels = [
        'C2 — Manaus COVID-19 crisis\n(hospital collapse, Jan 2021)',
        'C3 — SUS regional concentration\n(equity violation, chronic)',
        'C7 — Racial bias in health algorithm\n(Obermeyer 2019, USA)',
        'T-CLT-01 — Working-hours arrangement\n(no valid CBA — unlawful)',
        'T-CLT-02 — Time-bank scheme\n(distorted Súmula TST 85)',
        'T-CLT-03 — Working-hours arrangement\n(valid CBA in place — lawful)',
        'T-CLT-04 — Cited TST precedent\n(positive control — lawful)',
    ]

    theta  = df['theta_deg'].values
    gsp    = df['governance_suppression_pct'].values
    regime = df['interference_regime'].values
    n      = len(labels)

    # y positions: top-down (6 → 0)
    y = np.arange(n - 1, -1, -1)

    fig, ax = plt.subplots(figsize=(12.0, 6.4))

    # ── Domain background bands ───────────────────────────────────────────────
    # Health (rows 0-2 → y=6,5,4): y span 3.55–6.55
    # Labour (rows 3-6 → y=3,2,1,0): y span -0.55–3.45
    ax.axhspan(3.55, 6.62, color='#EBF5FB', alpha=0.55, zorder=0)
    ax.axhspan(-0.55, 3.45, color='#EAFAF1', alpha=0.55, zorder=0)

    # Domain labels (right margin, rotated)
    ax.annotate('', xy=(0.997, 0.98), xytext=(0.997, 0.525),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='-', color='#2471A3', lw=1.2))
    ax.annotate('', xy=(0.997, 0.48), xytext=(0.997, 0.02),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='-', color='#229954', lw=1.2))
    ax.text(1.002, 0.755, 'Health\nGovernance', transform=ax.transAxes,
            fontsize=8, color='#2471A3', fontweight='bold',
            va='center', ha='left', rotation=-90)
    ax.text(1.002, 0.255, 'Labour\nLaw', transform=ax.transAxes,
            fontsize=8, color='#229954', fontweight='bold',
            va='center', ha='left', rotation=-90)

    # ── Threshold reference lines ─────────────────────────────────────────────
    ax.axvline(120, color=CB_DARK,   lw=1.5, ls='--', alpha=0.80, zorder=2)
    ax.axvline(30,  color=STAC_DARK, lw=1.5, ls='--', alpha=0.80, zorder=2)

    ax.text(120.6, -0.9, '120° (CB)', color=CB_DARK,
            fontsize=8, va='top', fontweight='bold')
    ax.text(30.6,  -0.9, '30° (STAC)', color=STAC_DARK,
            fontsize=8, va='top', fontweight='bold')

    # ── Horizontal bars ───────────────────────────────────────────────────────
    bar_colors = [CB_DARK if r == 'CIRCUIT_BREAKER' else STAC_DARK for r in regime]
    bars = ax.barh(y, theta, color=bar_colors, alpha=0.80, height=0.58,
                   edgecolor='white', linewidth=0.6, zorder=3)

    # ── Value annotations ─────────────────────────────────────────────────────
    for i, (bar, th, gs, reg) in enumerate(zip(bars, theta, gsp, regime)):
        xend = bar.get_width()
        yi   = bar.get_y() + bar.get_height() / 2

        if reg == 'CIRCUIT_BREAKER':
            ann = f'θ = {th:.1f}°   GSP = {gs:.1f}%'
            ax.text(xend + 1.0, yi, ann,
                    va='center', ha='left', fontsize=8.5,
                    color=CB_DARK, fontweight='bold')
        else:
            # STAC: bar is short — annotate to the right of bar
            ann = f'θ = {th:.1f}°'
            ax.text(xend + 1.0, yi, ann,
                    va='center', ha='left', fontsize=8.5,
                    color=STAC_DARK, fontweight='bold')

        # Regime badge inside bar (white text)
        badge = '● CB' if reg == 'CIRCUIT_BREAKER' else '● STAC'
        bx    = min(th / 2, th - 0.5) if th > 1 else th + 0.3
        ax.text(bx, yi, badge, va='center', ha='center',
                fontsize=7.5, color='white', fontweight='bold',
                zorder=5)

    # ── Domain separator line ─────────────────────────────────────────────────
    ax.axhline(3.5 - 0.075, color=SEP_COL, lw=1.0, ls='-', alpha=0.6, zorder=2)

    # ── Axes setup ────────────────────────────────────────────────────────────
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9.2)
    ax.set_xlim(0, 162)
    ax.set_ylim(-0.75, 6.75)
    ax.set_xlabel('Interference angle  θ  (degrees)', fontsize=11, labelpad=6)
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    ax.grid(axis='x', which='major', alpha=0.20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # ── Legend ────────────────────────────────────────────────────────────────
    leg_elems = [
        mpatches.Patch(facecolor=CB_DARK,   alpha=0.80,
                       label='Circuit-Breaker (CB):  θ ≥ 120°'),
        mpatches.Patch(facecolor=STAC_DARK, alpha=0.80,
                       label='STAC (stable alignment):  θ < 30°'),
        Line2D([0], [0], color=CB_DARK,   lw=1.5, ls='--',
               label='CB threshold (120°)'),
        Line2D([0], [0], color=STAC_DARK, lw=1.5, ls='--',
               label='STAC threshold (30°)'),
    ]
    ax.legend(handles=leg_elems, loc='lower right', fontsize=8.5, framealpha=0.93)

    # ── Title ─────────────────────────────────────────────────────────────────
    ax.set_title(
        'Figure 3.  Q-FENG Governance Regime Classification — Seven Cross-Domain Scenarios\n'
        'Interference angle θ by scenario; Governance Suppression Percentage (GSP) '
        'annotated for Circuit-Breaker cases.',
        fontsize=9.5, pad=9, loc='left', color='#1C2833'
    )

    plt.tight_layout()
    for ext in ('png', 'pdf'):
        fig.savefig(OUTPUT_DIR / f'F3_seven_scenarios.{ext}')
    plt.close(fig)
    print('OK F3 saved -> outputs/figures/F3_seven_scenarios.{png,pdf}')


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Generating PAPER1 figures...')
    make_f2()
    make_f3()
    print('Done.')
