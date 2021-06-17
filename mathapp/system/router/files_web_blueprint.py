from flask import (
    Blueprint, request, g
)
from mathapp.system.router.auth_web_blueprint import web_auth_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('files', __name__)

@bp.route('/files/<string:filename>', methods=('GET',))
@web_auth_required
def download_file(filename):
	return controller(request).get_file(filename)


def controller(request):
	return RootComposer(request).compose_file_web_controller()