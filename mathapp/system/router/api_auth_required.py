import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app, make_response, abort
)

from mathapp.main.root_composer import RootComposer

def api_auth_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):

        ##Get Authorization header
        authorization_header = request.headers.get('Authorization')
        if authorization_header is None:
            abort(401)

        ##Get token from header
        if not authorization_header.startswith('Bearer '):
            abort(401)
        token = authorization_header[len('Bearer '):]

        ##Check if token valid
        if not controller(request).auth_token_is_valid(token):
            abort(401)

        response = make_response(view(**kwargs))
        return response
    return wrapped_view


def controller(request):
    return RootComposer(request).get_system_controller_composer().compose_auth_api_controller()