from mathapp.system.domain_model.role import Role

class Student(Role):

    def __init__(self,
                 unit_of_work):
        super().__init__(unit_of_work)

    def get_type(self):
        return 'student'

    def initialize_student_course(self, 
                                  course, 
                                  course_push_control,
                                  student_course_factory):
        fields = {'configured_course_push_number': course_push_control.get_current_course_push_number()}
        student_course = student_course_factory.create(fields=fields,
                                                       student=self,
                                                       course=course)
        return student_course
    
    def __repr__(self):
        return f'<Student(role_type_name={self._role_type_name}) ID(id={self._id})>'

