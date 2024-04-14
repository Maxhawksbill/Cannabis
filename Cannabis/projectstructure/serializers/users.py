from rest_framework import serializers
from django.contrib.auth import get_user_model
from Cannabis.projectstructure.models import UserProfile, InternalUser, ExternalUser

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'role', 'first_name', 'last_name', 'position', 'start_working_day']

class InternalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalUser
        fields = ['user', 'position']

class ExternalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalUser
        fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    internal_profile = InternalUserSerializer(read_only=True)
    external_profile = ExternalUserSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'oauth_token', 'internal_profile', 'external_profile']
