from mathapp.curriculum.interactor.topic_interactor import TopicInteractor

from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer

class CurriculumInteractorComposer:

    def __init__(self,
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._curriculum_repository_composer = CurriculumRepositoryComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session)

    def compose_topic_interactor(self):
        topic_repository = self._curriculum_repository_composer.compose_topic_repository()
        return TopicInteractor(topic_repository=topic_repository,
                                unit_of_work=self._unit_of_work)
        