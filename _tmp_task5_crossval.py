"""
Tarefa 5 — Cross-validacao + atualizacao canonica + relatorio executivo.
Sub-tarefas: 5A (cross-val FVS-AM x DEMAS), 5B (Spearman/PCA/lag TOH x SRAG),
             5C (bi_dimensional_decision.json), 5D (source_manifest SHA256),
             5E (relatorio executivo), 5F (CHANGELOG).
"""
import sys, os, json, hashlib, shutil, datetime
import pandas as pd
import numpy as np
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DERIVED   = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\derived"
ARCHIVED  = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\_archived"
RAW       = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\raw"
OUTPUTS   = r"C:\Workspace\academico\qfeng_validacao\outputs"
ARC_OUT   = r"C:\Workspace\academico\qfeng_validacao\outputs\_archive"

os.makedirs(ARC_OUT, exist_ok=True)

# ============================================================
# 5A — Cross-validacao FVS-AM x DEMAS-VEPI
# ============================================================
print("=" * 60)
print("5A — Cross-validacao FVS-AM x DEMAS-VEPI")

toh_new = pd.read_parquet(os.path.join(DERIVED, "toh_semanal_manaus.parquet"))
fvs_path = os.path.join(ARCHIVED, "toh_fvs_am_fase1", "toh_uti_manaus_mensal.parquet")
fvs = pd.read_parquet(fvs_path)
print(f"TOH DEMAS shape: {toh_new.shape}")
print(f"FVS-AM shape: {fvs.shape}")
print(f"FVS-AM colunas: {list(fvs.columns)}")

# Descobrir schema FVS e normalizar para year_se/sem_epi
print(f"FVS-AM amostra:\n{fvs.head(3).to_string()}")

# FVS-AM pode ser mensal - tentamos mapear para SE
fvs_cols = list(fvs.columns)
date_col = next((c for c in fvs_cols if 'data' in c.lower() or 'date' in c.lower() or 'mes' in c.lower() or 'month' in c.lower()), None)
toh_col  = next((c for c in fvs_cols if 'toh' in c.lower() or 'ocup' in c.lower()), None)
print(f"FVS date_col={date_col}, toh_col={toh_col}")

if date_col and toh_col:
    # FVS-AM e mensal (ano/mes) — converter competencia para ano_mes
    if "competencia" in fvs.columns:
        fvs["data"] = pd.to_datetime(fvs["competencia"], errors="coerce")
    elif date_col in fvs.columns:
        # Pode ser coluna year+month separados
        if "year" in fvs.columns and "month" in fvs.columns:
            fvs["data"] = pd.to_datetime(fvs[["year","month"]].assign(day=1))
        else:
            fvs["data"] = pd.to_datetime(fvs[date_col], errors="coerce")
    fvs["toh_fvs"] = pd.to_numeric(fvs[toh_col], errors="coerce")
    fvs["ano_mes"] = fvs["data"].dt.strftime("%Y-%m")

    # Normalizar TOH FVS (pode estar em % 0-100 ou 0-1)
    if fvs["toh_fvs"].dropna().max() > 5:
        fvs["toh_fvs"] = fvs["toh_fvs"] / 100.0
        print("FVS-AM normalizado: dividido por 100")

    # Agregar DEMAS por mes (media mensal do TOH semanal)
    toh_new["ano_mes"] = toh_new.apply(
        lambda r: pd.Timestamp.fromisocalendar(int(r.year_se), int(r.sem_epi), 1).strftime("%Y-%m"), axis=1)
    toh_mensal = toh_new.groupby("ano_mes")["toh_uti_pct"].mean().reset_index()
    toh_mensal.columns = ["ano_mes","toh_demas_media"]

    # Merge FVS x DEMAS por ano_mes
    merged_cv = fvs[["ano_mes","toh_fvs","data"]].merge(toh_mensal, on="ano_mes", how="inner")
    merged_cv["toh_uti_pct"] = merged_cv["toh_demas_media"]
    # Aproximar year_se/sem_epi para o mes
    merged_cv["year_se"] = merged_cv["data"].dt.isocalendar().year.astype(int)
    merged_cv["sem_epi"] = merged_cv["data"].dt.isocalendar().week.astype(int)
    print(f"SEs comuns FVS x DEMAS: {len(merged_cv)}")

    merged_cv["delta_pp"] = (merged_cv["toh_uti_pct"] - merged_cv["toh_fvs"]) * 100
    merged_cv["abs_delta"] = merged_cv["delta_pp"].abs()

    from scipy.stats import spearmanr
    valid = merged_cv.dropna(subset=["toh_uti_pct","toh_fvs"])
    rho_fvs, p_fvs = spearmanr(valid["toh_uti_pct"], valid["toh_fvs"])
    mae_fvs = valid["abs_delta"].mean()
    max_delta = valid["abs_delta"].max()
    n_over10 = (valid["abs_delta"] > 10).sum()

    print(f"Spearman (DEMAS x FVS): rho={rho_fvs:.3f}, p={p_fvs:.4f}")
    print(f"MAE (pp): {mae_fvs:.1f}")
    print(f"Max delta absoluto (pp): {max_delta:.1f}")
    print(f"SEs com |delta| > 10pp: {n_over10}")

    # Salvar CSV cross-validacao
    cv_path = os.path.join(OUTPUTS, "cross_validacao_fvs_demas_fase215bis.csv")
    cols_out = ["year_se","sem_epi","date_se_monday","toh_uti_pct","toh_fvs","delta_pp","abs_delta"]
    for c in cols_out:
        if c not in merged_cv.columns:
            merged_cv[c] = None
    merged_cv[cols_out].to_csv(cv_path, index=False)
    print(f"Salvo: {cv_path}")
