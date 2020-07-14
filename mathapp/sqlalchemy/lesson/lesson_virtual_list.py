

class LessonVirtualList:
	
	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work


	def get_list(self):
		orm_lessons = self._orm_model.lessons
		lessons = [orm_lesson.get_model(unit_of_work=self._unit_of_work) for orm_lesson in orm_lessons]
		return lessons