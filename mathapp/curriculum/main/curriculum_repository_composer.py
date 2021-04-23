from mathapp.curriculum.data_mapper.topic.topic_repository import TopicRepository
from mathapp.curriculum.data_mapper.lesson.lesson_repository import LessonRepository

class CurriculumRepositoryComposer:

    def __init__(self,
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._sqlalchemy_session = sqlalchemy_session

    def compose_topic_repository(self):
        return TopicRepository(unit_of_work=self._unit_of_work,
                               session=self._sqlalchemy_session)

    def compose_lesson_repository(self):
    	return LessonRepository(unit_of_work=self._unit_of_work,
    							session=self._sqlalchemy_session)