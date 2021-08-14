from mathapp.curriculum.interactor.domain_to_data_transforms.course import course_to_data
from mathapp.student.interactor.domain_to_data_transforms.student_topic import student_topic_to_data

def student_course_to_enriched_data(student_course):
	course_data = course_to_data(student_course.get_course())
	student_topics_data = [student_topic_to_data(x) for x in student_course.get_student_topics()]
	return {'id': student_course.get_id(), 
			'configured_course_push_number': student_course.get_configured_course_push_number(),
			'course': course_data,
			'student_topics': student_topics_data}

