# B5.7.4 — Dedup Retroativo do Parquet

**Timestamp UTC-3:** 2026-04-29 09:54:08

- Pré-dedup: 3436 linhas
- Pós-dedup: 2400 linhas
- Duplicatas removidas: 1036
- SHAs únicos: 2400
- SHA256 parquet pós-dedup: `79d051f119197dcfad69c314dadd6373...`
- Política: `keep='last'` por sha256 (alinhada ao upsert B5.7.3)

## Cardinalidade pós-dedup

| Braço | Modelo | n |
|---|---|---|
| B1 | gemma3:12b | 150 |
| B1 | llama3.1:8b | 150 |
| B1 | phi4:14b | 150 |
| B1 | qwen3:14b | 150 |
| B2 | gemma3:12b | 150 |
| B2 | llama3.1:8b | 150 |
| B2 | phi4:14b | 150 |
| B2 | qwen3:14b | 150 |
| B3 | gemma3:12b | 150 |
| B3 | llama3.1:8b | 150 |
| B3 | phi4:14b | 150 |
| B3 | qwen3:14b | 150 |
| B4 | gemma3:12b | 150 |
| B4 | llama3.1:8b | 150 |
| B4 | phi4:14b | 150 |
| B4 | qwen3:14b | 150 |

## Invariantes verificados

- sha256 único em todo o parquet ✓
- status='ok' em todas as linhas ✓
- B1=600, B2=600, B3=600 ✓
- B4=600 (dentro de 597-600) ✓
- B5=0 (não iniciado) ✓
- Q-FENG colunas None para B1-B4 ✓

**Status: B5.7.4 PASSED**