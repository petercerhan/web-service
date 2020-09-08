from mathapp.system.controller.auth_web_controller import AuthWebController
from mathapp.system.presenter.auth_presenter import AuthPresenter
from mathapp.system.interactor.auth_interactor import AuthInteractor
from mathapp.system.data_mapper.user.user_repository import UserRepository
from mathapp.system.data_mapper.user.user_factory import UserFactory
from mathapp.system.domain_model.user_factory_validating_decorator import UserFactoryValidatingDecorator

class SystemComposer:

    def __init__(self, 
                request, 
                sqlalchemy_session, 
                unit_of_work, 
                flask_session, 
                encryption_service, 
                token_service,
                date_service):
        self._request = request
        self._sqlalchemy_session = sqlalchemy_session
        self._unit_of_work = unit_of_work
        self._flask_session = flask_session
        self._encryption_service = encryption_service
        self._token_service = token_service
        self._date_service = date_service

        ##Singleton Lifestyle Components

        self._user_repository = None


    ##Auth Web Controller

    def compose_auth_web_controller(self):
        presenter = self.compose_auth_presenter()
        interactor = self.compose_auth_interactor()
        return AuthWebController(request = self._request, 
                                 flask_session = self._flask_session,
                                 auth_presenter = presenter, 
                                 auth_interactor = interactor)

    def compose_auth_presenter(self):
        return AuthPresenter()

    def compose_auth_interactor(self):
        user_repository = self.compose_user_repository()        
        user_factory = self.compose_user_factory()
        return AuthInteractor(user_repository = user_repository, 
                                user_factory = user_factory,
                                encryption_service = self._encryption_service, 
                                date_service = self._date_service,
                                token_service = self._token_service,
                                unit_of_work_committer = self._unit_of_work)

    def compose_user_factory(self):
        user_repository = self.compose_user_repository()
        user_factory = UserFactory(unit_of_work = self._unit_of_work, 
                                    user_repository = user_repository)
        return UserFactoryValidatingDecorator(user_factory = user_factory,
                                                 user_repository = user_repository)

    def compose_user_repository(self):
        if self._user_repository is not None:
            return self._user_repository
        user_repository = UserRepository(unit_of_work = self._unit_of_work, 
                                            session = self._sqlalchemy_session)
        self._user_repository = user_repository
        return user_repository




