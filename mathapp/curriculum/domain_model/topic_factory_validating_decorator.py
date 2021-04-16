from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

class TopicFactoryValidatingDecorator:

	def __init__(self, topic_factory, topic_repository):
		self._topic_factory = topic_factory
		self._topic_repository = topic_repository

	def create(self, fields):
		name = fields.get('name')
		if name is not None:
			self._check_name_unique(name)

		return self._topic_factory.create(fields)

	def _check_name_unique(self, name):
		try:
			self._topic_repository.get_by_name(name)
			raise ValidationError(message='Topic name must be unique')
		except NotFoundError:
			pass
	
