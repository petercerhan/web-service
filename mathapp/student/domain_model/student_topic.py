from mathapp.libraries.general_library.errors.validation_error import ValidationError

class StudentTopic:

    def __init__(self,
                 lessons_completed,
                 total_lessons,
                 completed,
                 topic_value_holder,
                 unit_of_work):
        self._id = None
        self._lessons_completed = lessons_completed
        self._total_lessons = total_lessons
        self._completed = completed
        self._topic_value_holder = topic_value_holder
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._lessons_completed is None:
            raise ValidationError(message='StudentTopic requires lessons_completed')

        if self._total_lessons is None:
            raise ValidationError(message='StudentTopic requires total_lessons')

        if self._completed is None:
            raise ValidationError(message='StudentTopic requires completed')

        if not self._topic_value_holder.get_set_at_init():
            raise ValidationError(message='StudentTopic requires topic')


    def get_id(self):
        return self._id

    def get_lessons_completed(self):
        return self._lessons_completed

    def get_total_lessons(self):
        return self._total_lessons

    def get_completed(self):
        return self._completed

    def get_topic(self):
        return self._topic_value_holder.get()

    def __repr__(self):
        return f'<StudentTopic(id={self._id})>'
