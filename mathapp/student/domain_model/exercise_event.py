from mathapp.libraries.general_library.errors.validation_error import ValidationError

class ExerciseEvent:

    def __init__(self,
                 completed,
                 correct,
                 unit_of_work):
        self._id = None
        self._completed = completed
        self._correct = correct
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._completed is None:
            raise ValidationError(message="ExerciseEvent requires completed")

        if self._correct is None:
            raise ValidationError(message="ExerciseEvent requires correct")

    def __repr__(self):
        return f'<ExerciseEvent(id={self._id})>'

        