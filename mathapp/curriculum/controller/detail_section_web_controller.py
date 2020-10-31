from flask import request
from mathapp.curriculum.controller.url_from_lesson_graph_branch import url_from_lesson_graph_branch
from mathapp.library.errors.mathapp_error import MathAppError

import json

class DetailSectionWebController:

	def __init__(self,
				 request, 
				 detail_section_presenter, 
				 detail_section_interactor):
		self._request = request
		self._detail_section_presenter = detail_section_presenter
		self._detail_section_interactor = detail_section_interactor

	def handle_update_request(self, id):
		if self._request.method == 'POST':
			return self._post_update_form(id)
		else:
			return self._get_update_form(id, error=None)

	def _post_update_form(self, id):
		fields = {}
		fields['title'] = self._request.form.get('title')
		detail_glyphs = self._request.form.get('detail_glyphs')
		if detail_glyphs is not None:
			fields['detail_glyphs'] = json.loads(detail_glyphs)		

		try:
			self._detail_section_interactor.update(id, fields)
			branch = self._detail_section_interactor.get_branch_for_node(id)
			branch.pop()
			url = url_from_lesson_graph_branch(branch)
			return self._detail_section_presenter.present_update_successful(url)
		except MathAppError as error:
			return self._get_update_form(id, error)

	def _get_update_form(self, id, error):
		detail_section = self._detail_section_interactor.read(id)
		return self._detail_section_presenter.present_update(detail_section)


	def handle_create_text_glyph_request(self, detail_section_id):
		fields = {}
		fields['text'] = self._request.form.get('text')

		try:
			self._detail_section_interactor.create_text_glyph(detail_section_id, fields)
			return self._detail_section_presenter.present_create_detail_glyph_successful(detail_section_id)
		except MathAppError as error:
			self._get_update_form(id=detail_section_id, error=error)

	def handle_create_formula_glyph_request(self, detail_section_id):
		fields = {}
		fields['formula'] = self._request.form.get('formula')

		try:
			self._detail_section_interactor.create_formula_glyph(detail_section_id, fields)
			return self._detail_section_presenter.present_create_detail_glyph_successful(detail_section_id)
		except MathAppError as error:
			self._get_update_form(id=detail_section_id, error=error)

	def handle_create_image_glyph_request(self, user_id, detail_section_id):
		source_code_file = self._request.files.get('source_code_file')
		image_file = self._request.files.get('image_file')
		fields = {}

		try:
			self._detail_section_interactor.create_image_glyph(user_id, detail_section_id, source_code_file, image_file, fields)
			return self._detail_section_presenter.present_create_detail_glyph_successful(detail_section_id)
		except MathAppError as error:
			self._get_update_form(id=detail_section_id, error=error)














