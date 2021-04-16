from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer
from mathapp.curriculum.main.curriculum_factory_composer import CurriculumFactoryComposer

from mathapp.curriculum.interactor.topic_interactor import TopicInteractor

class CurriculumInteractorComposer:

    def __init__(self,
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._curriculum_repository_composer = CurriculumRepositoryComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session)
        self._curriculum_factory_composer = CurriculumFactoryComposer(unit_of_work=unit_of_work,
                                                                      sqlalchemy_session=sqlalchemy_session)

    def compose_topic_interactor(self):
        topic_repository = self._curriculum_repository_composer.compose_topic_repository()
        topic_factory = self._curriculum_factory_composer.compose_topic_factory()
        return TopicInteractor(topic_repository=topic_repository,
                                topic_factory=topic_factory,
                                unit_of_work=self._unit_of_work)
        