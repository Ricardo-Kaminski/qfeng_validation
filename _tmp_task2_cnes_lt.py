"""
Tarefa 2 — Pipeline denominador: CNES-LT → UTI mensal Manaus
Parseia 24 arquivos LTAM*.dbc, filtra Manaus + UTI adulto, salva parquet.
"""
import sys, os, struct, ctypes, re, glob
import pandas as pd
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DLL_PATH  = r"C:\Workspace\academico\qfeng_validacao\blast.dll"
DBC_DIR   = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\raw\cnes_lt_am"
OUT_PATH  = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\derived\cnes_lt_manaus_uti_mensal.parquet"
BLAST_SKIP = 4
UTI_ADULT_CODES = {'74','75','76','77'}

# ---------- blast setup ----------
lib = ctypes.CDLL(DLL_PATH)
lib.blast_decompress_skip.restype  = ctypes.POINTER(ctypes.c_ubyte)
lib.blast_decompress_skip.argtypes = [
    ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
]
lib.blast_free.restype  = None
lib.blast_free.argtypes = [ctypes.POINTER(ctypes.c_ubyte)]

def read_dbc(path):
    with open(path, "rb") as f:
        raw = f.read()
    n_records   = struct.unpack_from('<I', raw, 4)[0]
    header_size = struct.unpack_from('<H', raw, 8)[0]
    record_size = struct.unpack_from('<H', raw, 10)[0]
    fields = []
    off = 32
    while raw[off] != 0x0D and off < header_size:
        fname = raw[off:off+11].split(b'\x00')[0].decode('latin1').strip()
        ftype = chr(raw[off+11])
        flen  = raw[off+16]
        fields.append({'name': fname, 'type': ftype, 'len': flen})
        off += 32
    compressed = raw[header_size:]
    in_buf = (ctypes.c_ubyte * len(compressed)).from_buffer_copy(compressed)
    out_sz = ctypes.c_size_t(0)
    out_ptr = lib.blast_decompress_skip(in_buf, len(compressed), BLAST_SKIP, ctypes.byref(out_sz))
    if not out_ptr:
        raise RuntimeError(f"blast falhou: {out_sz.value}")
    data = bytes(out_ptr[:out_sz.value])
    lib.blast_free(out_ptr)
    records = []
    for ri in range(n_records):
        roff = ri * record_size
        if roff + record_size > len(data):
            break
        rec_raw = data[roff:roff + record_size]
        if rec_raw[0] == ord('*'):
            continue
        rec = {}
        foff = 1
        for fd in fields:
            val = rec_raw[foff:foff + fd['len']].decode('latin1', errors='replace').strip()
            rec[fd['name']] = val
            foff += fd['len']
        records.append(rec)
    return pd.DataFrame(records)

# ---------- processar 24 arquivos ----------
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
dbc_files = sorted(glob.glob(os.path.join(DBC_DIR, "LTAM*.dbc")))
print(f"Arquivos DBC encontrados: {len(dbc_files)}")

all_monthly = []
log_rows = []

