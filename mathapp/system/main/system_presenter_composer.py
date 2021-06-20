from mathapp.system.presenter.auth_presenter import AuthPresenter
from mathapp.system.presenter.file_presenter import FilePresenter
from mathapp.system.presenter.auth_api_presenter import AuthApiPresenter

class SystemPresenterComposer:

    def __init__(self,
                 infrastructure_service_composer):
        self._infrastructure_service_composer = infrastructure_service_composer


    def compose_auth_presenter(self):
        return AuthPresenter()

    def composer_file_presenter(self):
        file_service = self._infrastructure_service_composer.compose_file_service()
        return FilePresenter(file_service=file_service)

    def compose_auth_api_presenter(self):
        return AuthApiPresenter()

        