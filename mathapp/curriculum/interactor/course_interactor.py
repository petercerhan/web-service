from mathapp.curriculum.interactor.domain_to_data_transforms.course import course_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.course import course_to_enriched_data

class CourseInteractor:

    def __init__(self, 
                 course_repository, 
                 topic_repository,
                 course_factory, 
                 course_topic_factory,
                 unit_of_work_committer):
        self._course_repository = course_repository
        self._topic_repository = topic_repository
        self._course_factory = course_factory
        self._course_topic_factory = course_topic_factory
        self._unit_of_work_committer = unit_of_work_committer

    def list(self):
        courses = self._course_repository.list()
        courses_data = [course_to_data(course) for course in courses]
        return courses_data
        
    
    def read(self, id):
        course = self._course_repository.get(id=id)
        enriched_course = course_to_enriched_data(course)
        return enriched_course


    def create(self, fields):
        course = self._course_factory.create(fields)
        self._unit_of_work_committer.commit()
        enriched_course = course_to_enriched_data(course)
        return enriched_course


    def update(self, id, fields):
        course = self._course_repository.get(id=id)

        display_name = fields.get('display_name')
        if display_name is not None:
            course.set_display_name(display_name)

        course_topics = fields.get('course_topics')
        if course_topics is not None:
            course.sync_course_topic_positions(course_topics)

        self._unit_of_work_committer.commit()

        enriched_course = course_to_enriched_data(course)
        return course
    
    def delete(self, id):
        course = self._course_repository.get(id=id)
        course.delete()
        self._unit_of_work_committer.commit()
        
        enriched_course = course_to_enriched_data(course)
        return course



    def create_course_topic(self, course_id, topic_id):        
        course = self._course_repository.get(course_id)
        topic = self._topic_repository.get(topic_id)

        course.create_course_topic(topic=topic,
                                   course_topic_factory=self._course_topic_factory)
        self._unit_of_work_committer.commit()
        return course_to_enriched_data(course)

    def delete_course_topic(self, course_id, course_topic_id):      
        course = self._course_repository.get(course_id)
        course.delete_course_topic(course_topic_id)
        self._unit_of_work_committer.commit()
        return course_to_enriched_data(course)
        






