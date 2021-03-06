from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer
from mathapp.curriculum.main.curriculum_factory_composer import CurriculumFactoryComposer

from mathapp.curriculum.interactor.course_interactor import CourseInteractor
from mathapp.curriculum.interactor.topic_interactor import TopicInteractor
from mathapp.curriculum.interactor.lesson_interactor import LessonInteractor
from mathapp.curriculum.interactor.tutorial_interactor import TutorialInteractor
from mathapp.curriculum.interactor.tutorial_step_interactor import TutorialStepInteractor
from mathapp.curriculum.interactor.exercise_interactor import ExerciseInteractor
from mathapp.curriculum.interactor.problem_set_generator_interactor import ProblemSetGeneratorInteractor

class CurriculumInteractorComposer:

    def __init__(self,
                 unit_of_work,
                 sqlalchemy_session,
                 infrastructure_service_composer):
      self._unit_of_work = unit_of_work
      self._infrastructure_service_composer = infrastructure_service_composer
      self._curriculum_repository_composer = CurriculumRepositoryComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session)
      self._curriculum_factory_composer = CurriculumFactoryComposer(unit_of_work=unit_of_work,
                                                                      sqlalchemy_session=sqlalchemy_session)

    def compose_course_interactor(self):
      course_repository = self._curriculum_repository_composer.compose_course_repository()
      topic_repository = self._curriculum_repository_composer.compose_topic_repository()
      course_factory = self._curriculum_factory_composer.compose_course_factory()
      course_topic_factory = self._curriculum_factory_composer.compose_course_topic_factory()
      return CourseInteractor(course_repository=course_repository,
                              topic_repository=topic_repository,
                              course_factory=course_factory,
                              course_topic_factory=course_topic_factory,
                              unit_of_work_committer=self._unit_of_work)

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

    def compose_tutorial_step_interactor(self):
      tutorial_repository = self._curriculum_repository_composer.compose_tutorial_repository()
      text_tutorial_step_factory = self._curriculum_factory_composer.compose_text_tutorial_step_factory()
      formula_tutorial_step_factory = self._curriculum_factory_composer.compose_formula_tutorial_step_factory()
      image_tutorial_step_factory = self._curriculum_factory_composer.compose_image_tutorial_step_factory()
      file_service = self._infrastructure_service_composer.compose_file_service()
      date_service = self._infrastructure_service_composer.compose_date_service()
      return TutorialStepInteractor(tutorial_repository=tutorial_repository,
                                    text_tutorial_step_factory=text_tutorial_step_factory,
                                    formula_tutorial_step_factory=formula_tutorial_step_factory,
                                    image_tutorial_step_factory=image_tutorial_step_factory,
                                    file_service=file_service,
                                    date_service=date_service,
                                    unit_of_work=self._unit_of_work)

    def compose_exercise_interactor(self):
      topic_repository = self._curriculum_repository_composer.compose_topic_repository()
      formula_exercise_factory = self._curriculum_factory_composer.compose_formula_exercise_factory()
      diagram_exercise_factory = self._curriculum_factory_composer.compose_diagram_exercise_factory()
      exercise_repository = self._curriculum_repository_composer.compose_exercise_repository()
      file_service = self._infrastructure_service_composer.compose_file_service()
      date_service = self._infrastructure_service_composer.compose_date_service()
      return ExerciseInteractor(topic_repository=topic_repository,
                                formula_exercise_factory=formula_exercise_factory,
                                diagram_exercise_factory=diagram_exercise_factory,
                                exercise_repository=exercise_repository,
                                file_service=file_service,
                                date_service=date_service,
                                unit_of_work=self._unit_of_work)

    def compose_problem_set_generator_interactor(self):
      list_problem_set_generator_factory = self._curriculum_factory_composer.compose_list_problem_set_generator_factory()
      lesson_repository = self._curriculum_repository_composer.compose_lesson_repository()
      problem_set_generator_repository = self._curriculum_repository_composer.compose_problem_set_generator_repository()
      exercise_repository = self._curriculum_repository_composer.compose_exercise_repository()
      return ProblemSetGeneratorInteractor(list_problem_set_generator_factory=list_problem_set_generator_factory,
                                           lesson_repository=lesson_repository,
                                           problem_set_generator_repository=problem_set_generator_repository,
                                           exercise_repository=exercise_repository,
                                           unit_of_work=self._unit_of_work)









