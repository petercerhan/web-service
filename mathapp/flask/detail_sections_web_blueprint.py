from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('detail_sections', __name__)

@bp.route('/detail_sections/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
	return controller(request).handle_update_request(id)

def controller(request):
	return RootComposer(request).compose_detail_section_web_controller()