# P1.4 — Auditoria: interference.py + corpora_clingo

**Data:** 29/abr/2026

---

## interference.py — Auditoria (301 linhas)

**Arquivo:** `src/qfeng/core/interference.py`
**Veredicto:** VÁLIDO — lógica do motor θ correta. Problema está no canal de comunicação.

### Funções auditadas

| Função | Linha | Status | Obs |
|--------|-------|--------|-----|
| `normalize(v)` | 42 | ✅ OK | L2-norm correta |
| `compute_theta(psi_n, psi_s)` | 50 | ✅ OK | arccos(⟨ψ_N\|ψ_S⟩) correto |
| `born_rule(alpha_sq, beta_sq, theta)` | 71 | ✅ OK | P = \|α\|² + \|β\|² + 2\|α\|\|β\|cos(θ) |
| `quantum_penalty(theta)` | 98 | ✅ OK | max(0, -cos(θ)) correto |
| `cybernetic_loss(...)` | 116 | ✅ OK | ℒ_Global = ℒ_Perf + λ_ont·QP + λ_fair·FL |
| `theta_eff(theta_history, ...)` | 145 | ✅ OK | Média ponderada exponencial |
| `CircuitBreakerConfig` | 199 | ✅ OK | θ_STAC=60°, θ_BLOCK=120° |

### Ponto de isolamento para P_FASE4

`interference.py` deve ser chamado APENAS pelo `motor_theta_pod`. O pod recebe
`psi_n` e `psi_s` como arrays JSON — sem `scenario_id`, sem `modelo`, sem
`scenario_text`. Retorna `theta_deg`, `regime`, `p_action`.

O isolamento por encapsulamento de função (B5-A) é suficiente para validação.
P_FASE4 implementará `motor_theta_pod.py` com chamada real a `interference.py`.

---

## corpora_clingo/ — Inventário

**Localização:** `corpora_clingo/`

### Estrutura

```
corpora_clingo/
├── brasil/         ← CF/88, CLT, Lei 8.080, portarias SUS/Manaus
├── eu/             ← EU AI Act, GDPR
├── usa/            ← Medicaid/SSA Title XIX, CFR 42
├── scenarios/      ← facts files por cenário (T-CLT-01..04)
└── _deprecated/    ← versões antigas
```

### Cenários CLT disponíveis (`corpora_clingo/scenarios/`)

A verificar em P_FASE2: quais cenários têm `.lp` de fatos concretos vs
apenas referência à âncora. O extrator Claude Sonnet (P1.5) produzirá
fatos concretos por cenário em `corpora_clingo/extracted_facts/`.

### ground_truth_predicates.json

`experiments/adversarial_clt/scenarios/ground_truth_predicates.json` (232 linhas):
- Predicados por família de âncora (T-CLT-01 a T-CLT-04)
- Usado incorretamente em B3 como `{predicate_list}` estático
- Em B3-novo: será substituído por extração dinâmica do solver Clingo real
- Manter como referência de vocabulário de predicados esperados

### Nota sobre satisfiability

O solver Clingo retorna `{"satisfiable": bool, ...}` (key `satisfiable`).
`run_arm.py` linha 291 lê `clingo_result.get("satisfiability", "")` — mismatch.
A key correta é `satisfiable` (bool), não `"satisfiability"` (string).
Corrigir em P_FASE3 ao implementar `clingo_pod.py`.
