

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from django.contrib.auth import get_user_model

User = get_user_model()


def register_user(*, username: str, email: str, password: str) -> User:
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        is_active=False, # Done  # TODO use email verification, set to False initially
    )
    return user




def logout_user(*, refresh_token: str) -> None:
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
    except TokenError:
        # token invalid / expired / already blacklisted
        pass


def change_password(*, user, old_password: str, new_password: str):
    if not user.check_password(old_password):
        raise ValueError("Old password is incorrect")
    user.set_password(new_password)
    user.save()


def update_profile(*, user, username: str, email: str):
    user.username = username
    user.email = email
    user.save()
    return user
