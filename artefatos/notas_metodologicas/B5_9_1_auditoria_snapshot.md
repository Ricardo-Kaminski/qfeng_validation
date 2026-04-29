# B5.9.1 — Auditoria Snapshot e Dataset Derivado B1-B4

**Data:** 29/Wedbr/2026 10:45
**Branch:** `caminho2`

## Snapshot Input

- Arquivo: `results_b1_b4_para_analise_29abr2026.parquet`
- Linhas: 2.400 | SHAs únicos: 2.400
- SHA256: `06e70f2742aeb2d88279c723d3911a47...`

## Dataset Derivado Output

- Arquivo: `results_b1_b4_derivado.parquet`
- Linhas: 2400 | SHA256: `5ff5f918d1ac91bab0ea08c1b996ce04...`
- Colunas adicionadas: `hallucination_flag`, `coverage_score`, `clingo_satisfiable`, `correct_decision`

## Nota Metodológica: clingo_satisfiability

O campo `clingo_satisfiability` está vazio em todos os braços (B1-B4) devido a bug de
mismatch de chave no `run_arm.py`: a função `run_scenario()` retorna `satisfiable` (bool),
mas o código persiste `record["clingo_satisfiability"] = clingo_result.get("satisfiability", "")`.
A satisfiability dos 4 anchors foi re-derivada via re-execução de `run_scenario()`:

| Anchor | Satisfiável | Categoria |
|--------|------------|-----------|
| T-CLT-01 | False (UNSAT) | derivacional |
| T-CLT-02 | False (UNSAT) | procedural |
| T-CLT-03 | True (SAT) | controle_positivo |
| T-CLT-04 | True (SAT) | controle_negativo |

## Definição Operacional Adaptada: hallucination_flag

**Critério:** `hallucination_flag = 1` se `correct_decision='VIOLACAO'` E resposta do LLM
não identifica a violação (sem menção textual a violação, nulidade, irregularidade etc.).

Ground truth source: `scenarios.yaml` campo `correct_decision`.

## Distribuição por Braço

       n_hall rate_hall  n_total
braco                           
B1        119     0.198      600
B2        171     0.285      600
B3         23     0.038      600
B4          4     0.007      600

## Distribuição por (Braço, Modelo)

modelo  gemma3:12b  llama3.1:8b  phi4:14b  qwen3:14b
braco                                               
B1           0.113        0.293     0.320      0.067
B2           0.233        0.373     0.367      0.167
B3           0.000        0.107     0.047      0.000
B4           0.000        0.027     0.000      0.000

## Distribuição coverage_score (média)

braco
B1    1.958
B2    1.648
B3    1.295
B4    1.103

## Distribuição friccao_categoria

friccao_categoria
derivacional         1102
procedural            528
controle_positivo     528
controle_negativo     239
test                    1

## Status

**B5.9.1: PASSED** — dataset derivado pronto para análises H1-H6.
