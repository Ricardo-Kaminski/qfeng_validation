"""
extract_manaus_sih.py
=====================
Extração de dados SIH/SUS para o Caso Manaus (Cenário C2 — Q-FENG PoC)

Fonte: FTP público DATASUS via PySUS
Período: outubro 2020 a março 2021 (baseline + crise + recuperação)
UF: AM (Amazonas)
CIDs: J96 (insuficiência respiratória), J18 (pneumonia), U07 (COVID-19)

Saída: data/predictors/manaus_sih/sih_manaus_2020_2021.parquet

Uso:
    pip install pysus
    python scripts/extract_manaus_sih.py

Referência:
    PySUS — AlertaDengue/PySUS (GitHub)
    Saldanha et al. (2019) — microdatasus, Cad. Saúde Pública
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

OUTPUT_DIR = Path(__file__).parent.parent / "data" / "predictors" / "manaus_sih"
OUTPUT_FILE = OUTPUT_DIR / "sih_manaus_2020_2021.parquet"

# Município de Manaus — código IBGE 6 dígitos
MANAUS_IBGE = "130260"

# CIDs relevantes para o cenário de colapso respiratório
CIDS_INTERESSE = {
    "J96",   # Insuficiência respiratória
    "J960",  # Insuficiência respiratória aguda
    "J969",  # Insuficiência respiratória NE
    "J18",   # Pneumonia não especificada
    "J180",  # Broncopneumonia NE
    "J189",  # Pneumonia NE
    "U07",   # COVID-19
    "U071",  # COVID-19 confirmado (vírus identificado)
    "U072",  # COVID-19 suspeito
}

# Período: out/2020 → mar/2021
PERIODOS = [
    (2020, 10),
    (2020, 11),
    (2020, 12),
    (2021, 1),
    (2021, 2),
    (2021, 3),
]

# Variáveis de interesse para o Q-FENG
# (subset do SIH-RD para reduzir tamanho)
COLS_INTERESSE = [
    "ANO_CMPT",      # Ano de competência
    "MES_CMPT",      # Mês de competência
    "MUNIC_RES",     # Município de residência do paciente
    "MUNIC_MOV",     # Município do movimento hospitalar
    "DIAG_PRINC",    # Diagnóstico principal (CID-10)
    "DIAG_SECUN",    # Diagnóstico secundário
    "MORTE",         # Indicador de óbito (0/1)
    "DIAS_PERM",     # Dias de permanência
    "UTI_MES_TO",    # Total de dias em UTI no mês
    "MARCA_UTI",     # Marcador UTI
    "ESPEC",         # Especialidade do leito
    "QT_DIARIAS",    # Quantidade de diárias
    "VAL_TOT",       # Valor total da internação
    "CNES",          # CNES do estabelecimento
    "SEXO",          # Sexo do paciente
    "IDADE",         # Idade
    "COD_IDADE",     # Unidade da idade (anos/meses/dias)
    "COMPLEX",       # Complexidade
    "INSTRU",        # Instrução
    "ETNIA",         # Etnia
]


def extrair_sih_pysus() -> pd.DataFrame:
    """
    Extrai dados SIH/SUS via PySUS para AM, out/2020 a mar/2021.
    Retorna DataFrame filtrado para Manaus + CIDs de interesse.
    """
    try:
        from pysus.ftp.databases.sih import SIH
    except ImportError:
        log.error(
            "PySUS não instalado. Execute: pip install pysus\n"
            "Ou via conda: conda install -c conda-forge pysus"
        )
        raise

    log.info("Conectando ao FTP DATASUS via PySUS...")
    sih = SIH().load()

    dfs = []
    for year, month in PERIODOS:
        log.info(f"Baixando SIH-RD AM {year}/{month:02d}...")
        try:
            files = sih.get_files("RD", uf="AM", year=year, month=month)
            if not files:
                log.warning(f"  Nenhum arquivo encontrado para AM {year}/{month:02d}")
                continue
            parquets = sih.download(files)
            df_mes = parquets.to_dataframe()
            log.info(f"  {len(df_mes):,} registros baixados")
            dfs.append(df_mes)
        except Exception as e:
            log.error(f"  Erro ao baixar {year}/{month:02d}: {e}")
            continue

    if not dfs:
        raise RuntimeError("Nenhum dado foi baixado. Verificar conexão com FTP DATASUS.")

    df_raw = pd.concat(dfs, ignore_index=True)
    log.info(f"Total bruto: {len(df_raw):,} registros (AM, todos municípios)")

    # Filtrar apenas Manaus
    df_manaus = df_raw[df_raw["MUNIC_RES"].astype(str) == MANAUS_IBGE].copy()
    log.info(f"Filtrado Manaus (IBGE {MANAUS_IBGE}): {len(df_manaus):,} registros")

    # Filtrar CIDs de interesse
    df_manaus["CID_3"] = df_manaus["DIAG_PRINC"].str[:3].str.upper()
    cids_3 = {cid[:3] for cid in CIDS_INTERESSE}
    df_cid = df_manaus[
        df_manaus["DIAG_PRINC"].str.upper().isin(CIDS_INTERESSE) |
        df_manaus["CID_3"].isin(cids_3)
    ].copy()
    log.info(f"Filtrado CIDs J96/J18/U07: {len(df_cid):,} registros")

    # Selecionar colunas disponíveis (subset seguro)
    cols_disponiveis = [c for c in COLS_INTERESSE if c in df_cid.columns]
    cols_faltando = set(COLS_INTERESSE) - set(cols_disponiveis)
    if cols_faltando:
        log.warning(f"Colunas não encontradas (ignoradas): {cols_faltando}")

    df_final = df_cid[cols_disponiveis].copy()

    # Adicionar coluna de período para série temporal
    df_final["COMPETENCIA"] = (
        df_final["ANO_CMPT"].astype(str) + df_final["MES_CMPT"].astype(str).str.zfill(2)
    )

    return df_final


def gerar_serie_temporal(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega os dados em série temporal mensal para uso no cenário C2.

    Retorna DataFrame com uma linha por mês, com métricas:
    - internacoes_total: total de internações CID J96/J18/U07
    - obitos: total de óbitos
    - dias_uti_total: total de dias em UTI
    - internacoes_j96: internações por insuficiência respiratória
    - internacoes_u07: internações COVID-19
    - taxa_mortalidade: óbitos / internações
    """
    df["MORTE_NUM"] = pd.to_numeric(df["MORTE"], errors="coerce").fillna(0)
    df["UTI_DIAS"] = pd.to_numeric(df.get("UTI_MES_TO", 0), errors="coerce").fillna(0)

    serie = df.groupby("COMPETENCIA").agg(
        internacoes_total=("DIAG_PRINC", "count"),
        obitos=("MORTE_NUM", "sum"),
        dias_uti_total=("UTI_DIAS", "sum"),
        internacoes_j96=(
            "DIAG_PRINC",
            lambda x: x.str.upper().str.startswith("J96").sum()
        ),
        internacoes_u07=(
            "DIAG_PRINC",
            lambda x: x.str.upper().str.startswith("U07").sum()
        ),
    ).reset_index()

    serie["taxa_mortalidade"] = serie["obitos"] / serie["internacoes_total"]
    serie["COMPETENCIA_DT"] = pd.to_datetime(
        serie["COMPETENCIA"], format="%Y%m"
    )
    serie = serie.sort_values("COMPETENCIA_DT")

    log.info("Série temporal mensal gerada:")
    log.info(serie[["COMPETENCIA", "internacoes_total", "obitos",
                     "taxa_mortalidade", "dias_uti_total"]].to_string(index=False))

    return serie


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Extrair dados brutos
    df = extrair_sih_pysus()

    # 2. Salvar dados filtrados completos
    df.to_parquet(OUTPUT_FILE, index=False)
    log.info(f"Salvo: {OUTPUT_FILE} ({OUTPUT_FILE.stat().st_size / 1024:.1f} KB)")

    # 3. Gerar e salvar série temporal agregada
    serie = gerar_serie_temporal(df)
    serie_file = OUTPUT_DIR / "serie_temporal_manaus.parquet"
    serie.to_parquet(serie_file, index=False)
    log.info(f"Série temporal salva: {serie_file}")

    # 4. Exportar também como CSV para inspeção fácil
    serie.to_csv(OUTPUT_DIR / "serie_temporal_manaus.csv", index=False)
    log.info("CSV exportado para inspeção.")

    log.info("Extração concluída. Dados prontos para o Cenário C2 (Manaus).")


if __name__ == "__main__":
    main()
