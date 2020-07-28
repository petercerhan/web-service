from mathapp.domain.errors.validation_error import ValidationError

class Subject:
    
    def __init__(self, name, lesson_virtual_list, unit_of_work):
        self._id = None

        self._name = name
        if not name:
            raise ValidationError(message = "Subject requires name")
        
        self._lesson_virtual_list = lesson_virtual_list
        self._unit_of_work = unit_of_work

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        self._unit_of_work.register_dirty(self)

    def get_lessons(self):
        return self._lesson_virtual_list.get_list()
        
    def delete(self):
        self._unit_of_work.register_deleted(self)

    def __repr__(self):
        return "<Subject(name='%s') ID(id='%s')>" % (self._name, self._id)