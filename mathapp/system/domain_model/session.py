from mathapp.library.errors.validation_error import ValidationError

import sys

class Session:

    def __init__(self, 
                 user_value_holder, 
                 revoked, 
                 created_at, 
                 unit_of_work):
        self._id = None

        self._user_value_holder = user_value_holder
        self._revoked = revoked
        self._created_at = created_at

        self._unit_of_work = unit_of_work

        self._check_invariants

    def _check_invariants(self):
        if self._revoked is None:
            raise ValidationError(message = "Session requires revoked")
            
        if self._created_at is None:
            raise ValidationError(message = "Session requires created_at")

        if not self._user_value_holder.get_set_at_init():
            raise ValidationError(message = "Session requires user")


    def get_id(self):
        return self._id

    def get_revoked(self):
        return self._revoked

    def set_revoked(self, revoked):
        self._revoked = revoked
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def __repr__(self):
        return "<Session ID(id='%s') CreatedAt(created_at='%s') Revoked(revoked='%s')>" % (self._id, self._created_at, self._revoked)


