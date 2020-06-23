from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from mathapp.auth import login_required
from mathapp.subjects.subjects_web_controller import SubjectsWebController

bp = Blueprint('subjects', __name__)

## Index

@bp.route('/')
def index():
    controller = SubjectsWebController(request)
    return controller.handle_index_request()

## Create

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    controller = SubjectsWebController(request)
    return controller.handle_create_request()

## Update

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    controller = SubjectsWebController(request)
    return controller.handle_update_request(id)

## Delete

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    controller = SubjectsWebController(request)
    return controller.handle_delete_request(id)

