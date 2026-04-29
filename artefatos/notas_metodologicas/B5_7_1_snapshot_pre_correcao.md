# B5.7.1 — Snapshot Pré-Correção

**Timestamp UTC-3:** 2026-04-29 09:54:08
**Branch:** caminho2

## Estado de B4 na conclusão

- B4 completed: 600
- B4 failed: 0
- Total processado: 600/600
- Última chave B4: `B4__qwen3:14b__T-CTRL-NEG-005__run3`

## Cardinalidade raw_responses

| Braço:Status | Count |
|---|---|
| B1:ok | 600 |
| B2:ok | 600 |
| B3:ok | 600 |
| B4:ok | 600 |

## Cardinalidade parquet (pré-dedup)

| Braço | Linhas |
|---|---|
| B1 | 1276 |
| B2 | 960 |
| B3 | 600 |
| B4 | 600 |

- **Total parquet:** 3436
- **SHAs únicos:** 2400
- **Duplicatas:** 1036

## Chaves `failed` no manifest

- `B3__phi4:14b__T-CTRL-NEG-004__run1`
- `B3__gemma3:12b__T-CLT-04-008__run3`

## SHAs dos arquivos do snapshot

```
273de88fba213b7dbea9f797f54e947cfe0e7b234c420fbc61ce9c51ce7d1206  manifest_pre_B5_7.json
6847704558a2731220a4bfe95f8de062b1ac0426393c5b7dfddeca70bb16925b  results_pre_B5_7.parquet
349cf3542db3119d192ebf88825e8e836e08c428badfa3bb310990bc27113e33  run_log_pre_B5_7.txt
965f770f082af71951079e60b6adb0d41ad232a7ebf9fb05deae6363a5273559  runner_log_pre_B5_7.txt
```

**Status: B5.7.1 PASSED**