from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    role = models.CharField(max_length=20)  # e.g., admin, customer
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    start_working_day = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.role}'
