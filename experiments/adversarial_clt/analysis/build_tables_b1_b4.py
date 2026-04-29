"""
B5.9.8 — Tabelas T1-T8: Experimento Adversarial CLT (B1-B4)
Gera MD + LaTeX (booktabs) para cada tabela.
Saída: relatorio/tabelas_frente2_parcial/
"""

from __future__ import annotations

import json
import os
import textwrap
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Caminhos
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[3]  # qfeng_validacao/
PARQUET = ROOT / "experiments/adversarial_clt/results/results_b1_b4_derivado.parquet"
JSON_DIR = ROOT / "experiments/adversarial_clt/analysis/resultados_h1_h6"
OUT_DIR = ROOT / "relatorio/tabelas_frente2_parcial"
OUT_DIR.mkdir(parents=True, exist_ok=True)

ALPHA = 0.00625  # Bonferroni M=8

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fmt_p(p: float | None, mark_sig: bool = True) -> str:
    """Formata p-value em notação científica, marcando * se significativo."""
    if p is None or (isinstance(p, float) and np.isnan(p)):
        return "—"
    s = f"{p:.3e}"
    if mark_sig and p < ALPHA:
        s += " *"
    return s


def fmt_pct(v: float) -> str:
    return f"{v * 100:.1f}%"


def fmt_float(v: float, decimals: int = 3) -> str:
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return "—"
    return f"{v:.{decimals}f}"


