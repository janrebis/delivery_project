import jwt
from rest_framework import authentication, exceptions
from rest_framework.authtoken.admin import User

from project import settings


class JWTAuthentication(authentication.BaseAuthentication):
    token_prefix = 'Token'

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix = auth_data[0].decode('utf-8')
        token = auth_data[1].decode('utf-8')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)

            user = User.object.get(username=payload('id'))
            return user, token

        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Your token is invalid')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Your token is expired')
