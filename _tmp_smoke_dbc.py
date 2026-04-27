"""Smoke test completo do leitor DBC via blast.dll (skip=4)."""
import sys, struct, ctypes, os
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DLL_PATH = r"C:\Workspace\academico\qfeng_validacao\blast.dll"
DBC_PATH = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\raw\cnes_lt_am\LTAM2001.dbc"
BLAST_SKIP = 4  # bytes de pre-header DATASUS antes do stream blast

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

    # Field descriptors
    fields = []
    off = 32
    while raw[off] != 0x0D and off < header_size:
        fname = raw[off:off+11].split(b'\x00')[0].decode('latin1').strip()
        ftype = chr(raw[off+11])
        flen  = raw[off+16]
        fields.append({'name': fname, 'type': ftype, 'len': flen})
        off += 32

    # Descomprimir
    compressed = raw[header_size:]
    in_buf = (ctypes.c_ubyte * len(compressed)).from_buffer_copy(compressed)
    out_sz = ctypes.c_size_t(0)
    out_ptr = lib.blast_decompress_skip(in_buf, len(compressed), BLAST_SKIP, ctypes.byref(out_sz))
    if not out_ptr:
        raise RuntimeError(f"blast falhou: {out_sz.value}")
    data = bytes(out_ptr[:out_sz.value])
    lib.blast_free(out_ptr)

    # Parsear records
    records = []
    for ri in range(n_records):
        roff = ri * record_size
        if roff + record_size > len(data):
            break
        rec_raw = data[roff:roff + record_size]
        if rec_raw[0] == ord('*'):  # deletado
            continue
        rec = {}
        foff = 1
        for fd in fields:
            val = rec_raw[foff:foff + fd['len']].decode('latin1', errors='replace').strip()
            rec[fd['name']] = val
            foff += fd['len']
        records.append(rec)

    return fields, records

print(f"Lendo: {DBC_PATH}")
fields, records = read_dbc(DBC_PATH)

n_linhas = len(records)
n_cols   = len(fields)
lista_colunas = [f['name'] for f in fields]

print(f"\nn_linhas: {n_linhas}")
print(f"n_cols:   {n_cols}")
print(f"\nlista_colunas:\n  {lista_colunas}")

print(f"\nPrimeiras 3 linhas:")
for r in records[:3]:
    print(f"  {r}")

# Distribuicao CODUFMUN
codufmun = [r.get('CODUFMUN', '') for r in records]
dist_mun = Counter(codufmun)
manaus_recs = sum(v for k, v in dist_mun.items() if k.startswith('130260') or k == '130260')
print(f"\nCODUFMUN top 10: {dist_mun.most_common(10)}")
print(f"Manaus (CODUFMUN startswith 130260): {manaus_recs} registros")

# Distribuicao CODLEITO
codleito = [r.get('CODLEITO', '') for r in records]
dist_leito = Counter(codleito)
uti_codes = {str(c) for c in range(74, 84)}
uti_recs = sum(v for k, v in dist_leito.items() if k in uti_codes)
print(f"\nCODLEITO top 15: {dist_leito.most_common(15)}")
print(f"UTI adulto (74-83): {uti_recs} registros")

# Sanity checks
print("\n=== SANITY CHECKS ===")
s1 = n_linhas > 100
s2 = n_cols >= 28
mun_ok = any(k.startswith('130260') for k in dist_mun)
uti_ok = any(k in uti_codes for k in dist_leito)
print(f"n_linhas > 100:            {'OK' if s1 else 'FALHA'} ({n_linhas})")
print(f"n_cols >= 28:              {'OK' if s2 else 'FALHA'} ({n_cols})")
print(f"CODUFMUN contem Manaus:    {'OK' if mun_ok else 'FALHA'}")
print(f"CODLEITO contem UTI 74-83: {'OK' if uti_ok else 'FALHA'}")

all_ok = s1 and s2 and mun_ok and uti_ok
print(f"\nRESULTADO: {'PASSOU' if all_ok else 'FALHOU'}")
