"""
download_sih_manaus_ftp.py
==========================
Download direto dos arquivos SIH/SUS (AM) do FTP DATASUS via ftplib (stdlib).
Período: out/2020 a mar/2021 — Caso C2 Q-FENG (Crise Oxigênio Manaus)

Uso:
    python scripts/download_sih_manaus_ftp.py

Saída:
    data/predictors/manaus_sih/raw/RDAM20{MM}.dbc
"""
from __future__ import annotations

import ftplib
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

FTP_HOST = "ftp.datasus.gov.br"
FTP_DIR = "/dissemin/publicos/SIHSUS/200801_/Dados"

ARQUIVOS = [
    "RDAM2010.dbc",  # out/2020
    "RDAM2011.dbc",  # nov/2020
    "RDAM2012.dbc",  # dez/2020
    "RDAM2101.dbc",  # jan/2021
    "RDAM2102.dbc",  # fev/2021
    "RDAM2103.dbc",  # mar/2021
]

OUTPUT_DIR = Path(__file__).parent.parent / "data" / "predictors" / "manaus_sih" / "raw"


def download_file(ftp: ftplib.FTP, filename: str, dest: Path) -> int:
    dest.mkdir(parents=True, exist_ok=True)
    local_path = dest / filename
    if local_path.exists():
        log.info(f"  Já existe: {local_path.name} ({local_path.stat().st_size:,} bytes) — pulando")
        return local_path.stat().st_size

    log.info(f"  Baixando {filename}...")
    with open(local_path, "wb") as f:
        ftp.retrbinary(f"RETR {filename}", f.write)

    size = local_path.stat().st_size
    log.info(f"  OK: {local_path.name} — {size:,} bytes ({size / 1024 / 1024:.1f} MB)")
    return size


def main() -> None:
    log.info(f"Conectando a {FTP_HOST}...")
    with ftplib.FTP(FTP_HOST, timeout=60) as ftp:
        ftp.login()
        log.info(f"Conectado. Entrando em {FTP_DIR}")
        ftp.cwd(FTP_DIR)

        total = 0
        ok = []
        falhas = []
        for arquivo in ARQUIVOS:
            try:
                size = download_file(ftp, arquivo, OUTPUT_DIR)
                total += size
                ok.append(arquivo)
            except ftplib.error_perm as e:
                log.error(f"  FTP erro em {arquivo}: {e}")
                falhas.append(arquivo)
            except Exception as e:
                log.error(f"  Erro inesperado em {arquivo}: {e}")
                falhas.append(arquivo)

    log.info("=" * 60)
    log.info(f"Concluído: {len(ok)}/{len(ARQUIVOS)} arquivos")
    log.info(f"Total baixado: {total / 1024 / 1024:.1f} MB")
    log.info(f"Destino: {OUTPUT_DIR}")
    if falhas:
        log.warning(f"Falhas: {falhas}")
    else:
        log.info("Todos os arquivos baixados com sucesso.")


if __name__ == "__main__":
    main()
