



class LessonSectionListValueHolder:

		def __init__(self, orm_model, unit_of_work):
			self._orm_model = orm_model
			self._unit_of_work = unit_of_work
			self._queried = False

		def get_list(self):
			orm_lesson_sections = self._orm_model.lesson_sections
			if not self._queried:
				self._unit_of_work.register_queried(orm_lesson_sections)
			lesson_sections = [orm_item.get_model(unit_of_work=self._unit_of_work) for orm_item in orm_lesson_sections]
			self._queried = True
			return lesson_sections

		def get_queried(self):
			return self._queried



