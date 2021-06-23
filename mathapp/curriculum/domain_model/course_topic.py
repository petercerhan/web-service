from mathapp.library.errors.validation_error import ValidationError

class CourseTopic:

    def __init__(self,
                 position,
                 course_value_holder,
                 topic_value_holder,
                 unit_of_work):
        self._id = None
        self._position = position
        self._course_value_holder = course_value_holder
        self._topic_value_holder = topic_value_holder
        self._unit_of_work = unit_of_work

        self._check_invariants()

    def _check_invariants(self):
        if self._position is None:
            raise ValidationError(message = "CourseTopic requires position")

        if not self._topic_value_holder.get_set_at_init():
            raise ValidationError(message="CourseTopic required topic")

        if not self._course_value_holder.get_set_at_init():
            raise ValidationError(message="CourseTopic required course")
            

    def get_id(self):
        return self._id

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_topic(self):
        return self._topic_value_holder.get()


    def delete(self):
        self._unit_of_work.register_deleted(self)

    def topic_deleted(self):
        course = self._course_value_holder.get()
        course.delete_course_topic(self.get_id())

    def __repr__(self):
        return "<CourseTopic(position='%s') topic_id(name='%s')>" % (self._position, self._topic_value_holder.get().get_id())


