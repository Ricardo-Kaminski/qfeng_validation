"""Smoke test IPC: sobe motor_theta_pod stub, faz 1 chamada, verifica ack.

Uso:
  python experiments/adversarial_clt/runners/_smoke_test_ipc_pods.py

Para teste completo com 3 pods (B5_SIDECAR), abrir 3 terminais:
  python -m qfeng.pods.llm_pod
  python -m qfeng.pods.clingo_pod
  python -m qfeng.pods.motor_theta_pod
Depois rodar qfeng.pods.orchestrator.
"""
import subprocess
import sys
import time
import json
from pathlib import Path

SRC_DIR = str(Path(__file__).resolve().parents[3] / "src")


def test_motor_theta_pod_ipc():
    sys.path.insert(0, SRC_DIR)
    from qfeng.pods.transport import call_pod
    from qfeng.pods.motor_theta_pod import PORT

    proc = subprocess.Popen(
        [sys.executable, "-m", "qfeng.pods.motor_theta_pod"],
        cwd=SRC_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(2)  # aguardar bind ZeroMQ
    try:
        resp = call_pod(PORT, {"psi_n": [1.0, 0.0], "psi_s": [0.7, 0.7]}, timeout_ms=5000)
        assert resp["status"] == "stub_ok", f"Expected stub_ok, got: {resp['status']}"
        assert resp["regime"] == "STAC", f"Expected STAC, got: {resp['regime']}"
        print("OK: IPC motor_theta_pod funcionando.")
        print(f"    Response: {json.dumps(resp, ensure_ascii=False)}")
        return True
    except Exception as e:
        print(f"FAIL: IPC error: {e}")
        return False
    finally:
        proc.terminate()
        proc.wait(timeout=5)


def test_imports():
    sys.path.insert(0, SRC_DIR)
    from qfeng.pods.transport import PodServer, call_pod, pod_client
    from qfeng.pods import llm_pod, clingo_pod, motor_theta_pod, orchestrator

    assert llm_pod.PORT == 5555, f"LLM port: {llm_pod.PORT}"
    assert clingo_pod.PORT == 5556, f"Clingo port: {clingo_pod.PORT}"
    assert motor_theta_pod.PORT == 5557, f"Motor port: {motor_theta_pod.PORT}"
    print("OK: pods importam, portas atribuidas (5555/5556/5557).")
    return True


if __name__ == "__main__":
    ok1 = test_imports()
    ok2 = test_motor_theta_pod_ipc()
    if ok1 and ok2:
        print("\nSTATUS: P1.6 smoke test PASSED")
        sys.exit(0)
    else:
        print("\nSTATUS: P1.6 smoke test FAILED")
        sys.exit(1)
