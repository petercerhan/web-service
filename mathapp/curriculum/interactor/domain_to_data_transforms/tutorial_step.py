from mathapp.curriculum.interactor.domain_to_data_transforms.text_tutorial_step import text_tutorial_step_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.formula_tutorial_step import formula_tutorial_step_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.image_tutorial_step import image_tutorial_step_to_data

import sys

def tutorial_step_to_data(tutorial_step):	
	type = tutorial_step.get_type()
	if type == 'text_tutorial_step':
		return text_tutorial_step_to_data(tutorial_step)
	if type == 'formula_tutorial_step':
		return formula_tutorial_step_to_data(tutorial_step)
	if type == 'image_tutorial_step':
		return image_tutorial_step_to_data(tutorial_step)