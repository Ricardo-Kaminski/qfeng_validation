# F1.1 — Migração runner.py para loader semanal (Fase 2.1.5-bis)

**Data:** 27/abr/2026 | **Branch:** caminho2 | **Tarefa:** Frente 1, Sub-tarefas F1.1.a–c

## Mudanças aplicadas

### runner.py
| Antes | Depois |
|-------|--------|
| `from .manaus_sih_loader import load_manaus_real_series` | `from .manaus_bi_loader import load_manaus_bi_series, load_sih_with_fixed_tmort` |
| Import interno `_psi_n_from_score` de `manaus_sih_loader` | Import de `manaus_bi_loader` |
| `σ = 0.05 if data_source == "sih_datasus" else 0.10` | `σ = 0.05` uniforme |
| `run_theta_efetivo_manaus()`: 12 linhas mensais | 74 linhas semanais |
| Campos: `ano_cmpt`, `mes_cmpt`, `internacoes_total`, `obitos_total` | `year`, `week_se`, `month_sih`, `internacoes`, `obitos`, `toh_is_estimated`, `srag_n_covid`, `srag_is_stub` |
| `delta_pressao`/`delta_theta`: mês-a-mês | **SE-a-SE** (ver nota abaixo) |

### manaus_bi_loader.py
| Bug | Correção |
|-----|----------|
| `_load_toh()` indexava `["year","week_se"]` mas parquet usa `year_se`/`sem_epi` | Adicionado `rename(year_se→year, sem_epi→week_se)` antes do set_index |
| `hospital_occupancy_pct = int(round(toh_uti_pct))` — sem ×100 | `int(round(toh_uti_pct * 100))` — exporta em % (0–211.5) |
| `toh_row["is_estimated"]` — campo inexistente no parquet | `toh_row["is_imputed"]` |
| `_PSI_N_BASE = [0.7, 0.2, 0.1]` / `_PSI_N_CRISIS = [0.1, 0.3, 0.6]` — vetores invertidos | `[0.50, 0.30, 0.20]` / `[0.93, 0.04, 0.03]` — idênticos ao manaus_sih_loader |
| `SE_WINDOW` usava `range(10, 53)` — perdia SE 53/2020 | `range(10, 54)` — 74 SEs alinhado com parquet |

### Correção crítica: vetores psi_N
O bi_loader foi inicializado com vetores psi_N incorretos que **invertiam o comportamento de θ**:
- Com vetores errados: score=1.0 (crise) → θ=57.89°, score=0 → θ=118.92°
- Com vetores corretos: score=1.0 (crise) → θ=133.07°, score=0 → θ=100.59°

## Nota sobre granularidade delta

`delta_pressao` e `delta_theta` são agora **SE-a-SE** (não mês-a-mês).
- **Implicação narrativa F1.3/F1.4:** variações de ±Δ refletem mudanças semanais.
  Um delta de ±0.05 por SE equivale a ~0.20–0.25 por mês — escala diferente.
- **Documentar no paper (§6.4):** comparações com pipeline mensal antigo devem
  especificar explicitamente a granularidade temporal.

## Unificação σ bootstrap

Justificativa: a distinção anterior σ=0.05/0.10 baseava-se em "literature months" (meses sem
dado SIH real, estimados de literatura). Com DEMAS-VEPI real + SRAG SIVEP, **todas as 74 SEs
provêm de fontes primárias**. A distinção torna-se sem base empírica.
Migração documentada como contrato de reprodutibilidade Zenodo v2026.04.
