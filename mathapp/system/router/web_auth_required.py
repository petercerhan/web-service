import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app, make_response
)

from mathapp.main.root_composer import RootComposer

def web_auth_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):

        ##Check Auth

        auth_token = request.cookies.get('auth_token')
        if auth_token is None:
            return redirect(url_for('auth.login'))

        check_auth_result = controller(request=None).check_authentication(auth_token)
        if not check_auth_result.get('auth_valid'):
            return redirect(url_for('auth.login'))

        if request.method == 'POST' and not _csrf_token_is_valid(request=request, auth_token=auth_token):
            return redirect(url_for('auth.login'))

        g.user_id = check_auth_result.get('user_id')
        g.user_name = check_auth_result.get('user_name')

        ##Update Token

        ####Pull from check_auth_result tuple
        # new_auth_token = controller(request=None).get_updated_auth_token(auth_token)
        new_auth_token = check_auth_result['auth_token']
        if new_auth_token is None:
            return redirect(url_for('auth.login'))

        csrf_token = controller(request=None).get_csrf_token(new_auth_token)
        g.csrf_token = csrf_token

        ##Execute Request

        response = make_response(view(**kwargs))
        response.set_cookie('auth_token', new_auth_token, httponly=True)
        return response
    
    return wrapped_view

def _csrf_token_is_valid(request, auth_token):
    csrf_token = request.form.get('csrf_token')
    if csrf_token is None:
        return False
    token_is_valid = controller(request=None).check_csrf_token(csrf_token=csrf_token, auth_token=auth_token)
    return token_is_valid



def controller(request):
    return RootComposer(request).get_system_controller_composer().compose_auth_web_controller()


