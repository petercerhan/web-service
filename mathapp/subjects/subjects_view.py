from flask import (
    Blueprint, request
)
from mathapp.auth import login_required
from mathapp.root_composer import RootComposer
from mathapp.db import Session

bp = Blueprint('subjects', __name__)

## Index

@bp.route('/')
def index():
    return controller(request).handle_index_request()

## Create

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    return controller(request).handle_create_request()

## Update

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
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
	session = Session()
	return RootComposer(request, session).compose_subjects_web_controller()
