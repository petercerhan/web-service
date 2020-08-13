import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from mathapp.db import Session
from mathapp.user import User

from mathapp.root_composer import RootComposer


import sys

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

    print(user_id, file=sys.stderr)
    
    if user_id is None:
        g.user = None
    else:
        g.user = Session.query(User).filter(User.id == user_id).first()

        print(g.user, file=sys.stderr)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
            
        return view(**kwargs)
    
    return wrapped_view


## Util

def controller(request):
    session = Session()
    return RootComposer(request, session).compose_auth_web_controller()
