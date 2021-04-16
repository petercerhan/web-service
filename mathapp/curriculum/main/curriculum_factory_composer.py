from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer

from mathapp.curriculum.data_mapper.topic.topic_factory import TopicFactory
from mathapp.curriculum.domain_model.topic_factory_validating_decorator import TopicFactoryValidatingDecorator

class CurriculumFactoryComposer:

    def __init__(self, 
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._curriculum_repository_composer = CurriculumRepositoryComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session)

    def compose_topic_factory(self):
        topic_factory = TopicFactory(unit_of_work=self._unit_of_work)
        topic_repository = self._curriculum_repository_composer.compose_topic_repository()
        return TopicFactoryValidatingDecorator(topic_factory=topic_factory,
                                               topic_repository=topic_repository)