from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_data

class TopicInteractor:

	def __init__(self,
				topic_repository,
				unit_of_work):
		self._topic_repository = topic_repository
		self.unit_of_work = unit_of_work

	def list(self):
		topics = self._topic_repository.list()
		return [topic_to_data(topic) for topic in topics]