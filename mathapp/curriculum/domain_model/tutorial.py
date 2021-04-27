from mathapp.library.errors.validation_error import ValidationError

class Tutorial:

    def __init__(self,
                 name,
                 lesson_value_holder,
                 tutorial_step_list_value_holder,
                 unit_of_work):
        self._id = None
        self._name = name
        self._lesson_value_holder = lesson_value_holder
        self._tutorial_step_list_value_holder = tutorial_step_list_value_holder
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

    def set_name(self, name):
        self._name = name
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_lesson(self):
        return self._lesson_value_holder.get()

    def get_tutorial_steps(self):
        return self._tutorial_step_list_value_holder.get_list()

    def delete(self):
        self._unit_of_work.register_deleted(self)

    def __repr__(self):
        return "<Tutorial(name='%s') ID(id='%s')>" % (self._name, self._id)



