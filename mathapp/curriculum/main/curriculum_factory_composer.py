from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer

from mathapp.curriculum.data_mapper.course.course_factory import CourseFactory
from mathapp.curriculum.domain_model.course_factory_validating_decorator import CourseFactoryValidatingDecorator
from mathapp.curriculum.data_mapper.course_topic.course_topic_factory import CourseTopicFactory

from mathapp.curriculum.data_mapper.topic.topic_factory import TopicFactory
from mathapp.curriculum.domain_model.topic_factory_validating_decorator import TopicFactoryValidatingDecorator
from mathapp.curriculum.data_mapper.lesson.lesson_factory import LessonFactory
from mathapp.curriculum.data_mapper.tutorial.tutorial_factory import TutorialFactory

from mathapp.curriculum.data_mapper.text_tutorial_step.text_tutorial_step_factory import TextTutorialStepFactory
from mathapp.curriculum.data_mapper.formula_tutorial_step.formula_tutorial_step_factory import FormulaTutorialStepFactory
from mathapp.curriculum.data_mapper.image_tutorial_step.image_tutorial_step_factory import ImageTutorialStepFactory

from mathapp.curriculum.data_mapper.formula_exercise.formula_exercise_factory import FormulaExerciseFactory
from mathapp.curriculum.data_mapper.diagram_exercise.diagram_exercise_factory import DiagramExerciseFactory

from mathapp.curriculum.data_mapper.list_problem_set_generator.list_problem_set_generator_factory import ListProblemSetGeneratorFactory

class CurriculumFactoryComposer:

    def __init__(self, 
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._curriculum_repository_composer = CurriculumRepositoryComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session)

    def compose_course_factory(self):
        course_factory = CourseFactory(unit_of_work=self._unit_of_work)
        course_repository = self._curriculum_repository_composer.compose_course_repository()
        validating_decorator = CourseFactoryValidatingDecorator(course_factory=course_factory,
                                                                course_repository=course_repository)
        return validating_decorator

    def compose_course_topic_factory(self):
        return CourseTopicFactory(unit_of_work=self._unit_of_work)

    def compose_topic_factory(self):
        topic_factory = TopicFactory(unit_of_work=self._unit_of_work)
        topic_repository = self._curriculum_repository_composer.compose_topic_repository()
        validating_decorator = TopicFactoryValidatingDecorator(topic_factory=topic_factory,
                                                                topic_repository=topic_repository)
        return validating_decorator

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

    def compose_formula_exercise_factory(self):
        return FormulaExerciseFactory(unit_of_work=self._unit_of_work)

    def compose_diagram_exercise_factory(self):
        return DiagramExerciseFactory(unit_of_work=self._unit_of_work)

    def compose_list_problem_set_generator_factory(self):
        return ListProblemSetGeneratorFactory(unit_of_work=self._unit_of_work)










