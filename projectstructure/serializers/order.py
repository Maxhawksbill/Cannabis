from rest_framework import serializers
from projectstructure.models import Order
from projectstructure.serializers import OrderProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'payment_method', 'created_at', 'updated_at', 'order_products']
