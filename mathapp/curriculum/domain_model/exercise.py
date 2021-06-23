from mathapp.library.errors.validation_error import ValidationError

class Exercise:

    def __init__(self, 
                 name, 
                 tag,
                 topic_value_holder,
                 unit_of_work):
        self._id = None
        self._name = name
        self._tag  = tag
        self._topic_value_holder = topic_value_holder
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._name is None:
            raise ValidationError(message = f'Exercise requires name (name={self._name})')

        if self._name.strip() == '':
            raise ValidationError(message = f'Invalid name for exercise (name={self._name})')

        if self._tag is None:
            raise ValidationError(message = f'Exercise requires tag (name={self._name})')

        if self._tag.strip() == '':
            raise ValidationError(message = f'Invalid tag for exercise (name={self._name})')

        if not self._topic_value_holder.get_set_at_init():
            raise ValidationError(message = f'Exercise required topic (name={self._name})')

    def get_type(self):
        return 'exercise'

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_tag(self):
        return self._tag

    def set_tag(self, tag):
        self._tag = tag
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_topic(self):
        return self._topic_value_holder.get()

    def delete(self):
        self._unit_of_work.register_deleted(self)

    def __repr__(self):
        return f'<Exercise(id={self._id}, name={self._name})>'







