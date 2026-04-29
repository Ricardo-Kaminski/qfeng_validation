"""Q-FENG Pods: IPC ZeroMQ REQ-REP para arquitetura B5_SIDECAR.

Portas:
  LLM pod       → 5555  (S1-S2: raciocinio neural, sem motor)
  Clingo pod    → 5556  (S3-S4: solver simbolico)
  Motor theta   → 5557  (S5: interferencia quantica, interceptor)

P_FASE1.6: stubs. Logica real em P_FASE3 (llm/clingo) e P_FASE4 (motor).
"""
from qfeng.pods.transport import PodServer, call_pod, pod_client
from qfeng.pods.llm_pod import PORT as LLM_PORT
from qfeng.pods.clingo_pod import PORT as CLINGO_PORT
from qfeng.pods.motor_theta_pod import PORT as MOTOR_PORT

__all__ = [
    "PodServer",
    "call_pod",
    "pod_client",
    "LLM_PORT",
    "CLINGO_PORT",
    "MOTOR_PORT",
]
