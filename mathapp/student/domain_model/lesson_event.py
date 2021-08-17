from mathapp.libraries.general_library.errors.validation_error import ValidationError

class LessonEvent:

    def __init__(self,
                 completed,
                 unit_of_work):
        self._id = None
        self._completed = completed
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._completed is None:
            raise ValidationError(message="LessonEvent requires completed")
    

    def __repr__(self):
        return f'<LessonEvent(id={self._id})>'

