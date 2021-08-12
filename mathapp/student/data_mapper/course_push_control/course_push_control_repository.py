from mathapp.student.data_mapper.course_push_control.orm_course_push_control import ORMCoursePushControl
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError

class CoursePushControlRepository:

	def __init__(self,
				 unit_of_work,
				 session):
		self._unit_of_work = unit_of_work
		self._session = session

	def get_by_course_id(self, course_id):
		orm_course_push_control = self._session.query(ORMCoursePushControl).filter(ORMCoursePushControl.course_id == course_id).first()

		if not orm_course_push_control:
			raise NotFoundError(message = "CoursePushControl not found")

		course_push_control = orm_course_push_control.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_course_push_control])

		return course_push_control
