from mathapp.libraries.general_library.errors.validation_error import ValidationError

class StudentCourse:

	def __init__(self,
				 configured_course_push_number,
				 course_value_holder,
				 unit_of_work):
        self._id = None
		self._configured_course_push_number = configured_course_push_number
		self._course_value_holder = course_value_holder
		self._unit_of_work = unit_of_work
		self._check_invariants()

	def _check_invariants(self):
		if self._configured_course_push_number is None:
			raise ValidationError(message='StudentCourse requires configured_course_push_number')

		if not self._course_value_holder.get_set_at_init():
			raise ValidationError(message='StudentCourse requires course')


	def __repr__(self):
		return f'<StudentCourse(id={self._id})>'

		