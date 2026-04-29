# B5.7.3 — Smoke Test: Upsert por sha256 em `_append_to_parquet`

**Data:** 29/abr/2026  
**Branch:** `caminho2`  
**Arquivo patcheado:** `experiments/adversarial_clt/runners/run_full_experiment.py`

## Patch aplicado

Substituição da lógica de append cego por upsert determinístico por `sha256`:

```python
# ANTES (append cego — bug)
if RESULTS_PARQUET.exists():
    existing = pd.read_parquet(RESULTS_PARQUET)
    combined = pd.concat([existing, row], ignore_index=True)

# DEPOIS (upsert por sha256 — idempotente)
if RESULTS_PARQUET.exists():
    existing = pd.read_parquet(RESULTS_PARQUET)
    existing = existing[existing["sha256"] != record["sha256"]]  # remove duplicata
    combined = pd.concat([existing, row], ignore_index=True)
```

## Resultado do smoke test

```
=== Smoke test upsert _append_to_parquet ===

  PASS: 1 linha após 1ª inserção
  PASS: sha256 correto na linha 1
  PASS: Ainda 1 linha após upsert com mesmo sha256
  PASS: latency_ms atualizado para 9999
  PASS: 2 linhas após inserção de sha256 distinto
  PASS: 2 SHAs únicos no parquet
  PASS: 3 linhas após 3ª inserção
  PASS: Ainda 3 linhas após re-upsert de bbb222
  PASS: bbb222 atualizado para 8888
  PASS: sha256 único em todas as linhas
  PASS: status='ok' em todas as linhas
  PASS: qfeng_theta_deg None para todos os registros de teste

=== Resultado: 12 PASSED, 0 FAILED ===
```

## Verificação de código

```python
import inspect
from experiments.adversarial_clt.runners.run_full_experiment import _append_to_parquet
src = inspect.getsource(_append_to_parquet)
assert 'existing["sha256"] != record["sha256"]' in src  # PASS
assert "pd.concat" in src  # PASS
assert "to_parquet" in src  # PASS
```

## Status

**B5.7.3: PASSED** — upsert ativo, idempotência confirmada. Pronto para B5.7.4 (dedup retroativo, aguarda B4 concluir).
