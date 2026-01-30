from rest_framework_simplejwt.tokens import Token
from datetime import timedelta

class EmailVerificationToken(Token):
    token_type = "email_verification"
    lifetime = timedelta(minutes=30) 
