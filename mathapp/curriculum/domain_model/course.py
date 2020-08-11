from mathapp.library.errors.validation_error import ValidationError

class Course:
    
    def __init__(self, name, lesson_sequence_item_list_value_holder, unit_of_work):
        self._id = None

        self._name = name

        self._lesson_sequence_item_list_value_holder = lesson_sequence_item_list_value_holder        
        self._unit_of_work = unit_of_work

        self._check_invariants()


    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message = "Course requires name")

        if (self._lesson_sequence_item_list_value_holder.get_queried()):
            self._check_lesson_sequence_items_valid_order()

    def _check_lesson_sequence_items_valid_order(self):
        lesson_sequence_items = self._lesson_sequence_item_list_value_holder.get_list()
        positions = [item.get_position() for item in lesson_sequence_items]
        if len(positions) > len(set(positions)):
            raise ValidationError(message = "Lessons Sequence Items for course must have unique positions")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        self._unit_of_work.register_dirty(self)
        self._check_invariants()

    def get_lesson_sequence_items(self):
        return self._lesson_sequence_item_list_value_holder.get_list()

    def sync_lesson_sequence_item_positions(self, lesson_sequence_items_data_array):
        lesson_sequence_items = self._lesson_sequence_item_list_value_holder.get_list()
        for data_item in lesson_sequence_items_data_array:
            lesson_sequence_item = next(x for x in lesson_sequence_items if x.get_id() == data_item['id'])
            if lesson_sequence_item is not None:
                lesson_sequence_item.set_position(data_item['position'])
                    
        self._unit_of_work.register_dirty(self)
        self._check_invariants()
        
    def delete(self):
        self._unit_of_work.register_deleted(self)

    def __repr__(self):
        return "<Course(name='%s') ID(id='%s')>" % (self._name, self._id)