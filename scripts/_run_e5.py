import subprocess
result = subprocess.run(
    ["python", "-m", "pytest", "tests/test_e5/", "-v", "--tb=short", "-q"],
    cwd="C:/Workspace/academico/qfeng_validacao",
    capture_output=True, text=True
)
lines = result.stdout.splitlines()
for l in lines[-50:]:
    print(l)
print("exit:", result.returncode)
