from mathapp.curriculum.main.curriculum_presenter_composer import CurriculumPresenterComposer
from mathapp.curriculum.main.curriculum_interactor_composer import CurriculumInteractorComposer

from mathapp.curriculum.controller.topic_web_controller import TopicWebController
from mathapp.curriculum.controller.lesson_web_controller import LessonWebController
from mathapp.curriculum.controller.tutorial_web_controller import TutorialWebController
from mathapp.curriculum.controller.tutorial_step_web_controller import TutorialStepWebController
from mathapp.curriculum.controller.exercise_web_controller import ExerciseWebController


class CurriculumControllerComposer:

    def __init__(self,
                 request,
                 sqlalchemy_session,
                 infrastructure_service_composer,
                 unit_of_work):
        self._request = request
        self._sqlalchemy_session = sqlalchemy_session
        self._infrastructure_service_composer = infrastructure_service_composer
        self._unit_of_work = unit_of_work
        self._curriculum_presenter_composer = CurriculumPresenterComposer(infrastructure_service_composer=infrastructure_service_composer)
        self._curriculum_interactor_composer = CurriculumInteractorComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session,
                                                                            infrastructure_service_composer=infrastructure_service_composer)


    def compose_topic_web_controller(self):
        topic_interactor = self._curriculum_interactor_composer.compose_topic_interactor()
        topic_presenter = self._curriculum_presenter_composer.compose_topic_presenter()
        return TopicWebController(request=self._request,
                                  topic_interactor=topic_interactor,
                                  topic_presenter=topic_presenter)

    def compose_lesson_web_controller(self):
        lesson_interactor = self._curriculum_interactor_composer.compose_lesson_interactor()
        lesson_presenter = self._curriculum_presenter_composer.compose_lesson_presenter()
        return LessonWebController(request=self._request,
                                    lesson_interactor=lesson_interactor,
                                    lesson_presenter=lesson_presenter)

    def compose_tutorial_web_controller(self):
        tutorial_presenter = self._curriculum_presenter_composer.compose_tutorial_presenter()
        tutorial_interactor = self._curriculum_interactor_composer.compose_tutorial_interactor()
        return TutorialWebController(request=self._request,
                                     tutorial_presenter=tutorial_presenter,
                                     tutorial_interactor=tutorial_interactor)
    
    def compose_tutorial_step_web_controller(self):
        tutorial_step_presenter = self._curriculum_presenter_composer.compose_tutorial_step_presenter()
        tutorial_step_interactor = self._curriculum_interactor_composer.compose_tutorial_step_interactor()
        return TutorialStepWebController(request=self._request,
                                         tutorial_step_presenter=tutorial_step_presenter,
                                         tutorial_step_interactor=tutorial_step_interactor)

    def compose_exercise_web_controller(self):
        exercise_presenter = self._curriculum_presenter_composer.compose_exercise_presenter()
        topic_interactor = self._curriculum_interactor_composer.compose_topic_interactor()
        return ExerciseWebController(request=self._request,
                                     exercise_presenter=exercise_presenter,
                                     topic_interactor=topic_interactor)














