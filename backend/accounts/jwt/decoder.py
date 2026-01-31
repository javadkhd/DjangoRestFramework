import time
from .base import json_decode
from .signer import verify


class JWTDecodeError(Exception):
    pass


def decode_jwt(token: str) -> dict:
    try:
        header_b64, payload_b64, signature = token.split(".")
    except ValueError:
        raise JWTDecodeError("Invalid token format")

    message = f"{header_b64}.{payload_b64}"

    if not verify(message, signature):
        raise JWTDecodeError("Invalid signature")

    payload = json_decode(payload_b64)

    if payload.get("exp") < int(time.time()):
        raise JWTDecodeError("Token expired")

    return payload
