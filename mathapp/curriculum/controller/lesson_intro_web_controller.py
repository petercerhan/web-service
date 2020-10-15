from flask import request
from mathapp.library.errors.mathapp_error import MathAppError
from mathapp.library.errors.validation_error import ValidationError
import json


class LessonIntroWebController:

	def __init__(self, 
				request, 
				lesson_intro_presenter, 
				detail_section_presenter,
				lesson_intro_interactor,
				lesson_interactor, 
				detail_section_interactor):
		self._request = request
		self._lesson_intro_presenter = lesson_intro_presenter
		self._detail_section_presenter = detail_section_presenter
		self._lesson_intro_interactor = lesson_intro_interactor
		self._lesson_interactor = lesson_interactor
		self._detail_section_interactor = detail_section_interactor



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
		fields = {}
		instruction_sections = self._request.form.get('instruction_sections')
		if instruction_sections is not None:
			fields['instruction_sections'] = json.loads( instruction_sections )

		try: 
			self._lesson_intro_interactor.update(lesson_id, lesson_section_id, fields)
			return self._lesson_intro_presenter.present_update_successful(lesson_id=lesson_id)
		except MathAppError as error:
			self._get_update_form(lesson_id=lesson_id, lesson_section_id=lesson_section_id, error=error)

	def _get_update_form(self, lesson_id, lesson_section_id, error=None):
		lesson = self._lesson_interactor.read(lesson_id)
		lesson_intro = self._lesson_intro_interactor.read(lesson_id=lesson_id, lesson_section_id=lesson_section_id)
		return self._lesson_intro_presenter.present_update(lesson=lesson, lesson_intro=lesson_intro, error=error)


	def handle_create_detail_section_request(self, lesson_id, lesson_section_id):
		fields = {}
		fields['title'] = self._request.form.get('title')

		try:
			self._lesson_intro_interactor.create_detail_section(lesson_id, lesson_section_id, fields)
			return self._lesson_intro_presenter.present_create_detail_section_successful(lesson_id, lesson_section_id)
		except MathAppError as error:
			self._get_update_form(lesson_id=lesson_id, lesson_section_id=lesson_section_id, error=error)












