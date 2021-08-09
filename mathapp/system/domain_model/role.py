from mathapp.libraries.general_library.errors.validation_error import ValidationError

class Role:

    def __init__(self, unit_of_work):
        self._id = None
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        pass

    def get_id(self):
        return self._id

    def get_type(self):
        return 'role'

    def __repr__(self):
        return f'<Role(role_type_name={self._role_type_name}) ID(id={self._id})>'

