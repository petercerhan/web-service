from mathapp.curriculum.presenter.topic_presenter import TopicPresenter
from mathapp.curriculum.presenter.lesson_presenter import LessonPresenter

class CurriculumPresenterComposer:

    def compose_topic_presenter(self):
        return TopicPresenter()

    def compose_lesson_presenter(self):
    	return LessonPresenter()