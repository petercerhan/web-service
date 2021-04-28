

def text_tutorial_step_to_data(text_tutorial_step):
	return {'id': text_tutorial_step.get_id(), 
			'position': text_tutorial_step.get_position(), 
			'display_group': text_tutorial_step.get_display_group(),
			'text': text_tutorial_step.get_text(), 
			'type': text_tutorial_step.get_type()}