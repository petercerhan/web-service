from flask import request

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
			return self._post_create_form()
		else:
			return self._get_create_form(id)

	def _post_create_form(self):
		pass

	def _get_create_form(self, id):
		detail_section = self._detail_section_interactor.read(id)
		return self._detail_section_presenter.present_update(detail_section)