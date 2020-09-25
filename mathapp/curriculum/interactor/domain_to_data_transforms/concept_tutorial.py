

def concept_tutorial_to_data(concept_tutorial):
	return {'id': concept_tutorial.get_id(), 
			'position': concept_tutorial.get_position(), 
			'display_name': concept_tutorial.get_display_name(),
			'type': concept_tutorial.get_type()}

