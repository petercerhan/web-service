from mathapp.library.errors.validation_error import ValidationError



class LessonSection:

    def __init__(self, position, complete_lesson):
        self._id = None

        self._position = position
        self._complete_lesson = complete_lesson

        self._check_invariants()

    def _check_invariants(self):
        if not self._position:
            raise ValidationError(message = "LessonSection requires position")

        if not self._complete_lesson:
            raise ValidationError(message = "LessonSection requires complete_lesson")
