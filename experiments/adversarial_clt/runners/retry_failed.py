"""Retenta jobs com status 'failed' no manifest, com backoff exponencial."""

from __future__ import annotations

import logging
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src"))

from experiments.adversarial_clt.runners.run_arm import run_arm
from experiments.adversarial_clt.runners.run_full_experiment import (
    EXPERIMENT_ROOT,
    MANIFEST_PATH,
    SCENARIOS_FILE,
    _append_to_parquet,
    _build_job_list,
    _job_key,
    _load_manifest,
    _load_scenario_ids,
    _save_manifest,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(EXPERIMENT_ROOT / "results" / "retry_log.txt", mode="a", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)

MAX_RETRIES = 3
BACKOFF_BASE_S = 10


def retry_failed_jobs() -> None:
    scenario_ids = _load_scenario_ids()
    all_jobs = _build_job_list(scenario_ids)
    manifest = _load_manifest()

    failed_jobs = [
        j for j in all_jobs
        if manifest.get(_job_key(**{k: j[k] for k in ("braco", "modelo", "scenario_id", "run_id")})) == "failed"
    ]

    log.info("Jobs com status 'failed': %d", len(failed_jobs))
    if not failed_jobs:
        log.info("Nenhuma falha para retentar.")
        return

    recovered = 0
    still_failed = 0

    for job in failed_jobs:
        key = _job_key(**{k: job[k] for k in ("braco", "modelo", "scenario_id", "run_id")})
        success = False

        for attempt in range(1, MAX_RETRIES + 1):
            wait = BACKOFF_BASE_S * (2 ** (attempt - 1))
            log.info("Retentando %s (tentativa %d/%d)", key, attempt, MAX_RETRIES)
            try:
                record = run_arm(**job, force=True)
                if record["status"] == "ok":
                    manifest[key] = "completed"
                    _append_to_parquet(record)
                    _save_manifest(manifest)
                    log.info("Recuperado: %s", key)
                    success = True
                    recovered += 1
                    break
                else:
                    log.warning("Ainda falhou (tentativa %d): %s — %s", attempt, key, record.get("error"))
            except Exception as exc:
                log.error("Exceção na tentativa %d para %s: %s", attempt, key, exc)

            if attempt < MAX_RETRIES:
                log.info("Aguardando %ds antes de próxima tentativa...", wait)
                time.sleep(wait)

        if not success:
            manifest[key] = "failed_permanent"
            _save_manifest(manifest)
            still_failed += 1
            log.error("Falha permanente após %d tentativas: %s", MAX_RETRIES, key)

    log.info("Retry concluído: %d recuperados, %d falhas permanentes.", recovered, still_failed)


if __name__ == "__main__":
    retry_failed_jobs()
