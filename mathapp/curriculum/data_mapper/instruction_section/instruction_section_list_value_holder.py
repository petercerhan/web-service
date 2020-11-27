

class InstructionSectionListValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get_list(self):
		orm_instruction_sections = self._orm_model.instruction_sections
		if not self._queried:
			self._unit_of_work.register_queried(orm_instruction_sections)
		instruction_sections = [x.get_model(unit_of_work=self._unit_of_work) for x in orm_instruction_sections]
		self._queried = True
		return instruction_sections

	def add(self, instruction_section):
		orm_instruction_section = self._unit_of_work.orm_model_for_model(instruction_section)
		self._orm_model.instruction_sections.append(orm_instruction_section)

	def remove_at_index(self, index):
		orm_instruction_section = self._orm_model.instruction_sections.pop(index)

	def get_queried(self):
		return self._queried