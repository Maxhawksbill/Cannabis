from rest_framework import serializers
from Cannabis.projectstructure.models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'product', 'quantity_available', 'last_restocked_timestamp']
