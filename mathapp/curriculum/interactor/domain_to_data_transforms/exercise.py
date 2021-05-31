from mathapp.curriculum.interactor.domain_to_data_transforms.formula_exercise import formula_exercise_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.diagram_exercise import diagram_exercise_to_data

def exercise_to_data(exercise):
	type = exercise.get_type()
	if type == 'formula_exercise':
		return formula_exercise_to_data(exercise)
	if type == 'diagram_exercise':
		return diagram_exercise_to_data(exercise)