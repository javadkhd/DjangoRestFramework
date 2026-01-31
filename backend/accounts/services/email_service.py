from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from accounts.tokens import EmailVerificationToken, PasswordResetToken


def send_verification_email(user):
    token = EmailVerificationToken.for_user(user)
    host = settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else "localhost"
    verify_url = (
        f"http://{host}/api/auth/verify-email/"
        f"?token={str(token)}"
    )

    send_mail(
        subject="Verify your email",
        message=f"Click the link to verify your email:\n{verify_url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )



def send_password_reset_email(user):
    token = PasswordResetToken.for_user(user)
    host = settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else "localhost"

    reset_url = (
        f"http://{host}/api/auth/reset-password/confirm/"
        f"?token={str(token)}"
    )

    send_mail(
        subject="Reset your password",
        message=f"Click the link to reset your password:\n{reset_url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
