import jwt
from mathapp.library.errors.validation_error import ValidationError
import datetime

import sys

class TokenService:

    def __init__(self, web_signing_key, api_signing_key):
        self._web_signing_key = web_signing_key
        self._api_signing_key = api_signing_key

    def get_web_auth_token(self, 
                           expiration_period,
                           user_id,
                           name,
                           session_id, 
                           current_datetime):
        payload = {
            'exp': current_datetime + expiration_period,
            'iat': current_datetime,
            'sub': user_id,
            'session_id': session_id,
            'name': name,
            'expiration_period': expiration_period.total_seconds()
        }
        token = jwt.encode(payload, self._web_signing_key, algorithm='HS256')
        return token.decode('utf-8')

    def update_web_auth_token(self, payload, current_datetime):
        expiration_period = datetime.timedelta(seconds = payload['expiration_period'])
        payload['exp'] = current_datetime + expiration_period
        token = jwt.encode(payload, self._web_signing_key, algorithm='HS256')
        return token.decode('utf-8')

    def get_web_token_payload(self, token):
        try:
            return jwt.decode(token, self._web_signing_key, options={'verify_exp': False}, algorithms='HS256')
        except jwt.InvalidTokenError as e:
            raise ValidationError('Invalid token')

    # def create_api_token

    # def refresh_api_token

    # def get_api_token_payload

