from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('lessons', __name__)

## Index

@bp.route('/lessons/')
@login_required
def index():
	return controller(request).handle_index_request()

@bp.route('/lessons/create', methods=('GET', 'POST'))
@login_required
def create():
	return controller(request).handle_create_request()

@bp.route('/lessons/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
	return controller(request).handle_update_request(id)

## Util

def controller(request):
	return RootComposer(request).compose_lesson_web_controller()