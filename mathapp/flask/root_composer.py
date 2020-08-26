from mathapp.curriculum.curriculum_composer import CurriculumComposer
from mathapp.system.system_composer import SystemComposer

from mathapp.sqlalchemy.unit_of_work import UnitOfWork

from mathapp.flask.flask_session import FlaskSession

from mathapp.infrastructure_services.encryption_service import EncryptionService

class RootComposer:

    def __init__(self, request, session):
        self._request = request
        self._session = session

        ##Singleton Lifestyle Components

        self._unit_of_work = None
        self._user_repository = None


    def compose_unit_of_work(self):
        if self._unit_of_work is None:
            self._unit_of_work = UnitOfWork(self._session)
            return self._unit_of_work
        else:
            return self._unit_of_work


    def compose_course_web_controller(self):
        unit_of_work = self.compose_unit_of_work()
        curriculum_composer = CurriculumComposer(request=self._request, 
                                                    sqlalchemy_session = self._session,
                                                     unit_of_work = unit_of_work)

        return curriculum_composer.compose_course_web_controller()

    def compose_lesson_web_controller(self):
        unit_of_work = self.compose_unit_of_work()
        curriculum_composer = CurriculumComposer(request=self._request, 
                                                    sqlalchemy_session = self._session,
                                                     unit_of_work = unit_of_work)

        return curriculum_composer.compose_lesson_web_controller()

    def compose_auth_web_controller(self):
        unit_of_work = self.compose_unit_of_work()
        flask_session = self.compose_flask_session()
        encryption_service = self.compose_encryption_service()
        system_composer = SystemComposer(request = self._request, 
                                        sqlalchemy_session = self._session, 
                                        unit_of_work = self._unit_of_work, 
                                        flask_session = flask_session, 
                                        encryption_service = encryption_service)

        return system_composer.compose_auth_web_controller()

    def compose_flask_session(self):
        return FlaskSession()

    def compose_encryption_service(self):
        return EncryptionService()

