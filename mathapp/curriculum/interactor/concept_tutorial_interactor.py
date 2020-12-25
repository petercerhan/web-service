from mathapp.curriculum.interactor.domain_to_data_transforms.concept_tutorial import concept_tutorial_to_enriched_data
from mathapp.curriculum.interactor.domain_to_data_transforms.detail_section import detail_section_to_data

from mathapp.library.errors.mathapp_error import MathAppError
from mathapp.library.errors.validation_error import ValidationError

class ConceptTutorialInteractor:

	def __init__(self, 
				lesson_repository, 
				concept_tutorial_factory, 
				detail_section_factory,
				unit_of_work):
		self._lesson_repository = lesson_repository
		self._concept_tutorial_factory = concept_tutorial_factory
		self._detail_section_factory = detail_section_factory
		self._unit_of_work = unit_of_work


	def create(self, fields, lesson_id):
		lesson = self._lesson_repository.get(id=lesson_id)
		concept_tutorial = lesson.create_concept_tutorial(fields=fields, 
														  concept_tutorial_factory=self._concept_tutorial_factory)
		self._unit_of_work.commit()
		return concept_tutorial_to_enriched_data(concept_tutorial)


	def read(self, lesson_id, lesson_section_id):
		lesson = self._lesson_repository.get(id=lesson_id)
		concept_tutorial = lesson.get_lesson_section(id=lesson_section_id)
		return concept_tutorial_to_enriched_data(concept_tutorial)


	def update(self, lesson_id, lesson_section_id, fields):
		lesson = self._lesson_repository.get(id=lesson_id)
		concept_tutorial = lesson.get_lesson_section(id=lesson_section_id)

		display_name = fields.get('display_name')
		if display_name is not None:
			concept_tutorial.set_display_name(display_name)

		self._unit_of_work.commit()

		return concept_tutorial_to_enriched_data(concept_tutorial)


	def create_detail_section(self, lesson_id, lesson_section_id, fields):
		lesson = self._lesson_repository.get(id=lesson_id)
		concept_tutorial = lesson.get_lesson_section(id=lesson_section_id)
		detail_section = concept_tutorial.create_instruction_section(fields=fields, instruction_section_factory=self._detail_section_factory)
		self._unit_of_work.commit()
		return detail_section_to_data(detail_section)
