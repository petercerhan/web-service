

class CourseTopicListValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get_list(self):
		orm_course_topics = self._orm_model.course_topics
		if not self._queried:
			self._unit_of_work.register_queried(orm_course_topics)
		course_topics = [x.get_model(unit_of_work=self._unit_of_work) for x in orm_course_topics]
		self._queried = True
		return course_topics

	def add(self, course_topic):
		orm_course_topic = self._unit_of_work.orm_model_for_model(course_topic)
		self._orm_model.course_topics.append(orm_course_topic)

	def removeAtIndex(self, index):
		del self._orm_model.course_topics[index]

	def get_queried(self):
		return self._queried

