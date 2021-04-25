from mathapp.curriculum.main.curriculum_composer import CurriculumComposer
from mathapp.system.system_composer import SystemComposer
from mathapp.sqlalchemy.sqlalchemy_composer import SQLAlchemyComposer
from mathapp.infrastructure_services.infrastructure_service_composer import InfrastructureServiceComposer

from mathapp.curriculum.main.curriculum_controller_composer import CurriculumControllerComposer

from flask import current_app
import sys

class RootComposer:

    def __init__(self, request):
        self._request = request

        self._sqlalchemy_composer = SQLAlchemyComposer()
        self._sqlalchemy_session = self._sqlalchemy_composer.compose_session()
        self._unit_of_work = self._sqlalchemy_composer.compose_unit_of_work()

        self._infrastructure_service_composer = InfrastructureServiceComposer(file_uploads_path=current_app.config['FILE_UPLOADS_PATH'])


    def compose_course_web_controller(self):
        curriculum_composer = self.compose_curriculum_composer()
        return curriculum_composer.compose_course_web_controller()

    # def compose_lesson_web_controller(self):
    #     curriculum_composer = self.compose_curriculum_composer()
    #     return curriculum_composer.compose_lesson_web_controller()

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

    def compose_lesson_intro_web_controller(self):
        curriculum_composer = self.compose_curriculum_composer()
        return curriculum_composer.compose_lesson_intro_web_controller()

    def compose_concept_tutorial_web_controller(self):
        curriculum_composer = self.compose_curriculum_composer()
        return curriculum_composer.compose_concept_tutorial_web_controller()

    def compose_detail_section_web_controller(self):
        curriculum_composer = self.compose_curriculum_composer()
        return curriculum_composer.compose_detail_section_web_controller()

    def compose_topic_web_controller(self):
        controller_composer = self._get_curriculum_controller_composer()
        return controller_composer.compose_topic_web_controller()

    def compose_lesson_web_controller(self):
        controller_composer = self._get_curriculum_controller_composer()
        return controller_composer.compose_lesson_web_controller()

    def compose_tutorial_web_controller(self):
        controller_composer = self._get_curriculum_controller_composer()
        return controller_composer.compose_tutorial_web_controller()

    def _get_curriculum_controller_composer(self):
        return CurriculumControllerComposer(request=self._request,
                                            sqlalchemy_session = self._sqlalchemy_session, 
                                            infrastructure_service_composer=self._infrastructure_service_composer,
                                            unit_of_work = self._unit_of_work)
        

    def compose_curriculum_composer(self):
        return CurriculumComposer(request=self._request,
                                  sqlalchemy_session = self._sqlalchemy_session, 
                                  infrastructure_service_composer=self._infrastructure_service_composer,
                                  unit_of_work = self._unit_of_work)











