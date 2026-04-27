# Análise Descritiva Frente 1 — Q-FENG Semanal Manaus 2020-2021

**Tarefa:** F1.3 | **Branch:** caminho2 | **Data:** 2026-04-27

---

## 1. Contextualização

Esta análise documenta a capacidade de antecipação do framework Q-FENG
aplicado à crise hospitalar de Manaus (2020-2021), usando série semanal de
70 SEs ativas (SE 14/2020 – SE 30/2021, Opção 2) derivada dos microdados primários DEMAS-VEPI
(TOH denominador CNES-LT estrito) após a refundação Fase 2.1.5-bis.

**SE de colapso canônica:** SE 03/2021 (18-24/jan/2021) — decreto AM 43.269/2021
(calamidade pública; oxigênio esgotado, transferências interestadurais emergenciais).

**Nota de granularidade:** `delta_pressao` e `delta_theta` operam em escala SE-a-SE
(granularidade semanal), distinta do pipeline mensal original. Variações de ±Δ por SE
correspondem a ~4× maior magnitude mensal aparente — comparações com pipeline anterior
devem especificar a distinção.

---

## 2. Distribuição de Regimes de Interferência

| Regime | SEs | % |
|--------|-----|---|
| CIRCUIT_BREAKER | 26 | 37.1% |
| HITL | 44 | 62.9% |
| STAC | 0 | 0% |

**Thresholds primários:** CB ≥ 120.0°, HITL ≥ 60.0°

O Q-FENG opera inteiramente em regime HITL ou CIRCUIT_BREAKER durante as 70 SEs ativas,
confirmando que a janela 2020-2021 representa um episódio de pressão sistêmica contínua
sem retorno ao regime de operação normal (STAC). A concentração de regime CB em ondas
(ver §4) é coerente com a dinâmica de colapso-recuperação parcial-recolapso documentada
clinicamente para Manaus.

---

## 3. Métricas de Antecipação (Gate Criterion)

| Métrica | Valor | Interpretação |
|---------|-------|---------------|
| ΔSE_HITL | 42 SEs | SEs entre primeiro HITL e colapso (202014) |
| ΔSE_CB | 19 SEs | SEs entre primeiro CB e colapso (202037) |
| ΔSE_CB_estável | 19 SEs | SEs entre CB estável (≥3 consec.) e colapso (202037) |

**Gate criterion (ΔSE_CB_estável > 4 semanas):** **✓ APROVADO**

O sistema Q-FENG detectou regime CIRCUIT_BREAKER sustentado (≥3 SEs consecutivas)
com **19 semanas de antecipação** em relação ao colapso público documentado
(decreto AM 43.269/2021). Este resultado confirma a hipótese central do Paper 1:
a arquitetura Q-FENG captura a deterioração sistêmica antes da manifestação visível
ao sistema regulatório formal.

---

## 4. Ondas CB (Circuit Breaker)

| Onda | Início | Fim | Duração |
|------|--------|-----|---------|
| 1 | 202037 | 202044 | 8 SEs |
| 2 | 202101 | 202118 | 18 SEs |

**Interpretação:** O padrão de ondas reflete a dinâmica epidemiológica documentada —
onda 1 (set-out/2020) corresponde à segunda onda da pandemia com esgotamento progressivo;
onda 2 (jan-maio/2021) cobre o colapso catastrófico e a fase de recuperação lenta.
A CB% resultante (37.1%) concentra-se temporalmente em ondas,
não distribuída uniformemente — distinção metodológica relevante para o argumento do paper.

---

## 5. Correlações Descritivas

| Par | ρ Spearman | p-valor |
|-----|-----------|---------|
| TOH × θ_efetivo | 0.3262 | 0.005858 |
| score_pressao × θ_efetivo | 0.9375 | 0.0 |
| óbitos × θ_efetivo | 0.4168 | 0.000331 |

---

## 6. Fricção Ontológica — 4 Camadas (SE 03/2021)

