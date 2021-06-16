from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

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
        fields['username'] = self._request.form.get('username')
        fields['password'] = self._request.form.get('password')

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
        fields['username'] = self._request.form.get('username')
        fields['password'] = self._request.form.get('password')

        try:
            auth_token = self._interactor.login_web(fields)
        except ValidationError as error:
            return self._presenter.present_login(error_message = error.message)
        else:
            response = self._presenter.present_login_successful()
            response.set_cookie('auth_token', auth_token, httponly=True)
            return response

    def _get_login_form(self):
        return self._presenter.present_login(error_message = None)


    def get_user(self, user_id):
        return self._interactor.get_user(user_id)

    def check_authentication(self, auth_token):
        return self._interactor.check_authentication(auth_token)

    def get_updated_auth_token(self, prior_auth_token):
        return self._interactor.get_updated_auth_token(prior_auth_token)

    def get_csrf_token(self, auth_token):
        return self._interactor.get_csrf_token(auth_token)

    def check_csrf_token(self, csrf_token, auth_token):
        return self._interactor.check_csrf_token(csrf_token, auth_token)

    def logout(self, auth_token):
        self._interactor.logout(auth_token)









