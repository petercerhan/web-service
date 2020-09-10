import functools

import jwt
import datetime

import sys

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, make_response
)

from mathapp.flask.root_composer import RootComposer

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    return controller(request).handle_register_request()

@bp.route('/login', methods=('GET', 'POST'))
def login():
    return controller(request).handle_login_request()

@bp.route('/logout')
def logout():
    auth_token = request.cookies.get('auth_token')
    controller(request=None).logout(auth_token)

    response = make_response( redirect(url_for('auth.login')) )
    response.set_cookie('auth_token', '', expires=0)
    return response


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = controller(request).get_user(user_id)

@bp.after_app_request
def remove_flask_session(response):
    response.set_cookie('session', '', expires=0)
    return response    

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):

        ##Check Auth

        auth_token = request.cookies.get('auth_token')
        if auth_token is None:
            return redirect(url_for('auth.login'))

        check_auth_result = controller(request=None).check_authentication(auth_token)
        if not check_auth_result.get('auth_valid'):
            return redirect(url_for('auth.login'))

        g.user_id = check_auth_result.get('user_id')
        g.user_name = check_auth_result.get('user_name')

        ##Execute Request

        response = make_response(view(**kwargs))

        ##Update Token

        new_auth_token = controller(request=None).get_updated_auth_token(auth_token)
        if new_auth_token is None:
            return redirect(url_for('auth.login'))

        response.set_cookie('auth_token', new_auth_token, httponly=True)
        return response
    
    return wrapped_view


## Util

def controller(request):
    return RootComposer(request).compose_auth_web_controller()








