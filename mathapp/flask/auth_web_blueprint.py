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
    ##Issue auth token
    return controller(request).handle_login_request()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))



@bp.before_app_request
def load_logged_in_user():

    # cookies = request.cookies
    # session_cookie = cookies.get('session')
    # print(session_cookie, file=sys.stderr)

    # signing_key = current_app.config['AUTH_SECRET_KEY']

    # try:
    #     payload = {
    #         'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
    #         'iat': datetime.datetime.utcnow(),
    #         'sub': 1
    #     }
    #     token = jwt.encode(payload, signing_key, algorithm='HS256')
    # except Exception as e:
    #     print('failed to create jwt', file=sys.stderr)
    #     print(e, file=sys.stderr)

    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = controller(request).get_user(user_id)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
            
        response = make_response(view(**kwargs))
        # response.set_cookie('test_cookie', 'test_bp', httponly=True)
        return response
    
    return wrapped_view


## Util

def controller(request):
    return RootComposer(request).compose_auth_web_controller()








