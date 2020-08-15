from mathapp.db import Session
from mathapp.system.data_mapper.user.orm_user import ORMUser

from mathapp.library.errors.validation_error import ValidationError

from mathapp.system.interactor.domain_to_data_transforms.user import user_to_data

class AuthInteractor:

    def __init__(self, 
                 user_repository,
                 user_factory, 
                 encryption_service,
                 unit_of_work_committer):
        self._user_repository = user_repository
        self._user_factory = user_factory
        self._encryption_service = encryption_service
        self._unit_of_work_committer = unit_of_work_committer

    def register(self, fields):
        fields['password'] = self._encryption_service.generate_password_hash(fields['password'])
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
        else:
            return self._validate_login(user, password)

    def _validate_login(self, user, password):        
        if not self._encryption_service.check_password_hash(encrypted_password = user.get_password(), check_password = password):
            raise ValidationError(message = "Invalid Login")
        else:
            return user_to_data(user)

    def get_user(self, user_id):
        user = self._user_repository.get(user_id)
        return user_to_data(user)