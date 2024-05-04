from rest_framework import serializers
from projectstructure.models import Order
from projectstructure.serializers.order_product import OrderProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['uuid', 'user', 'total_price', 'status', 'payment_method', 'created_at', 'updated_at', 'order_products']
