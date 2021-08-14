from mathapp.student.data_mapper.student_topic.orm_student_topic import ORMStudentTopic

class StudentTopicFactory:

    def __init__(self, unit_of_work):
        self._unit_of_work = unit_of_work

    def create(self, fields, student, topic):
        lessons_completed = fields.get('lessons_completed')
        total_lessons = fields.get('total_lessons')
        completed = fields.get('completed')
        orm_student_topic = ORMStudentTopic(student_id=student.get_id(),
                                            topic_id=topic.get_id(),
                                            lessons_completed=lessons_completed,
                                            total_lessons=total_lessons,
                                            completed=completed)
        student_topic = orm_student_topic.get_model(unit_of_work=self._unit_of_work)
        self._unit_of_work.register_created(orm_student_topic)
        return student_topic
        



