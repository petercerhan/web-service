import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app, make_response, abort
)

from mathapp.main.root_composer import RootComposer

def api_auth_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        authorization_header = _get_auth_header(request)
        token = _get_token_from_auth_header(authorization_header)
        _check_auth_token_valid(token)

        response = make_response(view(**kwargs))
        return response
    return wrapped_view

def _get_auth_header(request):
    authorization_header = request.headers.get('Authorization')
    if authorization_header is None:
        abort(401)
    return authorization_header

def _get_token_from_auth_header(authorization_header):
    if not authorization_header.startswith('Bearer '):
        abort(401)
    token = authorization_header[len('Bearer '):]
    return token

def _check_auth_token_valid(token):
    if not controller(request).auth_token_is_valid(token):
        abort(401)



def controller(request):
    return RootComposer(request).get_system_controller_composer().compose_auth_api_controller()