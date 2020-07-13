from mathapp.sqlalchemy.subject.orm_subject import ORMSubject
from mathapp.sqlalchemy.subject.subject_mapper import SubjectMapper
from mathapp.domain.errors.validation_error import ValidationError

class SubjectFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		name = fields.get('name')
		if not name:
			raise ValidationError(message = "Invalid create fields")

		orm_subject = ORMSubject(name=name)

		# mapper = SubjectMapper(self._unit_of_work, orm_subject)

		subject = orm_subject.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_subject)

		return subject
