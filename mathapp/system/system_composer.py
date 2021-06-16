from mathapp.system.controller.auth_web_controller import AuthWebController
from mathapp.system.controller.file_web_controller import FileWebController

from mathapp.system.presenter.auth_presenter import AuthPresenter
from mathapp.system.interactor.auth_interactor import AuthInteractor

from mathapp.system.data_mapper.user.user_repository import UserRepository
from mathapp.system.data_mapper.user.user_factory import UserFactory
from mathapp.system.domain_model.user_factory_validating_decorator import UserFactoryValidatingDecorator

from mathapp.system.data_mapper.session.session_factory import SessionFactory
from mathapp.system.data_mapper.session.session_repository import SessionRepository

from mathapp.system.presenter.file_presenter import FilePresenter

from mathapp.system.controller.auth_api_controller import AuthApiController
from mathapp.system.presenter.auth_api_presenter import AuthApiPresenter

class SystemComposer:

    def __init__(self, 
                request, 
                sqlalchemy_session, 
                unit_of_work,  
                encryption_service, 
                token_service,
                date_service,
                file_service):
        self._request = request
        self._sqlalchemy_session = sqlalchemy_session
        self._unit_of_work = unit_of_work
        self._encryption_service = encryption_service
        self._token_service = token_service
        self._date_service = date_service
        self._file_service = file_service

        ##Singleton Lifestyle Components

        self._user_repository = None
        self._session_repository = None


    ##Auth Web Controller

    def compose_auth_web_controller(self):
        presenter = self.compose_auth_presenter()
        interactor = self.compose_auth_interactor()
        return AuthWebController(request = self._request, 
                                 auth_presenter = presenter, 
                                 auth_interactor = interactor)

    def compose_auth_presenter(self):
        return AuthPresenter()

    def compose_auth_interactor(self):
        user_repository = self.compose_user_repository()        
        user_factory = self.compose_user_factory()
        session_repository = self.compose_session_repository()
        session_factory = self.compose_session_factory()
        return AuthInteractor(user_repository = user_repository, 
                                user_factory = user_factory, 
                                session_repository = session_repository,
                                session_factory = session_factory,
                                encryption_service = self._encryption_service, 
                                date_service = self._date_service,
                                token_service = self._token_service,
                                unit_of_work_committer = self._unit_of_work)

    def compose_user_factory(self):
        user_repository = self.compose_user_repository()
        user_factory = UserFactory(unit_of_work = self._unit_of_work)
        return UserFactoryValidatingDecorator(user_factory = user_factory,
                                                 user_repository = user_repository)

    def compose_user_repository(self):
        if self._user_repository is not None:
            return self._user_repository
        user_repository = UserRepository(unit_of_work = self._unit_of_work, 
                                            session = self._sqlalchemy_session)
        self._user_repository = user_repository
        return user_repository

    def compose_session_factory(self):
        session_factory = SessionFactory(unit_of_work = self._unit_of_work)
        return session_factory

    def compose_session_repository(self):
        if self._session_repository is not None:
            return self._session_repository
        session_repository = SessionRepository(unit_of_work = self._unit_of_work, 
                                                sqlalchemy_session = self._sqlalchemy_session)
        self._session_repository = session_repository
        return session_repository


    ##File Web Controller

    def compose_file_web_controller(self):
        file_presenter = self.compose_file_presenter()
        return FileWebController(request=self._request,
                                 file_presenter=file_presenter)

    def compose_file_presenter(self):
        return FilePresenter(file_service=self._file_service)


    ##API Auth Controller

    def compose_auth_api_controller(self):
        auth_interactor = self.compose_auth_interactor()
        auth_api_presenter = self.compose_auth_api_presenter()
        return AuthApiController(request=self._request,
                                 auth_interactor=auth_interactor,
                                 auth_api_presenter=auth_api_presenter)

    def compose_auth_api_presenter(self):
        return AuthApiPresenter()

















