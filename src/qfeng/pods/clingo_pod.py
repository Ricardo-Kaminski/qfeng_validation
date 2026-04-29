"""Pod Clingo (S3-S4). Recebe scenario, executa solver, retorna psi_s.

STUB de P_FASE1.6. Implementacao real em P_FASE3.

Protocolo:
  Request:  {"scenario_id", "scenario_text", "scenario_type"}
  Response: {"status", "satisfiability": "SAT"|"UNSAT", "active_sovereign", "active_elastic",
             "psi_s": [...], "facts_lp_used", "t_extract_ms", "t_solve_ms"}

Pipeline interno (a implementar em P_FASE3):
  1. Buscar facts em corpora_clingo/extracted_facts/{scenario_id}.lp
     (se nao existe: chamar extractor Claude Sonnet — P_FASE2)
  2. Concatenar com regras do corpus normativo
  3. Executar Clingo solve
  4. Construir psi_s a partir de SAT/UNSAT + atomos no modelo
"""
from qfeng.pods.transport import PodServer

PORT = 5556


def handler_stub(req: dict) -> dict:
    return {
        "status": "stub_ok",
        "scenario_id": req.get("scenario_id"),
        "satisfiability": "SAT",  # placeholder
        "active_sovereign": [],
        "active_elastic": [],
        "psi_s": [0.7, 0.3],  # placeholder
        "facts_lp_used": "[STUB]",
        "t_extract_ms": 0,
        "t_solve_ms": 0,
        "note": "P_FASE1.6 stub; implementar em P_FASE3",
    }


if __name__ == "__main__":
    server = PodServer(port=PORT, name="clingo_pod")
    server.serve(handler_stub)
