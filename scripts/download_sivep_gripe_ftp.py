"""Download INFLUD20.csv e INFLUD21.csv do DATASUS para SIVEP-Gripe.

NOTA DE DISPONIBILIDADE (verificado 26/abr/2026):
  O FTP datasus.gov.br NAO contem mais o path original
  /dissemin/publicos/SIVEP_Gripe/Dados/INFLUD20.csv.
  Os arquivos SIVEP-Gripe foram migrados para o OpenDataSUS.

Fontes alternativas:
  - OpenDataSUS SRAG 2020:
      https://opendatasus.saude.gov.br/dataset/srag-2020
  - OpenDataSUS SRAG 2021:
      https://opendatasus.saude.gov.br/dataset/srag-2021
  - S3 direto (URL historica, pode ter expirado):
      https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2020/INFLUD20-01-02-2021.csv
      https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2021/INFLUD21-22-06-2021.csv

Instrucoes de download manual:
  1. Acesse https://opendatasus.saude.gov.br/dataset/srag-2020
  2. Baixe o CSV mais recente do ano 2020 (INFLUD20-*.csv)
  3. Repita para 2021
  4. Salve em: data/predictors/manaus_bi/raw/srag_manaus_sivep/

Uso (requer arquivos ja presentes no diretorio raw/):
    python scripts/download_sivep_gripe_ftp.py
    -> verifica se os arquivos ja existem e reporta o status
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[1]
DEST_DIR = PROJECT_ROOT / "data/predictors/manaus_bi/raw/srag_manaus_sivep"

EXPECTED_FILES = {
    "INFLUD20": "SRAG 2020 (jul/2020-dez/2020 relevante para Manaus BI)",
    "INFLUD21": "SRAG 2021 (jan/2021-jun/2021 relevante para Manaus BI)",
}


def _find_influd(year_tag: str) -> Path | None:
    """Find INFLUD file for given year tag (e.g. '20' or '21')."""
    candidates = list(DEST_DIR.glob(f"INFLUD{year_tag}*.csv"))
    if candidates:
        return candidates[0]
    return None


def main() -> None:
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    print("=== Status dos arquivos SIVEP-Gripe ===")
    all_ok = True
    for tag, desc in EXPECTED_FILES.items():
        f = _find_influd(tag[-2:])
        if f:
            size_mb = f.stat().st_size / (1024 * 1024)
            print(f"[OK  ] {f.name} ({size_mb:.1f} MB) — {desc}")
        else:
            print(f"[MISS] {tag}*.csv — {desc}")
            print(f"       -> Baixe manualmente de opendatasus.saude.gov.br/dataset/srag-20{tag[-2:]}")
            print(f"       -> Salve em: {DEST_DIR}/")
            all_ok = False
    if not all_ok:
        print("\nArquivos faltando. Execute extract_srag_manaus.py para criar stub.")
        sys.exit(1)
    else:
        print("\nTodos os arquivos presentes. Execute extract_srag_manaus.py para extrair.")


if __name__ == "__main__":
    main()