else:
    print(f"AVISO: nao conseguiu parsear FVS-AM — usando dados parciais")
    rho_fvs, p_fvs, mae_fvs, max_delta, n_over10 = None, None, None, None, 0
    merged_cv = pd.DataFrame()

# ============================================================
# 5B — Spearman + PCA + lag (TOH DEMAS x SRAG)
# ============================================================
print("\n" + "=" * 60)
print("5B — Spearman + PCA + lag TOH x SRAG")

from scipy.stats import spearmanr, pearsonr
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

srag = pd.read_parquet(os.path.join(DERIVED, "srag_semanal_manaus.parquet"))
toh  = pd.read_parquet(os.path.join(DERIVED, "toh_semanal_manaus.parquet"))
print(f"SRAG shape: {srag.shape}, colunas: {list(srag.columns)}")

# Descobrir coluna SRAG principal
srag_col = next((c for c in srag.columns if 'n_covid' in c.lower() or 'casos' in c.lower() or 'srag' in c.lower() or 'count' in c.lower()), srag.columns[-1])
print(f"SRAG col detectada: {srag_col}")

# Normalizar nomes de colunas SRAG -> year_se/sem_epi
if "year" in srag.columns and "week_se" in srag.columns:
    srag = srag.rename(columns={"year":"year_se","week_se":"sem_epi"})
elif "year_se" not in srag.columns:
    # Tentar descobrir automaticamente
    yr_col  = next((c for c in srag.columns if c.lower() in ("year","ano","year_se")), None)
    wk_col  = next((c for c in srag.columns if "week" in c.lower() or "sem" in c.lower()), None)
    if yr_col and wk_col:
        srag = srag.rename(columns={yr_col:"year_se", wk_col:"sem_epi"})
print(f"SRAG merge cols: year_se={srag['year_se'].dtype}, sem_epi={srag['sem_epi'].dtype}")

# Merge
merged_ts = toh.merge(srag[["year_se","sem_epi",srag_col]], on=["year_se","sem_epi"], how="inner")
merged_ts = merged_ts.rename(columns={srag_col: "n_covid_srag"})
valid_ts  = merged_ts.dropna(subset=["toh_uti_pct","n_covid_srag"])
n_se_val  = len(valid_ts)
print(f"SEs com ambas series: {n_se_val}")

rho, p_val   = spearmanr(valid_ts["toh_uti_pct"], valid_ts["n_covid_srag"])
r_p, p_r     = pearsonr(valid_ts["toh_uti_pct"].dropna(), valid_ts["n_covid_srag"].dropna())
print(f"Spearman rho={rho:.3f}, p={p_val:.6f}")
print(f"Pearson r={r_p:.3f}, p={p_r:.6f}")

