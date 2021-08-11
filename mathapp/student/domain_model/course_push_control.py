from mathapp.libraries.general_library.errors.validation_error import ValidationError

class CoursePushControl:

    def __init__(self,
                 current_course_push_number,
                 course_id,
                 unit_of_work):
        self._id = None
        self._current_course_push_number = current_course_push_number
        self._course_id = course_id
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._current_course_push_number is None:
            raise ValidationError(message='CoursePushControl requires current_course_push_number')
            
        if self._course_id is None:
            raise ValidationError(message='CoursePushControl requires course_id')

    def get_current_course_push_number(self):
        return self._current_course_push_number

    def get_course_id(self):
        return self._course_id

    def __repr__(self):
        return f'<CoursePushControl(id={self._id})>'

