from mathapp.library.errors.validation_error import ValidationError

class Exercise:

    def __init__(self, 
                 name, 
                 tag,
                 unit_of_work):
        self._id = None
        self._name = name
        self._tag  = tag
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._name is None:
            raise ValidationError(message = f'Exercise requires name (id={self._id})')

        if self._name.strip() == '':
            raise ValidationError(message = f'Invalid name for exercise (id={self._id})')

        if self._tag is None:
            raise ValidationError(message = f'Exercise requires tag (id={self._id})')

        if self._tag.strip() == '':
            raise ValidationError(message = f'Invalid tag for exercise (id={self._id})')

    def get_type(self):
        return 'exercise'

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_tag(self):
        return self._tag


    def __repr__(self):
        return f'<Exercise(id={self._id}, name={self._name})>'