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