| Camada | Tipo | Estimativa (leitos) |
|--------|------|---------------------|
| 1 | Operacional — enfermaria operando como UTI | ~85 |
| 2 | Administrativa — habilitação MS com cadastro defasado | ~208 |
| 3 | Categorial — LSVP criada (Portaria SAES/MS 510/2020) | 0 (criada, não adotada) |
| 4 | Institucional — LSVP não adotada em 23/24 meses Manaus | 0 |
| **Total reconstituído** | | **≈293 leitos acima do CNES** |

**Denominador CNES jan/2021:** 319 leitos UTI
**Denominador FVS-AM jan/2021:** 612 leitos UTI (103,69% de ocupação reconhecida pelo estado)
**TOH Q-FENG (CNES estrito):** 211,5% — metodologicamente correto como sintoma estrutural da Fricção Ontológica

22/26 SEs em CB têm TOH>100%, confirmando que o regime CB capta especificamente as semanas de colapso sistêmico documentado pelas fontes primárias (DEMAS-VEPI + FVS-AM).

---

## 7. Análise de Sensibilidade (Resumo)

15/25 configurações de threshold (60.0%) aprovam o gate criterion (ΔSE_CB_estável > 4 semanas).

| CB threshold | HITL threshold | N_CB_SEs | ΔSE_CB | ΔSE_CB_estável | Gate |
|---|---|---|---|---|---|
| 110.0° | 45.0° | 67 | 42 | 42 | ✓ |
| 110.0° | 52.5° | 67 | 42 | 42 | ✓ |
| 110.0° | 60.0° | 67 | 42 | 42 | ✓ |
| 110.0° | 67.5° | 67 | 42 | 42 | ✓ |
| 110.0° | 75.0° | 67 | 42 | 42 | ✓ |
| 115.0° | 45.0° | 58 | 42 | 42 | ✓ |
| 115.0° | 52.5° | 58 | 42 | 42 | ✓ |
| 115.0° | 60.0° | 58 | 42 | 42 | ✓ |
| 115.0° | 67.5° | 58 | 42 | 42 | ✓ |
| 115.0° | 75.0° | 58 | 42 | 42 | ✓ |
| 120.0° | 45.0° | 26 | 19 | 19 | ✓ |
| 120.0° | 52.5° | 26 | 19 | 19 | ✓ |
| 120.0° | 60.0° | 26 | 19 | 19 | ✓ |
| 120.0° | 67.5° | 26 | 19 | 19 | ✓ |
| 120.0° | 75.0° | 26 | 19 | 19 | ✓ |
| 125.0° | 45.0° | 12 | 17 | — | ✗ |
| 125.0° | 52.5° | 12 | 17 | — | ✗ |
| 125.0° | 60.0° | 12 | 17 | — | ✗ |
| 125.0° | 67.5° | 12 | 17 | — | ✗ |
| 125.0° | 75.0° | 12 | 17 | — | ✗ |
| 130.0° | 45.0° | 5 | — | — | ✗ |
| 130.0° | 52.5° | 5 | — | — | ✗ |
| 130.0° | 60.0° | 5 | — | — | ✗ |
| 130.0° | 67.5° | 5 | — | — | ✗ |
| 130.0° | 75.0° | 5 | — | — | ✗ |

Ver figura `frente1_sensibilidade_thresholds.png` para visualização matricial.

---

## 8. Limitações e Notas Metodológicas

1. **Granularidade SE-a-SE:** delta_pressao/delta_theta refletem variação semanal.
   Narrativa nos §6.3-6.4 do paper deve especificar explicitamente.
2. **CB% = 37.1% ≠ 50% do benchmark mensal:** A concentração em ondas,
   não a CB média, é o fenômeno relevante. ΔSE_CB_estável = 19 semanas é o
   resultado que sustenta o argumento de antecipação.
3. **TOH denominador CNES:** Decisão epistemológica deliberada — manter CNES estrito
   expõe a Fricção Ontológica em vez de mascará-la via denominador "corrigido".
4. **sigma=0.05 uniforme:** Todas as 70 SEs ativas são fontes primárias; distinção anterior
   (0.05/0.10 por "literature months") eliminada — documentada como contrato Zenodo v2026.04.

---

*Gerado por `scripts/analise_frente1.py` | Frente 1 Tarefa F1.3 | Branch caminho2*
