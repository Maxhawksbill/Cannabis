from rest_framework import serializers
from Cannabis.projectstructure.models import Order
from Cannabis.projectstructure.serializers import OrderProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'payment_method', 'created_at', 'updated_at', 'order_products']
