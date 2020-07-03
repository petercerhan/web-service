from mathapp.subjects.subject import Subject

class SubjectFactory:

	def create(self, fields):
		name = fields.get('name')
		if not name:
			raise ValidationError(message = "Invalid fields")

		return Subject(name=name)