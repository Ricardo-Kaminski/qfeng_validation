"""Transport ZeroMQ REQ-REP para comunicacao inter-pods.

Pattern: cada pod tem servidor REP em porta dedicada. Orchestrator (cliente)
abre conexao REQ por requisicao. Mensagens em JSON UTF-8.

Latencia esperada local: ~0.5-2 ms por round-trip.
"""
import json
import zmq
from typing import Any
from contextlib import contextmanager

DEFAULT_TIMEOUT_MS = 30000  # 30s para chamadas LLM longas


class PodServer:
    """Wrapper para servidor REP de um pod."""

    def __init__(self, port: int, name: str):
        self.port = port
        self.name = name
        self.ctx = zmq.Context()
        self.socket = self.ctx.socket(zmq.REP)
        self.socket.bind(f"tcp://127.0.0.1:{port}")
        print(f"[{name}] Listening on tcp://127.0.0.1:{port}")

    def serve(self, handler):
        """Loop de servico. handler eh funcao (request_dict) -> response_dict."""
        try:
            while True:
                raw = self.socket.recv_string()
                req = json.loads(raw)
                try:
                    resp = handler(req)
                except Exception as e:
                    resp = {"status": "error", "error": str(e), "type": type(e).__name__}
                self.socket.send_string(json.dumps(resp, ensure_ascii=False, default=str))
        except KeyboardInterrupt:
            print(f"\n[{self.name}] Shutting down gracefully.")
        finally:
            self.socket.close()
            self.ctx.term()


@contextmanager
def pod_client(port: int, timeout_ms: int = DEFAULT_TIMEOUT_MS):
    """Context manager para cliente REQ. Use com `with`."""
    ctx = zmq.Context()
    socket = ctx.socket(zmq.REQ)
    socket.setsockopt(zmq.RCVTIMEO, timeout_ms)
    socket.setsockopt(zmq.SNDTIMEO, timeout_ms)
    socket.setsockopt(zmq.LINGER, 0)
    socket.connect(f"tcp://127.0.0.1:{port}")
    try:
        yield socket
    finally:
        socket.close()
        ctx.term()


def call_pod(port: int, request: dict, timeout_ms: int = DEFAULT_TIMEOUT_MS) -> dict:
    """Chamada single-shot a um pod. Retorna resposta como dict."""
    with pod_client(port, timeout_ms) as sock:
        sock.send_string(json.dumps(request, ensure_ascii=False))
        raw = sock.recv_string()
        return json.loads(raw)
