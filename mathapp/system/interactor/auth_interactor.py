from mathapp.db import Session
from mathapp.system.data_mapper.user.orm_user import ORMUser
from werkzeug.security import check_password_hash, generate_password_hash

from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

from mathapp.system.interactor.domain_to_data_transforms.user import user_to_data

class AuthInteractor:

    def __init__(self, user_repository, user_factory, unit_of_work_committer):
        self._user_repository = user_repository
        self._user_factory = user_factory
        self._unit_of_work_committer = unit_of_work_committer

    def register(self, fields):
        fields['password'] = generate_password_hash(password)
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
        if not check_password_hash(user.get_password(), password):
            raise ValidationError(message = "Invalid Login")
        else:
            return user_to_data(user)

    def get_user(self, user_id):
        user = self._user_repository.get(user_id)
        return user_to_data(user)