from mathapp.student.data_mapper.student_course.student_course_factory import StudentCourseFactory
from mathapp.student.data_mapper.student_topic.student_topic_factory import StudentTopicFactory

class StudentFactoryComposer:

    def __init__(self, 
                 unit_of_work):
        self._unit_of_work = unit_of_work

    def compose_student_course_factory(self):
        return StudentCourseFactory(unit_of_work=self._unit_of_work)

    def compose_student_topic_factory(self):
        return StudentTopicFactory(unit_of_work=self._unit_of_work)