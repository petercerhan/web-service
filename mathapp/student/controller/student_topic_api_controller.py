import json
from datetime import datetime

class StudentTopicApiController:

	def __init__(self,
				 request,
				 student_topic_interactor):
		self._request = request
		self._student_topic_interactor = student_topic_interactor

	def get_next_lesson_completable(self, student_topic_id):
		return self._student_topic_interactor.get_next_lesson_completable(student_topic_id=student_topic_id)

	def complete_lesson(self, student_topic_id):
		request_json = self._request.get_json()
		lesson_event_fields = {}
		lesson_event_fields['lesson_id'] = request_json.get('lesson_id')
		lesson_event_fields['completed'] = request_json.get('completed')
		lesson_event_fields['start_datetime'] = datetime.strptime(request_json.get('start_datetime'), '%Y-%m-%d %H:%M:%S')
		lesson_event_fields['end_datetime'] = datetime.strptime(request_json.get('end_datetime'), '%Y-%m-%d %H:%M:%S')
		lesson_event_fields['client_timezone'] = request_json.get('client_timezone')
		lesson_event_fields['activity_data'] = json.dumps(request_json)

		return self._student_topic_interactor.complete_lesson(student_topic_id=student_topic_id, 
															  lesson_event_fields=lesson_event_fields)
		
