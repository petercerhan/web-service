from mathapp.library.errors.validation_error import ValidationError

class LessonSection:

    def __init__(self, position, complete_lesson, parent_value_holder, unit_of_work):
        self._id = None

        self._position = position
        self._complete_lesson = complete_lesson

        self._parent_value_holder = parent_value_holder
        self._unit_of_work = unit_of_work

        self._check_invariants()

    def _check_invariants(self):
        if self._position is None:
            raise ValidationError(message = "LessonSection requires position")

        if self._complete_lesson is None:
            raise ValidationError(message = "LessonSection requires complete_lesson")

    def get_id(self):
        return self._id

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_type(self):
        return 'lesson_section'

    def get_display_name(self):
        return f'Lesson section id: {self._id}'

    def delete(self):
        self._unit_of_work.register_deleted(self)

    def get_parent(self):
        return self._parent_value_holder.get()

    def __repr__(self):
        return f'<LessonSection(id={self._id}, positon={self._position})>'