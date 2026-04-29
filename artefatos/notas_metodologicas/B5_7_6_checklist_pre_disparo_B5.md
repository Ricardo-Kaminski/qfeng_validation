# B5.7.6 — Checklist Pré-Disparo B5

**Timestamp UTC-3:** 2026-04-29 09:55:08
**ETA B5:** ~5.1h (mediana B4=27.9s/chamada + 10% overhead θ)

## Checklist

| # | Item | Status | Detalhe |
|---|---|---|---|
| 1a | B1=600 no parquet | PASSED | B1=600 |
| 1b | B2=600 no parquet | PASSED | B2=600 |
| 1c | B3=600 no parquet | PASSED | B3=600 |
| 1d | B4 dentro de 597-600 | PASSED | B4=600 |
| 1e | B5=0 (não iniciado) | PASSED | B5=0 |
| 2a | Manifest B1=600 completed | PASSED | m_b1=600 |
| 2b | Manifest B2=600 completed | PASSED | m_b2=600 |
| 2c | Manifest B3=600 completed | PASSED | m_b3=600 |
| 2d | Sem failed em B1/B2/B3 | PASSED | failed: B1=0 B2=0 B3=0 |
| 3 | Upsert ativo em _append_to_parquet | PASSED |  |
| 4 | sha256 único no parquet | PASSED | duplicatas=0 |
| 5 | Smoke test B5 motor θ (3 cenários) | PASSED | T-CLT-01 BLOCK, T-CLT-03/04 STAC |
| 6a | Ollama disponível | PASSED |  |
| 6b | 4 modelos presentes | PASSED | todos presentes |
| 7 | GPU livre (>1500MB) | PASSED | usado=1845MB total=12288MB livre=10443MB |

## STATUS PRE-DISPARO B5: GO

Todos os itens PASSED. Executar B5.8 via:
```
cd /d C:\Workspace\academico\qfeng_validacao
C:/Users/ricar/miniconda3/envs/qfeng/python.exe -m experiments.adversarial_clt.runners.run_full_experiment
```