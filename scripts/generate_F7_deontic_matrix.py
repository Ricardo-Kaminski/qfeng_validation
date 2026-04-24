"""
F7 — DeonticAtom distribution across normative tracks
=======================================================
Paper 1 (Applied Intelligence): Empirical Validation of the Q-FENG C1 Pipeline

Source data: outputs/e2_report.md + outputs/e2_report_trabalhista.md

Fonte canônica (confirmada via Claude Code + memória Serena):
O reporter.py do projeto acumula contadores em memória durante o run E2 e os
escreve nos *_report.md ao final. O deontic_cache e os e3_predicates/*.lp são
artefatos downstream (cache = resíduo de runs; .lp = subset que sobreviveu a
E3 translation + E4 HITL), NÃO são fontes de contagem oficial.

Representação:
  Duas subplots lado a lado, sem cross-tab regime × modality (não há fonte
  consolidada para isso no pipeline atual — documentado em
  artefatos/briefings/DIAGNOSTICO_F7_atom_counts_21abr2026.md):

    (a) DeonticAtoms por regime normativo × trilha aplicada
        Barras horizontais agrupadas: saúde (BR/EU/USA) + trabalhista (BR).
        Mostra o peso relativo de cada jurisdição em cada trilha.

    (b) Distribuição por modalidade deôntica, agrupada por trilha
        Barras verticais agrupadas (obligation/permission/prohibition/faculty),
        saúde vs. trabalhista lado a lado. Revela assimetria empírica:
        prohibition no corpus trabalhista (16.3%) vs. saúde (4.8%) — diferença
        3.4x que reflete a estrutura normativa distinta (direito do trabalho
        tende a formular mais vedações explícitas ao empregador).

Tipografia e paleta consistentes com F2–F6 (serif, greyscale; sem cor
decorativa).

Valores codificados do e2_report.md (21 abr 2026 run):
  Saúde       : 5.136 atoms | BR 3.206 / EU 1.101 / USA 829
                modality    : obligation 4.325 (84.2%) | permission 482 (9.4%)
                              prohibition 245 (4.8%)   | faculty    84 (1.6%)

  Trabalhista : 5.006 atoms | BR 5.006 (apenas)
                modality    : obligation 3.536 (70.6%) | prohibition 814 (16.3%)
                              permission 461 (9.2%)    | faculty   195 (3.9%)

  TOTAL       : 10.142 atoms

Usage:
    python scripts/generate_F7_deontic_matrix.py

Output (in outputs/figures/):
    F7_deontic_regime_modality.pdf
    F7_deontic_regime_modality.png   (300 dpi)
    F7_deontic_regime_modality.svg

Author: Ricardo S. Kaminski
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# --------------------------------------------------------------------
# 1. PATHS
# --------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = PROJECT_ROOT / "outputs" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------
# 2. TYPOGRAPHY (consistent with F2–F6)
# --------------------------------------------------------------------
mpl.rcParams["font.family"] = "serif"
mpl.rcParams["font.serif"] = [
    "DejaVu Serif",
    "Times New Roman",
    "Nimbus Roman",
    "serif",
]
mpl.rcParams["mathtext.fontset"] = "dejavuserif"
mpl.rcParams["axes.unicode_minus"] = False
mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42

# --------------------------------------------------------------------
# 3. CANONICAL DATA (from e2_report.md + e2_report_trabalhista.md)
# --------------------------------------------------------------------
SAUDE_REGIMES = {
    "Brazil (health)": 3206,
    "EU (health)": 1101,
    "USA (health)": 829,
}
TRAB_REGIMES = {
    "Brazil (labour)": 5006,
}

SAUDE_MODALITY = {
    "Obligation": 4325,
    "Permission": 482,
    "Prohibition": 245,
    "Faculty": 84,
}
TRAB_MODALITY = {
    "Obligation": 3536,
    "Permission": 461,
    "Prohibition": 814,
    "Faculty": 195,
}

MODALITIES = ["Obligation", "Permission", "Prohibition", "Faculty"]
TOTAL_SAUDE = sum(SAUDE_MODALITY.values())
TOTAL_TRAB = sum(TRAB_MODALITY.values())
GRAND_TOTAL = TOTAL_SAUDE + TOTAL_TRAB

# --------------------------------------------------------------------
# 4. GREYSCALE TONES
# --------------------------------------------------------------------
TONE_SAUDE = "#3a3a3a"
TONE_TRAB = "#9a9a9a"
EDGE = "#000000"


def _save_all(fig: plt.Figure, out_base: Path) -> None:
    for ext in ("pdf", "png", "svg"):
        path = out_base.with_suffix(f".{ext}")
        kwargs = {"dpi": 300} if ext == "png" else {}
        fig.savefig(path, bbox_inches="tight", facecolor="white", **kwargs)
        print(f"  wrote {path.relative_to(PROJECT_ROOT)}")


def plot_figure(out_base: Path) -> None:
    fig, (ax_left, ax_right) = plt.subplots(
        1, 2, figsize=(13, 4.8),
        gridspec_kw={"width_ratios": [1.0, 1.15]},
    )

    # --- LEFT: atoms per regime, horizontal bars grouped by track ---
    all_regimes = list(SAUDE_REGIMES.keys()) + list(TRAB_REGIMES.keys())
    all_counts = list(SAUDE_REGIMES.values()) + list(TRAB_REGIMES.values())
    all_colors = [TONE_SAUDE] * len(SAUDE_REGIMES) + [TONE_TRAB] * len(TRAB_REGIMES)

    y_pos = np.arange(len(all_regimes))
    bars = ax_left.barh(
        y_pos, all_counts,
        color=all_colors, edgecolor=EDGE, linewidth=0.8, height=0.65,
    )
    ax_left.set_yticks(y_pos)
    ax_left.set_yticklabels(all_regimes, fontsize=10)
    ax_left.invert_yaxis()
    ax_left.set_xlabel("DeonticAtoms extracted (E2)", fontsize=10)
    ax_left.set_title(
        "(a) Atoms per normative regime, by applied track",
        fontsize=10.5, pad=10,
    )
    ax_left.grid(axis="x", linestyle=":", alpha=0.35, zorder=0)
    ax_left.set_axisbelow(True)

    # Value labels at end of each bar
    for bar, val in zip(bars, all_counts):
        ax_left.text(
            bar.get_width() + max(all_counts) * 0.012,
            bar.get_y() + bar.get_height() / 2,
            f"{val:,}",
            va="center", ha="left",
            fontsize=9.5,
        )

    # Extra room on the right for the longest-bar label AND the legend
    ax_left.set_xlim(0, max(all_counts) * 1.22)

    # Track legend for left panel — anchored to middle-right region, clear of bars
    left_legend = [
        Patch(facecolor=TONE_SAUDE, edgecolor=EDGE, label="Health / governance"),
        Patch(facecolor=TONE_TRAB, edgecolor=EDGE, label="Labour"),
    ]
    ax_left.legend(
        handles=left_legend, loc="center right",
        bbox_to_anchor=(1.0, 0.50),
        frameon=True, fontsize=8.5, edgecolor="#666666",
    )

    # --- RIGHT: modality distribution, grouped bars (health vs labour) ---
    x = np.arange(len(MODALITIES))
    width = 0.38

    vals_saude = [SAUDE_MODALITY[m] for m in MODALITIES]
    vals_trab = [TRAB_MODALITY[m] for m in MODALITIES]

    b1 = ax_right.bar(
        x - width / 2, vals_saude, width,
        color=TONE_SAUDE, edgecolor=EDGE, linewidth=0.8,
        label=f"Health / governance (n={TOTAL_SAUDE:,})",
    )
    b2 = ax_right.bar(
        x + width / 2, vals_trab, width,
        color=TONE_TRAB, edgecolor=EDGE, linewidth=0.8,
        label=f"Labour (n={TOTAL_TRAB:,})",
    )

    ax_right.set_xticks(x)
    ax_right.set_xticklabels(MODALITIES, fontsize=10)
    ax_right.set_ylabel("DeonticAtoms (count)", fontsize=10)
    ax_right.set_title(
        "(b) Modality distribution, by track",
        fontsize=10.5, pad=10,
    )
    ax_right.grid(axis="y", linestyle=":", alpha=0.35, zorder=0)
    ax_right.set_axisbelow(True)

    # Value + percentage labels on each bar
    for bars, totals in ((b1, TOTAL_SAUDE), (b2, TOTAL_TRAB)):
        for bar in bars:
            h = bar.get_height()
            pct = h / totals * 100
            ax_right.text(
                bar.get_x() + bar.get_width() / 2,
                h + max(vals_saude + vals_trab) * 0.015,
                f"{int(h):,}\n({pct:.1f}%)",
                ha="center", va="bottom",
                fontsize=8.5, linespacing=1.05,
            )

    # More headroom so the tallest bar's label does not collide with legend
    ax_right.set_ylim(0, max(vals_saude + vals_trab) * 1.34)
    ax_right.legend(
        loc="upper right",
        frameon=True, fontsize=9, edgecolor="#666666",
    )

    # --- Global footer with total ---
    fig.text(
        0.5, -0.01,
        f"Total: {GRAND_TOTAL:,} DeonticAtoms extracted at E2 "
        f"(source: outputs/e2_report*.md)",
        ha="center", fontsize=8.5, style="italic", color="#555555",
    )

    plt.tight_layout(rect=[0, 0.02, 1, 1])
    _save_all(fig, out_base)
    plt.close(fig)


def main() -> None:
    print("F7 — DeonticAtom distribution across normative tracks")
    print("  Canonical source: outputs/e2_report*.md")
    print(f"    Saude      : {TOTAL_SAUDE:,} atoms "
          f"(BR {SAUDE_REGIMES['Brazil (health)']:,} + "
          f"EU {SAUDE_REGIMES['EU (health)']:,} + "
          f"USA {SAUDE_REGIMES['USA (health)']:,})")
    print(f"    Trabalhista: {TOTAL_TRAB:,} atoms (BR only)")
    print(f"    TOTAL      : {GRAND_TOTAL:,}")

    print("\n  Modality distribution:")
    for m in MODALITIES:
        s = SAUDE_MODALITY[m]
        t = TRAB_MODALITY[m]
        print(f"    {m:<12}: health {s:>5,} ({s/TOTAL_SAUDE*100:>4.1f}%) | "
              f"labour {t:>5,} ({t/TOTAL_TRAB*100:>4.1f}%)")

    out_base = FIG_DIR / "F7_deontic_regime_modality"
    print("\n  Writing figure:")
    plot_figure(out_base)
    print("\nDone.")


if __name__ == "__main__":
    main()
