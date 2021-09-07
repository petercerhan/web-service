from mathapp.student.interactor.domain_to_data_transforms.student_course import student_course_to_data

def role_to_data(role):
	type = role.get_type()
	if type == 'student':
		latest_student_course_data = None
		latest_student_course = role.get_latest_student_course()
		if latest_student_course is not None:
			latest_student_course_data = student_course_to_data(latest_student_course)
		return {'id': role.get_id(),
				'latest_student_course': latest_student_course_data,
				'type': role.get_type()}

	return {'id': role.get_id(), 
			'type': role.get_type()}