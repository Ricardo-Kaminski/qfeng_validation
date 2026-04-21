# extract_manaus_sih_r.R
# ======================
# Extração SIH/SUS Manaus via microdatasus (R)
# Caso C2 — Q-FENG PoC: Crise de Oxigênio Manaus 2021
#
# Instalação:
#   install.packages("remotes")
#   remotes::install_github("rfsaldanha/microdatasus")
#   install.packages(c("dplyr", "arrow", "readr"))
#
# Uso:
#   Rscript scripts/extract_manaus_sih_r.R
#
# Saída:
#   data/predictors/manaus_sih/sih_manaus_2020_2021.parquet
#   data/predictors/manaus_sih/serie_temporal_manaus.parquet
#   data/predictors/manaus_sih/serie_temporal_manaus.csv

library(microdatasus)
library(dplyr)
library(arrow)
library(readr)

OUTPUT_DIR <- file.path(
  dirname(dirname(rstudioapi::getSourceEditorContext()$path)),
  "data", "predictors", "manaus_sih"
)

# Se não estiver no RStudio, usar path relativo
if (!exists("OUTPUT_DIR") || is.null(OUTPUT_DIR)) {
  OUTPUT_DIR <- file.path("..", "data", "predictors", "manaus_sih")
}

dir.create(OUTPUT_DIR, recursive = TRUE, showWarnings = FALSE)

MANAUS_IBGE <- "130260"
CIDS_INTERESSE <- c("J96", "J18", "U07")

cat("Baixando SIH/SUS AM — out/2020 a mar/2021...\n")

# Baixar dados mês a mês para AM
dados_brutos <- fetch_datasus(
  year_start  = 2020,
  year_end    = 2021,
  month_start = 10,
  month_end   = 3,
  uf          = "AM",
  information_system = "SIH-RD"
)

cat(sprintf("Total bruto AM: %d registros\n", nrow(dados_brutos)))

# Pré-processar (rotulagem de variáveis)
dados_proc <- process_sih(dados_brutos)

# Filtrar Manaus
dados_manaus <- dados_proc %>%
  filter(MUNIC_RES == MANAUS_IBGE)

cat(sprintf("Filtrado Manaus: %d registros\n", nrow(dados_manaus)))

# Filtrar CIDs de interesse (J96, J18, U07)
dados_cid <- dados_manaus %>%
  filter(substr(DIAG_PRINC, 1, 3) %in% CIDS_INTERESSE)

cat(sprintf("Filtrado J96/J18/U07: %d registros\n", nrow(dados_cid)))

# Criar coluna de competência AAAAMM
dados_cid <- dados_cid %>%
  mutate(
    COMPETENCIA = paste0(ANO_CMPT, sprintf("%02d", as.integer(MES_CMPT))),
    MORTE_N = as.numeric(as.character(MORTE)),
    UTI_DIAS = as.numeric(as.character(UTI_MES_TO))
  )

# Salvar dados completos filtrados
arrow::write_parquet(
  dados_cid,
  file.path(OUTPUT_DIR, "sih_manaus_2020_2021.parquet")
)
cat("Salvo: sih_manaus_2020_2021.parquet\n")

# Agregar série temporal mensal
serie <- dados_cid %>%
  group_by(COMPETENCIA) %>%
  summarise(
    internacoes_total  = n(),
    obitos             = sum(MORTE_N, na.rm = TRUE),
    dias_uti           = sum(UTI_DIAS, na.rm = TRUE),
    internacoes_j96    = sum(substr(DIAG_PRINC, 1, 3) == "J96"),
    internacoes_u07    = sum(substr(DIAG_PRINC, 1, 3) == "U07"),
    .groups = "drop"
  ) %>%
  mutate(
    taxa_mortalidade = obitos / internacoes_total,
    COMPETENCIA_DT   = as.Date(paste0(COMPETENCIA, "01"), format = "%Y%m%d")
  ) %>%
  arrange(COMPETENCIA_DT)

# Salvar série temporal
arrow::write_parquet(
  serie,
  file.path(OUTPUT_DIR, "serie_temporal_manaus.parquet")
)
readr::write_csv(
  serie,
  file.path(OUTPUT_DIR, "serie_temporal_manaus.csv")
)

cat("\nSérie temporal gerada:\n")
print(serie[, c("COMPETENCIA","internacoes_total","obitos","taxa_mortalidade","dias_uti")])

cat(sprintf("\nConcluído. Arquivos em: %s\n", OUTPUT_DIR))

# Diagnóstico rápido para validação
cat("\n--- DIAGNÓSTICO Q-FENG ---\n")
cat(sprintf("Pico de mortalidade: competência %s (%.1f%%)\n",
    serie$COMPETENCIA[which.max(serie$taxa_mortalidade)],
    max(serie$taxa_mortalidade, na.rm=TRUE) * 100))
cat(sprintf("Pico UTI: competência %s (%d dias)\n",
    serie$COMPETENCIA[which.max(serie$dias_uti)],
    max(serie$dias_uti, na.rm=TRUE)))
cat("Trajetória θ esperada: θ<30° (out) → θ≈90° (dez) → θ>120° (jan)\n")
