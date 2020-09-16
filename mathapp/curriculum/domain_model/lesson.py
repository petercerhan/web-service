from mathapp.library.errors.validation_error import ValidationError

class Lesson:

    def __init__(self, name, display_name, unit_of_work):
        self._id = None
        self._name = name
        self._display_name = display_name
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message = "Lesson requires name")

        if not self._name.strip():
            raise ValidationError(message = "Invalid name for lesson")

        if not self._display_name:
            raise ValidationError(message = "Lesson requires display name")

        if not self._display_name.strip():
            raise ValidationError(message = "Invalid display name for lesson")



    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        self._unit_of_work.register_dirty(self)
        self._check_invariants()

    def get_display_name(self):
        return self._display_name

    def set_display_name(self, display_name):
        self._display_name = display_name
        self._unit_of_work.register_dirty(self)
        self._check_invariants()

    def delete(self):
        self._unit_of_work.register_deleted(self)

    def __repr__(self):
        return "<Lesson(name='%s') ID(id='%s')>" % (self._name, self._id)