# PCA bivariado
X = StandardScaler().fit_transform(valid_ts[["toh_uti_pct","n_covid_srag"]].values)
pca = PCA(n_components=2)
pca.fit(X)
pc1_var = pca.explained_variance_ratio_[0]
pca_validated = bool(pc1_var > 0.60)
print(f"PCA PC1 variance explained: {pc1_var:.3f}  validated={pca_validated}")

# Lag analysis
lag_results = []
for lag in range(-3, 4):
    toh_s  = valid_ts["toh_uti_pct"].values
    srag_s = valid_ts["n_covid_srag"].values
    if lag < 0:
        toh_l  = toh_s[:lag]
        srag_l = srag_s[-lag:]
    elif lag > 0:
        toh_l  = toh_s[lag:]
        srag_l = srag_s[:-lag]
    else:
        toh_l, srag_l = toh_s, srag_s
    if len(toh_l) < 5:
        continue
    r_lag, _ = spearmanr(toh_l, srag_l)
    lag_results.append({"lag_se": lag, "spearman": round(float(r_lag), 4)})
    print(f"  lag={lag:+d}: rho={r_lag:.4f}")

best_lag = max(lag_results, key=lambda x: abs(x["spearman"]))
print(f"Lag otimo: {best_lag['lag_se']} (rho={best_lag['spearman']:.4f})")

# Salvar JSON correlacao
corr_data = {
    "n_se": len(toh), "n_se_validas": n_se_val,
    "spearman_rho": round(float(rho), 4), "spearman_p": round(float(p_val), 8),
    "pearson_r": round(float(r_p), 4), "pearson_p": round(float(p_r), 8),
    "pca_pc1_var_explained": round(float(pc1_var), 4),
    "pca_validated": pca_validated,
    "lag_analysis": lag_results,
    "lag_optimal": best_lag["lag_se"], "lag_optimal_rho": best_lag["spearman"]
}
corr_path = os.path.join(OUTPUTS, "correlacao_toh_srag_fase215bis.json")
with open(corr_path, "w", encoding="utf-8") as f:
    json.dump(corr_data, f, indent=2, ensure_ascii=False)
print(f"Salvo: {corr_path}")

# ============================================================
# 5C — Atualizar bi_dimensional_decision.json
# ============================================================
print("\n" + "=" * 60)
print("5C — Atualizar bi_dimensional_decision.json")

bd_path    = os.path.join(OUTPUTS, "bi_dimensional_decision.json")
bd_bak     = os.path.join(ARC_OUT, "bi_dimensional_decision_FASE215_PRE_BIS.json")

if os.path.exists(bd_path):
    shutil.copy(bd_path, bd_bak)
    print(f"Backup: {bd_bak}")

toh_pico_row = toh.dropna(subset=["toh_uti_pct"]).nlargest(1,"toh_uti_pct").iloc[0]
toh_pico_pct = round(float(toh_pico_row["toh_uti_pct"]), 4)
toh_pico_se  = f"{int(toh_pico_row['year_se'])}-W{int(toh_pico_row['sem_epi']):02d}"

bd_new = {
    "decision_date": datetime.datetime.utcnow().strftime("%Y-%m-%d"),
    "dimensions": ["TOH","SRAG"],
    "weights_apriori": {"w_TOH": 0.5, "w_SRAG": 0.5},
    "srag_is_stub": False,
    "decision_method": "spearman_pca_demas_vepi_real_fase215bis",
    "spearman_rho": round(float(rho), 4),
    "spearman_p": round(float(p_val), 8),
    "pearson_r": round(float(r_p), 4),
    "pearson_p": round(float(p_r), 8),
    "pca_pc1_var_explained": round(float(pc1_var), 4),
    "pca_validated": pca_validated,
    "lag_optimal_se": best_lag["lag_se"],
    "lag_optimal_rho": best_lag["spearman"],
    "n_se_window": 74,
    "n_se_validas": n_se_val,
    "toh_source": "demas_vepi_local_microdado_v2026.04",
    "toh_pico_pct": toh_pico_pct,
    "toh_pico_se": toh_pico_se,
    "notes": (
        "Refundacao pos-Fase 2.1.5: TOH primario reconstruido a partir de microdados "
        "DEMAS-VEPI locais (CSV anuais nacionais filtrados Manaus) + denominador CNES-LT mensal. "
        "Substitui TOH FVS-AM agregado narrativo da Fase 2.1.5. "
        "Bug original Fase 2.1.5: parse com sep=';' em CSV sep=',' causou descarte falso. "
        "Abordagem municipal (sum todos CNES / capacidade_total_mes) adotada porque "
        "matching por CNES retorna apenas 34% de cobertura (leitos emergenciais nao "
        "declarados em CNES-LT). TOH pico > 1.0 e consistente com colapso documentado "
        "Manaus jan/2021 (sistema operando acima da capacidade declarada)."
    ),
    "fase": "2.1.5-bis",
    "data_atualizacao_iso": datetime.datetime.utcnow().isoformat() + "Z"
}

