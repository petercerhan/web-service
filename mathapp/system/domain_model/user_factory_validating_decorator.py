from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

class UserFactoryValidatingDecorator:

    def __init__(self, user_factory, user_repository):
        self._user_factory = user_factory
        self._user_repository = user_repository

    def create(self, fields):
        username = fields.get('username')
        if username is not None:
            self._check_username_unique(username)

        return self._user_factory.create(fields)

    def _check_username_unique(self, username):
        try:
            self._user_repository.get_by_username(username)
            raise ValidationError(message = 'User {} is already registered.'.format(username))
        except NotFoundError:
            return None
