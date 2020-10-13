from mathapp.curriculum.interactor.domain_to_data_transforms.lesson_intro import lesson_intro_to_enriched_data


class LessonIntroInteractor:

	def __init__(self, 
				lesson_repository, 
				lesson_intro_factory, 
				unit_of_work):
		self._lesson_repository = lesson_repository
		self._lesson_intro_factory = lesson_intro_factory
		self._unit_of_work = unit_of_work

	def create(self, lesson_id):
		lesson = self._lesson_repository.get(id=lesson_id)
		lesson_intro = lesson.create_lesson_intro(self._lesson_intro_factory)
		self._unit_of_work.commit()
		return lesson_intro_to_enriched_data(lesson_intro)

	def read(self, lesson_id, lesson_section_id):
		lesson = self._lesson_repository.get(id=lesson_id)
		lesson_intro = lesson.get_lesson_intro(lesson_section_id)
		return lesson_intro_to_enriched_data(lesson_intro)

	def update(self, lesson_id, lesson_section_id, fields):
		lesson = self._lesson_repository.get(id=lesson_id)
		lesson_intro = lesson.get_lesson_section(id=lesson_section_id)

		instruction_sections = fields.get('instruction_sections')
		if instruction_sections is not None:
			lesson_intro.sync_instruction_section_positions(instruction_sections)

		self._unit_of_work.commit()

		return lesson_intro_to_enriched_data(lesson_intro)