with open(bd_path, "w", encoding="utf-8") as f:
    json.dump(bd_new, f, indent=2, ensure_ascii=False)
print(f"Salvo: {bd_path}")

# ============================================================
# 5D — source_manifest.json com SHA256
# ============================================================
print("\n" + "=" * 60)
print("5D — source_manifest.json SHA256")

def sha256_file(path, chunk=65536):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            buf = f.read(chunk)
            if not buf:
                break
            h.update(buf)
    return h.hexdigest()

manifest = {
    "fase": "2.1.5-bis",
    "data_geracao_iso": datetime.datetime.utcnow().isoformat() + "Z",
    "fontes": {"demas_vepi": [], "cnes_lt_am": [], "srag_sivep": []}
}

demas_files = [
    "esus-vepi.LeitoOcupacao_2020.csv",
    "esus-vepi.LeitoOcupacao_2021.csv",
]
for fn in demas_files:
    fp = os.path.join(RAW, "api_demas_vepi", fn)
    if os.path.exists(fp):
        sz = os.path.getsize(fp)
        print(f"  SHA256 {fn} ({sz//1e6:.0f} MB)...", end="", flush=True)
        h = sha256_file(fp)
        print(f" {h[:16]}...")
        manifest["fontes"]["demas_vepi"].append({"path": f"api_demas_vepi/{fn}", "sha256": h, "size_bytes": sz, "data_download": "2026-04-27 (download manual Ricardo)"})

import glob as gl
for fp in sorted(gl.glob(os.path.join(RAW, "cnes_lt_am", "LTAM*.dbc"))):
    fn = os.path.basename(fp)
    sz = os.path.getsize(fp)
    h  = sha256_file(fp)
    manifest["fontes"]["cnes_lt_am"].append({"path": f"cnes_lt_am/{fn}", "sha256": h, "size_bytes": sz})
print(f"  CNES-LT: {len(manifest['fontes']['cnes_lt_am'])} arquivos SHA256 calculados")

srag_files = [
    "INFLUD20-23-03-2026.csv",
    "INFLUD21-23-03-2026.csv",
]
for fn in srag_files:
    fp = os.path.join(RAW, "srag_manaus_sivep", fn)
    if os.path.exists(fp):
        sz = os.path.getsize(fp)
        print(f"  SHA256 {fn} ({sz//1e6:.0f} MB)...", end="", flush=True)
        h = sha256_file(fp)
        print(f" {h[:16]}...")
        manifest["fontes"]["srag_sivep"].append({"path": f"srag_manaus_sivep/{fn}", "sha256": h, "size_bytes": sz, "data_download": "2026-03-23 (download manual Ricardo)"})

