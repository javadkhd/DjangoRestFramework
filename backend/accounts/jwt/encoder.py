import time
from .base import json_encode
from .signer import sign


def encode_jwt(*, payload: dict) -> str:
    header = {
        "alg": "HS256",
        "typ": "JWT",
    }

    header_b64 = json_encode(header)
    payload_b64 = json_encode(payload)

    message = f"{header_b64}.{payload_b64}"
    signature = sign(message)

    return f"{message}.{signature}"


def build_payload(*, user_id: int, token_type: str, lifetime: int, extra: dict | None = None):
    now = int(time.time())

    payload = {
        "user_id": user_id,
        "token_type": token_type,
        "iat": now,
        "exp": now + lifetime,
    }

    if extra:
        payload.update(extra)

    return payload
