from mathapp.curriculum.domain_model.lesson_section import LessonSection

from mathapp.library.errors.validation_error import ValidationError

class ConceptTutorial(LessonSection):

    def __init__(self, 
                 position, 
                 complete_lesson, 
                 display_name, 
                 instruction_section_list_value_holder, 
                 parent_value_holder, 
                 unit_of_work):
        self._display_name = display_name
        self._instruction_section_list_value_holder = instruction_section_list_value_holder
        self._unit_of_work = unit_of_work

        super().__init__(position, complete_lesson, parent_value_holder, unit_of_work)

        self._check_invariants()

    def _check_invariants(self):
        super()._check_invariants()
        if self._display_name is None:
            raise ValidationError(message = "Concept Tutorial requires display_name")

        if not self._display_name.strip():
            raise ValidationError(message = "Invalid display_name for Concept Tutorial")

        if self._instruction_section_list_value_holder.get_queried():
            self._check_instruction_sections_valid_order()

        super()._check_invariants()

    def _check_instruction_sections_valid_order(self):
        instruction_sections = self._instruction_section_list_value_holder.get_list()
        positions = [x.get_position() for x in instruction_sections]
        if len(positions) > len(set(positions)):
            raise ValidationError(message = "InstructionSections for ConceptTutorial must have unique positions")

    def get_type(self):
        return 'concept_tutorial'

    def get_display_name(self):
        return self._display_name

    def set_display_name(self, display_name):
        self._display_name = display_name
        self._check_invariants
        self._unit_of_work.register_dirty(self)

    def get_instruction_sections(self):
        return self._instruction_section_list_value_holder.get_list()

    def create_instruction_section(self, fields, instruction_section_factory):
        max_position = max([x.get_position() for x in self._instruction_section_list_value_holder.get_list()], default=-1)
        instruction_section = instruction_section_factory.create(fields=fields, position=max_position+1)
        self._instruction_section_list_value_holder.add(instruction_section)
        self._check_invariants()
        self._unit_of_work.register_dirty(self)
        return instruction_section


    def __repr__(self):
        return f'<ConceptTutorial(id={self._id}, display_name={self._display_name})'







