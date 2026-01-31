import base64
import json


def base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")


def base64url_decode(data: bytes) -> str:
    padding = "=" * ( -len(data) % 4 )
    return base64.urlsafe_b64decode(data + padding)


def json_encode(data: dict) -> str:
    return base64url_encode(
        json.dumps(data, separators=(",", ":")).encode("utf-8")
    )

def json_decode(data: str) -> dict:
    return json.loads(base64url_decode(data))
