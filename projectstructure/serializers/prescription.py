from rest_framework import serializers
from projectstructure.models import Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        exclude = ['verification_status']
