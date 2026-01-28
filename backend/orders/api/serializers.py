from rest_framework import serializers
from orders.models import Order


class CreateOrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "amount",
            "status",
            "metadata",
            "created_at",
            "updated_at",
        )
