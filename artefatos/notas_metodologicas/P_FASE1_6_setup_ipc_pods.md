# P1.6 — Setup IPC ZeroMQ + Pods Stub

**Data:** 29/abr/2026

## Estrutura criada

```
src/qfeng/pods/
├── __init__.py           ← exports + constantes de porta
├── transport.py          ← PodServer (REP) + call_pod + pod_client (REQ)
├── llm_pod.py            ← PORT=5555, stub retorna psi_n=[0.5,0.5]
├── clingo_pod.py         ← PORT=5556, stub retorna psi_s=[0.7,0.3]
├── motor_theta_pod.py    ← PORT=5557, stub retorna regime=STAC
└── orchestrator.py       ← run_b5_sidecar: coordena 3 pods sem cruzar outputs
```

## Decisão de transporte

**ZeroMQ REQ-REP sobre TCP localhost.** Cada pod escuta em porta dedicada:

| Pod | Porta | VSM Level |
|-----|-------|-----------|
| LLM pod | 5555 | S1-S2 |
| Clingo pod | 5556 | S3-S4 |
| Motor θ pod | 5557 | S5 |

## Princípio arquitetônico preservado

`motor_theta_pod` recebe APENAS `{"psi_n": [...], "psi_s": [...]}`.
Nunca recebe `scenario_id`, `scenario_text`, `modelo` ou qualquer contexto
que identifique o cenário ou o modelo LLM.

## Smoke test

```
OK: pods importam, portas atribuidas (5555/5556/5557).
OK: IPC motor_theta_pod funcionando.
    Response: {"status": "stub_ok", "theta_deg": 45.0, "regime": "STAC", ...}
STATUS: P1.6 smoke test PASSED
```

IPC verificado com subprocess: `motor_theta_pod` subido em background,
`call_pod(5557, {...})` retorna `status=stub_ok` e `regime=STAC`.

## pyzmq

Versão 27.1.0 instalada no env qfeng (já estava disponível).

## TODO para P_FASE3 e P_FASE4

- `llm_pod.py`: chamar Ollama com `temperature=0.7 + seed`; embedding → ψ_n
- `clingo_pod.py`: consumir `extracted_facts/{scenario_id}.lp`; executar solver; ψ_s
- `motor_theta_pod.py`: chamar `interference.py`; retornar θ + regime real
- Shutdown gracioso via signal handler (SIGTERM → socket.close + ctx.term)
- Possível paralelização LLM ⊥ Clingo (asyncio + zmq.asyncio)
