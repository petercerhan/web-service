from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('topics', __name__)

@bp.route('/topics/')
@login_required
def index():
	return controller(request).get_index()

def controller(request):
	return RootComposer(request).compose_topic_web_controller()