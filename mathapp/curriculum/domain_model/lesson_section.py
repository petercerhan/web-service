from mathapp.library.errors.validation_error import ValidationError

import sys

class LessonSection:

    def __init__(self, position, complete_lesson):
        self._id = None

        self._position = position
        self._complete_lesson = complete_lesson

        self._check_invariants()

    def _check_invariants(self):
        if self._position is None:
            raise ValidationError(message = "LessonSection requires position")

        if self._complete_lesson is None:
            raise ValidationError(message = "LessonSection requires complete_lesson")

    def get_id(self):
        return self._id

    def get_position(self):
        return self._position

    def get_type(self):
        return 'lesson_section'