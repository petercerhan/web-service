from mathapp.system.system_composer import SystemComposer
from mathapp.sqlalchemy.sqlalchemy_composer import SQLAlchemyComposer
from mathapp.infrastructure_services.infrastructure_service_composer import InfrastructureServiceComposer

from mathapp.curriculum.main.curriculum_controller_composer import CurriculumControllerComposer

from flask import current_app

class RootComposer:

    def __init__(self, request):
        self._request = request
        self._sqlalchemy_composer = SQLAlchemyComposer()
        self._sqlalchemy_session = self._sqlalchemy_composer.compose_session()
        self._unit_of_work = self._sqlalchemy_composer.compose_unit_of_work()
        self._infrastructure_service_composer = InfrastructureServiceComposer(file_uploads_path=current_app.config['FILE_UPLOADS_PATH'])


    def get_system_controller_composer(self):
        encryption_service = self._infrastructure_service_composer.compose_encryption_service()
        date_service = self._infrastructure_service_composer.compose_date_service()
        token_service = self._infrastructure_service_composer.compose_token_service()
        file_service = self._infrastructure_service_composer.compose_file_service()
        system_composer = SystemComposer(request = self._request, 
                                        sqlalchemy_session = self._sqlalchemy_session, 
                                        unit_of_work = self._unit_of_work, 
                                        encryption_service = encryption_service, 
                                        token_service = token_service,
                                        date_service = date_service,
                                        file_service=file_service)
        return system_composer


    def get_curriculum_controller_composer(self):
        curriculum_composer =  CurriculumControllerComposer(request=self._request,
                                                            sqlalchemy_session = self._sqlalchemy_session,
                                                            infrastructure_service_composer=self._infrastructure_service_composer,
                                                            unit_of_work = self._unit_of_work)
        return curriculum_composer





