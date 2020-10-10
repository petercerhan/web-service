from flask import request
from mathapp.library.errors.validation_error import ValidationError


class LessonIntroWebController:

	def __init__(self, 
				request, 
				lesson_intro_presenter, 
				lesson_intro_interactor):
		self._request = request
		self._lesson_intro_presenter = lesson_intro_presenter
		self._lesson_intro_interactor = lesson_intro_interactor



	def handle_create_request(self, lesson_id):
		if self._request.method == 'POST':
			return self._post_create_form(lesson_id=lesson_id)
		else:
			return self._get_create_form()

	def _post_create_form(self, lesson_id):
		try:
			self._lesson_intro_interactor.create(lesson_id=lesson_id)
			return self._lesson_intro_presenter.present_create_successful(lesson_id=lesson_id)
		except ValidationError as error:
			return self._lesson_intro_presenter.present_create(error=error)

	def _get_create_form(self):
		return self._lesson_intro_presenter.present_create()



	def handle_update_request(self, lesson_id, lesson_section_id):
		if self._request.method == 'POST':
			return self._post_update_form(lesson_id, lesson_section_id)
		else:
			return self._get_update_form(lesson_id, lesson_section_id)

	def _post_update_form(self, lesson_id, lesson_section_id):
		pass

	def _get_update_form(self, lesson_id, lesson_section_id):
		return self._lesson_intro_presenter.present_update(lesson_id, lesson_intro=None)

