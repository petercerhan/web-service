from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from mathapp.db import Session
from mathapp.user import User
from werkzeug.security import check_password_hash, generate_password_hash

class AuthWebController:

    def __init__(self, request, auth_presenter):
        self._request = request
        self._presenter = auth_presenter

    def handle_register_request(self):
        if self._request.method == 'POST':
            return self._post_register_form()
        return self._get_register_form()

    def _post_register_form(self):
        username = self._request.form['username']
        password = self._request.form['password']
        error = None
        
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif Session.query(User).filter(User.username == username).first() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            user = User(username=username, password=generate_password_hash(password))
            Session.add(user)
            Session.commit()
            return self._presenter.present_register_successful()
        
        return self._presenter.present_register(error_message = error)

    def _get_register_form(self):
        return self._presenter.present_register(error = None)



    def handle_login_request(self):
        if request.method == 'POST':
            return self._post_login_form()
        return self._get_login_form()

    def _post_login_form(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            error = None

            user = Session.query(User).filter(User.username == username).first()
            
            if user is None:
                error = 'Incorrect username.'
            elif not check_password_hash(user.password, password):
                error = 'Incorrect password.'
            
            if error is None:
                session.clear()
                session['user_id'] = user.id
                return self._presenter.present_login_successful()

        return self._presenter.present_login(error_message = error)

    def _get_login_form(self):
        return self._presenter.present_login(error_message = None)


    def get_user(self, user_id):
        return Session.query(User).filter(User.id == user_id).first()



