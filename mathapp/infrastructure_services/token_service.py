import jwt
from mathapp.libraries.general_library.errors.validation_error import ValidationError
import datetime

class TokenService:

    def __init__(self, web_signing_key, api_signing_key):
        self._web_signing_key = web_signing_key
        self._api_signing_key = api_signing_key

    def get_web_auth_token(self, 
                           expiration_period,
                           refresh_expiration_period,
                           user_id,
                           name,
                           session_id, 
                           current_datetime):
        payload = {
            'exp': current_datetime + expiration_period,
            'refresh_exp': (current_datetime + refresh_expiration_period).isoformat(),
            'iat': current_datetime,
            'sub': user_id,
            'session_id': session_id,
            'name': name,
            'expiration_period': expiration_period.total_seconds(),
            'refresh_expiration_period': refresh_expiration_period.total_seconds()
        }
        token = jwt.encode(payload, self._web_signing_key, algorithm='HS256')
        return token.decode('utf-8')

    def update_web_auth_token(self, payload, current_datetime):
        expiration_period = datetime.timedelta(seconds = payload['expiration_period'])
        payload['exp'] = current_datetime + expiration_period

        refresh_expiration_period = datetime.timedelta(seconds = payload['refresh_expiration_period'])
        payload['refresh_exp'] = (current_datetime + refresh_expiration_period).isoformat()

        token = jwt.encode(payload, self._web_signing_key, algorithm='HS256')
        return token.decode('utf-8')

    def get_web_token_payload(self, token):
        try:
            payload = jwt.decode(token, self._web_signing_key, options={'verify_exp': False}, algorithms='HS256')
            payload['refresh_exp'] = datetime.datetime.fromisoformat(payload['refresh_exp'])
            return payload
        except jwt.InvalidTokenError as e:
            raise ValidationError('Invalid token')

    def create_api_auth_token(self,
                             expiration_period,
                             refresh_expiration_period,
                             user_id,
                             name,
                             session_id,
                             current_datetime):
        payload = {
            'exp': current_datetime + expiration_period,
            'refresh_exp': (current_datetime + refresh_expiration_period).isoformat(),
            'iat': current_datetime,
            'sub': user_id,
            'session_id': session_id,
            'name': name,
            'expiration_period': expiration_period.total_seconds(),
            'refresh_expiration_period': refresh_expiration_period.total_seconds()
        }
        token = jwt.encode(payload, self._api_signing_key, algorithm='HS256')
        return token.decode('utf-8')



    # def refresh_api_token

    # def get_api_token_payload
    def get_api_token_payload(self, token):
        try:
            payload = jwt.decode(token, self._api_signing_key, options={'verify_exp': False}, algorithms='HS256')
            payload['refresh_exp'] = datetime.datetime.fromisoformat(payload['refresh_exp'])
            return payload
        except jwt.InvalidTokenError as e:
            raise ValidationError('Invalid token')









