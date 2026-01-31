from accounts.models import RefreshToken as RefreshTokenModel


def is_blacklisted(jti: str) -> bool:
    return RefreshTokenModel.objects.filter(
        jti=jti,
        is_blacklisted=True,
    ).exists()


def blacklist_token(jti: str):
    RefreshTokenModel.objects.filter(jti=jti).update(is_blacklisted=True)
