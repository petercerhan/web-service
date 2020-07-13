from mathapp.sqlalchemy.subject.orm_subject import ORMSubject
from mathapp.domain.errors.validation_error import ValidationError

class SubjectFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		name = fields.get('name')
		if not name:
			raise ValidationError(message = "Invalid create fields")

		orm_subject = ORMSubject(name=name)

		subject = orm_subject.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_subject)

		return subject
