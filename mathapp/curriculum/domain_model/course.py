from mathapp.libraries.general_library.errors.validation_error import ValidationError

class Course:
    
    def __init__(self, 
        name, 
        display_name,
        course_topic_list_value_holder,
        unit_of_work):

        self._id = None

        self._name = name
        self._display_name = display_name

        self._course_topic_list_value_holder = course_topic_list_value_holder
        self._unit_of_work = unit_of_work

        self._check_invariants()


    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message = "Course requires name")

        if not self._name.strip():
            raise ValidationError(message = "Invalid name for Course")

        if not self._display_name:
            raise ValidationError(message = "Course requires displa_name")

        if not self._display_name.strip():
            raise ValidationError(message = "Invalid display_name for Course")

        if (self._course_topic_list_value_holder.get_queried()):
            self._check_course_topics_valid_order()


    def _check_course_topics_valid_order(self):
        course_topics = self._course_topic_list_value_holder.get_list()
        positions = [x.get_position() for x in course_topics]
        if len(positions) > len(set(positions)):
            raise ValidationError(message = "CourseTopics for Course must have unique positions")

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
        
    def delete(self):
        course_topics = self._course_topic_list_value_holder.get_list()
        for course_topic in course_topics:
            course_topic.delete()
        self._unit_of_work.register_deleted(self)


    def get_course_topics(self):
        return self._course_topic_list_value_holder.get_list()

    def create_course_topic(self, topic, course_topic_factory):
        max_position = max([x.get_position() for x in self._course_topic_list_value_holder.get_list()], default=-1)
        next_position = max_position+1
        course_topic = course_topic_factory.create(position=next_position, topic=topic, course=self)

    def sync_course_topic_positions(self, course_topics_data_array):
        course_topics = self._course_topic_list_value_holder.get_list()
        for data_item in course_topics_data_array:
            course_topic = next(x for x in course_topics if x.get_id() == data_item['id'])
            if course_topic is not None:
                course_topic.set_position(data_item['position'])

    def delete_course_topic(self, course_topic_id):
        course_topics = self._course_topic_list_value_holder.get_list()
        deleted_position = None
        for course_topic in course_topics:
            if course_topic.get_id() == course_topic_id:
                deleted_position = course_topic.get_position()
                course_topic.delete()
                self._course_topic_list_value_holder.removeAtIndex(deleted_position)

        if deleted_position is None:
            return

        for course_topic in course_topics:
            if course_topic.get_position() > deleted_position:
                prior_position = course_topic.get_position()
                course_topic.set_position(prior_position-1)

        self._check_invariants()
        self._unit_of_work.register_dirty(self)



    def __repr__(self):
        return "<Course(name='%s') ID(id='%s')>" % (self._name, self._id)







