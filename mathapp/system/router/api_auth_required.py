import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app, make_response, abort
)

from mathapp.main.root_composer import RootComposer

def api_auth_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):

        ##Get token from header
        authorization_header = request.headers.get('Authorization')
        if authorization_header is None:
            abort(401)


        ##get payload from token

        ####If token is not correct format (e.g., bearer), logout




        ##check if exp is passed    

        ####if no payload, logout
        ####if exp passed, logout

        response = make_response(view(**kwargs))
        return response
    return wrapped_view