from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default='customer')
    oauth_token = models.CharField(max_length=255, blank=True, null=True)
    # In the built-in User model (in a custom User model that extends AbstractUser)
    groups = models.ManyToManyField(Group, related_name='auth_user_set')

    # Add or change the related_name for user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='user_custom_permissions',  # Change this to a unique related name
    )

    def __str__(self):
        return self.username


