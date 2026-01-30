from django.urls import path



from accounts.api.views import RegisterView, VerifyEmailView, LoginView, RefreshTokenView, \
    LogoutView, ChangePasswordView, UpdateProfileView, CurrentUserView

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify_email"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/", LoginView.as_view(), name="token_obtain"),
    path("token/refresh/", RefreshTokenView.as_view(), name="token_refresh"),
    
    path("update-profile/", UpdateProfileView.as_view(), name="update_profile"),
    path("me/", CurrentUserView.as_view(), name="current_user"),
]
