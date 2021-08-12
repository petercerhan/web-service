from mathapp.curriculum.interactor.domain_to_data_transforms.course import course_to_data

def student_course_to_data(student_course):
	course_data = course_to_data(student_course.get_course())
	return {'id': student_course.get_id(), 
			'configured_course_push_number': student_course.get_configured_course_push_number(),
			'course': course_data}

