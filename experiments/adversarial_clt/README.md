# Frente 2 — Adversarial CLT

Experimento controlado: 4 braços × 4 modelos × 50 cenários × 3 runs = **2.400 chamadas LLM**.

## Objetivo

Demonstrar empiricamente que a camada simbólica Q-FENG (Clingo + ψ_S) bloqueia alucinações
que LLMs sem ancoragem normativa produzem em cenários CLT adversariais, de forma independente
da arquitetura do modelo.

## Estrutura

```
experiments/adversarial_clt/
├── prompts/            # Templates YAML por braço (B1-B4)
├── scenarios/          # 50 cenários + gabarito ground truth
├── runners/            # Orquestração (run_arm, run_full_experiment, retry_failed)
├── evaluators/         # Avaliadores determinísticos D1 (alucinação) e D2 (cobertura)
├── results/
│   ├── raw_responses/  # SHA256-named JSON por chamada
│   ├── results.parquet # Tabela master 2400 linhas
│   └── manifest.json   # SHA256 de cada artefato + status de completude
├── analysis/           # Scripts estatísticos (McNemar, Wilcoxon, ANOVA)
└── relatorio/          # RELATORIO_FRENTE2_FINAL.md
```

## Como executar

```bash
# Rodar experimento completo (resumível via manifest)
C:/Users/ricar/miniconda3/envs/qfeng/python.exe -m experiments.adversarial_clt.runners.run_full_experiment

# Retentar falhas
C:/Users/ricar/miniconda3/envs/qfeng/python.exe -m experiments.adversarial_clt.runners.retry_failed

# Validar cenários contra Clingo
C:/Users/ricar/miniconda3/envs/qfeng/python.exe -m experiments.adversarial_clt.runners.validate_scenarios

# Avaliar responses (D1 + D2)
C:/Users/ricar/miniconda3/envs/qfeng/python.exe -m experiments.adversarial_clt.evaluators.eval_d1_alucinacao
C:/Users/ricar/miniconda3/envs/qfeng/python.exe -m experiments.adversarial_clt.evaluators.eval_d2_cobertura
```

## Reprodutibilidade

Cada chamada LLM é identificada por SHA256(prompt_completo + modelo + seed).
O arquivo `results/manifest.json` registra status de cada job — permite retomada exata
após interrupção sem re-executar chamadas já concluídas.

## Modelos (Ollama local, RTX 3060 12GB)

| ID  | Modelo        | Família  | Tamanho |
|-----|---------------|----------|---------|
| M1  | qwen3:14b     | Qwen     | 9.3 GB  |
| M2  | phi4:14b      | Phi      | 9.1 GB  |
| M3  | gemma3:12b    | Gemma    | ~9 GB   |
| M4  | llama3.1:8b   | Llama    | ~4.7 GB |

## Braços

| ID | Braço             | Ancoragem simbólica |
|----|-------------------|---------------------|
| B1 | LLM bruto         | Nenhuma             |
| B2 | RAG baseline      | Texto normativo     |
| B3 | dPASP-style       | Predicados textuais |
| B4 | Q-FENG completo   | Clingo SAT/UNSAT + ψ_S |
