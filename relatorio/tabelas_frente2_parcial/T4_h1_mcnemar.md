# T4 — H1: McNemar B3 vs B1 (Taxa de Alucinação)

## Resultado Global

| Escopo | N pares | Taxa B1 | Taxa B3 | Redução (pp) | OR discordância | Estatística McNemar | p (unicaudal) | Sig.? |
| ------ | ------- | ------- | ------- | ------------ | --------------- | ------------------- | ------------- | ----- |
| Global | 600 | 19.8% | 3.8% | 16.0 pp | 9.727 | 11.0 | 3.202e-21 * | Sim * |

## Breakdown por Modelo

| Modelo | N pares | Taxa B1 | Taxa B3 | OR discordância | p (unicaudal) | Sig.? |
| ------ | ------- | ------- | ------- | --------------- | ------------- | ----- |
| gemma3:12b | 150 | 11.3% | 0.0% | ∞ | 7.629e-06 * | Sim * |
| llama3.1:8b | 150 | 29.3% | 10.7% | 5.000 | 7.549e-06 * | Sim * |
| phi4:14b | 150 | 32.0% | 4.7% | 11.250 | 4.113e-10 * | Sim * |
| qwen3:14b | 150 | 6.7% | 0.0% | ∞ | 9.766e-04 * | Sim * |

**Nota:** α Bonferroni = 0.00625. * = significativo. OR discordância = n_10 / n_01. ∞ indica n_01 = 0 (sem reversão B3→B1).

**Interpretação:** B3 reduz alucinação em 16.0 pp (de 19.8% para 3.8%). McNemar exato: p_unicaudal = 3.202e-21 (significativo a α corrigido = 0,00625). OR discordância = 9.73.