for dbc_path in dbc_files:
    fname = os.path.basename(dbc_path)
    # LTAMYYMM.dbc → ano_mes
    m = re.match(r'LTAM(\d{2})(\d{2})\.dbc', fname, re.IGNORECASE)
    if not m:
        print(f"  Nome inesperado: {fname} — pulando")
        continue
    yy, mm = m.group(1), m.group(2)
    ano = int('20' + yy)
    ano_mes = f"{ano}-{mm}"

    print(f"\n[{fname}] {ano_mes}:")
    df = read_dbc(dbc_path)
    n_total = len(df)
    print(f"  Total registros: {n_total}")

    # Filtrar Manaus — CODUFMUN startswith '130260'
    df_mun = df[df['CODUFMUN'].str.startswith('130260', na=False)].copy()
    n_manaus = len(df_mun)
    print(f"  Apos filtro Manaus (CODUFMUN~130260): {n_manaus} (de {n_total})")

    # Filtrar UTI adulto
    df_uti = df_mun[df_mun['CODLEITO'].isin(UTI_ADULT_CODES)].copy()
    n_uti = len(df_uti)
    print(f"  Apos filtro UTI adulto (CODLEITO 74-77): {n_uti}")

    if n_uti == 0:
        print(f"  AVISO: nenhum leito UTI adulto em {ano_mes} — CODLEITO unique: {df_mun['CODLEITO'].unique()[:10].tolist()}")

    # Cast numericos
    for col in ['QT_EXIST', 'QT_SUS', 'QT_CONTR', 'QT_NSUS']:
        if col in df_uti.columns:
            df_uti[col] = pd.to_numeric(df_uti[col], errors='coerce')

    # Agregar por CNES
    if n_uti > 0:
        grp = df_uti.groupby('CNES').agg(
            qt_uti_existente_total=('QT_EXIST', 'sum'),
            qt_uti_existente_sus=('QT_SUS', 'sum') if 'QT_SUS' in df_uti.columns else ('QT_EXIST', 'first'),
            n_tipos_leito_uti=('CODLEITO', 'nunique'),
            n_registros_origem=('CNES', 'count'),
        ).reset_index()
        grp['ano_mes'] = ano_mes
        grp['competencia'] = pd.Timestamp(f"{ano}-{mm}-01")
        grp['source_file'] = fname
        all_monthly.append(grp)
        print(f"  CNES Manaus com UTI: {len(grp)}, total leitos UTI: {grp['qt_uti_existente_total'].sum()}")

    log_rows.append({
        'ano_mes': ano_mes,
        'n_cnes_manaus': n_manaus,
        'total_uti_existente': df_uti['QT_EXIST'].apply(pd.to_numeric, errors='coerce').sum() if n_uti > 0 else 0,
        'total_uti_sus': df_uti['QT_SUS'].apply(pd.to_numeric, errors='coerce').sum() if 'QT_SUS' in df_uti.columns and n_uti > 0 else 0,
        'n_cnes_com_uti': n_uti,
    })

# ---------- consolidar ----------
if not all_monthly:
    print("\nERRO: nenhum dado UTI coletado!")
    sys.exit(1)

df_out = pd.concat(all_monthly, ignore_index=True)

# Garantir schema
col_order = ['ano_mes','competencia','cnes','qt_uti_existente_total','qt_uti_existente_sus',
             'n_tipos_leito_uti','n_registros_origem','source_file']
df_out = df_out.rename(columns={'CNES':'cnes'})
for c in col_order:
    if c not in df_out.columns:
        df_out[c] = None
df_out = df_out[col_order]

df_out.to_parquet(OUT_PATH, index=False)
print(f"\nSalvo: {OUT_PATH}")
print(f"Shape: {df_out.shape}")

# ---------- sanity checks ----------
print("\n=== SANITY CHECKS ===")
meses = df_out['ano_mes'].nunique()
s1 = meses == 24
print(f"24 meses presentes: {'OK' if s1 else 'FALHA'} ({meses})")

min_cnes_per_month = df_out.groupby('ano_mes')['cnes'].nunique().min()
s2 = min_cnes_per_month >= 5
print(f"Min 5 CNES/mes com UTI: {'OK' if s2 else 'FALHA'} ({min_cnes_per_month})")

cap_jan2020 = df_out[df_out['ano_mes']=='2020-01']['qt_uti_existente_total'].sum()
cap_jul2021 = df_out[df_out['ano_mes']=='2021-07']['qt_uti_existente_total'].sum()
s3 = cap_jan2020 <= cap_jul2021
print(f"Capacidade jan/2020 <= jul/2021: {'OK' if s3 else 'FALHA'} ({cap_jan2020} <= {cap_jul2021})")

# Pico esperado dez/2020-mar/2021
peak_months = ['2020-12','2021-01','2021-02','2021-03']
cap_by_month = df_out.groupby('ano_mes')['qt_uti_existente_total'].sum()
peak_val = cap_by_month[peak_months].max()
peak_month = cap_by_month[peak_months].idxmax()
print(f"Pico capacidade em {peak_month}: {peak_val} leitos")

# Tabela log
print("\n--- Tabela mensal (ano_mes | n_cnes_manaus | total_uti | total_sus) ---")
for r in log_rows:
    print(f"  {r['ano_mes']} | {r['n_cnes_manaus']:3d} CNES | {r['total_uti_existente']:4.0f} UTI | {r['total_uti_sus']:4.0f} SUS")

all_ok = s1 and s2 and s3
print(f"\nRESULTADO: {'PASSOU' if all_ok else 'FALHOU — ver avisos acima'}")
