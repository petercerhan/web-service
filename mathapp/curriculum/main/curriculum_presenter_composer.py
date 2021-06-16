from mathapp.curriculum.presenter.course_presenter import CoursePresenter
from mathapp.curriculum.presenter.topic_presenter import TopicPresenter
from mathapp.curriculum.presenter.lesson_presenter import LessonPresenter
from mathapp.curriculum.presenter.tutorial_presenter import TutorialPresenter
from mathapp.curriculum.presenter.tutorial_step_presenter import TutorialStepPresenter
from mathapp.curriculum.presenter.exercise_presenter import ExercisePresenter
from mathapp.curriculum.presenter.problem_set_generator_presenter import ProblemSetGeneratorPresenter

class CurriculumPresenterComposer:

    def __init__(self, infrastructure_service_composer):
        self._infrastructure_service_composer = infrastructure_service_composer

    def compose_course_presenter(self):
        return CoursePresenter()

    def compose_topic_presenter(self):
        return TopicPresenter()

    def compose_lesson_presenter(self):
        return LessonPresenter()

    def compose_tutorial_presenter(self):
        return TutorialPresenter()

    def compose_tutorial_step_presenter(self):
        file_service = self._infrastructure_service_composer.compose_file_service()
        return TutorialStepPresenter(file_service=file_service)

    def compose_exercise_presenter(self):
        file_service = self._infrastructure_service_composer.compose_file_service()
        return ExercisePresenter(file_service=file_service)

    def compose_problem_set_generator_presenter(self):
        return ProblemSetGeneratorPresenter()