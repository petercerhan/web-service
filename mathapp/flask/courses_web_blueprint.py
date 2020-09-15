from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('courses', __name__)

## Index

@bp.route('/')
@login_required
def index():
    return controller(request).handle_index_request()

## Create

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    return controller(request).handle_create_request()

## Update

@bp.route('/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    return controller(request).handle_update_request(id)

## Delete

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    return controller(request).handle_delete_request(id)

## Util

def controller(request):
	return RootComposer(request).compose_course_web_controller()
