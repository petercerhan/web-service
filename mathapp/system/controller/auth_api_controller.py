from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from mathapp.libraries.general_library.errors.validation_error import ValidationError
from mathapp.libraries.general_library.errors.mathapp_error import MathAppError

import datetime

class AuthApiController:

    def __init__(self, 
                 request,
                 auth_interactor,
                 auth_api_presenter,
                 token_service,
                 date_service):
        self._request = request
        self._auth_interactor = auth_interactor
        self._auth_api_presenter = auth_api_presenter
        self._token_service = token_service
        self._date_service = date_service

    def login(self):
        json = self._request.get_json()
        fields = {}
        fields['username'] = json.get('username')
        fields['password'] = json.get('password')

        try:
            auth_token = self._auth_interactor.login_api(fields=fields)
            auth_token_payload = self._token_service.get_api_token_payload(auth_token)
            user = self._auth_interactor.get_user(user_id=auth_token_payload.get('sub'))
            return self._auth_api_presenter.login_package(auth_token, auth_token_payload, user)
        except MathAppError as error:
            return self._auth_api_presenter.error(error)
    

    def auth_token_is_valid(self, token):
        try:
            payload = self._token_service.get_api_token_payload(token)
            expiration = payload.get('exp')
            expiration_datetime = datetime.datetime.utcfromtimestamp(expiration)
            current_datetime = self._date_service.current_datetime_utc()
            if expiration_datetime > current_datetime:
                return True
            else:
                return False
        except MathAppError as error:
            return False

    def refresh_auth(self):
        token = self._request.form.get('token')
        try:
            new_token = self._auth_interactor.refresh_api_token(token=token)  
            token_payload = self._token_service.get_api_token_payload(new_token)
            user = self._auth_interactor.get_user(user_id=token_payload.get('sub')) 
            return self._auth_api_presenter.login_package(auth_token=new_token, auth_token_payload=token_payload, user=user)
        except MathAppError as error:
            return self._auth_api_presenter.error(error)





