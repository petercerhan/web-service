from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.mathapp_error import MathAppError

class AuthApiController:

    def __init__(self, 
                 request,
                 auth_interactor,
                 auth_api_presenter):
        self._request = request
        self._auth_interactor = auth_interactor
        self._auth_api_presenter = auth_api_presenter

    def login(self):
        fields = {}
        fields['username'] = self._request.form.get('username')
        fields['password'] = self._request.form.get('password')

        try:
            auth_token = self._auth_interactor.login_api(fields=fields)
            return self._auth_api_presenter.auth_credentials(auth_token=auth_token)
        except MathAppError as error:
            return self._auth_api_presenter.error(error)