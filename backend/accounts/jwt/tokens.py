from datetime import timedelta
from django.conf import settings
from accounts.jwt.encoder import encode_jwt, build_payload
import uuid
from django.utils import timezone
from accounts.models import RefreshToken as RefreshTokenModel




class BaseToken:
    token_type = None
    lifetime = None

    def __init__(self, token: str):
        self.token = token

    def __str__(self):
        return self.token

    @classmethod
    def for_user(cls, user, extra: dict | None = None):
        payload = build_payload(
            user_id=user.id,
            token_type=cls.token_type,
            lifetime=int(cls.lifetime.total_seconds()),
            extra=extra,
        )
        token = encode_jwt(payload=payload)
        return cls(token)


class LoginToken(BaseToken):
    token_type = "access"
    lifetime = settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]



class RefreshToken(BaseToken):
    token_type = "refresh"
    lifetime = settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"]

    @classmethod
    def for_user(cls, user):
        jti = uuid.uuid4().hex

        payload = build_payload(
            user_id=user.id,
            token_type=cls.token_type,
            lifetime=int(cls.lifetime.total_seconds()),
            extra={"jti": jti},
        )

        token = encode_jwt(payload=payload)

        RefreshTokenModel.objects.create(
            user=user,
            jti=jti,
            expires_at=timezone.now() + cls.lifetime,
        )

        return cls(token)
