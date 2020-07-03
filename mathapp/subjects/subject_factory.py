from mathapp.subjects.orm_subject import ORMSubject

class SubjectFactory:

	def create(self, fields):
		name = fields.get('name')
		if not name:
			raise ValidationError(message = "Invalid fields")

		return ORMSubject(name=name)