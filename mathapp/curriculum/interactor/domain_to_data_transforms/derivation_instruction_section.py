

def derivation_instruction_section_to_data(derivation_instruction_section):
	return {'id': derivation_instruction_section.get_id(), 
			'position': derivation_instruction_section.get_position(), 
			'display_name': derivation_instruction_section.get_display_name(), 
			'type': derivation_instruction_section.get_type()}