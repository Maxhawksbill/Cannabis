from rest_framework import serializers
from django.contrib.auth import get_user_model
from projectstructure.models import User
from projectstructure.serializers.user_profile import UserProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='userprofile_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'oauth_token']

