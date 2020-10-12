from mathapp.curriculum.interactor.domain_to_data_transforms.detail_section import detail_section_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.derivation_instruction_section import derivation_instruction_section_to_data

def instruction_section_to_data(instruction_section):
	type = instruction_section.get_type()
	if type == 'detail_section':
		return detail_section_to_data(instruction_section)
	elif type == 'derivation_instruction_section':
		return derivation_instruction_section_to_data(instruction_section)


