from rest_framework import serializers
from Cannabis.projectstructure.models import Promotion

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'code', 'description', 'discount_amount', 'start_date', 'end_date', 'applicable_products', 'applicable_categories']
