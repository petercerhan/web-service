from mathapp.libraries.general_library.errors.validation_error import ValidationError
from mathapp.curriculum.domain_model.exercise import Exercise

class DiagramExercise(Exercise):

	def __init__(self,
				 name,
				 tag,
				 topic_value_holder,
				 text,
				 diagram_image_data,
				 source_code_filename,
				 correct_option,
				 incorrect_option_1,
				 incorrect_option_2,
				 incorrect_option_3,
				 unit_of_work):
		self._text = text
		self._diagram_image_data = diagram_image_data
		self._source_code_filename = source_code_filename
		self._correct_option = correct_option
		self._incorrect_option_1 = incorrect_option_1
		self._incorrect_option_2 = incorrect_option_2
		self._incorrect_option_3 = incorrect_option_3
		self._unit_of_work = unit_of_work
		super().__init__(name, tag, topic_value_holder, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if self._text is None:
			raise ValidationError(message = f'DiagramExercise requires text (id={self._id})')

		if self._text.strip() == '':
			raise ValidationError(message = f'Invalid text for DiagramExercise (id={self._id})')

		if self._diagram_image_data is None:
			raise ValidationError(message = f'DiagramExercise (id={self._id}) requires diagram_image_data')

		if self._source_code_filename is None:
			raise ValidationError(message = f'DiagramExercise (id={self._id}) requires source_code_filename')

		if self._correct_option is None:
			raise ValidationError(message = f'DiagramExercise requires correct_option (id={self._id})')

		if self._correct_option.strip() == '':
			raise ValidationError(message = f'Invalid correct_option for DiagramExercise (id={self._id})')

		if self._incorrect_option_1 is None:
			raise ValidationError(message = f'DiagramExercise requires incorrect_option_1 (id={self._id})')

		if self._incorrect_option_1.strip() == '':
			raise ValidationError(message = f'Invalid incorrect_option_1 for DiagramExercise (id={self._id})')

		if self._incorrect_option_2 is None:
			raise ValidationError(message = f'DiagramExercise requires incorrect_option_2 (id={self._id})')

		if self._incorrect_option_2.strip() == '':
			raise ValidationError(message = f'Invalid incorrect_option_2 for DiagramExercise (id={self._id})')

		if self._incorrect_option_3 is None:
			raise ValidationError(message = f'DiagramExercise requires incorrect_option_3 (id={self._id})')

		if self._incorrect_option_3.strip() == '':
			raise ValidationError(message = f'Invalid incorrect_option_3 for DiagramExercise (id={self._id})')

		super()._check_invariants()


	def get_type(self):
		return 'diagram_exercise'
		
	def get_text(self):
		return self._text

	def set_text(self, text):
		self._text = text
		self._check_invariants()
		self._unit_of_work.register_dirty(self)
		
	def get_diagram_image_data(self):
		return self._diagram_image_data

	def get_source_code_filename(self):
		return self._source_code_filename

	def set_diagram_image(self, diagram_image_data, source_code_filename):
		self._diagram_image_data = diagram_image_data
		self._source_code_filename = source_code_filename
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_correct_option(self):
		return self._correct_option

	def set_correct_option(self, correct_option):
		self._correct_option = correct_option
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_incorrect_option_1(self):
		return self._incorrect_option_1

	def set_incorrect_option_1(self, incorrect_option_1):
		self._incorrect_option_1 = incorrect_option_1
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_incorrect_option_2(self):
		return self._incorrect_option_2

	def set_incorrect_option_2(self, incorrect_option_2):
		self._incorrect_option_2 = incorrect_option_2
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_incorrect_option_3(self):
		return self._incorrect_option_3

	def set_incorrect_option_3(self, incorrect_option_3):
		self._incorrect_option_3 = incorrect_option_3
		self._check_invariants()
		self._unit_of_work.register_dirty(self)


	def __repr__(self):
		return f'<DiagramExercise(id={self._id}, name={self._name})>'




