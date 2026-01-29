# Import here to use in URL routing
from rest_framework_simplejwt.views import (
                                            TokenObtainPairView,
                                            TokenRefreshView,
                                        )




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.api.serializers import RegisterSerializer, LogoutSerializer
from accounts.services.auth_service import register_user, logout_user
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
