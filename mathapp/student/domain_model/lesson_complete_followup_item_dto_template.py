from mathapp.libraries.general_library.errors.validation_error import ValidationError

class LessonCompleteFollowupItemDtoTemplate:

    def __init__(self,
                 lesson):
        self.lesson = lesson
        self.type = 'lesson_complete_followup_item'
        self._check_invariants()

    def _check_invariants(self):
        if self.lesson is None:
            raise ValidationError(message='LessonCompleteFollowupItemDtoTemplate requires lesson')

    