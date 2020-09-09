import jwt
from mathapp.library.errors.validation_error import ValidationError
import datetime

import sys

class TokenService:

    def __init__(self, web_signing_key):
        self._web_signing_key = web_signing_key

    def get_web_auth_token(self, user_claims, current_datetime):
        payload = {
            'exp': current_datetime + user_claims.expiration_period,
            'iat': current_datetime,
            'sub': user_claims.user_id,
            'session_id': '123456789',
            'name': user_claims.name,
            'expiration_period': user_claims.expiration_period.total_seconds()
        }
        token = jwt.encode(payload, self._web_signing_key, algorithm='HS256')
        return token

    def update_web_auth_token(self, payload, current_datetime):
        expiration_period = datetime.timedelta(seconds = payload['expiration_period'])
        payload['exp'] = current_datetime + expiration_period
        token = jwt.encode(payload, self._web_signing_key, algorithm='HS256')
        return token

    def get_web_token_payload(self, token):
        try:
            return jwt.decode(token, self._web_signing_key, options={'verify_exp': False})
        except jwt.InvalidTokenError as e:
            raise ValidationError('Invalid token')