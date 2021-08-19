from mathapp.libraries.general_library.errors.validation_error import ValidationError

class LessonCompletableDtoTemplate:

    def __init__(self,
                 lesson,
                 tutorial,
                 problem_set_dto_template):
        self.lesson = lesson
        self.tutorial = tutorial
        self.problem_set_dto_template = problem_set_dto_template
        self._check_invariants()

    def _check_invariants(self):
        if self.lesson is None:
            raise ValidationError(message='LessonCompletableDtoTemplate requires lesson')

        if (self.tutorial is None) and (self.problem_set_dto_template is None):
            raise ValidationError(message='LessonCompletableDtoTemplate requires at least one of: tutorial, problem_set')
    