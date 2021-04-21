

class LessonListValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get_list(self):
		orm_lessons = self._orm_model.lessons
		if not self._queried:
			self._unit_of_work.register_queried(orm_lessons)
		lessons = [x.get_model(unit_of_work=self._unit_of_work) for x in orm_lessons]
		self._queried = True
		return lessons

	def add(self, lesson):
		orm_lesson = self._unit_of_work.orm_model_for_model(lesson)
		self._orm_model.lessons.append(orm_lesson)

	def removeAtIndex(self, index):
		del self._orm_model.lessons[index]

	def get_queried(self):
		return self._queried