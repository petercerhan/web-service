from mathapp.curriculum.main.curriculum_presenter_composer import CurriculumPresenterComposer
from mathapp.curriculum.main.curriculum_interactor_composer import CurriculumInteractorComposer

from mathapp.curriculum.controller.topic_web_controller import TopicWebController


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
        self._curriculum_presenter_composer = CurriculumPresenterComposer()
        self._curriculum_interactor_composer = CurriculumInteractorComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session)


    def compose_topic_web_controller(self):
        topic_interactor = self._curriculum_interactor_composer.compose_topic_interactor()
        topic_presenter = self._curriculum_presenter_composer.compose_topic_presenter()
        return TopicWebController(request=self._request,
                                  topic_interactor=topic_interactor,
                                  topic_presenter=topic_presenter)
