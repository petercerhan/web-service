from mathapp.student.interactor.domain_to_data_transforms.lesson_completable_dto_template import lesson_completable_dto_template_to_data
from mathapp.student.interactor.domain_to_data_transforms.lesson_followup_item import lesson_followup_item_to_data

class StudentTopicInteractor:

	def __init__(self,
				 student_topic_repository,
				 lesson_event_factory,
				 unit_of_work):
		self._student_topic_repository = student_topic_repository
		self._lesson_event_factory = lesson_event_factory
		self._unit_of_work = unit_of_work

	def get_next_lesson_completable(self, student_topic_id):
		student_topic = self._student_topic_repository.get(student_topic_id=student_topic_id)
		lesson_completable_dto_template = student_topic.get_next_lesson_completable()
		return lesson_completable_dto_template_to_data(lesson_completable_dto_template)

	def complete_lesson(self, student_topic_id, lesson_event_fields):
		student_topic = self._student_topic_repository.get(student_topic_id=student_topic_id)
		followup_items = student_topic.complete_lesson(lesson_event_fields=lesson_event_fields,
									  				   lesson_event_factory=self._lesson_event_factory)

		self._unit_of_work.commit()

		followup_items_data = [lesson_followup_item_to_data(x) for x in followup_items]
		return followup_items_data



