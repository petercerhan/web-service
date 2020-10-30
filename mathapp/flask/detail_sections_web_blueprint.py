from flask import (
    Blueprint, request, g
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('detail_sections', __name__)

@bp.route('/detail_sections/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
	return controller(request).handle_update_request(id)

@bp.route('/detail_sections/<int:detail_section_id>/create_text_glyph', methods=('POST',))
@login_required
def create_text_glyph(detail_section_id):
	return controller(request).handle_create_text_glyph_request(detail_section_id)

@bp.route('/detail_sections/<int:detail_section_id>/create_formula_glyph', methods=('POST',))
@login_required
def create_formula_glyph(detail_section_id):
	return controller(request).handle_create_formula_glyph_request(detail_section_id)

@bp.route('/detail_sections/<int:detail_section_id>/create_image_glyph', methods=('POST',))
@login_required
def create_image_glyph(detail_section_id):
	return controller(request).handle_create_image_glyph_request(g.user_id, detail_section_id)



def controller(request):
	return RootComposer(request).compose_detail_section_web_controller()