from json import JSONDecodeError

from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class UserHeaderAuthentication(BaseAuthentication):
    header_name = "X-User-Id"

    def authenticate(self, request):
        try:
            user_id = request.headers[self.header_name]
        except (KeyError, JSONDecodeError):
            return None

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

        if not user:
            raise AuthenticationFailed()

        if not user.is_active:
            raise AuthenticationFailed()

        return user, None
