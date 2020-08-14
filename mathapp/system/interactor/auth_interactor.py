from mathapp.db import Session
from mathapp.user import User
from werkzeug.security import check_password_hash, generate_password_hash

from mathapp.library.errors.validation_error import ValidationError


class AuthInteractor:

    def register(self, fields):
        username = fields['username']
        password = fields['password']
        
        if not username:
            raise ValidationError(message = 'Username is required.')
        elif not password:
            raise ValidationError(message = 'Password is required.')
        elif Session.query(User).filter(User.username == username).first() is not None:
            raise ValidationError(message = 'User {} is already registered.'.format(username))

        else:
            user = User(username=username, password=generate_password_hash(password))
            Session.add(user)
            Session.commit()


    def login(self, fields):
        username = fields['username']
        password = fields['password']

        user = Session.query(User).filter(User.username == username).first()

        if user is None:
            raise ValidationError(message = 'Username Required')
        elif not check_password_hash(user.password, password):
            raise ValidationError(message = 'Incorrect password.')
        else:
            return user


    def get_user(self, user_id):
        return Session.query(User).filter(User.id == user_id).first()