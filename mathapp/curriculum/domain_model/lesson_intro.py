from mathapp.curriculum.domain_model.lesson_section import LessonSection
from mathapp.library.errors.validation_error import ValidationError

class LessonIntro(LessonSection):

    def __init__(self, 
                 position, 
                 complete_lesson, 
                 description, 
                 instruction_section_list_value_holder,
                 unit_of_work):
        self._description = description
        self._instruction_section_list_value_holder = instruction_section_list_value_holder
        self._unit_of_work = unit_of_work

        super().__init__(position, complete_lesson, unit_of_work)

        self._check_invariants()

    def _check_invariants(self):
        if not self._description:
            raise ValidationError(message = "LessonIntro requires description")

        if self._instruction_section_list_value_holder.get_queried():
            self._check_instruction_sections_valid_order()

        super()._check_invariants()

    def _check_instruction_sections_valid_order(self):
        instruction_sections = self._instruction_section_list_value_holder.get_list()
        positions = [x.get_position() for x in instruction_sections]
        if len(positions) > len(set(positions)):
            raise ValidationError(message = "InstructionSections for LessonIntro must have unique positions")


    def get_type(self):
        return 'lesson_intro'

    def get_description(self):
        return self._description

    def get_instruction_sections(self):
        return self._instruction_section_list_value_holder.get_list()

    def sync_instruction_section_positions(self, instruction_section_data_array):
        instruction_sections = self._instruction_section_list_value_holder.get_list()
        for data_item in instruction_section_data_array:
            instruction_section = next(x for x in instruction_sections if x.get_id() == data_item['id'])
            if instruction_section is not None:
                instruction_section.set_position(data_item['position'])

        self._check_invariants()
        self._unit_of_work.register_dirty(self)


    def __repr__(self):
        return f'<LessonIntro(id={self._id}, description={self._description})>'




