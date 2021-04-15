

class TopicValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get(self):
		orm_topic = self._orm_model.topic
		if not self._queried:
			self._unit_of_work.register_queried([orm_topic])
		topic = orm_topic.get_model(unit_of_work=self._unit_of_work)
		self._queried = True
		return topic

	def get_queried(self):
		return self._queried