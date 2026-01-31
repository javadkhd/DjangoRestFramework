from rest_framework_simplejwt.tokens import Token
from django.conf import settings


class EmailVerificationToken(Token):
    token_type = "email_verification"
    lifetime = settings.EMAIL_VERIFICATION_TOKEN_LIFETIME


class PasswordResetToken(Token):
    token_type = "password_reset"
    lifetime = settings.PASSWORD_RESET_TOKEN_LIFETIME
