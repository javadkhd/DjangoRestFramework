from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from orders.services.order_service import create_order, get_order, cancel_order, filter_order
from orders.tasks import process_order_task
from orders.api.serializers import CreateOrderSerializer, OrderDetailSerializer
from orders.services.exceptions import OrderNotFound

from orders.api.permissions import IsOrderOwner



class OrderListView(ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated, IsOrderOwner]

    def get_queryset(self):
        return filter_order(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = create_order(user=request.user, amount=serializer.validated_data["amount"])

        process_order_task.delay(str(order.id))
        
        return Response(
            OrderDetailSerializer(order).data,
            status=status.HTTP_201_CREATED,
        )


# class OrderDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderDetailSerializer
#     permission_classes = [IsAuthenticated, IsOrderOwner]
#     lookup_field = "id"

#     def get_queryset(self):
#         return filter_order(user=self.request.user)

class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, order_id):
        try:
            order = get_order(order_id=order_id)
        except OrderNotFound:
            return Response(
                {"detail": "Order not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(OrderDetailSerializer(order).data)



class OrderCancelView(APIView):
    permission_classes = [IsAuthenticated, IsOrderOwner]
    def post(self, request, order_id):
        try:
            order = cancel_order(order_id=order_id)
        except OrderNotFound:
            return Response(
                {"detail": "Order not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        return Response(
            OrderDetailSerializer(order).data,
            status=status.HTTP_200_OK,
        )


