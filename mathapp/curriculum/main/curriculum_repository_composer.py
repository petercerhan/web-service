from mathapp.curriculum.data_mapper.topic.topic_repository import TopicRepository

class CurriculumRepositoryComposer:

	def __init__(self,
		         unit_of_work,
		         sqlalchemy_session):
		self._unit_of_work = unit_of_work
		self._sqlalchemy_session = sqlalchemy_session

	def compose_topic_repository(self):
		return TopicRepository(unit_of_work=self._unit_of_work,
							   session=self._sqlalchemy_session)
