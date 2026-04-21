# converter_dbc.R
library(read.dbc)
library(arrow)

raw_dir <- "C:/Workspace/academico/qfeng_validacao/data/predictors/manaus_sih/raw"
out_dir  <- "C:/Workspace/academico/qfeng_validacao/data/predictors/manaus_sih"

files <- list.files(raw_dir, pattern = "\\.dbc$", full.names = TRUE)
dfs <- lapply(files, read.dbc)
df_all <- do.call(rbind, dfs)

# Filtrar Manaus + CIDs relevantes
df_manaus <- df_all[
  df_all$MUNIC_RES == "130260" &
  substr(df_all$DIAG_PRINC, 1, 3) %in% c("J96","J18","U07"),
]

write_parquet(df_manaus, file.path(out_dir, "sih_manaus_2020_2021.parquet"))
cat(sprintf("Salvo: %d registros\n", nrow(df_manaus)))
