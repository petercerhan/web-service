from mathapp.system.data_mapper.user.orm_user import ORMUser

from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

from mathapp.system.interactor.domain_to_data_transforms.user import user_to_data

import sys

class AuthInteractor:

    def __init__(self, 
                 user_repository,
                 user_factory, 
                 encryption_service, 
                 date_service, 
                 token_service,
                 unit_of_work_committer):
        self._user_repository = user_repository
        self._user_factory = user_factory
        self._encryption_service = encryption_service
        self._date_service = date_service
        self._token_service = token_service
        self._unit_of_work_committer = unit_of_work_committer

    def register(self, fields):
        raw_password = fields.get('password')
        if raw_password is None:
            raise ValidationError(message='User requires password')

        fields['password'] = self._encryption_service.generate_password_hash(raw_password)
        user = self._user_factory.create(fields)
        self._unit_of_work_committer.commit()
        return user_to_data(user)

    def login(self, fields):
        username = fields['username']
        password = fields['password']

        try:
            user = self._user_repository.get_by_username(username)
        except ValidationError as error:
            raise ValidationError(message = "Invalid Login")
        except NotFoundError as error:
            raise ValidationError(message = "Invalid Login")
        else:
            return self._validate_login(user, password)

    def _validate_login(self, user, password):        
        if not self._encryption_service.check_password_hash(encrypted_password = user.get_password(), check_password = password):
            raise ValidationError(message = "Invalid Login")
        else:
            current_datetime = self._date_service.current_datetime_utc()
            claims = user.get_session_data(current_datetime)
            token = self._token_service.get_web_auth_token(user_claims = claims, 
                                                            current_datetime = current_datetime)

            return token

    def get_user(self, user_id):
        user = self._user_repository.get(user_id)
        return user_to_data(user)

    def check_authentication(self, auth_token):
        try:
            payload = self._token_service.get_web_token_payload(auth_token)

            print(payload, file=sys.stderr)

            return self._validate_token_payload(payload)
        except ValidationError:

            print('invalid token', file=sys.stderr)

            return False

    def _validate_token_payload(self, payload):
        return True







