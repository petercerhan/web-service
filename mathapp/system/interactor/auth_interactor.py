from mathapp.system.data_mapper.user.orm_user import ORMUser

from mathapp.libraries.general_library.errors.validation_error import ValidationError
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError

from mathapp.system.interactor.domain_to_data_transforms.user import user_to_data

import datetime

class AuthInteractor:

    def __init__(self, 
                 user_repository,
                 user_factory, 
                 session_repository,
                 session_factory,
                 encryption_service, 
                 date_service, 
                 token_service,
                 unit_of_work_committer):
        self._user_repository = user_repository
        self._user_factory = user_factory
        self._session_repository = session_repository
        self._session_factory = session_factory
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


    def login_web(self, fields):
        username = fields['username']
        password = fields['password']

        user = self._get_user_by_username(username)
        self._validate_password(user=user, password=password)
        session = self._create_session(user=user)
        token = self._get_web_token(user=user, session=session)
        return token

    def login_api(self, fields):
        username = fields['username']
        password = fields['password']

        user = self._get_user_by_username(username)
        self._validate_password(user=user, password=password)
        session = self._create_session(user=user)
        token = self._get_api_token(user=user, session=session)

        return token


    def _get_user_by_username(self, username):
        try:
            user = self._user_repository.get_by_username(username)
            return user
        except ValidationError as error:
            raise ValidationError(message = "Invalid Login")
        except NotFoundError as error:
            raise ValidationError(message = "Invalid Login")

    def _validate_password(self, user, password):
        if not self._encryption_service.check_password_hash(encrypted_password=user.get_password(), 
                                                            check_password=password):
            raise ValidationError(message = "Invalid Login")        

    def _create_session(self, user):
        current_datetime = self._date_service.current_datetime_utc()
        session = self._session_factory.create(user=user, created_at=current_datetime)
        self._unit_of_work_committer.commit()
        return session

    def _get_web_token(self, user, session):
        session_parameters = user.get_session_parameters()
        current_datetime = self._date_service.current_datetime_utc()
        token = self._token_service.get_web_auth_token(expiration_period=session_parameters.expiration_period,
                                                        refresh_expiration_period=session_parameters.refresh_expiration_period,
                                                        user_id=session_parameters.user_id,
                                                        name=session_parameters.name,
                                                        session_id=session.get_id(),
                                                        current_datetime=current_datetime)
        return token

    def _get_api_token(self, user, session):
        session_parameters = user.get_session_parameters()
        current_datetime = self._date_service.current_datetime_utc()
        token = self._token_service.create_api_auth_token(expiration_period=session_parameters.api_expiration_period,
                                                          refresh_expiration_period=session_parameters.api_refresh_expiration_period,
                                                          user_id=session_parameters.user_id,
                                                          name=session_parameters.name,
                                                          session_id=session.get_id(),
                                                          current_datetime=current_datetime)
        return token


    def get_user(self, user_id):
        user = self._user_repository.get(user_id)
        return user_to_data(user)

    def check_authentication(self, auth_token):
        try:
            payload = self._token_service.get_web_token_payload(auth_token)
            return self._validate_token_payload(payload=payload, initial_auth_token=auth_token)
        except ValidationError:
            return {'auth_valid': False, 'user_id': None, 'user_name': None, 'auth_token': None}
            return False

    def _validate_token_payload(self, payload, initial_auth_token):
        expiration = payload.get('exp')
        expiration_datetime = datetime.datetime.utcfromtimestamp(expiration)
        refresh_expiration_datetime = payload.get('refresh_exp')
        current_datetime = self._date_service.current_datetime_utc()

        if current_datetime < expiration_datetime:
            return {'auth_valid': True, 'user_id': payload['sub'], 'user_name': payload['name'], 'auth_token': initial_auth_token}

        if current_datetime >= expiration_datetime and current_datetime < refresh_expiration_datetime:
            if self._session_is_revoked(payload=payload):
                return {'auth_valid': False, 'user_id': None, 'user_name': None, 'auth_token': None}
            else:
                new_token = self._get_updated_web_auth_token(prior_payload=payload)
                return {'auth_valid': True, 'user_id': payload['sub'], 'user_name': payload['name'], 'auth_token': new_token}

        if current_datetime >= refresh_expiration_datetime:
            return {'auth_valid': False, 'user_id': None, 'user_name': None, 'auth_token': None}

    def _session_is_revoked(self, payload):
        session_id = payload.get('session_id')
        session = self._session_repository.get(session_id)
        return session.get_revoked()


    def _get_updated_web_auth_token(self, prior_payload):
        current_datetime = self._date_service.current_datetime_utc()
        new_token = self._token_service.update_web_auth_token(payload=prior_payload, current_datetime=current_datetime)
        return new_token


    def get_csrf_token(self, auth_token):
        return self._encryption_service.generate_hash_for_csrf(auth_token)

    def check_csrf_token(self, csrf_token, auth_token):
        return self._encryption_service.check_hash_for_csrf(check_hash=csrf_token, message=auth_token)

    def logout(self, auth_token):
        try:
            payload = self._token_service.get_web_token_payload(auth_token)
            session_id = payload.get('session_id')
            session = self._session_repository.get(session_id)
            session.set_revoked(True)
            self._unit_of_work_committer.commit()
        except Exception:
            pass




