from mathapp.library.errors.validation_error import ValidationError

class Topic:

    def __init__(self,
                 name,
                 display_name,
                 lesson_list_value_holder,
                 course_topic_list_value_holder,
                 exercise_list_value_holder,
                 unit_of_work):

        self._id = None
        self._name = name
        self._display_name = display_name
        self._lesson_list_value_holder = lesson_list_value_holder
        self._course_topic_list_value_holder = course_topic_list_value_holder
        self._exercise_list_value_holder = exercise_list_value_holder
        self._unit_of_work = unit_of_work
        self._check_invariants()


    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message = "Topic requires name")

        if not self._name.strip():
            raise ValidationError(message = "Invalid name for Topic")

        if not self._display_name:
            raise ValidationError(message = "Topic requires display_name")

        if not self._display_name.strip():
            raise ValidationError(message = "Invalid display_name for Topic")


    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_display_name(self):
        return self._display_name

    def set_display_name(self, display_name):
        self._display_name = display_name
        self._check_invariants()
        self._unit_of_work.register_dirty(self)



    def get_lessons(self):
        return self._lesson_list_value_holder.get_list()

    def create_lesson(self, lesson_factory, fields):
        max_position = max([x.get_position() for x in self._lesson_list_value_holder.get_list()], default=-1)
        next_position = max_position+1
        lesson = lesson_factory.create(position=next_position, fields=fields, topic=self)
        self._lesson_list_value_holder.add(lesson)
        self._check_invariants()

    def sync_lesson_positions(self, lessons_data_array):
        lessons = self._lesson_list_value_holder.get_list()
        for data_item in lessons_data_array:
            lesson = next(x for x in lessons if x.get_id() == data_item['id'])
            if lesson is not None:
                lesson.set_position(data_item['position'])

    def delete_lesson(self, lesson_id):
        lessons = self._lesson_list_value_holder.get_list()
        deleted_position = None
        for lesson in lessons:
            if lesson.get_id() == lesson_id:
                deleted_position = lesson.get_position()
                lesson.delete()
                self._lesson_list_value_holder.removeAtIndex(deleted_position)

        if deleted_position is None:
            return

        for lesson in lessons:
            if lesson.get_position() > deleted_position:
                prior_position = lesson.get_position()
                lesson.set_position(prior_position-1)

        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_exercises(self):
        return self._exercise_list_value_holder.get_list()

    def create_exercise(self, exercise_factory, fields):
        exercise = exercise_factory.create(fields=fields, topic=self)
        return exercise


    def delete(self):
        course_topics = self._course_topic_list_value_holder.get_list()
        for course_topic in course_topics:
            course_topic.topic_deleted()

        lessons = self._lesson_list_value_holder.get_list()
        for lesson in lessons:
            lesson.delete()

        self._unit_of_work.register_deleted(self)


    def __repr__(self):
        return "<Topic(name='%s') ID(id='%s')>" % (self._name, self._id)












