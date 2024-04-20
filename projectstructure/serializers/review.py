from rest_framework import serializers
from projectstructure.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'review_text', 'timestamp']
