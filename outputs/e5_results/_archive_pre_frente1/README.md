# Archive: E5 outputs pré-Frente 1

**Snapshot:** 27/abr/2026 — antes da migração para pipeline semanal Fase 2.1.5-bis.

**Runner antigo:** `manaus_sih_loader.py` (mensal, 12 linhas)
**Loader antigo:** `load_manaus_real_series()` — SIH/DATASUS + FVS-AM interpolado

## Conteúdo

| Arquivo | Shape | Granularidade | Fonte TOH |
|---------|-------|---------------|-----------|
| `theta_efetivo_manaus.parquet` | 12×19 | Mensal (jul/2020–jun/2021) | FVS-AM interpolado |
| `manaus_bootstrap_ci.parquet` | 12×9 | Mensal | σ=0.05/0.10 por data_source |
| `validation_results.parquet` | 6×28 | Por cenário | — |
| `psi_sensitivity.parquet` | 6×9 | Por cenário | — |
| `threshold_robustness.parquet` | 6×35×5 | Por cenário | — |
| `llm_comparison.parquet` | 1×10 | Stub (C4 skipped) | — |

## Por que este snapshot existe

A Frente 1 migra o consumer do runner de `manaus_sih_loader.py` (mensal, 12 SIH competências)
para `manaus_bi_loader.py` (semanal, 73 SEs DEMAS-VEPI+SRAG SIVEP).
Os outputs pré-migração são preservados aqui para comparação metodológica e auditoria.

## Diferenças esperadas pós-Frente 1

- `theta_efetivo_manaus.parquet`: 73 linhas semanais vs. 12 mensais
- `hospital_occupancy_pct`: agora em % real (pico=211%) vs. estimado (pico=100%)
- `delta_pressao`/`delta_theta`: SE-a-SE em vez de mês-a-mês
- Bootstrap σ: 0.05 uniforme em vez de 0.05/0.10 por data_source
