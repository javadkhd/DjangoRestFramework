# Import here to use in URL routing
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.api.serializers import RegisterSerializer, LogoutSerializer, CurrentUserSerializer, \
    ChangePasswordSerializer, UpdateProfileSerializer
    
from accounts.services.auth_service import register_user, logout_user, change_password, update_profile
from rest_framework.permissions import IsAuthenticated





class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = register_user(**serializer.validated_data)

        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_201_CREATED,
        )




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






