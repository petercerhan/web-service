import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app, make_response
)

from mathapp.main.root_composer import RootComposer

bp = Blueprint('api_auth', __name__)

@bp.route('/api/login', methods=('POST',))
def login():
	return controller(request).login()


def controller(request):
	return RootComposer(request).get_system_controller_composer().compose_auth_api_controller()