import json

class CoursePushControlApiPresenter:

	def single(self, course_push_control):
		return json.dumps(course_push_control)

