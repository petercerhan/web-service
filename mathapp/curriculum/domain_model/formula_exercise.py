from mathapp.library.errors.validation_error import ValidationError
from mathapp.curriculum.domain_model.exercise import Exercise

class FormulaExercise(Exercise):

	def __init__(self,
				 name,
				 tag,
				 topic_value_holder,
				 text,
				 formula_latex,
				 correct_option,
				 incorrect_option_1,
				 incorrect_option_2,
				 incorrect_option_3,
				 unit_of_work):
		self._text = text
		self._formula_latex = formula_latex
		self._correct_option = correct_option
		self._incorrect_option_1 = incorrect_option_1
		self._incorrect_option_2 = incorrect_option_2
		self._incorrect_option_3 = incorrect_option_3
		self._unit_of_work = unit_of_work
		super().__init__(name, tag, topic_value_holder, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if self._text is None:
			raise ValidationError(message = f'FormulaExercise requires text (id={self._id})')

		if self._text.strip() == '':
			raise ValidationError(message = f'Invalid text for FormulaExercise (id={self._id})')

		if self._formula_latex is None:
			raise ValidationError(message = f'FormulaExercise requires formula_latex (id={self._id})')

		if self._formula_latex.strip() == '':
			raise ValidationError(message = f'Invalid formula_latex for FormulaExercise (id={self._id})')

		if self._correct_option is None:
			raise ValidationError(message = f'FormulaExercise requires correct_option (id={self._id})')

		if self._correct_option.strip() == '':
			raise ValidationError(message = f'Invalid correct_option for FormulaExercise (id={self._id})')

		if self._incorrect_option_1 is None:
			raise ValidationError(message = f'FormulaExercise requires incorrect_option_1 (id={self._id})')

		if self._incorrect_option_1.strip() == '':
			raise ValidationError(message = f'Invalid incorrect_option_1 for FormulaExercise (id={self._id})')

		if self._incorrect_option_2 is None:
			raise ValidationError(message = f'FormulaExercise requires incorrect_option_2 (id={self._id})')

		if self._incorrect_option_2.strip() == '':
			raise ValidationError(message = f'Invalid incorrect_option_2 for FormulaExercise (id={self._id})')

		if self._incorrect_option_3 is None:
			raise ValidationError(message = f'FormulaExercise requires incorrect_option_3 (id={self._id})')

		if self._incorrect_option_3.strip() == '':
			raise ValidationError(message = f'Invalid incorrect_option_3 for FormulaExercise (id={self._id})')

		super()._check_invariants()


	def get_type(self):
		return 'formula_exercise'
		
	def get_text(self):
		return self._text

	def set_text(self, text):
		self._text = text
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_formula_latex(self):
		return self._formula_latex

	def set_formula_latex(self, formula_latex):
		self._formula_latex = formula_latex
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
		return f'<FormulaExercise(id={self._id}, name={self._name})>'








