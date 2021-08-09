from mathapp.libraries.general_library.errors.validation_error import ValidationError

class Role:

    def __init__(self, role_type_name, unit_of_work):
        self._id = None
        self._role_type_name = role_type_name
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if not self._role_type_name:
            raise ValidationError(message = "Role requires role_type_name")

    def get_id(self):
        return self._id

    def get_role_type_name(self):
        return self._role_type_name

    def __repr__(self):
        return f'<Role(role_type_name={self._role_type_name}) ID(id={self._id})>'

