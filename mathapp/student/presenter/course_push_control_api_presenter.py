import json
from flask import abort

class CoursePushControlApiPresenter:

	def single(self, course_push_control):
		return json.dumps(course_push_control)

	def error(self):
		abort(404)

