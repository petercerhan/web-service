from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class DetailSectionPresenter:

	def present_update(self, detail_section, error=None):
		if error is not None:
			flash(error.message)
		return render_template('detail_sections/update.html', 
								detail_section=detail_section, 
								detail_section_json=json.dumps(detail_section))

	def present_update_successful(self, parent_resource_url):
		return redirect(parent_resource_url)

	def present_create_detail_glyph_successful(self, detail_section_id):
		return redirect(url_for('detail_sections.update', id=detail_section_id))