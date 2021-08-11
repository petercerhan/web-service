

def course_push_control_to_data(course_push_control):
	return {'current_course_push_number': course_push_control.get_current_course_push_number(), 
			'course_id': course_push_control.get_course_id()}

