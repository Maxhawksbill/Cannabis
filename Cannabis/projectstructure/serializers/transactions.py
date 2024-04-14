from rest_framework import serializers
from Cannabis.projectstructure.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['uuid', 'order', 'payment_method', 'status', 'timestamp']
