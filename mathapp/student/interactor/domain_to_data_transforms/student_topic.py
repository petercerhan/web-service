from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_data

def student_topic_to_data(student_topic):
    topic_data = topic_to_data(student_topic.get_topic())
    return {'id': student_topic.get_id(), 
            'lessons_completed': student_topic.get_lessons_completed(),
            'total_lessons': student_topic.get_total_lessons(),
            'completed': student_topic.get_completed(),
            'topic': topic_data}