from flask import request


class LessonIntroWebController:

	def __init__(self, request, lesson_intro_presenter):
		self._request = request
		self._lesson_intro_presenter = lesson_intro_presenter

	def handle_create_request(self, lesson_id):
		return self._lesson_intro_presenter.present_create()

