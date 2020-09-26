from mathapp.library.errors.validation_error import ValidationError

class Lesson:

    def __init__(self, name, display_name, lesson_section_list_value_holder, unit_of_work):
        self._id = None
        self._name = name
        self._display_name = display_name
        self._lesson_section_list_value_holder = lesson_section_list_value_holder
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message = "Lesson requires name")

        if not self._name.strip():
            raise ValidationError(message = "Invalid name for lesson")

        if not self._display_name:
            raise ValidationError(message = "Lesson requires display name")

        if not self._display_name.strip():
            raise ValidationError(message = "Invalid display name for lesson")

        if (self._lesson_section_list_value_holder.get_queried()):
            self._check_lesson_sections_valid_order()


    def _check_lesson_sections_valid_order(self):
        lesson_sections = self._lesson_section_list_value_holder.get_list()
        positions = [item.get_position() for item in lesson_sections]
        if len(positions) > len(set(positions)):
            raise ValidationError(message = "LessonsSections for Lesson must have unique positions")


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

    def get_lesson_sections(self):
        return self._lesson_section_list_value_holder.get_list()

    def sync_lesson_section_positions(self, lesson_sections_data_array):
        lesson_sections = self._lesson_section_list_value_holder.get_list()
        for data_item in lesson_sections_data_array:
            lesson_section = next(x for x in lesson_sections if x.get_id() == data_item['id'])
            if lesson_section is not None:
                lesson_section.set_position(data_item['position'])

        self._unit_of_work.register_dirty(self)
        self._check_invariants()

    def delete(self):
        self._unit_of_work.register_deleted(self)







    def __repr__(self):
        return "<Lesson(name='%s') ID(id='%s')>" % (self._name, self._id)






