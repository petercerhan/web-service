from mathapp.student.data_mapper.student_course.student_course_factory import StudentCourseFactory

class StudentFactoryComposer:

    def __init__(self, 
                 unit_of_work):
        self._unit_of_work = unit_of_work

    def compose_student_course_factory(self):
        return StudentCourseFactory(unit_of_work=self._unit_of_work)
