from mathapp.curriculum.interactor.domain_to_data_transforms.list_problem_set_dto_template import list_problem_set_dto_template_to_data

def problem_set_dto_template_to_data(problem_set_dto_template):
    type = problem_set_dto_template.type
    if type == 'list_problem_set':
        return list_problem_set_dto_template_to_data(problem_set_dto_template)