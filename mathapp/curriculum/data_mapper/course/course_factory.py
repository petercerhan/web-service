from mathapp.curriculum.data_mapper.course.orm_course import ORMCourse

class CourseFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		name = fields.get('name')
		display_name = fields.get('display_name')
		orm_course = ORMCourse(name=name, display_name=display_name)

		course = orm_course.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_course)

		return course
