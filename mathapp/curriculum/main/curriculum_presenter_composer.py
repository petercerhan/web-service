from mathapp.curriculum.presenter.topic_presenter import TopicPresenter
from mathapp.curriculum.presenter.lesson_presenter import LessonPresenter
from mathapp.curriculum.presenter.tutorial_presenter import TutorialPresenter
from mathapp.curriculum.presenter.tutorial_step_presenter import TutorialStepPresenter

class CurriculumPresenterComposer:

    def compose_topic_presenter(self):
        return TopicPresenter()

    def compose_lesson_presenter(self):
        return LessonPresenter()

    def compose_tutorial_presenter(self):
        return TutorialPresenter()

    def compose_tutorial_step_presenter(self):
        return TutorialStepPresenter()

