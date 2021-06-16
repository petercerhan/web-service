from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from mathapp.library.errors.validation_error import ValidationError

class AuthApiController:

    def __init__(self, request):
        self._request = request

    def login(self):
        fields = {}
        fields['username'] = self._request.form.get('username')
        fields['password'] = self._request.form.get('password')

        