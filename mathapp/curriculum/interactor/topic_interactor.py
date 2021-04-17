from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_data

import sys

class TopicInteractor:

	def __init__(self,
				topic_repository,
				topic_factory,
				unit_of_work):
		self._topic_repository = topic_repository
		self._topic_factory = topic_factory
		self._unit_of_work = unit_of_work

	def list(self):
		topics = self._topic_repository.list()
		return [topic_to_data(topic) for topic in topics]

	def create(self, fields):
		topic = self._topic_factory.create(fields)
		self._unit_of_work.commit()
		return topic_to_data(topic)