from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from accounts.api.views import RegisterView, TokenObtainPairView, TokenRefreshView, LogoutView

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"), # LogIn
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
