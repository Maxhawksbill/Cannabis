from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication


class MottoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        motto = request.GET.get('motto')

        if motto == 'Smoky!':
            return User.objects.get(is_superuser=True), None

        return None
