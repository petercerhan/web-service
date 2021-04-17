from mathapp.curriculum.data_mapper.topic.orm_topic import ORMTopic
from mathapp.library.errors.not_found_error import NotFoundError

class TopicRepository:
	
	def __init__(self, unit_of_work, session):
		self._unit_of_work = unit_of_work
		self._session = session

	def list(self):
		orm_topics = self._session.query(ORMTopic).all()
		topics = [orm_topic.get_model(unit_of_work=self._unit_of_work) for orm_topic in orm_topics]
		self._unit_of_work.register_queried(orm_topics)
		return topics

	def get(self, id):
		orm_topic = self._session.query(ORMTopic).filter(ORMTopic.id == id).first()

		if not orm_topic:
			raise NotFoundError(message=f'Topic id={id} not found')

		topic = orm_topic.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_topic])
		return topic

	def get_by_name(self, name):
		orm_topic = self._session.query(ORMTopic).filter(ORMTopic.name == name).first()

		if orm_topic is None:
			raise NotFoundError(message='Not Found')

		topic = orm_topic.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_topic])

		return topic