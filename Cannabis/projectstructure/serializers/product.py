from rest_framework import serializers
from Cannabis.projectstructure.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'thc_content', 'cbd_content', 'image', 'created_at', 'updated_at', 'category']
