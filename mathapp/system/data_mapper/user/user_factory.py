from mathapp.system.data_mapper.user.orm_user import ORMUser
from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

class UserFactory:

    def __init__(self, unit_of_work, user_repository):
        self._unit_of_work = unit_of_work
        self._user_repository = user_repository

    def create(self, fields):
        username = fields.get('username')
        password = fields.get('password')

        self._check_username_unique(username)

        orm_user = ORMUser(username = username, password = password)

        user = orm_user.get_model(self._unit_of_work)
        self._unit_of_work.register_created(orm_user)

        return user

    def _check_username_unique(self, username):
        try:
            self._user_repository.get_by_username(username)
            raise ValidationError(message = 'User {} is already registered.'.format(username))
        except NotFoundError:
            return None

    def _user_exists_for_username(self, username):
        try:
            return self._user_repository.get_by_username(username)
        except NotFoundError:
            return None