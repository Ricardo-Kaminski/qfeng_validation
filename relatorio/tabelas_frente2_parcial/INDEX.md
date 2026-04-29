# Índice de Tabelas — Experimento Adversarial CLT (B1-B4)

Gerado automaticamente por `build_tables_b1_b4.py`. α Bonferroni (M=8) = 0.00625.

| ID | Arquivo MD | Arquivo TeX | Conteúdo |
|----|-----------|-------------|---------|
| T1 | [T1_cardinalidade.md](T1_cardinalidade.md) | [T1_cardinalidade.tex](T1_cardinalidade.tex) | Cardinalidade 4×4×50×3 do experimento |
| T2 | [T2_latencia.md](T2_latencia.md) | [T2_latencia.tex](T2_latencia.tex) | Latência mediana ± IQR por (braço, modelo) |
| T3 | [T3_sovereign_active.md](T3_sovereign_active.md) | [T3_sovereign_active.tex](T3_sovereign_active.tex) | Distribuição n_sovereign_active por braço (proxy satisfiability) |
| T4 | [T4_h1_mcnemar.md](T4_h1_mcnemar.md) | [T4_h1_mcnemar.tex](T4_h1_mcnemar.tex) | H1 — McNemar B3 vs B1: taxa de alucinação (global + breakdown por modelo) |
| T5 | [T5_h2_wilcoxon.md](T5_h2_wilcoxon.md) | [T5_h2_wilcoxon.tex](T5_h2_wilcoxon.tex) | H2 — Wilcoxon não-inferioridade de cobertura B3 vs B1 |
| T6 | [T6_h4_b2_vs_b1.md](T6_h4_b2_vs_b1.md) | [T6_h4_b2_vs_b1.tex](T6_h4_b2_vs_b1.tex) | H4 — B2 vs B1: alucinação (McNemar) e cobertura (Wilcoxon) |
| T7 | [T7_h5_variabilidade.md](T7_h5_variabilidade.md) | [T7_h5_variabilidade.tex](T7_h5_variabilidade.tex) | H5 — Levene + Bootstrap overlap (variabilidade intra-grupo) |
| T8 | [T8_h6_anova_friccao.md](T8_h6_anova_friccao.md) | [T8_h6_anova_friccao.tex](T8_h6_anova_friccao.tex) | H6 — ANOVA two-way fricção × braço (F-stats + taxas) |

## Notas Metodológicas

- **α Bonferroni**: 0,00625 (M=8 hipóteses; * indica p < α)
- **p-values**: notação científica (`p = x.xxxe-xx`)
- **Parquet**: `results_b1_b4_derivado.parquet` (2.400 linhas, 38 colunas)
- **Tabelas geradas**: MD + LaTeX (booktabs). DOCX omitido (python-docx não requerido).
- **`clingo_satisfiability`**: string vazia em todos os braços — T3 usa `n_sovereign_active` como proxy.
