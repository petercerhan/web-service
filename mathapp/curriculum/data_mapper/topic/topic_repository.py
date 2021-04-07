from mathapp.curriculum.data_mapper.topic.orm_topic import ORMTopic

class TopicRepository:
	
	def __init__(self, unit_of_work, session):
		self._unit_of_work = unit_of_work
		self._session = session

	def list(self):
		orm_topics = self._session.query(ORMTopic).all()
		topics = [orm_topic.get_model(unit_of_work=self._unit_of_work) for orm_topic in orm_topics]
		self._unit_of_work.register_queried(orm_topics)
		return topics

