from mathapp.libraries.general_library.errors.validation_error import ValidationError

class StudentCourse:

    def __init__(self,
                 configured_course_push_number,
                 course_value_holder,
                 course_push_control_value_holder,
                 student_topic_list_value_holder,
                 unit_of_work):
        self._id = None
        self._configured_course_push_number = configured_course_push_number
        self._course_value_holder = course_value_holder
        self._course_push_control_value_holder = course_push_control_value_holder
        self._student_topic_list_value_holder = student_topic_list_value_holder
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._configured_course_push_number is None:
            raise ValidationError(message='StudentCourse requires configured_course_push_number')

        if not self._course_value_holder.get_set_at_init():
            raise ValidationError(message='StudentCourse requires course')

    def get_id(self):
        return self._id

    def get_configured_course_push_number(self):
        return self._configured_course_push_number

    def get_course(self):
        return self._course_value_holder.get()

    def get_course_push_control(self):
        return self._course_push_control_value_holder.get()

    def get_student_topics(self):
        return self._student_topic_list_value_holder.get_list()


    def sync_latest_course_push(self, student_topic_factory):
        student_topics = self._student_topic_list_value_holder.get_list()
        setup_topic_ids = [x.get_topic().get_id() for x in student_topics]

        course_topics = self._course_value_holder.get().get_course_topics()
        topics = [x.get_topic() for x in course_topics]

        topics_need_setup = list(filter(lambda x: x.get_id() not in setup_topic_ids, topics))

        for topic in topics_need_setup:
            fields = {}
            fields['lessons_completed'] = 0
            fields['total_lessons'] = len(topic.get_lessons())
            fields['completed'] = 0
            student_topic_factory.create(fields=fields,
                                         student=self,
                                         topic=topic)

        self._configured_course_push_number = self._course_push_control_value_holder.get().get_current_course_push_number()
        self._unit_of_work.register_dirty(self)


    def __repr__(self):
        return f'<StudentCourse(id={self._id})>'

        