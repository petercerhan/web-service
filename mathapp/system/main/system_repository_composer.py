from mathapp.system.data_mapper.user.user_repository import UserRepository
from mathapp.system.data_mapper.session.session_repository import SessionRepository

class SystemRepositoryComposer:

    def __init__(self,
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._sqlalchemy_session = sqlalchemy_session

    def compose_user_repository(self):
        return UserRepository(unit_of_work=self._unit_of_work,
                              session=self._sqlalchemy_session)

    def compose_session_repository(self):
        return SessionRepository(unit_of_work=self._unit_of_work,
                                 sqlalchemy_session=self._sqlalchemy_session)