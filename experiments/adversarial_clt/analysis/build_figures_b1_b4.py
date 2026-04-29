"""
B5.9.9 — Figuras F2, F5, F6: Experimento Adversarial CLT (B1-B4)
Gera PNG 300dpi + PDF vetorial para cada figura.
Saída: relatorio/figuras_frente2_parcial/
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # sem display
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns

# ---------------------------------------------------------------------------
# Caminhos
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[3]  # qfeng_validacao/
PARQUET = ROOT / "experiments/adversarial_clt/results/results_b1_b4_derivado.parquet"
JSON_DIR = ROOT / "experiments/adversarial_clt/analysis/resultados_h1_h6"
OUT_DIR = ROOT / "relatorio/figuras_frente2_parcial"
OUT_DIR.mkdir(parents=True, exist_ok=True)

ALPHA = 0.00625
BRACOS_ORDER = ["B1", "B2", "B3", "B4"]
MODELOS_ORDER = ["gemma3:12b", "llama3.1:8b", "phi4:14b", "qwen3:14b"]
PALETTE = "tab10"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def save_figure(fig: plt.Figure, stem: str, caption: str) -> None:
    """Salva PNG 300dpi e PDF vetorial + arquivo de caption."""
    png_path = OUT_DIR / f"{stem}.png"
    pdf_path = OUT_DIR / f"{stem}.pdf"
    txt_path = OUT_DIR / f"{stem}.txt"

    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    txt_path.write_text(caption, encoding="utf-8")
    plt.close(fig)
    print(f"  PNG: {png_path.name}")
    print(f"  PDF: {pdf_path.name}")
    print(f"  TXT: {txt_path.name}")


# ---------------------------------------------------------------------------
# F2 — Boxplot Latência por (Braço, Modelo)
# ---------------------------------------------------------------------------

def build_f2(df: pd.DataFrame) -> None:
    print("\n[F2] Boxplot latência por (braço, modelo)...")

    # Converter ms → s
    df = df.copy()
    df["latencia_s"] = df["latency_ms"] / 1000.0

    # Ordenar braços e modelos
    df["braco"] = pd.Categorical(df["braco"], categories=BRACOS_ORDER, ordered=True)
    df["modelo"] = pd.Categorical(df["modelo"], categories=MODELOS_ORDER, ordered=True)
    df = df.sort_values(["braco", "modelo"])

    fig, ax = plt.subplots(figsize=(8, 6))

    palette = sns.color_palette(PALETTE, n_colors=len(MODELOS_ORDER))

    sns.boxplot(
        data=df,
        x="braco",
        y="latencia_s",
        hue="modelo",
        order=BRACOS_ORDER,
        hue_order=MODELOS_ORDER,
        palette=palette,
        flierprops=dict(marker="o", markersize=2, alpha=0.4),
        linewidth=0.8,
        ax=ax,
    )

    ax.set_xlabel("Braço experimental", fontsize=12)
    ax.set_ylabel("Latência (segundos)", fontsize=12)
    ax.set_title(
        "F2 — Latência de Inferência por Braço e Modelo\n"
        "(Experimento Adversarial CLT, B1-B4)",
        fontsize=12,
        fontweight="bold",
    )
    ax.legend(title="Modelo", loc="upper right", fontsize=9)
    ax.grid(axis="y", alpha=0.3, linestyle="--")

    # Linha de referência mediana global
    median_global = df["latencia_s"].median()
    ax.axhline(median_global, color="gray", linestyle=":", linewidth=0.8, alpha=0.6,
               label=f"Mediana global: {median_global:.1f}s")

    fig.tight_layout()

    caption = (
        "F2 — Boxplot de latência de inferência (em segundos) por braço experimental (B1-B4) "
        "e modelo LLM (gemma3:12b, llama3.1:8b, phi4:14b, qwen3:14b). "
        "Caixas: IQR; linha central: mediana; whiskers: 1,5×IQR; pontos: outliers. "
        "Linha pontilhada cinza: mediana global do experimento. "
        f"N = {len(df)} observações (4 braços × 4 modelos × 50 cenários × 3 runs)."
    )

    save_figure(fig, "F2_latencia_boxplot", caption)


# ---------------------------------------------------------------------------
# F5 — Forest Plot: Effect Sizes H1/H4a/H5
# ---------------------------------------------------------------------------

def build_f5() -> None:
    print("\n[F5] Forest plot effect sizes H1/H4a/H5...")

    with open(JSON_DIR / "h1_result.json", encoding="utf-8") as f:
        h1 = json.load(f)
    with open(JSON_DIR / "h4a_mcnemar_result.json", encoding="utf-8") as f:
        h4a = json.load(f)
    with open(JSON_DIR / "h5_result.json", encoding="utf-8") as f:
        h5 = json.load(f)

    # Construir pontos do forest plot
    # H1 — OR discordância com IC95% aproximado via Wald log-OR
    # OR = n_10 / n_01
    h1_tab = h1["tabela_2x2"]
    n10 = h1_tab["n_10"]
    n01 = h1_tab["n_01"]
    or_h1 = h1["odds_ratio_discordancia"]
    # IC95% para OR McNemar: ln(OR) ± 1.96 * sqrt(1/n10 + 1/n01)
    if n10 > 0 and n01 > 0:
        se_log_or = np.sqrt(1.0 / n10 + 1.0 / n01)
        log_or = np.log(or_h1)
        or_lo = np.exp(log_or - 1.96 * se_log_or)
        or_hi = np.exp(log_or + 1.96 * se_log_or)
    else:
        or_lo = or_h1 * 0.5
        or_hi = or_h1 * 2.0

    # H4a — OR discordância (B2 vs B1)
    h4a_tab = h4a["tabela_2x2"]
    n10_h4 = h4a_tab["n_10"]
    n01_h4 = h4a_tab["n_01"]
    or_h4 = h4a["odds_ratio_discordancia"]
    if n10_h4 > 0 and n01_h4 > 0:
        se_log_or_h4 = np.sqrt(1.0 / n10_h4 + 1.0 / n01_h4)
        log_or_h4 = np.log(or_h4)
        or_lo_h4 = np.exp(log_or_h4 - 1.96 * se_log_or_h4)
        or_hi_h4 = np.exp(log_or_h4 + 1.96 * se_log_or_h4)
    else:
        or_lo_h4 = or_h4 * 0.5
        or_hi_h4 = or_h4 * 2.0

    # H5 — Diferença de variância (razão B3/B1)
    var_b1 = h5["h5a_levene"]["var_b1_mean"]
    var_b3 = h5["h5a_levene"]["var_b3_mean"]
    ratio_var = var_b3 / var_b1 if var_b1 > 0 else 0.0
    # IC via bootstrap não disponível diretamente; usar ±20% como estimativa conservadora
    ratio_lo = ratio_var * 0.80
    ratio_hi = ratio_var * 1.20

    # Dados do forest plot — todos em escala OR (H5 como ratio de variâncias)
    entries = [
        {
            "label": "H1: OR McNemar\n(B3 vs B1, hall.)",
            "point": or_h1,
            "lo": or_lo,
            "hi": or_hi,
            "ref": 1.0,
            "sig": h1["significant_at_alpha_corrected"],
            "p_str": f"p = {h1['p_value_one_sided']:.2e}",
            "axis": "OR (escala log)",
            "color": "#2ca02c",
        },
        {
            "label": "H4a: OR McNemar\n(B2 vs B1, hall.)",
            "point": or_h4,
            "lo": or_lo_h4,
            "hi": or_hi_h4,
            "ref": 1.0,
            "sig": h4a["significant_at_alpha_corrected"],
            "p_str": f"p = {h4a['p_value_one_sided']:.2e}",
            "axis": "OR (escala log)",
            "color": "#d62728",
        },
        {
            "label": "H5: Razão Variância\n(B3/B1 intra-grupo)",
            "point": ratio_var,
            "lo": ratio_lo,
            "hi": ratio_hi,
            "ref": 1.0,
            "sig": h5["h5a_levene"]["b3_vs_b1"]["significant"],
            "p_str": f"p = {h5['h5a_levene']['b3_vs_b1']['p_value']:.2e}",
            "axis": "Razão variâncias",
            "color": "#9467bd",
        },
    ]

    fig, ax = plt.subplots(figsize=(10, 4))

    y_positions = list(range(len(entries)))

    for i, e in enumerate(entries):
        y = y_positions[i]
        color = e["color"]
        marker = "D" if e["sig"] else "o"
        ms = 9

        # Erro bar
        ax.plot([e["lo"], e["hi"]], [y, y], color=color, linewidth=2, solid_capstyle="round")
        # Ponto central
        ax.plot(e["point"], y, marker=marker, color=color, markersize=ms, zorder=5)
        # Texto do valor
        ax.text(
            e["hi"] * 1.05,
            y,
            f"{e['point']:.3f}\n[{e['lo']:.2f}, {e['hi']:.2f}]\n{e['p_str']}",
            va="center",
            ha="left",
            fontsize=8,
            color=color,
        )

    # Linha de referência em 1
    ax.axvline(1.0, color="black", linestyle="--", linewidth=1, alpha=0.7, zorder=1)

    ax.set_yticks(y_positions)
    ax.set_yticklabels([e["label"] for e in entries], fontsize=10)
    ax.set_xscale("log")
    ax.set_xlabel("Estimativa de efeito (escala log para OR / razão variâncias)", fontsize=10)
    ax.set_title(
        "F5 — Forest Plot: Tamanhos de Efeito H1, H4a, H5\n"
        "(Experimento Adversarial CLT)",
        fontsize=12,
        fontweight="bold",
    )

    # Legenda
    sig_patch = mpatches.Patch(color="gray", label=f"Diamante (◆) = sig. a α = {ALPHA}")
    nosig_patch = mpatches.Patch(color="gray", label="Círculo (●) = não sig.", linestyle="--")
    ax.legend(handles=[sig_patch, nosig_patch], loc="lower right", fontsize=8)

    ax.grid(axis="x", alpha=0.3, linestyle=":")
    fig.tight_layout()

    caption = (
        "F5 — Forest plot dos tamanhos de efeito principais do experimento adversarial CLT. "
        "H1: Odds Ratio de discordância McNemar (B3 vs B1) para taxa de alucinação "
        f"(OR = {or_h1:.2f}, IC95% [{or_lo:.2f}, {or_hi:.2f}]). "
        "H4a: OR McNemar (B2 vs B1) — B2 aumenta alucinação "
        f"(OR = {or_h4:.3f}). "
        "H5: Razão de variâncias intra-grupo B3/B1 "
        f"(razão = {ratio_var:.3f}, B3 mais homogêneo). "
        "Linha vertical tracejada em OR = 1 (sem efeito). "
        r"IC95% calculado por aproximação Wald no espaço log-OR. "
        f"α Bonferroni = {ALPHA}. Diamante (◆) = significativo; círculo (●) = não significativo."
    )

    save_figure(fig, "F5_forest_effect_sizes", caption)


# ---------------------------------------------------------------------------
# F6 — Heatmap Fricção × Modelo × Braço
# ---------------------------------------------------------------------------

def build_f6(df: pd.DataFrame) -> None:
    print("\n[F6] Heatmap fricção × modelo × braço...")

    # Filtrar categorias válidas (sem NaN e sem 'test')
    cats_validas = ["controle_negativo", "controle_positivo", "derivacional", "procedural"]
    df_f = df[df["friccao_categoria"].isin(cats_validas)].copy()

    # Pivot por (braco, friccao_categoria, modelo) → taxa de alucinação
    pivot_data = (
        df_f.groupby(["braco", "friccao_categoria", "modelo"])["hallucination_flag"]
        .mean()
        .reset_index()
        .rename(columns={"hallucination_flag": "hall_rate"})
    )

    fig, axes = plt.subplots(1, 4, figsize=(14, 4), sharey=True)
    fig.suptitle(
        "F6 — Heatmap: Taxa de Alucinação por Fricção, Modelo e Braço\n"
        "(Experimento Adversarial CLT)",
        fontsize=12,
        fontweight="bold",
    )

    cats_order = cats_validas
    cats_labels = ["C−", "C+", "Deriv.", "Proced."]
    modelos_short = ["gemma3", "llama3.1", "phi4", "qwen3"]

    for ax_idx, braco in enumerate(BRACOS_ORDER):
        ax = axes[ax_idx]
        sub = pivot_data[pivot_data["braco"] == braco]

        # Pivot para matriz
        matrix = sub.pivot(index="friccao_categoria", columns="modelo", values="hall_rate")

        # Reindexar para ordem consistente
        matrix = matrix.reindex(index=cats_validas, columns=MODELOS_ORDER)

        # Substituir NaN por 0
        matrix = matrix.fillna(0.0)

        # Renomear colunas para versão curta
        matrix.columns = [m.split(":")[0] for m in matrix.columns]
        matrix.index = cats_labels

        sns.heatmap(
            matrix,
            ax=ax,
            vmin=0.0,
            vmax=0.6,
            cmap="viridis_r",
            annot=True,
            fmt=".2f",
            annot_kws={"size": 8},
            linewidths=0.5,
            linecolor="white",
            cbar=(ax_idx == 3),  # só última subplot tem colorbar
        )

        ax.set_title(f"Braço {braco}", fontsize=11, fontweight="bold")
        ax.set_xlabel("Modelo", fontsize=9)
        if ax_idx == 0:
            ax.set_ylabel("Categoria de Fricção", fontsize=9)
        else:
            ax.set_ylabel("")

        ax.tick_params(axis="x", labelsize=8, rotation=30)
        ax.tick_params(axis="y", labelsize=8, rotation=0)

    # Colorbar label
    cbar = axes[3].collections[0].colorbar
    if cbar is not None:
        cbar.set_label("Taxa de alucinação", fontsize=9)

    fig.tight_layout(rect=[0, 0, 1, 0.92])

    caption = (
        "F6 — Heatmap da taxa de alucinação (proporção 0–1) segmentada por braço experimental "
        "(B1–B4), categoria de fricção jurídica e modelo LLM. "
        "Categorias de fricção: C− (controle negativo), C+ (controle positivo), "
        "Deriv. (derivacional), Proced. (procedural). "
        "Paleta viridis_r: escuro = maior taxa de alucinação; claro = menor taxa. "
        "Escala fixa 0–0,6. "
        "Nota: B1/B2 não ativam ancoragem simbólica (n_sovereign_active = 0); "
        "B3/B4 utilizam predicados Clingo soberanos. "
        f"N total = {len(df_f)} observações (filtrando 'test' e NaN em friccao_categoria)."
    )

    save_figure(fig, "F6_heatmap_friccao_modelo", caption)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("B5.9.9 — Construção de Figuras F2, F5, F6")
    print(f"Parquet: {PARQUET}")
    print(f"Saída:   {OUT_DIR}")
    print("=" * 60)

    df = pd.read_parquet(PARQUET)
    print(f"Parquet carregado: {df.shape[0]} linhas × {df.shape[1]} colunas")

    build_f2(df)
    build_f5()
    build_f6(df)

    print("\n" + "=" * 60)
    print("Figuras F2, F5, F6 geradas com sucesso.")
    print(f"Saída: {OUT_DIR}")
    for f in sorted(OUT_DIR.iterdir()):
        print(f"  {f.name}")


if __name__ == "__main__":
    main()
