"""Monitor E2 deontic extraction — verifica progresso a cada 10 min e retoma se interrompido."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

import psutil

CACHE_DIR = Path("outputs/deontic_cache_trabalhista")
TOTAL_CHUNKS = 4486
CHECK_INTERVAL = 600  # 10 minutos
CMD = [
    sys.executable, "-m", "qfeng.c1_digestion.deontic",
    "--corpus-dir", "outputs/e1_chunks_trabalhista/",
    "--output-dir", "outputs/deontic_cache_trabalhista/",
    "--report", "outputs/e2_report_trabalhista.md",
]

proc: subprocess.Popen[bytes] | None = None


def cache_count() -> int:
    if not CACHE_DIR.exists():
        return 0
    return sum(1 for f in CACHE_DIR.iterdir() if f.suffix == ".json")


def e2_already_running() -> bool:
    for p in psutil.process_iter(["cmdline"]):
        try:
            cmd = " ".join(p.info["cmdline"] or [])
            if "qfeng.c1_digestion.deontic" in cmd and "monitor_e2" not in cmd:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


def start_e2() -> subprocess.Popen[bytes]:
    print(f"[monitor] Iniciando E2... ({cache_count()}/{TOTAL_CHUNKS} já no cache)")
    return subprocess.Popen(CMD)


def main() -> None:
    global proc
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    if e2_already_running():
        print(f"[monitor] E2 já em execução — monitorando ({cache_count()}/{TOTAL_CHUNKS})")
    else:
        proc = start_e2()

    while True:
        time.sleep(CHECK_INTERVAL)
        done = cache_count()
        pct = done / TOTAL_CHUNKS * 100

        running = e2_already_running() or (proc is not None and proc.poll() is None)
        status = "rodando" if running else "parado"
        print(f"[monitor] {done}/{TOTAL_CHUNKS} ({pct:.1f}%) — processo: {status}")

        if done >= TOTAL_CHUNKS:
            print("[monitor] Concluído — todos os chunks processados.")
            break

        if not running:
            print("[monitor] Processo parado — retomando...")
            proc = start_e2()


if __name__ == "__main__":
    main()
