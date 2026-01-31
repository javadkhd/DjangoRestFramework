from rest_framework_simplejwt.tokens import Token, AccessToken
from django.conf import settings


class EmailVerificationToken(Token):
    token_type = "email_verification"
    lifetime = settings.EMAIL_VERIFICATION_TOKEN_LIFETIME


class PasswordResetToken(Token):
    token_type = "password_reset"
    lifetime = settings.PASSWORD_RESET_TOKEN_LIFETIME



class LoginToken(AccessToken):
    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)

        token["signature"] = "Asghar"
        token["username"] = user.username
        token["email"] = user.email
        token["permissions"] = list(
            user.get_all_permissions()
        )

        return token