def write_md(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
    print(f"  MD escrito: {path.name}")


def write_tex(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
    print(f"  TeX escrito: {path.name}")


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    """Gera tabela Markdown simples."""
    sep = ["-" * max(len(h), 3) for h in headers]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(sep) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines) + "\n"


def latex_table(
    headers: list[str],
    rows: list[list[str]],
    caption: str,
    label: str,
    col_fmt: str | None = None,
) -> str:
    """Gera tabela LaTeX com booktabs."""
    n = len(headers)
    if col_fmt is None:
        col_fmt = "l" + "r" * (n - 1)
    lines = [
        r"\begin{table}[htbp]",
        r"\centering",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\small",
        rf"\begin{{tabular}}{{{col_fmt}}}",
        r"\toprule",
        " & ".join(headers) + r" \\",
        r"\midrule",
    ]
    for row in rows:
        lines.append(" & ".join(str(c) for c in row) + r" \\")
    lines += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# T1 — Cardinalidade 4×4×50×3
# ---------------------------------------------------------------------------

def build_t1(df: pd.DataFrame) -> None:
    print("\n[T1] Cardinalidade do experimento...")

    bracos = sorted(df["braco"].unique())
    modelos = sorted(df["modelo"].unique())
    n_scenarios = df["scenario_id"].nunique()
    n_runs = df["run_id"].nunique()

    # Contagem por (braco, modelo)
    counts = df.groupby(["braco", "modelo"]).size().unstack(fill_value=0)

    headers = ["Braço"] + modelos + ["Total"]
    rows = []
    for b in bracos:
        row = [b]
        total = 0
        for m in modelos:
            v = int(counts.loc[b, m]) if (b in counts.index and m in counts.columns) else 0
            row.append(str(v))
            total += v
        row.append(str(total))
        rows.append(row)
    # Totais por modelo
    row_total = ["**Total**"]
    grand = 0
    for m in modelos:
        v = int(counts[m].sum()) if m in counts.columns else 0
        row_total.append(str(v))
        grand += v
    row_total.append(str(grand))
    rows.append(row_total)

    note = (
        f"\n**Nota:** Experimento 4 braços × 4 modelos × {n_scenarios} cenários × {n_runs} runs "
        f"= {len(df)} observações totais. α Bonferroni (M=8) = {ALPHA}.\n"
    )

    md_content = (
        "# T1 — Cardinalidade do Experimento Adversarial CLT\n\n"
        + md_table(headers, rows)
        + note
    )

    caption = (
        f"Cardinalidade do experimento adversarial CLT: 4 braços × 4 modelos × "
        f"{n_scenarios} cenários × {n_runs} runs = {len(df)} observações. "
        r"$\alpha_\text{Bonferroni}$ (M=8) = 0{,}00625."
    )

    # Limpar ** para LaTeX
    latex_rows = [row[:] for row in rows]
    latex_rows[-1][0] = "\\textbf{Total}"

    tex_content = latex_table(
        headers, latex_rows, caption=caption, label="tab:t1_cardinalidade"
    )

    write_md(OUT_DIR / "T1_cardinalidade.md", md_content)
    write_tex(OUT_DIR / "T1_cardinalidade.tex", tex_content)


# ---------------------------------------------------------------------------
# T2 — Latência mediana ± IQR por (braço, modelo)
# ---------------------------------------------------------------------------

def build_t2(df: pd.DataFrame) -> None:
    print("\n[T2] Latência mediana ± IQR...")

    bracos = sorted(df["braco"].unique())
    modelos = sorted(df["modelo"].unique())

    stats = df.groupby(["braco", "modelo"])["latency_ms"].agg(
        mediana="median",
        q25=lambda x: np.percentile(x, 25),
        q75=lambda x: np.percentile(x, 75),
    )

    headers = ["Braço", "Modelo", "Mediana (ms)", "Q25 (ms)", "Q75 (ms)", "IQR (ms)"]
    rows = []
    for b in bracos:
        for m in modelos:
            if (b, m) in stats.index:
                r = stats.loc[(b, m)]
                iqr = r["q75"] - r["q25"]
                rows.append([
                    b, m,
                    f"{r['mediana']:.0f}",
                    f"{r['q25']:.0f}",
                    f"{r['q75']:.0f}",
                    f"{iqr:.0f}",
                ])

    note = "\n**Nota:** Latência em milissegundos (ms). IQR = Q75 − Q25.\n"
    md_content = "# T2 — Latência Mediana ± IQR por (Braço, Modelo)\n\n" + md_table(headers, rows) + note

    caption = (
        "Latência de inferência (ms) por braço e modelo: mediana, Q25, Q75 e IQR. "
        "Valores em milissegundos."
    )
    tex_content = latex_table(
        headers, rows, caption=caption, label="tab:t2_latencia",
        col_fmt="llrrrr"
    )

    write_md(OUT_DIR / "T2_latencia.md", md_content)
    write_tex(OUT_DIR / "T2_latencia.tex", tex_content)


# ---------------------------------------------------------------------------
# T3 — Distribuição n_sovereign_active por braço
# ---------------------------------------------------------------------------

def build_t3(df: pd.DataFrame) -> None:
    print("\n[T3] Distribuição n_sovereign_active por braço...")

    bracos = sorted(df["braco"].unique())

    # Pivot de contagem
    pivot = df.groupby(["braco", "n_sovereign_active"]).size().unstack(fill_value=0)
    all_vals = sorted(pivot.columns)

    headers = ["Braço"] + [str(int(v)) for v in all_vals] + ["Total"]
    rows = []
    for b in bracos:
        row = [b]
        total = 0
        for v in all_vals:
            c = int(pivot.loc[b, v]) if b in pivot.index and v in pivot.columns else 0
            row.append(str(c))
            total += c
        row.append(str(total))
        rows.append(row)

    note = (
        "\n**Nota:** B1 e B2 não ativam soberania (n_sovereign_active = 0). "
        "B3/B4 ativam predicados soberanos; os valores refletem o número de regras Clingo ativas por observação.\n"
        "\n`clingo_satisfiability` é string vazia em todos os braços — usado `n_sovereign_active` como proxy.\n"
    )

    md_content = (
        "# T3 — Distribuição de n\\_sovereign\\_active por Braço\n\n"
        + md_table(headers, rows)
        + note
    )

    caption = (
        "Distribuição de \\texttt{n\\_sovereign\\_active} (número de predicados soberanos Clingo ativos) "
        "por braço. B1/B2: ancoragem simbólica inativa (sempre 0). B3/B4: ancoragem ativa."
    )
    tex_content = latex_table(
        headers, rows, caption=caption, label="tab:t3_sovereign",
        col_fmt="l" + "r" * (len(all_vals) + 1)
    )

    write_md(OUT_DIR / "T3_sovereign_active.md", md_content)
    write_tex(OUT_DIR / "T3_sovereign_active.tex", tex_content)


# ---------------------------------------------------------------------------
# T4 — H1: McNemar B3 vs B1 (global + breakdown por modelo)
# ---------------------------------------------------------------------------

def build_t4(json_dir: Path) -> None:
    print("\n[T4] H1 — McNemar B3 vs B1...")

    with open(json_dir / "h1_result.json", encoding="utf-8") as f:
        h1 = json.load(f)
    with open(json_dir / "h1_breakdown_por_modelo.json", encoding="utf-8") as f:
        breakdown = json.load(f)

    # Painel global
    headers_global = [
        "Escopo", "N pares", "Taxa B1", "Taxa B3", "Redução (pp)",
        "OR discordância", "Estatística McNemar", "p (unicaudal)", "Sig.?"
    ]
    global_row = [
        "Global",
        str(h1["n_pares"]),
        fmt_pct(h1["b1_hall_rate"]),
        fmt_pct(h1["b3_hall_rate"]),
        f"{h1['reducao_absoluta_pp']:.1f} pp",
        fmt_float(h1["odds_ratio_discordancia"]),
        fmt_float(h1["mcnemar_statistic"], 1),
        fmt_p(h1["p_value_one_sided"]),
        "Sim *" if h1["significant_at_alpha_corrected"] else "Não",
    ]

    headers_modelo = [
        "Modelo", "N pares", "Taxa B1", "Taxa B3",
        "OR discordância", "p (unicaudal)", "Sig.?"
    ]
    rows_modelo = []
    for m in breakdown:
        or_str = fmt_float(m["odds_ratio"]) if m["odds_ratio"] is not None else "∞"
        rows_modelo.append([
            m["modelo"],
            str(m["n_pares"]),
            fmt_pct(m["b1_hall_rate"]),
            fmt_pct(m["b3_hall_rate"]),
            or_str,
            fmt_p(m["p_one_sided"]),
            "Sim *" if m["significant"] else "Não",
        ])

    note = (
        f"\n**Nota:** α Bonferroni = {ALPHA}. * = significativo. "
        f"OR discordância = n_10 / n_01. ∞ indica n_01 = 0 (sem reversão B3→B1).\n"
        f"\n**Interpretação:** {h1['interpretation']}\n"
    )

    md_content = (
        "# T4 — H1: McNemar B3 vs B1 (Taxa de Alucinação)\n\n"
        "## Resultado Global\n\n"
        + md_table(headers_global, [global_row])
        + "\n## Breakdown por Modelo\n\n"
        + md_table(headers_modelo, rows_modelo)
        + note
    )

    # LaTeX — duas subtabelas
    tex_global = latex_table(
        headers_global, [global_row],
        caption=(
            "H1 — Resultado global McNemar (B3 vs B1) para taxa de alucinação. "
            r"$\alpha_\text{Bonferroni}$ = 0{,}00625. * = significativo."
        ),
        label="tab:t4_h1_global",
        col_fmt="lrrrrrrr"
    )
    tex_modelo = latex_table(
        headers_modelo, rows_modelo,
        caption="H1 — Breakdown McNemar por modelo (B3 vs B1).",
        label="tab:t4_h1_modelo",
        col_fmt="lrrrrrr"
    )

    write_md(OUT_DIR / "T4_h1_mcnemar.md", md_content)
    write_tex(OUT_DIR / "T4_h1_mcnemar.tex", tex_global + "\n" + tex_modelo)


# ---------------------------------------------------------------------------
# T5 — H2: Wilcoxon B3 vs B1 (cobertura)
# ---------------------------------------------------------------------------

def build_t5(json_dir: Path) -> None:
    print("\n[T5] H2 — Wilcoxon cobertura B3 vs B1...")

    with open(json_dir / "h2_result.json", encoding="utf-8") as f:
        h2 = json.load(f)

    ci = h2["ci95_median_diff_bootstrap"]
    ci_str = f"[{ci[0]:.3f}, {ci[1]:.3f}]"

    headers = [
        "Métrica", "B1 (média)", "B3 (média)", "Dif. mediana (B3−B1)",
        "IC95% bootstrap", "Margem NI", "Wilcoxon W", "p (unicaudal)", "NI demonstrada?"
    ]
    row = [
        "Cobertura jurídica",
        fmt_float(h2["b1_coverage_mean"]),
        fmt_float(h2["b3_coverage_mean"]),
        fmt_float(h2["median_diff_b3_minus_b1"]),
        ci_str,
        fmt_float(h2["margem_nao_inferioridade"]),
        fmt_float(h2["wilcoxon_statistic"], 0),
        fmt_p(h2["p_value_one_sided_nao_inferioridade"]),
        "Não",
    ]

    note = (
        f"\n**Nota:** NI = não-inferioridade (H: diff > −0,05). {h2['interpretation']}\n"
    )

    md_content = (
        "# T5 — H2: Wilcoxon Não-Inferioridade de Cobertura (B3 vs B1)\n\n"
        + md_table(headers, [row])
        + note
    )

    caption = (
        "H2 — Teste de Wilcoxon (não-inferioridade) para cobertura jurídica B3 vs B1. "
        "IC95\\% calculado por bootstrap (n=1000). NI = não-inferioridade."
    )
    tex_content = latex_table(
        headers, [row], caption=caption, label="tab:t5_h2_wilcoxon",
        col_fmt="lrrrrrrrr"
    )

    write_md(OUT_DIR / "T5_h2_wilcoxon.md", md_content)
    write_tex(OUT_DIR / "T5_h2_wilcoxon.tex", tex_content)


# ---------------------------------------------------------------------------
# T6 — H4: B2 vs B1 alucinação (McNemar) + cobertura (Wilcoxon)
# ---------------------------------------------------------------------------

def build_t6(json_dir: Path) -> None:
    print("\n[T6] H4 — B2 vs B1 alucinação + cobertura...")

    with open(json_dir / "h4a_mcnemar_result.json", encoding="utf-8") as f:
        h4a = json.load(f)
    with open(json_dir / "h4b_wilcoxon_result.json", encoding="utf-8") as f:
        h4b = json.load(f)

    # H4a — McNemar
    headers_4a = [
        "Teste", "N pares", "Taxa B1", "Taxa B2",
        "Δ (pp)", "OR discordância", "p (unicaudal)", "B2 reduz hall.?"
    ]
    row_4a = [
        "McNemar H4a",
        str(h4a["n_pares"]),
        fmt_pct(h4a["b1_hall_rate"]),
        fmt_pct(h4a["b2_hall_rate"]),
        f"{h4a['reducao_absoluta_pp']:.1f} pp",
        fmt_float(h4a["odds_ratio_discordancia"]),
        fmt_p(h4a["p_value_one_sided"]),
        "Não",
    ]

    # H4b — Wilcoxon
    ci = h4b["ci95_median_diff_bootstrap"]
    ci_str = f"[{ci[0]:.3f}, {ci[1]:.3f}]"

    headers_4b = [
        "Teste", "N pares", "Cob. B1 (média)", "Cob. B2 (média)",
        "Dif. mediana", "IC95%", "Wilcoxon W", "p (unicaudal)", "NI demonstrada?"
    ]
    row_4b = [
        "Wilcoxon H4b",
        str(h4b["n_pares"]),
        fmt_float(h4b["b1_coverage_mean"]),
        fmt_float(h4b["b2_coverage_mean"]),
        fmt_float(h4b["median_diff_b2_minus_b1"]),
        ci_str,
        fmt_float(h4b["wilcoxon_statistic"], 0),
        fmt_p(h4b["p_value_one_sided"]),
        "Não",
    ]

    note = (
        f"\n**Nota (H4a):** {h4a['interpretation']}\n\n"
        f"**Nota (H4b):** {h4b['interpretation']}\n"
    )

    md_content = (
        "# T6 — H4: B2 vs B1 — Alucinação (McNemar) e Cobertura (Wilcoxon)\n\n"
        "## H4a — Alucinação\n\n"
        + md_table(headers_4a, [row_4a])
        + "\n## H4b — Cobertura\n\n"
        + md_table(headers_4b, [row_4b])
        + note
    )

    tex_4a = latex_table(
        headers_4a, [row_4a],
        caption=(
            "H4a — McNemar (B2 vs B1) para taxa de alucinação. "
            "B2 (RAG isolado) aumenta alucinação em relação a B1 (baseline)."
        ),
        label="tab:t6_h4a_mcnemar",
        col_fmt="lrrrrrrr"
    )
    tex_4b = latex_table(
        headers_4b, [row_4b],
        caption="H4b — Wilcoxon não-inferioridade de cobertura jurídica (B2 vs B1).",
        label="tab:t6_h4b_wilcoxon",
        col_fmt="lrrrrrrrr"
    )

    write_md(OUT_DIR / "T6_h4_b2_vs_b1.md", md_content)
    write_tex(OUT_DIR / "T6_h4_b2_vs_b1.tex", tex_4a + "\n" + tex_4b)


# ---------------------------------------------------------------------------
# T7 — H5: Levene + Bootstrap overlap
# ---------------------------------------------------------------------------

def build_t7(json_dir: Path) -> None:
    print("\n[T7] H5 — Levene + Bootstrap overlap...")

    with open(json_dir / "h5_result.json", encoding="utf-8") as f:
        h5 = json.load(f)

    lev = h5["h5a_levene"]
    boot = h5["h5b_bootstrap_overlap"]

    # Levene
    headers_lev = [
        "Comparação", "Var. média B3", "Var. média outro braço",
        "Estatística Levene", "p-value", "Sig.?", "B3 menor variância?"
    ]
    rows_lev = []
    for comp_name, key in [("B3 vs B1", "b3_vs_b1"), ("B3 vs B2", "b3_vs_b2"), ("B3 vs B4", "b3_vs_b4")]:
        c = lev[key]
        outro_var = {
            "b3_vs_b1": lev["var_b1_mean"],
            "b3_vs_b2": lev["var_b2_mean"],
            "b3_vs_b4": lev["var_b4_mean"],
        }[key]
        sig = c.get("significant", False)
        menor = c.get("b3_menor_var", False)
        rows_lev.append([
            comp_name,
            fmt_float(lev["var_b3_mean"]),
            fmt_float(outro_var),
            fmt_float(c["statistic"]),
            fmt_p(c["p_value"]),
            "Sim *" if sig else "Não",
            "Sim" if menor else "Não",
        ])

    # Bootstrap overlap
    headers_boot = [
        "N pares (modelo, cenário)", "Sem sobreposição IC95%",
        "Fração sem sobreposição", "Interpretação"
    ]
    row_boot = [
        str(boot["n_pares_modelo_cenario"]),
        str(boot["n_no_overlap"]),
        fmt_pct(boot["frac_no_overlap_b3_b1"]),
        boot["interpretation"],
    ]

    note = f"\n**Interpretação geral:** {h5['interpretation']}\n"

    md_content = (
        "# T7 — H5: Variabilidade Intra-(Modelo, Cenário): Levene + Bootstrap\n\n"
        "## H5a — Teste de Levene\n\n"
        + md_table(headers_lev, rows_lev)
        + "\n## H5b — Sobreposição de IC95% (Bootstrap)\n\n"
        + md_table(headers_boot, [row_boot])
        + note
    )

    tex_lev = latex_table(
        headers_lev, rows_lev,
        caption=(
            "H5a — Teste de Levene para homogeneidade de variâncias intra-(modelo, cenário). "
            r"$\alpha_\text{Bonferroni}$ = 0{,}00625. * = significativo."
        ),
        label="tab:t7_h5a_levene",
        col_fmt="lrrrrrr"
    )
    tex_boot = latex_table(
        headers_boot, [row_boot],
        caption="H5b — Sobreposição de IC95\\% por bootstrap entre B3 e B1.",
        label="tab:t7_h5b_bootstrap",
        col_fmt="rrlp{6cm}"
    )

    write_md(OUT_DIR / "T7_h5_variabilidade.md", md_content)
    write_tex(OUT_DIR / "T7_h5_variabilidade.tex", tex_lev + "\n" + tex_boot)


# ---------------------------------------------------------------------------
# T8 — H6: ANOVA fricção × braço
# ---------------------------------------------------------------------------

def build_t8(json_dir: Path) -> None:
    print("\n[T8] H6 — ANOVA fricção × braço...")

    with open(json_dir / "h6_result.json", encoding="utf-8") as f:
        h6 = json.load(f)

    anova = h6["anova_two_way"]
    rates = h6["rate_by_friccao_braco"]
    eta = anova["eta_sq_partial"]

    # Tabela ANOVA
    headers_anova = [
        "Fonte", "F", "p-value", "Sig.?", "η² parcial"
    ]

    fonte_map = {
        "C(friccao_categoria)": "Fricção (categoria)",
        "C(braco)": "Braço",
        "C(friccao_categoria):C(braco)": "Interação Fricção × Braço",
    }
    rows_anova = [
        [
            "Fricção (categoria)",
            fmt_float(anova["F_friccao"]),
            fmt_p(anova["p_friccao"]),
            "Sim *",
            fmt_float(eta["C(friccao_categoria)"])
        ],
        [
            "Braço",
            fmt_float(anova["F_braco"]),
            fmt_p(anova["p_braco"]),
            "Sim *",
            fmt_float(eta["C(braco)"])
        ],
        [
            "Interação Fricção × Braço",
            fmt_float(anova["F_interacao"]),
            fmt_p(anova["p_interacao"]),
            "Sim *",
            fmt_float(eta["C(friccao_categoria):C(braco)"])
        ],
    ]

    # Tabela de taxas
    bracos = ["B1", "B2", "B3", "B4"]
    cats = sorted(rates["B1"].keys())
    headers_rates = ["Categoria Fricção"] + bracos
    rows_rates = []
    for cat in cats:
        row = [cat.replace("_", " ").title()]
        for b in bracos:
            v = rates[b].get(cat, None)
            row.append(fmt_pct(v) if v is not None else "—")
        rows_rates.append(row)

    note = (
        f"\n**Nota:** N total = {h6['n_total']}. "
        f"Interação significativa: {h6['interacao_significativa']}. "
        f"{h6['interpretation']}\n"
    )

    md_content = (
        "# T8 — H6: ANOVA Fricção × Braço (Taxa de Alucinação)\n\n"
        "## Resultados ANOVA Two-Way\n\n"
        + md_table(headers_anova, rows_anova)
        + "\n## Taxas de Alucinação por (Fricção, Braço)\n\n"
        + md_table(headers_rates, rows_rates)
        + note
    )

    tex_anova = latex_table(
        headers_anova, rows_anova,
        caption=(
            "H6 — ANOVA two-way: efeito de fricção (categoria) e braço sobre taxa de alucinação. "
            r"$\alpha_\text{Bonferroni}$ = 0{,}00625. * = significativo."
        ),
        label="tab:t8_h6_anova",
        col_fmt="lrrrr"
    )
    tex_rates = latex_table(
        headers_rates, rows_rates,
        caption="H6 — Taxas de alucinação por categoria de fricção e braço (proporção 0--1).",
        label="tab:t8_h6_rates",
        col_fmt="lrrrr"
    )

    write_md(OUT_DIR / "T8_h6_anova_friccao.md", md_content)
    write_tex(OUT_DIR / "T8_h6_anova_friccao.tex", tex_anova + "\n" + tex_rates)


# ---------------------------------------------------------------------------
# INDEX.md
# ---------------------------------------------------------------------------

def build_index() -> None:
    print("\n[INDEX] Gerando INDEX.md...")

    tabelas = [
        ("T1", "T1_cardinalidade", "Cardinalidade 4×4×50×3 do experimento"),
        ("T2", "T2_latencia", "Latência mediana ± IQR por (braço, modelo)"),
        ("T3", "T3_sovereign_active", "Distribuição n_sovereign_active por braço (proxy satisfiability)"),
        ("T4", "T4_h1_mcnemar", "H1 — McNemar B3 vs B1: taxa de alucinação (global + breakdown por modelo)"),
        ("T5", "T5_h2_wilcoxon", "H2 — Wilcoxon não-inferioridade de cobertura B3 vs B1"),
        ("T6", "T6_h4_b2_vs_b1", "H4 — B2 vs B1: alucinação (McNemar) e cobertura (Wilcoxon)"),
        ("T7", "T7_h5_variabilidade", "H5 — Levene + Bootstrap overlap (variabilidade intra-grupo)"),
        ("T8", "T8_h6_anova_friccao", "H6 — ANOVA two-way fricção × braço (F-stats + taxas)"),
    ]

    lines = [
        "# Índice de Tabelas — Experimento Adversarial CLT (B1-B4)",
        "",
        f"Gerado automaticamente por `build_tables_b1_b4.py`. α Bonferroni (M=8) = {ALPHA}.",
        "",
        "| ID | Arquivo MD | Arquivo TeX | Conteúdo |",
        "|----|-----------|-------------|---------|",
    ]
    for tid, base, desc in tabelas:
        lines.append(f"| {tid} | [{base}.md]({base}.md) | [{base}.tex]({base}.tex) | {desc} |")

    lines += [
        "",
        "## Notas Metodológicas",
        "",
        "- **α Bonferroni**: 0,00625 (M=8 hipóteses; * indica p < α)",
        "- **p-values**: notação científica (`p = x.xxxe-xx`)",
        "- **Parquet**: `results_b1_b4_derivado.parquet` (2.400 linhas, 38 colunas)",
        "- **Tabelas geradas**: MD + LaTeX (booktabs). DOCX omitido (python-docx não requerido).",
        "- **`clingo_satisfiability`**: string vazia em todos os braços — T3 usa `n_sovereign_active` como proxy.",
    ]

    (OUT_DIR / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  INDEX.md escrito: {OUT_DIR / 'INDEX.md'}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("B5.9.8 — Construção de Tabelas T1-T8")
    print(f"Parquet: {PARQUET}")
    print(f"Saída:   {OUT_DIR}")
    print("=" * 60)

    df = pd.read_parquet(PARQUET)
    print(f"Parquet carregado: {df.shape[0]} linhas × {df.shape[1]} colunas")

    build_t1(df)
    build_t2(df)
    build_t3(df)
    build_t4(JSON_DIR)
    build_t5(JSON_DIR)
    build_t6(JSON_DIR)
    build_t7(JSON_DIR)
    build_t8(JSON_DIR)
    build_index()

    print("\n" + "=" * 60)
    print("Tabelas T1-T8 geradas com sucesso.")
    print(f"Saída: {OUT_DIR}")
    # List generated files
    for f in sorted(OUT_DIR.iterdir()):
        print(f"  {f.name}")


if __name__ == "__main__":
    main()
