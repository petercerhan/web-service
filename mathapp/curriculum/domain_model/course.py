from mathapp.library.errors.validation_error import ValidationError

import sys

class Course:
    
    def __init__(self, 
        name, 
        display_name,
        lesson_sequence_item_list_value_holder, 
        unit_of_work):

        self._id = None

        self._name = name
        self._display_name = display_name

        self._lesson_sequence_item_list_value_holder = lesson_sequence_item_list_value_holder        
        self._unit_of_work = unit_of_work

        self._check_invariants()


    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message = "Course requires name")

        if not self._name.strip():
            raise ValidationError(message = "Invalid name for course")

        if not self._display_name:
            raise ValidationError(message = "Invalid display_name for course")

        if not self._display_name.strip():
            raise ValidationError(message = "Invalid display_name for course")

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

    def get_display_name(self):
        return self._display_name

    def set_display_name(self, display_name):
        self._display_name = display_name
        self._unit_of_work.register_dirty(self)
        self._check_invariants()

    def get_lesson_sequence_items(self):
        return self._lesson_sequence_item_list_value_holder.get_list()

    def add_lesson(self, lesson, lesson_sequence_item_factory):
        max_position = max([x.get_position() for x in self._lesson_sequence_item_list_value_holder.get_list()], default=-1)
        lesson_sequence_item = lesson_sequence_item_factory.create(position=max_position+1, lesson=lesson)
        self._lesson_sequence_item_list_value_holder.add(lesson_sequence_item)

    def remove_lesson_sequence_item(self, lesson_sequence_item_id):
        lesson_sequence_items = self._lesson_sequence_item_list_value_holder.get_list()
        deleted_position = None
        for lesson_sequence_item in lesson_sequence_items:
            if lesson_sequence_item.get_id() == lesson_sequence_item_id:
                deleted_position = lesson_sequence_item.get_position()
                self._lesson_sequence_item_list_value_holder.removeAtIndex(deleted_position)

        if deleted_position is None:
            return

        for lesson_sequence_item in lesson_sequence_items:
            if lesson_sequence_item.get_position() > deleted_position:
                prior_position = lesson_sequence_item.get_position()
                lesson_sequence_item.set_position(prior_position-1)

        self._unit_of_work.register_dirty(self)
        self._check_invariants()


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







