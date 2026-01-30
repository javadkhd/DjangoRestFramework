# Import here to use in URL routing
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from accounts.api.serializers import RegisterSerializer, LogoutSerializer, CurrentUserSerializer, \
    ChangePasswordSerializer, UpdateProfileSerializer
    
from accounts.services.auth_service import register_user, logout_user, change_password, update_profile
from rest_framework.permissions import IsAuthenticated

from accounts.services.email_service import send_verification_email

from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth import get_user_model


from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.api.serializers import CustomTokenObtainPairSerializer





class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save(is_active=False)

        send_verification_email(user)

        return Response(
            {"detail": "Verification email sent."},
            status=status.HTTP_201_CREATED,
        )


#### Before verification with email

# class RegisterView(APIView):
#     permission_classes = [permissions.AllowAny]
        
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = register_user(**serializer.validated_data)

#         return Response(
#             {
#                 "id": user.id,
#                 "username": user.username,
#                 "email": user.email,
#             },
#             status=status.HTTP_201_CREATED,
#         )


User = get_user_model()
class VerifyEmailView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        token = request.query_params.get("token")

        if not token:
            return Response(
                {"detail": "Token is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            validated_token = UntypedToken(token)
            user_id = validated_token["user_id"]

            user = User.objects.get(id=user_id)

            if user.is_active:
                return Response(
                    {"detail": "Email already verified"},
                    status=status.HTTP_200_OK,
                )

            user.is_active = True
            user.save(update_fields=["is_active"])

            return Response(
                {"detail": "Email verified successfully"},
                status=status.HTTP_200_OK,
            )

        except (InvalidToken, TokenError):
            return Response(
                {"detail": "Invalid or expired token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )



class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RefreshTokenView(TokenRefreshView):
    pass


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        logout_user(refresh_token=serializer.validated_data["refresh"])

        return Response(status=status.HTTP_204_NO_CONTENT)




class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CurrentUserSerializer(request.user)
        return Response(serializer.data)




class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            change_password(
                user=request.user,
                old_password=serializer.validated_data["old_password"],
                new_password=serializer.validated_data["new_password"],
            )
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Password changed successfully"})


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = UpdateProfileSerializer(instance=request.user, data=request.data, partial=True, context={"request": request})
        serializer.is_valid(raise_exception=True)

        user = update_profile(
            user=request.user,
            username=serializer.validated_data.get("username", request.user.username),
            email=serializer.validated_data.get("email", request.user.email),
        )
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })






