from celery import shared_task
from accounts.services.email_service import send_verification_email, send_password_reset_email
from django.contrib.auth import get_user_model

User = get_user_model()

# TODO: Mix both of them.



@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=10,
    retry_kwargs={"max_retries": 3},
)
def send_verification_email_task(self, user_id: int):
    user = User.objects.get(id=user_id)
    send_verification_email(user)




@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=10,
    retry_kwargs={"max_retries": 3},
)
def send_password_reset_email_task(self, user_id: int):
    user = User.objects.get(id=user_id)
    send_password_reset_email(user)
