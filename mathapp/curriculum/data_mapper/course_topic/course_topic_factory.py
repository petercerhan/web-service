from mathapp.curriculum.data_mapper.course_topic.orm_course_topic import ORMCourseTopic

class CourseTopicFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, position, topic, course):
		orm_course_topic = ORMCourseTopic(position=position,
										  topic_id=topic._id,
										  course_id=course._id)

		course_topic = orm_course_topic.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_created(orm_course_topic)

		return course_topic