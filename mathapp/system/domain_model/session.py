from mathapp.library.errors.validation_error import ValidationError

class Session:

    def __init__(self, user_id, revoked, created_at, unit_of_work):
        self._id = None

        self._user_id = user_id
        self._revoked = revoked
        self._created_at = created_at

        self._unit_of_work = unit_of_work

        self._check_invariants

    def _check_invariants(self):
        if not self._revoked:
            raise ValidationError(message = "Session requires revoked")
            
        if not self._created_at:
            raise ValidationError(message = "Session requires created_at")

    def get_id(self):
        return self._id

    def __repr__(self):
        return "<Session ID(id='%s') CreatedAt(created_at='%s') Revoked(revoked='%s')>" % (self._id, self._created_at, self._revoked)


