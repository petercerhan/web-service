from mathapp.curriculum.domain_model.lesson_section import LessonSection
from mathapp.library.errors.validation_error import ValidationError

class LessonIntro(LessonSection):

	def __init__(self, 
				 position, 
				 complete_lesson, 
				 description, 
				 instruction_section_list_value_holder,
				 unit_of_work):
		self._description = description
		self._instruction_section_list_value_holder = instruction_section_list_value_holder
		self._unit_of_work = unit_of_work

		super().__init__(position, complete_lesson, unit_of_work)

		self._check_invariants()

	def _check_invariants(self):
		if not self._description:
			raise ValidationError(message = "LessonIntro requires description")

		super()._check_invariants()

	def get_type(self):
		return 'lesson_intro'

	def get_description(self):
		return self._description

	def get_instruction_sections(self):
		return self._instruction_section_list_value_holder.get_list()



	def __repr__(self):
		return f'<LessonIntro(id={self._id}, description={self._description})>'