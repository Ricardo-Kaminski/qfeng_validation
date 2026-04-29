# P1.4 — Auditoria Forense: run_arm.py

**Data:** 29/abr/2026
**Arquivo auditado:** `experiments/adversarial_clt/runners/run_arm.py` (313 linhas)
**Contexto:** Auditoria pré-redesenho para documentar falhas arquitetônicas

---

## Falha 1 — Key mismatch: `satisfiability` vs `satisfiable` (linha 291)

```python
# Linha 291 — BUG: key errada
"clingo_satisfiability": clingo_result.get("satisfiability", "") if clingo_result else "",
```

`scenario_loader.run_scenario()` retorna `{"satisfiable": True/False}` (bool).
`run_arm.py` lê `clingo_result.get("satisfiability", "")` — key diferente, sempre retorna `""`.

**Consequência:** `clingo_satisfiability` está vazio em 100% dos registros B3/B4/B5.
Análise B5.9.1 usou `correct_decision` do `scenarios.yaml` como fallback operacional.

**Fix necessário no redesenho:** usar `clingo_result.get("satisfiable", None)` e
armazenar como boolean, não string.

---

## Falha 2 — B3: predicados estáticos do `ground_truth_predicates.json` (linhas 103-108)

```python
if braco == "B3":
    predicate_list = "\n".join(
        f"- {p}" for p in gt.get("violated_predicates", []) + gt.get("compliance_predicates", [])
    )
    return user_tpl.format(scenario_text=scenario_text, predicate_list=predicate_list)
```

`gt` (ground truth) vem de `ground_truth_predicates.json` — predicados estáticos por família
de cenário (âncora), não de execução do solver sobre o caso concreto.

**Consequência:** B3 não executa Clingo; entrega checklist textual de predicados ao LLM.
Mede scaffolding de prompting, não inferência simbólica (ver B3a/README.md).

---

## Falha 3 — B5: motor θ injetado no prompt LLM (linhas 130-193)

```python
if braco == "B5":
    # ... calcula theta e regime ...
    return user_tpl.format(
        scenario_text=scenario_text,
        theta_deg=f"{motor.theta_degrees:.2f}",   # ← VIOLAÇÃO: LLM recebe θ
        regime=regime_str,                          # ← VIOLAÇÃO: LLM recebe regime
        cos_theta=f"{motor.cos_theta:.4f}",         # ← VIOLAÇÃO: LLM recebe cos(θ)
        ...
    )
```

Motor θ (S5 VSM) comunica decisão ao LLM (S1-S2) via prompt. Viola opacidade
hierárquica VSM (Beer, 1979). LLM transcreve θ literalmente na resposta.

**Consequência:** B5 mede fidelidade de transcrição, não fricção ontológica emergente.
Dados B5 integralmente inválidos (ver B5/README.md no arquivo).

---

## Falha 4 — B4: satisfiability e psi_s injetados no prompt (linhas 110-128)

```python
if braco == "B4":
    satisfiability = clingo_result.get("satisfiability", "UNKNOWN")  # ← key mismatch
    ...
    return user_tpl.format(
        ...
        satisfiability=satisfiability,        # ← LLM recebe status Clingo
        psi_s_vector=f"[{psi_s}]",           # ← LLM recebe vetor ψ_s
    )
```

B4 instruía LLM a "apresentar-se como Q-FENG" enquanto recebia output simbólico.
O LLM ventriloqua a decisão, não a executa.

---

## O que ESTÁ correto

- **B1 (linhas 96-98):** apenas `scenario_text` no prompt — correto.
- **B2 (linhas 99-102):** `scenario_text + rag_context` — correto.
- **`interference.py`:** lógica do motor θ (compute_theta, born_rule, CircuitBreaker) é válida.
  O problema não está no motor, está no canal de comunicação (prompt-injection).
- **Arquitetura de pods (P1.6):** encapsulamento por função eliminará o canal de vazamento.

---

## Ações tomadas em P1.4

- B3/B4/B5 prompt templates arquivados em `prompts/_archive_pre_redesenho_29abr2026/`
- raw_responses B3/B4/B5 arquivados em `results/_archive_pre_redesenho_29abr2026/`
- run_arm.py mantido sem modificação (referência histórica)
- Redesenho: ver P1.5 (extrator), P1.6 (pods ZeroMQ), P_FASE3 (implementação real)
