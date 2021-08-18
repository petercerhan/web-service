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

		exercise_activity_data = request_json.get('exercise_activity_data')
		exercise_event_fields_list = self._process_exercise_event_request_data(exercise_activity_data)

		followup_items = self._student_topic_interactor.complete_lesson(student_topic_id=student_topic_id, 
															  			lesson_event_fields=lesson_event_fields,
															  			exercise_event_fields_list=exercise_event_fields_list)
		return {'data': followup_items}
		
	def _process_exercise_event_request_data(self, exercise_activity_data):
		exercise_event_data = []
		for x in exercise_activity_data:
			exercise_event = {}
			exercise_event['exercise_id'] = x.get('exercise_id')
			exercise_event['lesson_id'] = x.get('lesson_id')
			exercise_event['completed'] = x.get('completed')
			exercise_event['correct'] = x.get('correct')
			exercise_event['start_datetime'] = datetime.strptime(x.get('start_datetime'), '%Y-%m-%d %H:%M:%S')
			exercise_event['end_datetime'] = datetime.strptime(x.get('end_datetime'), '%Y-%m-%d %H:%M:%S')
			exercise_event['client_timezone'] = x.get('client_timezone')
			exercise_event['activity_data'] = json.dumps(x)
			exercise_event_data.append(exercise_event)
		return exercise_event_data
