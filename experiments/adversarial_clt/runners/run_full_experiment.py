"""Orquestrador batch: 4 braços × 4 modelos × 50 cenários × 3 runs = 2400 chamadas.

Resumível: consulta manifest.json antes de cada job e pula os já completos.
Progresso a cada 50 calls. Estimativa de tempo restante baseada em média móvel.
"""

from __future__ import annotations

import json
import logging
import sys
import time
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src"))

from experiments.adversarial_clt.runners.run_arm import (
    EXPERIMENT_ROOT,
    VALID_BRACOS,
    VALID_MODELOS,
    run_arm,
)

MANIFEST_PATH = EXPERIMENT_ROOT / "results" / "manifest.json"
RESULTS_PARQUET = EXPERIMENT_ROOT / "results" / "results.parquet"
SCENARIOS_FILE = EXPERIMENT_ROOT / "scenarios" / "scenarios.yaml"

RUNS_PER_JOB = 3
SEEDS = [42, 137, 271]  # Um seed fixo por run para reprodutibilidade

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(EXPERIMENT_ROOT / "results" / "run_log.txt", mode="a", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Manifest helpers
# ---------------------------------------------------------------------------

def _load_manifest() -> dict[str, str]:
    """Carrega manifest {job_key: status}. Cria vazio se não existe."""
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_manifest(manifest: dict[str, str]) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


def _job_key(braco: str, modelo: str, scenario_id: str, run_id: int) -> str:
    return f"{braco}__{modelo}__{scenario_id}__run{run_id}"


# ---------------------------------------------------------------------------
# Results helpers
# ---------------------------------------------------------------------------

def _append_to_parquet(record: dict[str, Any]) -> None:
    """Adiciona uma linha ao parquet de resultados (lê→append→salva)."""
    row = pd.DataFrame([{
        "sha256": record["sha256"],
        "braco": record["braco"],
        "modelo": record["modelo"],
        "scenario_id": record["scenario_id"],
        "run_id": record["run_id"],
        "seed": record["seed"],
        "timestamp_iso": record["timestamp_iso"],
        "response_text": record["response_text"],
        "tokens_in": record["tokens_in"],
        "tokens_out": record["tokens_out"],
        "latency_ms": record["latency_ms"],
        "status": record["status"],
        "error": record.get("error"),
        "clingo_satisfiability": record.get("clingo_satisfiability", ""),
        "n_sovereign_active": len(record.get("clingo_active_sovereign", [])),
        "n_elastic_active": len(record.get("clingo_active_elastic", [])),
    }])

    if RESULTS_PARQUET.exists():
        existing = pd.read_parquet(RESULTS_PARQUET)
        combined = pd.concat([existing, row], ignore_index=True)
    else:
        combined = row

    RESULTS_PARQUET.parent.mkdir(parents=True, exist_ok=True)
    combined.to_parquet(RESULTS_PARQUET, index=False)


# ---------------------------------------------------------------------------
# Construção da lista de jobs
# ---------------------------------------------------------------------------

def _build_job_list(scenario_ids: list[str]) -> list[dict]:
    jobs = []
    for braco in VALID_BRACOS:
        for modelo in VALID_MODELOS:
            for sid in scenario_ids:
                for run_id, seed in enumerate(SEEDS, start=1):
                    jobs.append({
                        "braco": braco,
                        "modelo": modelo,
                        "scenario_id": sid,
                        "run_id": run_id,
                        "seed": seed,
                    })
    return jobs


def _load_scenario_ids() -> list[str]:
    import yaml
    with open(SCENARIOS_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return [s["scenario_id"] for s in data["scenarios"]]


# ---------------------------------------------------------------------------
# Runner principal
# ---------------------------------------------------------------------------

def run_experiment(*, dry_run: bool = False, max_jobs: int | None = None) -> None:
    scenario_ids = _load_scenario_ids()
    all_jobs = _build_job_list(scenario_ids)
    total = len(all_jobs)
    log.info("Total de jobs no experimento: %d", total)

    manifest = _load_manifest()

    pending = [j for j in all_jobs if manifest.get(_job_key(**{k: j[k] for k in ("braco", "modelo", "scenario_id", "run_id")})) != "completed"]
    log.info("Jobs pendentes: %d (já completos: %d)", len(pending), total - len(pending))

    if max_jobs:
        pending = pending[:max_jobs]
        log.info("Limitado a %d jobs (dry_run/teste)", max_jobs)

    if dry_run:
        log.info("[DRY RUN] Listando primeiros 5 jobs:")
        for j in pending[:5]:
            log.info("  %s", _job_key(**{k: j[k] for k in ("braco", "modelo", "scenario_id", "run_id")}))
        return

    latencies: list[float] = []
    completed = 0
    failed = 0

    for i, job in enumerate(pending, start=1):
        key = _job_key(**{k: job[k] for k in ("braco", "modelo", "scenario_id", "run_id")})

        t0 = time.monotonic()
        try:
            record = run_arm(**job)
            elapsed = time.monotonic() - t0

            if record["status"] == "ok":
                manifest[key] = "completed"
                _append_to_parquet(record)
                completed += 1
            else:
                manifest[key] = "failed"
                failed += 1
                log.warning("Job FALHOU: %s — %s", key, record.get("error"))

            latencies.append(elapsed)

        except Exception as exc:
            elapsed = time.monotonic() - t0
            manifest[key] = "failed"
            failed += 1
            latencies.append(elapsed)
            log.error("Exceção no job %s: %s", key, exc)

        # Salva manifest a cada job
        _save_manifest(manifest)

        # Log de progresso a cada 50 calls
        if i % 50 == 0 or i == len(pending):
            avg_lat = sum(latencies[-50:]) / len(latencies[-50:])
            remaining = len(pending) - i
            eta_h = remaining * avg_lat / 3600
            log.info(
                "Progresso: %d/%d jobs | completos=%d falhas=%d | lat_média=%.1fs | ETA=%.1fh",
                i, len(pending), completed, failed, avg_lat, eta_h,
            )

    log.info("Experimento concluído: %d completos, %d falhas de %d jobs.", completed, failed, len(pending))
    _save_manifest(manifest)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Orquestrador Frente 2")
    parser.add_argument("--dry-run", action="store_true", help="Lista jobs sem executar")
    parser.add_argument("--max-jobs", type=int, default=None, help="Limitar número de jobs (para testes)")
    args = parser.parse_args()
    run_experiment(dry_run=args.dry_run, max_jobs=args.max_jobs)
