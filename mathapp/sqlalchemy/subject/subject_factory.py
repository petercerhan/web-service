from mathapp.sqlalchemy.subject.orm_subject import ORMSubject
from mathapp.sqlalchemy.subject.subject_mapper import SubjectMapper

class SubjectFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		name = fields.get('name')
		if not name:
			raise ValidationError(message = "Invalid fields")

		orm_subject = ORMSubject(name=name)
		mapper = SubjectMapper(self._unit_of_work, orm_subject)
		self._unit_of_work.register_created(mapper)

		return mapper.get_model()