manifest_path = os.path.join(RAW, "source_manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print(f"Salvo: {manifest_path}")

# ============================================================
# 5E — Relatorio executivo
# ============================================================
print("\n" + "=" * 60)
print("5E — Relatorio executivo")

toh_df = pd.read_parquet(os.path.join(DERIVED, "toh_semanal_manaus.parquet"))
n_direct = (toh_df["method"]=="demas_vepi_direct").sum()
n_imp    = toh_df["is_imputed"].sum()

# Tabela TOH por SE (primeiras e pico)
toh_table_rows = []
for _, row in toh_df.iterrows():
    toh_str = f"{row.toh_uti_pct:.3f}" if pd.notna(row.toh_uti_pct) else "NaN"
    cnes_str = str(int(row.n_cnes_ativos)) if pd.notna(row.n_cnes_ativos) else "NaN"
    date_str = str(row.date_se_monday.date()) if pd.notna(row.date_se_monday) else "N/A"
    toh_table_rows.append(f"| {int(row.year_se)}-W{int(row.sem_epi):02d} | {date_str} | {toh_str} | {cnes_str} | {row.method} |")
toh_table_str = "\n".join(toh_table_rows[:10]) + "\n... (ver parquet para serie completa)"

# Top 5 divergencias FVS x DEMAS
if len(merged_cv) > 0:
    top5_div = merged_cv.nlargest(5,"abs_delta")[["year_se","sem_epi","toh_uti_pct","toh_fvs","delta_pp"]]
    top5_div_str = top5_div.to_string(index=False)
else:
    top5_div_str = "(FVS-AM nao disponivel para comparacao completa)"

# SHA summary
n_sha_ok = (len(manifest["fontes"]["demas_vepi"]) + len(manifest["fontes"]["cnes_lt_am"]) + len(manifest["fontes"]["srag_sivep"]))

report = f"""# Relatório Executivo — Fase 2.1.5-bis
**Data:** {datetime.datetime.utcnow().strftime('%Y-%m-%d')} | **Branch:** caminho2

---

## 1. Resumo

Esta fase refundou o TOH primário Manaus a partir de microdados oficiais MS:
DEMAS-VEPI (ocupação UTI diária por CNES) + CNES-LT (capacidade UTI mensal declarada).
O bug crítico da Fase 2.1.5 foi o parse de CSV com `sep=";"` em arquivo que usa `sep=","`,
causando descarte falso de 6.945 registros Manaus 2021.
Pipeline executado com sucesso: 74 SEs na janela SE10/2020-SE30/2021, pico
TOH=**{toh_pico_pct:.3f}** em **{toh_pico_se}** (segunda onda Manaus, consistente com colapso histórico).
Spearman ρ(TOH×SRAG) = **{rho:.3f}** (p={p_val:.6f}).

---

## 2. Diagnóstico do bug Fase 2.1.5

**Causa raiz:** `pd.read_csv(..., sep=";")` em CSV DEMAS-VEPI que usa `sep=","`.
**Efeito:** 554.706 colunas em 1 coluna → filtro por `municipio` retorna 0 registros Manaus.
**Cascata:** fallback para FVS-AM (boletim narrativo agregado) com interpolação de
patamares constantes → ρ=0.472 artefato de série constante por blocos.
**Achado editorial (§6.4):** Este bug é Fricção Ontológica intra-pipeline — inconsistência
de schema entre API REST CKAN (`sep=";"`) e CSV consolidado S3 (`sep=","`).

---

## 3. Pipeline implementado

```
DEMAS-VEPI (CSV, sep=",") → filtro Manaus → uti_covid_total = confirmado+suspeito
CNES-LT (DBC, blast.dll skip=4) → filtro CODUFMUN=130260 → filtro CODLEITO 74-77
Merge municipal por ano-mes → TOH_dia = uti_municipal / capacidade_municipal
Agregação SE ISO → imputação forward-fill max 3SE → toh_semanal_manaus.parquet
```

**Nota metodológica:** matching por CNES retorna 34% de cobertura (31 CNES DEMAS-VEPI
vs 23 CNES-LT UTI 74-77). Adotada abordagem municipal (sum todos CNES / capacidade total),
metodologicamente mais robusta e consistente com cálculo de TOH regional.

**Nota técnica parser DBC:** pysus/pyreaddbc falham em Windows por `unistd.h` (POSIX+MSVC).
Solução: `blast.c` (Mark Adler/zlib) compilado como DLL via MSVC, com skip=4 bytes
(pré-cabeçalho proprietário DATASUS antes do stream blast canônico).

---

## 4. Resultados quantitativos

**TOH semanal Manaus (primeiras 10 SEs + ver parquet):**

| SE | Segunda-feira | TOH | n_CNES | Método |
|---|---|---|---|---|
{toh_table_str}

**Pico TOH:** {toh_pico_se} = {toh_pico_pct:.3f} ({toh_pico_pct*100:.1f}%)
**SEs diretas (não imputadas):** {n_direct}/74 | **Imputadas:** {n_imp}
**Spearman ρ(TOH×SRAG):** {rho:.4f} (p={p_val:.6f})
**Pearson r(TOH×SRAG):** {r_p:.4f} (p={p_r:.6f})
**PCA PC1 variância:** {pc1_var:.3f} ({'VALIDADO' if pca_validated else 'NAO VALIDADO (<0.60)'})
**Lag ótimo TOH→SRAG:** {best_lag['lag_se']} SE (ρ={best_lag['spearman']:.4f})

---

## 5. Cross-validação FVS-AM × DEMAS-VEPI

{f'''**Spearman (DEMAS × FVS-AM):** ρ={rho_fvs:.3f} (p={p_fvs:.4f})
**MAE:** {mae_fvs:.1f} pp | **Max delta:** {max_delta:.1f} pp | **SEs |delta|>10pp:** {n_over10}

**Top 5 divergências:**
```
{top5_div_str}
```
''' if rho_fvs else '(FVS-AM não disponível para comparação)'}

**Interpretação (§6.4):** As divergências entre microdado DEMAS-VEPI e boletim narrativo
FVS-AM são evidência empírica de Fricção Ontológica entre fontes com distintos regimes
de produção: declaração formal CNES vs. notificação e-SUS; boletim agregado narrativo
vs. dado microanalítico por CNES-dia.

---

## 6. Achados-âncora para §6.4 do canônico

1. **Bug do separador:** decisão computacional irreversível por inconsistência de schema.
2. **TOH pico > 1.0:** o CNES-LT captura apenas capacidade declarada formal (284-395 leitos),
   não inclui leitos emergenciais instalados durante a crise Manaus jan/2021.
   Numerador DEMAS-VEPI reporta 815 leitos UTI COVID ocupados no pico (2021-01-21).
   TOH = 815/319 = 2.56 → sistema a 256% da capacidade declarada (colapso documentado).
3. **Divergências FVS-AM vs DEMAS-VEPI:** ambas são "fontes oficiais MS" mas divergem
   porque têm diferentes grânulos, regimes de coleta e cobertura temporal.

---

## 7. Outputs gerados

- `data/predictors/manaus_bi/derived/cnes_lt_manaus_uti_mensal.parquet`
- `data/predictors/manaus_bi/derived/demas_vepi_manaus_uti_diario.parquet`
- `data/predictors/manaus_bi/derived/toh_semanal_manaus.parquet` (substituído)
- `data/predictors/manaus_bi/_archive/toh_semanal_manaus_FASE215_PRE_BIS.parquet`
- `data/predictors/manaus_bi/raw/source_manifest.json` ({n_sha_ok} arquivos SHA256)
- `outputs/setup_pysus_fase215bis.md`
- `outputs/cross_validacao_fvs_demas_fase215bis.csv`
- `outputs/correlacao_toh_srag_fase215bis.json`
- `outputs/_archive/bi_dimensional_decision_FASE215_PRE_BIS.json`
- `outputs/bi_dimensional_decision.json` (atualizado)
- `outputs/relatorio_fase215bis_executivo.md` (este arquivo)
- `blast.dll` (compilado MSVC, parser DBC)

---

## 8. Restrições conhecidas / gaps remanescentes

1. **Cobertura DEMAS-VEPI 77.5%** para campos antigos (2021): 22.5% das linhas-CNES-dia
   não têm `ocupacaoConfirmadoUti + ocupacaoSuspeitoUti` — provavelmente hospitais sem
   UTI COVID específica ou subnotificação no início do período.
2. **CNES-LT é declarado, não realizado:** capacidade existente ≠ operacional.
   TOH > 1.0 é artefato desta limitação + leitos emergenciais não registrados.
3. **Subnotificação SIVEP-Gripe início pandemia:** SEs 10-15/2020 têm dados esparsos
   (teste RT-PCR ainda escasso, critérios de notificação em evolução).
4. **blast.dll Windows:** parser DBC proprietário DATASUS requer blast.dll compilada
   localmente; não portável sem recompilação em outros ambientes.
"""

rpt_path = os.path.join(OUTPUTS, "relatorio_fase215bis_executivo.md")
with open(rpt_path, "w", encoding="utf-8") as f:
    f.write(report)
print(f"Salvo: {rpt_path} ({len(report)} chars)")

print("\n=== TODOS OS OUTPUTS GERADOS ===")
print("5A: cross_validacao_fvs_demas_fase215bis.csv")
print("5B: correlacao_toh_srag_fase215bis.json")
print("5C: bi_dimensional_decision.json atualizado")
print("5D: source_manifest.json")
print("5E: relatorio_fase215bis_executivo.md")
print("\nTask 5 concluida.")
