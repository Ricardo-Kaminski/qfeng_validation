# Manaus BI Bivariado — Provenance Manifest

**Projeto:** Q-FENG Caminho 2 — BI multi-fonte  
**Período:** SE 10/2020 – SE 30/2021 (73 Semanas Epidemiológicas)  
**Branch:** caminho2 | **Última atualização:** Fase 2.1.5 (26/abr/2026)

---

## Estrutura de diretórios

```
manaus_bi/
├── derived/                              ← parquets ativos (granularidade SE)
│   ├── toh_semanal_manaus.parquet        (73 SEs, is_estimated=True, FVS-AM interp.)
│   └── srag_semanal_manaus.parquet       (73 SEs, is_stub=False, SIVEP-Gripe)
├── raw/
│   ├── srag_manaus_sivep/               (INFLUD20/21 brutos — 2,9 GB, gitignored)
│   │   ├── INFLUD20-23-03-2026.csv
│   │   └── INFLUD21-23-03-2026.csv
│   └── boletins_fvs_am/                 (boletins PDF/referências FVS-AM)
├── _archived/                           ← parquets Fase 1 (granularidade mensal)
│   ├── README_archived.md
│   ├── toh_fvs_am_fase1/
│   │   ├── toh_uti_manaus_mensal.parquet (12 meses)
│   │   └── _TOH_FVS_AM_dict_snapshot.json
│   └── srag_stub_fase1/
│       └── srag_manaus_stub.parquet     (STUB — is_stub=True, n_covid=0)
├── oxigenio_unavailable.json            (Caminho C — sem dado retrospectivo)
└── README.md                            (este arquivo)
```

---

## Dimensões ativas (derived/)

| Dimensão | Arquivo | Granularidade | Status | Fonte |
|----------|---------|---------------|--------|-------|
| TOH UTI | `derived/toh_semanal_manaus.parquet` | Semanal (SE) | ✅ 73 SEs | FVS-AM/SES-AM interpolado |
| SRAG | `derived/srag_semanal_manaus.parquet` | Semanal (SE) | ✅ is_stub=False | SIVEP-Gripe INFLUD20/21 |
| O₂ supply | `oxigenio_unavailable.json` | — | Caminho C | — |

---

## TOH UTI Semanal (`derived/toh_semanal_manaus.parquet`)

**Origem:** Interpolação linear dos 12 meses FVS-AM/SES-AM → 73 SEs  
**Script:** `scripts/extract_toh_semanal_interpolado.py`  
**Diagnóstico API:** `outputs/api_demas_vepi_probe.json`

Schema: `year, week_se, date_se_monday, toh_uti_pct, is_estimated, method, source`

| Campo | Descrição |
|-------|-----------|
| `year` | Ano epidemiológico |
| `week_se` | Semana Epidemiológica (1-52) |
| `date_se_monday` | Data da segunda-feira da SE |
| `toh_uti_pct` | Taxa de Ocupação Hospitalar UTI COVID (%) |
| `is_estimated` | True (todos — interpolação, não medição direta) |
| `method` | `interpolacao_linear_fvs_am` |

**Sanity check:** Pico SE 3/2021 = 103.7% (FVS-AM boletim: 104%). ✓  
**Limitação:** SEs 10-28/2020 (mar-jun/2020) fixas em 30% — FVS-AM não sistemático antes de jul/2020.

**API DEMAS-VEPI descartada:** `ocupacaohospitalaruti`=null em todos os registros de Manaus. Sem campo de capacidade total UTI → TOH% inviável via API.

---

## SRAG Semanal (`derived/srag_semanal_manaus.parquet`)

**Origem:** SIVEP-Gripe INFLUD20 e INFLUD21 (CO_MUN_RES=130260)  
**Script:** `scripts/extract_srag_semanal_manaus.py`  
**Manifest (SHA256):** `outputs/source_manifest_srag.json`

Schema: `year, week_se, n_srag_total, n_covid, n_outros, n_sem_class, n_obitos, n_obitos_covid, letalidade_pct, source, is_stub`

**Estatísticas:**
- Total SEs: 73 (SE 10/2020 – SE 30/2021)
- n_covid total: **21.212**
- n_obitos total: **10.110**
- Pico: SE 3/2021 (1.447 casos COVID, 778 óbitos) — colapso documentado
- `is_stub`: **False** em todas as SEs

---

## Validação cruzada bivariada (Fase 2.1.5 Tarefa 2.C)

| Métrica | Valor | Status |
|---------|-------|--------|
| Spearman ρ(TOH, n_covid) | +0.472 (p<0.001) | ✓ significativo |
| PCA PC1 variância | 70.2% | ✓ critério ≥70% |
| Pesos PCA | TOH=50% / SRAG=50% | ✓ pca_validated |
| Delta vs apriori 50/50 | 0.0000 | ✓ perfeita confirmação |

**Decisão:** `pca_validated` — pesos 50/50 confirmados empiricamente.  
**JSON:** `outputs/bi_dimensional_decision_semanal.json`

---

## Decisão O₂ — Caminho C

Sem dado retrospectivo canônico viável para O₂ Manaus 2020-2021.  
BI permanece **bivariado** (TOH + SRAG). O₂ entra como limitação prospectiva no §7.4.

---

## Parquets arquivados (_archived/)

Ver `_archived/README_archived.md` para detalhes.

| Arquivo | Motivo do arquivo |
|---------|-------------------|
| `toh_uti_manaus_mensal.parquet` | Granularidade mensal substituída por semanal |
| `srag_manaus_stub.parquet` | STUB substituído por dados reais |

NÃO deletar — mantidos para auditoria forense e reprodutibilidade.
