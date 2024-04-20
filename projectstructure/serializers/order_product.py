from rest_framework import serializers
from projectstructure.models import OrderProduct

class OrderProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = OrderProduct
        fields = ['id', 'order', 'product', 'quantity', 'price']

    def get_price(self, obj):
        return obj.price
