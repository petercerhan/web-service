import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app, make_response
)

from mathapp.main.root_composer import RootComposer

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

@bp.after_app_request
def remove_flask_session(response):
    response.set_cookie('session', '', expires=0)
    return response    


def controller(request):
    return RootComposer(request).get_system_controller_composer().compose_auth_web_controller()








