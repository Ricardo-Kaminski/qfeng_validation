# Arquivo pré-Opção 2 — Snapshot Frente 1 (n=74 SEs)

**Data do snapshot:** 27/abr/2026  
**Operação:** Backup antes da operação retroativa Opção 2 (truncar série em SE 14/2020)

## Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| `theta_efetivo_manaus.parquet` | 74 linhas (SE 10/2020 – SE 30/2021) |
| `manaus_bootstrap_ci.parquet` | CI bootstrap sobre 74 SEs |
| `validation_results.parquet` | Resultados de validação E5 (74 SEs) |
| `psi_sensitivity.parquet` | Sensibilidade ψ (74 SEs) |
| `threshold_robustness.parquet` | Robustez de threshold (74 SEs) |
| `llm_comparison.parquet` | Comparação LLM (74 SEs) |
| `frente1_delta_se_antecipacao.json` | delta_se_hitl=46, first_hitl=202010 |
| `frente1_analise_descritiva.md` | Análise descritiva (n=74) |
| `frente1_theta_t_serie_semanal.png` | Figura série θ_t (74 SEs) |
| `frente1_sensibilidade_thresholds.png` | Heatmap sensibilidade (74 SEs) |

## Métricas pré-Opção 2

- **n SEs:** 74 (SE 10/2020 – SE 30/2021)
- **SEs com TOH=0:** 4 (202010, 202011, 202012, 202013) — consolidação tardia DEMAS-VEPI
- **θ_efetivo SEs zeradas:** 115,27° (valor de inicialização, HITL)
- **ΔSE_HITL:** 46 SEs
- **ΔSE_CB_estável:** 19 SEs
- **Primeira CB:** SE 37/2020 (202037) — não afetada pelo truncamento
- **Regimes:** HITL=48, CB=26

## Versão pós-Opção 2 (canônica)

- **n SEs:** 70 (SE 14/2020 – SE 30/2021)
- **ΔSE_HITL:** 42 SEs
- **ΔSE_CB_estável:** 19 SEs (preservado)
- Parquets canônicos em `outputs/e5_results/`

## Reprodutibilidade Zenodo

Este diretório deve ser preservado integralmente para reprodutibilidade.  
Não confundir com `_archive_pre_frente1/` (backup do pipeline mensal pré-Frente 1).
