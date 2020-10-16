from mathapp.curriculum.domain_model.node_content import NodeContent

class InstructionSectionParentValueHolder:

	def __init__(self, orm_instruction_section, unit_of_work):
		self._orm_instruction_section = orm_instruction_section
		self._unit_of_work = unit_of_work

	def get(self):
		orm_lesson_intro = self._orm_instruction_section.lesson_intro
		if orm_lesson_intro is not None:
			return NodeContent(model=orm_lesson_intro.get_model(unit_of_work=self._unit_of_work), model_name='lesson_intro')