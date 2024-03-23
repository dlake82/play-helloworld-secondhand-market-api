from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class TokenBlackVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer: ModelSerializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        token = UntypedToken(serializer.initial_data["token"])

        # Check if token is in the blacklist
        try:
            outstanding_token = OutstandingToken.objects.get(token=token)
            if BlacklistedToken.objects.filter(token=outstanding_token).exists():
                raise InvalidToken("Token is blacklisted")
        except OutstandingToken.DoesNotExist:
            raise InvalidToken("Token does not exist")

        return Response(status=status.HTTP_200_OK)
