from django.urls import path



from accounts.api.views import RegisterView, TokenObtainPairView, \
    TokenRefreshView, LogoutView, CurrentUserView, \
    ChangePasswordView, UpdateProfileView

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", CurrentUserView.as_view(), name="current_user"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("update-profile/", UpdateProfileView.as_view(), name="update_profile"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"), # LogIn
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
