from mathapp.libraries.general_library.errors.validation_error import ValidationError

class LessonCompletePackageDtoTemplate:

    def __init__(self,
                 student_topic,
                 lesson_complete_followup_item_dto_templates):
        self.student_topic = student_topic
        self.lesson_complete_followup_item_dto_templates = lesson_complete_followup_item_dto_templates
        self._check_invariants()

    def _check_invariants(self):
        if self.student_topic is None:
            raise ValidationError(message='LessonCompletePackageDtoTemplate requires student_topic')

        if len(self.lesson_complete_followup_item_dto_templates) < 1:
            raise ValidationError(message='LessonCompletePackageDtoTemplate requires at least one followup item')