from mathapp.system.main.system_repository_composer import SystemRepositoryComposer

from mathapp.system.data_mapper.user.user_factory import UserFactory
from mathapp.system.domain_model.user_factory_validating_decorator import UserFactoryValidatingDecorator
from mathapp.system.data_mapper.session.session_factory import SessionFactory

class SystemFactoryComposer:

    def __init__(self,
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._system_repository_composer = SystemRepositoryComposer(unit_of_work=unit_of_work,
                                                                    sqlalchemy_session=sqlalchemy_session)

    def compose_user_factory(self):
        user_repository = self._system_repository_composer.compose_user_repository()
        user_factory = UserFactory(unit_of_work=self._unit_of_work)
        decorated_factory = UserFactoryValidatingDecorator(user_factory=user_factory,
                                                           user_repository=user_repository)
        return decorated_factory

    def compose_session_factory(self):
        return SessionFactory(unit_of_work=self._unit_of_work)


