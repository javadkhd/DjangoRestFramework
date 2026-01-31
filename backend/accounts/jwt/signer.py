import hmac
import hashlib
from django.conf import settings

from .base import base64url_encode

def sign(message: str) -> str:
    secret = settings.SECRET_KEY.encode("utf-8")
    
    signature = hmac.new(
        key=secret,
        msg=message.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).digest()
    
    return base64url_encode(signature)



def verify(message: str, signature: str) -> bool:
    expected = sign(message)
    return hmac.compare_digest(expected, signature)


    
    