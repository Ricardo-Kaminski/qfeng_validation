"""Pod LLM (S1-S2). Recebe scenario+normativo, retorna psi_n.

STUB de P_FASE1.6 — apenas ecoa input. Implementacao real em P_FASE3.

Protocolo:
  Request:  {"scenario_id", "scenario_text", "normative_corpus", "modelo", "seed", "temperature"}
  Response: {"status": "ok", "psi_n": [...], "response_text", "tokens_in", "tokens_out", "latency_ms"}

CRITICO: este pod NUNCA recebe predicados Clingo, theta, regime, ou output do
motor. Ele opera como B2 (LLM + RAG normativo) e produz psi_n a partir do
embedding da resposta livre. Veja P_FASE3 para implementacao real.
"""
from qfeng.pods.transport import PodServer

PORT = 5555


def handler_stub(req: dict) -> dict:
    """STUB: ecoa o request com psi_n falso para validar pipeline."""
    return {
        "status": "stub_ok",
        "scenario_id": req.get("scenario_id"),
        "psi_n": [0.5, 0.5],  # placeholder
        "response_text": "[STUB RESPONSE]",
        "tokens_in": 0,
        "tokens_out": 0,
        "latency_ms": 0,
        "note": "P_FASE1.6 stub; implementar em P_FASE3",
    }


if __name__ == "__main__":
    server = PodServer(port=PORT, name="llm_pod")
    server.serve(handler_stub)
