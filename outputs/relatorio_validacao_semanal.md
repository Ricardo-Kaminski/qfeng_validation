# Relatorio Validacao Cruzada Bivariada Semanal

**Branch:** caminho2  
**Data:** 2026-04-26  
**Granularidade:** Semana Epidemiologica (SE)  

## 1. Dataset

- Semanas: 73 (SE 10/2020 - SE 30/2021)
- TOH: interpolado FVS-AM mensal (is_estimated=True para todas SEs)
- SRAG: SIVEP-Gripe INFLUD20/21, CO_MUN_RES=130260, is_stub=False
- n_covid total: 21212
- n_obitos total: 10110

## 2. Correlacao de Spearman (TOH x SRAG)

| Indicador | rho | p-valor | Significativo |
|-----------|-----|---------|---------------|
| Casos COVID | +0.4720 | 0.0000 | Sim * |
| Obitos SRAG | +0.3929 | 0.0006 | Sim * |
| Taxa crescimento COVID (%) | -0.0932 | 0.4330 | Nao |

## 3. Analise de Lag (semanas de atraso TOH -> n_covid)

| Lag | rho | p-valor |
|-----|-----|---------|
| 0 sem | +0.4720 | 0.0000 |
| 1 sem | +0.4546 | 0.0001 |
| 2 sem | +0.4339 | 0.0002 |
| 3 sem | +0.4080 | 0.0005 |
| 4 sem | +0.3577 | 0.0026 |

## 4. PCA Bivariado

- PC1 variancia explicada: 70.2%
- PC1 loading TOH: +0.7071
- PC1 loading SRAG: +0.7071
- Pesos PCA-derivados: TOH=0.5000 / SRAG=0.5000

## 5. Decisao de Pesos

- Metodo: `pca_validated`
- Pesos finais: TOH=0.5 / SRAG=0.5
- Pendente: False
- Nota: PCA confirma pesos proximos ao apriori 50/50. Diferenca max=0.0000 < 0.10.

## 6. Interpretacao Epidemiologica

### Primeira onda (SE 10-28/2020)
TOH fixo em 30% (FVS-AM nao registrou sistematicamente antes de jul/2020).
SRAG mostra pico massivo em SE 15-17/2020 (876-1031 casos/semana).
Correlacao nulo neste periodo - esperado, limitacao de cobertura TOH.

### Segunda onda (SE 49/2020 - SE 10/2021)
Ambas variaveis crescem em paralelo: TOH 84% -> 104%, SRAG 284 -> 1607/semana.
Pico sincronizado SE 3/2021: TOH=103.7%, n_covid=1.447.
Correlacao estrutural esperada para predictor C2.