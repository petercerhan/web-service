from mathapp.library.errors.validation_error import ValidationError

class Lesson:

    def __init__(self, 
                 name,
                 position,
                 unit_of_work):
        self._id = None
        self._name = name
        self._position = position
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message = "Lesson requires name")

        if not self._name.strip():
            raise ValidationError(message = "Invalid name for Lesson")

        if self._position is None:
            raise ValidationError(message = "Lesson requires position")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    


    def __repr__(self):
        return "<Lesson(name='%s') ID(id='%s')>" % (self._name, self._id)

