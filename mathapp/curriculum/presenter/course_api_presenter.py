import json

class CourseApiPresenter:

	def list(self, courses):
		envelope = {'data': courses}
		return json.dumps(envelope)

