from mathapp.curriculum.data_mapper.course_topic.orm_course_topic import ORMCourseTopic

class CourseTopicFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, position, topic):
		orm_topic = self._unit_of_work.orm_model_for_model(topic)
		orm_course_topic = ORMCourseTopic(position=position)
		orm_course_topic.topic = orm_topic

		course_topic = orm_course_topic.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_created(orm_course_topic)

		return course_topic