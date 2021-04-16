from mathapp.curriculum.data_mapper.topic.orm_topic import ORMTopic

class TopicFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		name = fields.get('name')
		display_name = fields.get('display_name')
		orm_topic = ORMTopic(name=name, display_name=display_name)

		topic = orm_topic.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_topic)

		return topic

