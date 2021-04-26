from mathapp.library.errors.validation_error import ValidationError

class Tutorial:

    def __init__(self,
                 name,
                 lesson_value_holder,
                 unit_of_work):
        self._id = None
        self._name = name
        self._lesson_value_holder = lesson_value_holder
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message="Tutorial requires name")

        if not self._name.strip():
            raise ValidationError(message="Invalid name for Tutorial")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_lesson(self):
        return self._lesson_value_holder.get()

    def __repr__(self):
        return "<Tutorial(name='%s') ID(id='%s')>" % (self._name, self._id)



