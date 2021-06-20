from mathapp.system.main.system_presenter_composer import SystemPresenterComposer
from mathapp.system.main.system_interactor_composer import SystemInteractorComposer

from mathapp.system.controller.auth_web_controller import AuthWebController
from mathapp.system.controller.file_web_controller import FileWebController
from mathapp.system.controller.auth_api_controller import AuthApiController

class SystemControllerComposer:

    def __init__(self,
                 request,
                 sqlalchemy_session,
                 infrastructure_service_composer,
                 unit_of_work):
        self._request = request
        self._sqlalchemy_session = sqlalchemy_session
        self._infrastructure_service_composer = infrastructure_service_composer
        self._unit_of_work = unit_of_work
        self._system_presenter_composer = SystemPresenterComposer(infrastructure_service_composer=infrastructure_service_composer)
        self._system_interactor_composer = SystemInteractorComposer(unit_of_work=unit_of_work,
                                                                    sqlalchemy_session=sqlalchemy_session,
                                                                    infrastructure_service_composer=infrastructure_service_composer)

    def compose_auth_web_controller(self):
        auth_presenter = self._system_presenter_composer.compose_auth_presenter()
        auth_interactor = self._system_interactor_composer.compose_auth_interactor()
        return AuthWebController(request=self._request,
                                 auth_presenter=auth_presenter,
                                 auth_interactor=auth_interactor)

    def compose_file_web_controller(self):
        file_presenter = self._system_presenter_composer.compose_file_presenter()
        return FileWebController(request=self._request,
                                 file_presenter=file_presenter)

    def compose_auth_api_controller(self):
        auth_interactor = self._system_interactor_composer.compose_auth_interactor()
        auth_api_presenter = self._system_presenter_composer.compose_auth_api_presenter()
        return AuthApiController(request=self._request,
                                 auth_interactor=auth_interactor,
                                 auth_api_presenteer=auth_api_presenter)




        