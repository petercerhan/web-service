from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer
from mathapp.curriculum.main.curriculum_factory_composer import CurriculumFactoryComposer

from mathapp.curriculum.interactor.topic_interactor import TopicInteractor
from mathapp.curriculum.interactor.lesson_interactor import LessonInteractor
from mathapp.curriculum.interactor.tutorial_interactor import TutorialInteractor

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
      lesson_factory = self._curriculum_factory_composer.compose_lesson_factory()
      return TopicInteractor(topic_repository=topic_repository,
                                topic_factory=topic_factory,
                                lesson_factory=lesson_factory,
                                unit_of_work=self._unit_of_work)
        
    def compose_lesson_interactor(self):
      lesson_repository = self._curriculum_repository_composer.compose_lesson_repository()
      return LessonInteractor(lesson_repository=lesson_repository,
                              unit_of_work=self._unit_of_work)

    def compose_tutorial_interactor(self):
      tutorial_factory = self._curriculum_factory_composer.compose_tutorial_factory()
      tutorial_repository = self._curriculum_repository_composer.compose_tutorial_repository()
      lesson_repository = self._curriculum_repository_composer.compose_lesson_repository()
      return TutorialInteractor(tutorial_factory=tutorial_factory,
                                tutorial_repository=tutorial_repository,
                                lesson_repository=lesson_repository,
                                unit_of_work=self._unit_of_work)      
