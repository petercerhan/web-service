from mathapp.student.data_mapper.student_course.student_course_factory import StudentCourseFactory
from mathapp.student.data_mapper.student_topic.student_topic_factory import StudentTopicFactory
from mathapp.student.data_mapper.lesson_event.lesson_event_factory import LessonEventFactory
from mathapp.student.data_mapper.exercise_event.exercise_event_factory import ExerciseEventFactory

class StudentFactoryComposer:

    def __init__(self, 
                 user_data,
                 unit_of_work):
        self._user_data = user_data
        self._unit_of_work = unit_of_work

    def compose_student_course_factory(self):
        return StudentCourseFactory(unit_of_work=self._unit_of_work)

    def compose_student_topic_factory(self):
        return StudentTopicFactory(unit_of_work=self._unit_of_work)

    def compose_lesson_event_factory(self):
        return LessonEventFactory(user_data=self._user_data,
                                  unit_of_work=self._unit_of_work)

    def compose_exercise_event_factory(self):
        return ExerciseEventFactory(user_data=self._user_data,
                                    unit_of_work=self._unit_of_work)



