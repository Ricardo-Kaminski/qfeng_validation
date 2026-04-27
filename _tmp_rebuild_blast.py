"""Recompila blast.dll e testa com diferentes offsets."""
import sys, os, struct, subprocess, tempfile, urllib.request, ctypes, shutil
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

dst_dll = r"C:\Workspace\academico\qfeng_validacao\blast.dll"
build_dir = tempfile.mkdtemp(prefix="blast2_")

# Baixar blast.c e blast.h
for fname, url in [
    ("blast.c", "https://raw.githubusercontent.com/madler/zlib/master/contrib/blast/blast.c"),
    ("blast.h", "https://raw.githubusercontent.com/madler/zlib/master/contrib/blast/blast.h"),
]:
    dst = os.path.join(build_dir, fname)
    urllib.request.urlretrieve(url, dst)
    print(f"{fname}: {os.path.getsize(dst)} bytes")

# Wrapper C com suporte a skip
wrapper_c = r"""
#include "blast.h"
#include <string.h>
#include <stdlib.h>

typedef struct { const unsigned char *data; size_t pos; size_t size; } InState;
typedef struct { unsigned char *data; size_t pos; size_t capacity; } OutState;

static unsigned in_func(void *how, unsigned char **buf) {
    InState *s = (InState*)how;
    if (s->pos >= s->size) return 0;
    size_t avail = s->size - s->pos;
    if (avail > 4096) avail = 4096;
    *buf = (unsigned char*)(s->data + s->pos);
    s->pos += avail;
    return (unsigned)avail;
}
static int out_func(void *how, unsigned char *buf, unsigned len) {
    OutState *s = (OutState*)how;
    if (s->pos + len > s->capacity) {
        size_t nc = s->capacity * 2 + len;
        unsigned char *nd = (unsigned char*)realloc(s->data, nc);
        if (!nd) return 1;
        s->data = nd; s->capacity = nc;
    }
    memcpy(s->data + s->pos, buf, len);
    s->pos += len;
    return 0;
}

/* blast_decompress: skip = bytes to skip before blast stream */
__declspec(dllexport) unsigned char* blast_decompress_skip(
    const unsigned char *in_data, size_t in_size, size_t skip, size_t *out_size)
{
    if (skip >= in_size) { *out_size = (size_t)-1; return NULL; }
    InState in_s = {in_data + skip, 0, in_size - skip};
    OutState out_s;
    out_s.capacity = (in_size - skip) * 12 + 4096;
    out_s.data = (unsigned char*)malloc(out_s.capacity);
    out_s.pos = 0;
    if (!out_s.data) { *out_size = (size_t)-2; return NULL; }
    int ret = blast(in_func, &in_s, out_func, &out_s, NULL, NULL);
    if (ret != 0) { free(out_s.data); *out_size = (size_t)ret; return NULL; }
    *out_size = out_s.pos;
    return out_s.data;
}
__declspec(dllexport) void blast_free(unsigned char *ptr) { free(ptr); }
"""

with open(os.path.join(build_dir, "blast_wrap.c"), "w") as f:
    f.write(wrapper_c)

vcvars = r"C:\Program Files\Microsoft Visual Studio\18\Community\VC\Auxiliary\Build\vcvars64.bat"
bat = f'@echo off\ncall "{vcvars}"\ncd /d "{build_dir}"\ncl.exe /LD /Fe:blast.dll /O2 /nologo blast_wrap.c blast.c\n'
bat_path = os.path.join(build_dir, "build.bat")
with open(bat_path, "w") as f:
    f.write(bat)

r = subprocess.run(["cmd.exe", "/c", bat_path], capture_output=True, text=True, encoding='cp1252', errors='replace')
dll_tmp = os.path.join(build_dir, "blast.dll")
if not os.path.exists(dll_tmp):
    print("FALHA compilação:\n", r.stdout[-1000:], r.stderr[-500:])
    sys.exit(1)

shutil.copy(dll_tmp, dst_dll)
print(f"\nDLL salva: {dst_dll} ({os.path.getsize(dst_dll):,} bytes)")

# Testar
lib = ctypes.CDLL(dst_dll)
lib.blast_decompress_skip.restype  = ctypes.POINTER(ctypes.c_ubyte)
lib.blast_decompress_skip.argtypes = [
    ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
]
lib.blast_free.restype  = None
lib.blast_free.argtypes = [ctypes.POINTER(ctypes.c_ubyte)]

dbc_path = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\raw\cnes_lt_am\LTAM2001.dbc"
with open(dbc_path, "rb") as f:
    raw = f.read()

header_size = struct.unpack_from('<H', raw, 8)[0]
n_records   = struct.unpack_from('<I', raw, 4)[0]
record_size = struct.unpack_from('<H', raw, 10)[0]
expected_sz = n_records * record_size
compressed  = raw[header_size:]
print(f"n_records={n_records}, record_size={record_size}, expected={expected_sz}")

in_buf = (ctypes.c_ubyte * len(compressed)).from_buffer_copy(compressed)

for skip in [0, 2, 4, 8]:
    out_sz = ctypes.c_size_t(0)
    out_ptr = lib.blast_decompress_skip(in_buf, len(compressed), skip, ctypes.byref(out_sz))
    sz = out_sz.value
    if out_ptr:
        data = bytes(out_ptr[:sz])
        lib.blast_free(out_ptr)
        match = "MATCH" if sz == expected_sz else f"sz={sz} (esperado {expected_sz})"
        print(f"skip={skip}: OK {sz} bytes — {match}")
        if sz == expected_sz:
            # Parsear 3 primeiros registros
            fields = []
            off2 = 32
            while raw[off2] != 0x0D:
                fname = raw[off2:off2+11].split(b'\x00')[0].decode('latin1').strip()
                flen = raw[off2+16]
                fields.append({'name': fname, 'len': flen})
                off2 += 32
            for ri in range(min(3, n_records)):
                roff = ri * record_size
                rec = {}
                foff = 1
                for fd in fields:
                    val = data[roff+foff:roff+foff+fd['len']].decode('latin1', errors='replace').strip()
                    rec[fd['name']] = val
                    foff += fd['len']
                print(f"  rec[{ri}]: CNES={rec.get('CNES')}, CODUFMUN={rec.get('CODUFMUN')}, CODLEITO={rec.get('CODLEITO')}, QT_EXIST={rec.get('QT_EXIST')}")
            print("SUCESSO!")
    else:
        if sz > 2**60:
            sz = sz - 2**64
        print(f"skip={skip}: ERRO blast={sz}")
