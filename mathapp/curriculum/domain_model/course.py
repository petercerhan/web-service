from mathapp.library.errors.validation_error import ValidationError

class Course:
    
    def __init__(self, name, lesson_sequence_item_list_value_holder, unit_of_work):
        self._id = None

        self._name = name
        if not name:
            raise ValidationError(message = "Course requires name")

        self._lesson_sequence_item_list_value_holder = lesson_sequence_item_list_value_holder
        
        self._unit_of_work = unit_of_work

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        self._unit_of_work.register_dirty(self)

    def get_lesson_sequence_items(self):
        return self._lesson_sequence_item_list_value_holder.get_list()
        
    def delete(self):
        self._unit_of_work.register_deleted(self)

    def __repr__(self):
        return "<Course(name='%s') ID(id='%s')>" % (self._name, self._id)