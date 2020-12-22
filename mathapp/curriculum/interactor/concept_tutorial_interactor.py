from mathapp.curriculum.interactor.domain_to_data_transforms.concept_tutorial import concept_tutorial_to_enriched_data

class ConceptTutorialInteractor:

	def __init__(self, 
				lesson_repository, 
				concept_tutorial_factory, 
				unit_of_work):
		self._lesson_repository = lesson_repository
		self._concept_tutorial_factory = concept_tutorial_factory
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


