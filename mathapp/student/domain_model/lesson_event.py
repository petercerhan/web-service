from mathapp.libraries.general_library.errors.validation_error import ValidationError

class LessonEvent:

    def __init__(self,
                 lesson_id,
                 completed,
                 unit_of_work):
        self._id = None
        self._lesson_id = lesson_id
        self._completed = completed
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._completed is None:
            raise ValidationError(message="LessonEvent requires completed")
    
    def get_lesson_id(self):
        return self._lesson_id

    def get_completed(self):
        return self._completed

    def __repr__(self):
        return f'<LessonEvent(id={self._id})>'

