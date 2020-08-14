from mathapp.db import Session
from mathapp.system.data_mapper.user.orm_user import ORMUser
from werkzeug.security import check_password_hash, generate_password_hash

from mathapp.library.errors.validation_error import ValidationError


class AuthInteractor:

    def __init__(self, user_repository, unit_of_work_committer):
        self._user_repository = user_repository
        self._unit_of_work_committer = unit_of_work_committer

    def register(self, fields):
        username = fields['username']
        password = fields['password']
        
        if not username:
            raise ValidationError(message = 'Username is required.')
        elif not password:
            raise ValidationError(message = 'Password is required.')
        elif Session.query(ORMUser).filter(ORMUser.username == username).first() is not None:
            raise ValidationError(message = 'User {} is already registered.'.format(username))

        else:
            user = ORMUser(username=username, password=generate_password_hash(password))
            Session.add(user)
            Session.commit()


    def login(self, fields):
        username = fields['username']
        password = fields['password']

        user = Session.query(ORMUser).filter(ORMUser.username == username).first()

        if user is None:
            raise ValidationError(message = 'Invalid login')
        elif not check_password_hash(user.password, password):
            raise ValidationError(message = 'Invalid login.')
        else:
            return user


    def get_user(self, user_id):
        return self._user_repository.get(user_id)