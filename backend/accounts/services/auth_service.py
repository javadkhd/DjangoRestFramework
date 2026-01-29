from django.contrib.auth import get_user_model

User = get_user_model()


def register_user(*, username: str, email: str, password: str) -> User:
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        is_active=True,  # TODO use email verification, set to False initially
    )
    return user





from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


def logout_user(*, refresh_token: str) -> None:
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
    except TokenError:
        # token invalid / expired / already blacklisted
        pass


