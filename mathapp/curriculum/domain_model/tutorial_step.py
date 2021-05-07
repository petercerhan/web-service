from mathapp.library.errors.validation_error import ValidationError

class TutorialStep:

    def __init__(self, 
                 position,
                 display_group,
                 unit_of_work):
        self._id = None
        self._position = position
        self._display_group = display_group
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._position is None:
            raise ValidationError(message = "TutorialStep requires position")

        if self._display_group is None:
            raise ValidationError(message = "TutorialStep requires display_group")

    def get_type(self):
        return 'tutorial_step'

    def get_id(self):
        return self._id

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_display_group(self):
        return self._display_group

    def set_display_group(self, display_group):
        self._display_group = display_group
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def delete(self):
        self._unit_of_work.register_deleted(self)
        
    def __repr__(self):
        return f'<TutorialStep(id={self._id})>'

