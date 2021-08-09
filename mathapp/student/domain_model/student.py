from mathapp.system.domain_model.role import Role

class Student(Role):

    def __init__(self,
                 unit_of_work):
        super().__init__(unit_of_work)

    def get_type(self):
        return 'student'
    
    def __repr__(self):
        return f'<Student(role_type_name={self._role_type_name}) ID(id={self._id})>'

