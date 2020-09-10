from mathapp.curriculum.curriculum_composer import CurriculumComposer
from mathapp.system.system_composer import SystemComposer
from mathapp.sqlalchemy.sqlalchemy_composer import SQLAlchemyComposer
from mathapp.infrastructure_services.infrastructure_service_composer import InfrastructureServiceComposer

class RootComposer:

    def __init__(self, request):
        self._request = request

        self._sqlalchemy_composer = SQLAlchemyComposer()
        self._sqlalchemy_session = self._sqlalchemy_composer.compose_session()
        self._unit_of_work = self._sqlalchemy_composer.compose_unit_of_work()

        self._infrastructure_service_composer = InfrastructureServiceComposer()


    def compose_course_web_controller(self):
        curriculum_composer = CurriculumComposer(request=self._request, 
                                                    sqlalchemy_session = self._sqlalchemy_session,
                                                     unit_of_work = self._unit_of_work)

        return curriculum_composer.compose_course_web_controller()

    def compose_lesson_web_controller(self):
        curriculum_composer = CurriculumComposer(request=self._request, 
                                                    sqlalchemy_session = self._sqlalchemy_session,
                                                     unit_of_work = self._unit_of_work)

        return curriculum_composer.compose_lesson_web_controller()

    def compose_auth_web_controller(self):
        encryption_service = self._infrastructure_service_composer.compose_encryption_service()
        date_service = self._infrastructure_service_composer.compose_date_service()
        token_service = self._infrastructure_service_composer.compose_token_service()
        system_composer = SystemComposer(request = self._request, 
                                        sqlalchemy_session = self._sqlalchemy_session, 
                                        unit_of_work = self._unit_of_work, 
                                        encryption_service = encryption_service, 
                                        token_service = token_service,
                                        date_service = date_service)

        return system_composer.compose_auth_web_controller()
