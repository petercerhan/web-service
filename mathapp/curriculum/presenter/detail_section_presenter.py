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

	def present_update_text_glyph(self, text_glyph, error=None):
		if error is not None:
			flash(error.message)
		return render_template('detail_glyphs/update_text_glyph.html', text_glyph=text_glyph)

	def present_update_formula_glyph(self, formula_glyph, error=None):
		if error is not None:
			flash(error.message)
		return render_template('detail_glyphs/update_formula_glyph.html', formula_glyph=formula_glyph)

	def present_update_detail_glyph_successful(self, detail_section_id):
		return redirect(url_for('detail_sections.update', id=detail_section_id))

	def present_update_image_glyph(self, image_glyph, error):
		if error is not None:
			flash(error.message)
		return render_template('detail_glyphs/update_image_glyph.html', image_glyph=image_glyph)