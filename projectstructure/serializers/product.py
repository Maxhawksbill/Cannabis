from rest_framework import serializers
from projectstructure.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'thc_content', 'cbd_content', 'created_at', 'updated_at', 'category']
