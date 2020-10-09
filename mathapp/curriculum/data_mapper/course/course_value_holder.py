

class CourseValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get(self):
		orm_course = self._orm_model.course
		if not self._queried:
			self._unit_of_work.register_queried([orm_course])
		course = orm_course.get_model(unit_of_work=self._unit_of_work)
		self._queried = True
		return course

	def get_queried(self):
		return self._queried