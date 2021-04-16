from mathapp.library.errors.validation_error import ValidationError

class Topic:

    def __init__(self,
                 name,
                 display_name,
                 unit_of_work):

        self._id = None
        self._name = name
        self._display_name = display_name
        self._unit_of_work = unit_of_work
        self._check_invariants()


    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message = "Topic requires name")

        if not self._name.strip():
            raise ValidationError(message = "Invalid name for Topic")

        if not self._display_name:
            raise ValidationError(message = "Topic requires display_name")

        if not self._display_name.strip():
            raise ValidationError(message = "Invalid display_name for Topic")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_display_name(self):
        return self._display_name


    def __repr__(self):
        return "<Topic(name='%s') ID(id='%s')>" % (self._name, self._id)




