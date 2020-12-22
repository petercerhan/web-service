from mathapp.curriculum.interactor.domain_to_data_transforms.instruction_section import instruction_section_to_data

def concept_tutorial_to_data(concept_tutorial):
	return {'id': concept_tutorial.get_id(), 
			'position': concept_tutorial.get_position(), 
			'display_name': concept_tutorial.get_display_name(),
			'type': concept_tutorial.get_type()}

def concept_tutorial_to_enriched_data(concept_tutorial):
	instruction_sections = [instruction_section_to_data(instruction_section) for instruction_section in concept_tutorial.get_instruction_sections()]
	return {'id': concept_tutorial.get_id(), 
			'position': concept_tutorial.get_position(), 
			'display_name': concept_tutorial.get_display_name(),
			'instruction_sections': instruction_sections,
			'type': concept_tutorial.get_type()}