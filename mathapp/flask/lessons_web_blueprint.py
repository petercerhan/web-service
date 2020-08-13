from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.root_composer import RootComposer
from mathapp.db import Session

bp = Blueprint('lessons', __name__)

## Index

@bp.route('/lessons/')
@login_required
def index():
	return controller(request).handle_index_request()

## Util

def controller(request):
	session = Session()
	return RootComposer(request, session).compose_lesson_web_controller()