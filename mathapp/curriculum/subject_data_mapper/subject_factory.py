from mathapp.curriculum.subject_data_mapper.orm_subject import ORMSubject

class SubjectFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		name = fields.get('name')
		orm_subject = ORMSubject(name=name)

		subject = orm_subject.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_subject)

		return subject
