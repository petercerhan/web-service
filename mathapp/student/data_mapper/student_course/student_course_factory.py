from mathapp.student.data_mapper.student_course.orm_student_course import ORMStudentCourse

class StudentCourseFactory:

    def __init__(self, unit_of_work):
        self._unit_of_work = unit_of_work

    def create(self, fields, student, course):
        configured_course_push_number = fields.get('configured_course_push_number')
        orm_student_course = ORMStudentCourse(student_id=student.get_id(),
                                              course_id=course.get_id(),
                                              configured_course_push_number=configured_course_push_number)
        student_course = orm_student_course.get_model(unit_of_work=self._unit_of_work)
        self._unit_of_work.register_created(orm_student_course)
        return student_course

