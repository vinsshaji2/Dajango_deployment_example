from django.contrib.auth.backends import BaseBackend
from books.models import UserLogin

class EmailPasswordAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = UserLogin.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserLogin.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserLogin.objects.get(pk=user_id)
        except UserLogin.DoesNotExist:
            return None
