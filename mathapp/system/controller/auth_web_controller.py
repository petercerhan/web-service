from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from mathapp.db import Session
from mathapp.user import User
from werkzeug.security import check_password_hash, generate_password_hash

from mathapp.library.errors.validation_error import ValidationError

class AuthWebController:

    def __init__(self, request, auth_presenter, auth_interactor):
        self._request = request
        self._presenter = auth_presenter
        self._interactor = auth_interactor

    def handle_register_request(self):
        if self._request.method == 'POST':
            return self._post_register_form()
        return self._get_register_form()

    def _post_register_form(self):
        fields = {}
        fields['username'] = self._request.form['username']
        fields['password'] = self._request.form['password']

        try:
            self._interactor.register(fields)
        except ValidationError as error:
            return self._presenter.present_register(error_message = error.message)
        else:
            return self._presenter.present_register_successful()


    def _get_register_form(self):
        return self._presenter.present_register(error_message = None)


    def handle_login_request(self):
        if request.method == 'POST':
            return self._post_login_form()
        return self._get_login_form()

    def _post_login_form(self):
        fields = {}
        fields['username'] = self._request.form['username']
        fields['password'] = self._request.form['password']

        try:
            user = self._interactor.login(fields)
        except ValidationError as error:
            return self._presenter.present_login(error_message = error.message)
        else:
            session.clear()
            session['user_id'] = user.id
            return self._presenter.present_login_successful()

    def _get_login_form(self):
        return self._presenter.present_login(error_message = None)


    def get_user(self, user_id):
        return self._interactor.get_user(user_id)



