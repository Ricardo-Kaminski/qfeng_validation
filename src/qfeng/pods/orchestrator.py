"""Orchestrator: cliente que coordena os 3 pods.

NAO eh um pod. Eh o codigo do braco B5_SIDECAR que: (1) chama llm_pod com cenario;
(2) chama clingo_pod com cenario; (3) chama motor_theta_pod com psi_n e psi_s
coletados; (4) aplica filtro de regime sobre a resposta do llm_pod.

Para B5_NLU_REFORMADO (verbalizador), o orchestrator chama clingo_pod primeiro,
depois llm_pod com input que INCLUI o output simbolico (legitimo neste caso —
LLM sabe que esta verbalizando, nao decidindo).
"""
import time
from qfeng.pods.transport import call_pod
from qfeng.pods.llm_pod import PORT as LLM_PORT
from qfeng.pods.clingo_pod import PORT as CLINGO_PORT
from qfeng.pods.motor_theta_pod import PORT as MOTOR_PORT


def run_b5_sidecar(
    scenario_id: str,
    scenario_text: str,
    scenario_type: str,
    normative_corpus: str,
    modelo: str,
    seed: int,
    temperature: float = 0.7,
) -> dict:
    """Pipeline B5_SIDECAR.

    1. llm_pod (cenario + normativo, SEM motor) -> psi_n + response_text
    2. clingo_pod (cenario) -> psi_s + sat
    3. motor_theta_pod (psi_n, psi_s) -> regime
    4. Filtro: aplicar regime sobre response_text
    """
    t0 = time.monotonic()

    t_llm_start = time.monotonic()
    llm_resp = call_pod(LLM_PORT, {
        "scenario_id": scenario_id,
        "scenario_text": scenario_text,
        "normative_corpus": normative_corpus,
        "modelo": modelo,
        "seed": seed,
        "temperature": temperature,
    })
    t_llm = (time.monotonic() - t_llm_start) * 1000

    t_clingo_start = time.monotonic()
    clingo_resp = call_pod(CLINGO_PORT, {
        "scenario_id": scenario_id,
        "scenario_text": scenario_text,
        "scenario_type": scenario_type,
    })
    t_clingo = (time.monotonic() - t_clingo_start) * 1000

    # Motor theta recebe APENAS os dois vetores — sem scenario_id nem modelo
    t_motor_start = time.monotonic()
    motor_resp = call_pod(MOTOR_PORT, {
        "psi_n": llm_resp["psi_n"],
        "psi_s": clingo_resp["psi_s"],
    })
    t_motor = (time.monotonic() - t_motor_start) * 1000

    regime = motor_resp["regime"]
    response_text = llm_resp["response_text"]

    if regime in ("BLOCK", "CIRCUIT_BREAKER"):
        final_response = (
            "[DECISAO BLOQUEADA pelo motor Q-FENG: "
            "divergencia critica entre raciocinio neural e ancoragem simbolica]"
        )
    elif regime == "HITL":
        final_response = (
            f"[REQUER REVISAO HUMANA — friccao ontologica "
            f"theta={motor_resp['theta_deg']:.1f}]\n\n{response_text}"
        )
    else:  # STAC ou fallback
        final_response = response_text

    t_total = (time.monotonic() - t0) * 1000

    return {
        "status": "ok",
        "scenario_id": scenario_id,
        "modelo": modelo,
        "seed": seed,
        "final_response": final_response,
        "regime_applied": regime,
        "t_llm_ms": t_llm,
        "t_clingo_ms": t_clingo,
        "t_motor_theta_ms": t_motor,
        "t_total_ms": t_total,
        "t_ipc_overhead_ms": t_total - (t_llm + t_clingo + t_motor),
        "psi_n": llm_resp["psi_n"],
        "psi_s": clingo_resp["psi_s"],
        "theta_deg": motor_resp["theta_deg"],
        "theta_eff_deg": motor_resp["theta_eff_deg"],
        "cos_theta": motor_resp["cos_theta"],
        "p_action": motor_resp["p_action"],
        "satisfiability": clingo_resp["satisfiability"],
        "active_sovereign": clingo_resp["active_sovereign"],
        "active_elastic": clingo_resp["active_elastic"],
        "raw_response_text": response_text,
        "tokens_in": llm_resp["tokens_in"],
        "tokens_out": llm_resp["tokens_out"],
    }


if __name__ == "__main__":
    # Smoke test integrado: precisa dos 3 pods rodando em paralelo.
    # Em terminais separados:
    #   python -m qfeng.pods.llm_pod
    #   python -m qfeng.pods.clingo_pod
    #   python -m qfeng.pods.motor_theta_pod
    # Depois rodar este script.
    import json
    result = run_b5_sidecar(
        scenario_id="SMOKE-001",
        scenario_text="Cenario de smoke test.",
        scenario_type="T-CLT-01",
        normative_corpus="(corpus stub)",
        modelo="qwen3:14b",
        seed=42,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
