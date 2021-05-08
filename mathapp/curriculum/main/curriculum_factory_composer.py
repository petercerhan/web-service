from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer

from mathapp.curriculum.data_mapper.topic.topic_factory import TopicFactory
from mathapp.curriculum.domain_model.topic_factory_validating_decorator import TopicFactoryValidatingDecorator
from mathapp.curriculum.data_mapper.lesson.lesson_factory import LessonFactory
from mathapp.curriculum.data_mapper.tutorial.tutorial_factory import TutorialFactory
from mathapp.curriculum.data_mapper.text_tutorial_step.text_tutorial_step_factory import TextTutorialStepFactory
from mathapp.curriculum.data_mapper.formula_tutorial_step.formula_tutorial_step_factory import FormulaTutorialStepFactory
from mathapp.curriculum.data_mapper.image_tutorial_step.image_tutorial_step_factory import ImageTutorialStepFactory

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

    def compose_lesson_factory(self):
        return LessonFactory(unit_of_work=self._unit_of_work)

    def compose_tutorial_factory(self):
        return TutorialFactory(unit_of_work=self._unit_of_work)

    def compose_text_tutorial_step_factory(self):
        return TextTutorialStepFactory(unit_of_work=self._unit_of_work)

    def compose_formula_tutorial_step_factory(self):
        return FormulaTutorialStepFactory(unit_of_work=self._unit_of_work)

    def compose_image_tutorial_step_factory(self):
        return ImageTutorialStepFactory(unit_of_work=self._unit_of_work)

