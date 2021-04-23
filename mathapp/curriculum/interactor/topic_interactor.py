from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_enriched_data

class TopicInteractor:

	def __init__(self,
				topic_repository,
				topic_factory,
				lesson_factory,
				unit_of_work):
		self._topic_repository = topic_repository
		self._topic_factory = topic_factory
		self._lesson_factory = lesson_factory
		self._unit_of_work = unit_of_work

	def list(self):
		topics = self._topic_repository.list()
		return [topic_to_data(topic) for topic in topics]

	def create(self, fields):
		topic = self._topic_factory.create(fields)
		self._unit_of_work.commit()
		return topic_to_enriched_data(topic)

	def get(self, topic_id):
		topic = self._topic_repository.get(topic_id)
		return topic_to_enriched_data(topic)

	def update(self, id, fields):
		topic = self._topic_repository.get(id)

		display_name = fields.get('display_name')
		if display_name is not None:
			topic.set_display_name(display_name)

		lessons = fields.get('lessons')
		if lessons is not None:
			topic.sync_lesson_positions(lessons)

		self._unit_of_work.commit()
		return topic_to_enriched_data(topic)


	def create_lesson(self, topic_id, fields):
		topic = self._topic_repository.get(topic_id)
		topic.create_lesson(lesson_factory=self._lesson_factory, fields=fields)
		self._unit_of_work.commit()
		return topic_to_enriched_data(topic)


