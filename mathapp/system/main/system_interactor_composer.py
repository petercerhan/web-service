from mathapp.system.main.system_repository_composer import SystemRepositoryComposer
from mathapp.system.main.system_factory_composer import SystemFactoryComposer

from mathapp.system.interactor.auth_interactor import AuthInteractor

class SystemInteractorComposer:

    def __init__(self,
                 unit_of_work,
                 sqlalchemy_session,
                 infrastructure_service_composer):
        self._unit_of_work = unit_of_work
        self._infrastructure_service_composer = infrastructure_service_composer
        self._system_repository_composer = SystemRepositoryComposer(unit_of_work=unit_of_work,
                                                                  sqlalchemy_session=sqlalchemy_session)
        self._system_factory_composer = SystemFactoryComposer(unit_of_work=unit_of_work,
                                                            sqlalchemy_session=sqlalchemy_session)

    def compose_auth_interactor(self):
        user_repository = self._system_repository_composer.compose_user_repository()
        user_factory = self._system_factory_composer.compose_user_factory()
        session_repository = self._system_repository_composer.compose_session_repository()
        session_factory = self._system_factory_composer.compose_session_factory()
        encryption_service = self._infrastructure_service_composer.compose_encryption_service()
        date_service = self._infrastructure_service_composer.compose_date_service()
        token_service = self._infrastructure_service_composer.compose_token_service()
        return AuthInteractor(user_repository=user_repository,
                              user_factory=user_factory,
                              session_repository=session_repository,
                              session_factory=session_factory,
                              encryption_service=encryption_service,
                              date_service=date_service,
                              token_service=token_service,
                              unit_of_work_committer=self._unit_of_work)