from mathapp.curriculum.domain_model.node_content import NodeContent

class LessonSectionParentValueHolder:

	def __init__(self, orm_lesson_section, unit_of_work):
		self._orm_lesson_section = orm_lesson_section
		self._unit_of_work = unit_of_work

	def get(self):
		orm_lesson = self._orm_lesson_section.lesson
		return orm_lesson.get_model(unit_of_work=self._unit_of_work)