from flask import request
from mathapp.curriculum.controller.url_from_lesson_graph_branch import url_from_lesson_graph_branch
from mathapp.library.errors.mathapp_error import MathAppError

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

		try:
			self._detail_section_interactor.update(id, fields)
			branch = self._detail_section_interactor.get_branch_for_node(id)
			branch.pop()
			url = url_from_lesson_graph_branch(branch)
			return self._detail_section_presenter.present_update_successful(url)
		except MathAppError as error:
			return self._get_update_form(id, error)

	def _get_update_form(self, id, error):
		self._detail_section_interactor.get_branch_for_node(id)
		detail_section = self._detail_section_interactor.read(id)
		return self._detail_section_presenter.present_update(detail_section)