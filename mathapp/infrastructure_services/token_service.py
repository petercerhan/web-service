import jwt
from mathapp.library.errors.validation_error import ValidationError

import sys

class TokenService:

    def __init__(self, web_signing_key):
        self._web_signing_key = web_signing_key

    def get_web_auth_token(self, user_claims, current_datetime):
        payload = {
            'exp': user_claims.expiration_datetime,
            'iat': current_datetime,
            'sub': user_claims.user_id,
            'session_id': '123456789',
            'name': user_claims.name
        }
        token = jwt.encode(payload, self._web_signing_key, algorithm='HS256')
        return token

    def get_web_token_payload(self, token):
        try:
            return jwt.decode(token, self._web_signing_key, options={'verify_exp': False})
        except jwt.InvalidTokenError as e:
            print(e, file=sys.stderr)
            raise ValidationError('Invalid token')