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
    session.clear()
    return redirect(url_for('index'))



@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = controller(request).get_user(user_id)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):

        auth_token = request.cookies.get('auth_token')
        if auth_token is None:
            return redirect(url_for('auth.login'))


        #Check auth
        if not controller(request=None).check_authentication(auth_token):
            return redirect(url_for('auth.login'))


        #remove
        if g.user is None:
            return redirect(url_for('auth.login'))
        ###

        response = make_response(view(**kwargs))

        ##Update auth

        return response
    
    return wrapped_view


## Util

def controller(request):
    return RootComposer(request).compose_auth_web_controller()








