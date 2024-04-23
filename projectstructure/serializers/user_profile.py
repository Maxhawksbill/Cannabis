from rest_framework import serializers
from django.contrib.auth import get_user_model
from projectstructure.models import UserProfile, User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'role', 'first_name', 'last_name', 'position', 'start_working_day']
        read_only_fields = ['user']  # Assuming user should not be modified directly
