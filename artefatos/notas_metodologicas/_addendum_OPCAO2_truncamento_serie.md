# Adendo Metodológico — Opção 2: Truncamento da Série em SE 14/2020

**Data da decisão:** 27/abr/2026  
**Branch:** caminho2  
**Operação:** OP2.1–OP2.8 (retroativa, registro auditável)

---

## 1. Contexto

A auditoria forense de fechamento da Frente 1 (OP2.1) identificou que as quatro primeiras semanas
epidemiológicas da série canônica (SE 10/2020 a SE 13/2020) registravam `hospital_occupancy_pct = 0`
no parquet `theta_efetivo_manaus.parquet`.

**Causa confirmada:** consolidação tardia do registro DEMAS-VEPI. O sistema só passa a registrar
consistentemente ocupação UTI COVID em Manaus a partir de SE 14/2020 (TOH = 48%), o que é
cronologicamente coerente com: (i) o início efetivo da pandemia em Manaus (primeiro caso 13/03/2020);
(ii) o tempo institucional médio de 4–6 semanas de estabilização de campos novos em sistemas DEMAS.

**Valores afetados:**

| Competência | TOH (%) | θ_efetivo (°) | Regime |
|-------------|---------|----------------|--------|
| 202010 | 0 | 115,27 | HITL |
| 202011 | 0 | 115,27 | HITL |
| 202012 | 0 | 115,27 | HITL |
| 202013 | 0 | 115,27 | HITL |

θ_efetivo = 115,27° nessas SEs é o valor de inicialização do cache Markoviano (não medição real).

---

## 2. Opções Consideradas

### Opção 1 — Manter n=74 com nota metodológica
Manter os 4 zeros na série ativa, reportar ΔSE_HITL = 46 com asterisco explicativo.  
**Rejeitada:** ΔSE_HITL artefatual introduz ruído na comparação cross-domínio do Paper 1.

### Opção 2 — Truncar série em SE 14/2020 ✅ **(ADOTADA)**
Excluir SE 10–13/2020 da série ativa. n: 74 → 70. Início canônico: SE 14/2020.  
**Adotada:** elimina o artefato pela raiz; ΔSE_CB_estável (resultado primário) inalterado.

### Opção 3 — Imputar TOH para SE 10–13/2020
Estimar retroativamente TOH por interpolação linear ou valor médio de março/2020.  
**Rejeitada:** introduziria dado fabricado onde há ausência genuína de registro; incompatível com
contrato de rastreabilidade Zenodo.

---

## 3. Impacto sobre Métricas

| Métrica | Pré-Opção 2 (n=74) | Pós-Opção 2 (n=70) | Δ |
|---------|-------------------|-------------------|---|
| n SEs | 74 | 70 | −4 |
| Início série | SE 10/2020 | SE 14/2020 | — |
| ΔSE_HITL | 46 SEs | 42 SEs | −4 |
| ΔSE_CB | 19 SEs | 19 SEs | 0 |
| ΔSE_CB_estável | 19 SEs | 19 SEs | 0 |
| Primeira CB | SE 37/2020 | SE 37/2020 | 0 |
| HITL count | 48 | 44 | −4 |
| CB count | 26 | 26 | 0 |
| Gate (>4w) | ✓ APROVADO | ✓ APROVADO | — |

**Os resultados primários (ΔSE_CB_estável = 19, Gate ✓) são idênticos.** A única métrica
afetada é ΔSE_HITL (−4), que era artefatual no valor pré-Opção 2.

---

## 4. Implementação Técnica

**Código alterado:**
- `src/qfeng/e5_symbolic/manaus_bi_loader.py`: adicionado `SE_INICIO_SERIE_FRENTE1 = 202014`;
  `load_manaus_bi_series()` aplica filtro `y * 100 + w >= SE_INICIO_SERIE_FRENTE1`.
- `tests/test_manaus_bi_loader.py`: contagem 74→70; 3 novos testes de regressão
  (`test_se_inicio_serie_frente1_constant`, `test_serie_starts_at_se14_2020`,
  `test_ses_202010_202013_excluidas`). Resultado: 18/18 passed.

**Parquets regenerados** (27/abr/2026):
- `outputs/e5_results/theta_efetivo_manaus.parquet` — 70 linhas (era 74)
- `outputs/e5_results/manaus_bootstrap_ci.parquet` — 70 linhas
- `outputs/e5_results/validation_results.parquet`
- `outputs/e5_results/psi_sensitivity.parquet`
- `outputs/e5_results/threshold_robustness.parquet`
- `outputs/e5_results/llm_comparison.parquet`

**Backup pré-Opção 2** preservado integralmente em:
`outputs/e5_results/_archive_pre_opcao2/` (commit `8b8506b`)

---

## 5. Reprodutibilidade Zenodo

O backup `_archive_pre_opcao2/` contém os parquets pré-Opção 2 (n=74) e deve ser preservado
para reprodutibilidade histórica. O diretório `outputs/e5_results/` (parquets canônicos, n=70)
representa o estado oficial da série Frente 1 a partir desta data.

Qualquer deposição Zenodo posterior deve incluir ambos os diretórios com este adendo como
documentação da mudança metodológica.

---

## 6. Referências Cruzadas

- `outputs/e5_results/_archive_pre_opcao2/README.md` — snapshot pré-Opção 2
- `artefatos/notas_metodologicas/OP2_1_auditoria_impacto.md` — auditoria forense detalhada
- `src/qfeng/e5_symbolic/manaus_bi_loader.py` — implementação do filtro
- `tests/test_manaus_bi_loader.py` — testes de regressão
