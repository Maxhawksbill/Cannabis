from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default='customer')
    oauth_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    role = models.CharField(max_length=20)  # e.g., admin, customer
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    start_working_day = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.role}'

class InternalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='internal_profile')
    position = models.CharField(max_length=100)
    # Add any other fields specific to internal users here


class ExternalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='external_profile')
    # Add any other fields specific to external users here
