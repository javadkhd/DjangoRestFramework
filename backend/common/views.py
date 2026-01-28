from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from common.health import check_db, check_redis


class HealthCheckView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        status_map = {
            "database": check_db(),
            "redis": check_redis(),
        }

        http_status = (
            status.HTTP_200_OK
            if all(status_map.values())
            else status.HTTP_503_SERVICE_UNAVAILABLE
        )

        return Response(status_map, status=http_status)
