from mathapp.subjects.subjects_web_controller import SubjectsWebController
from mathapp.subjects.subject_service import SubjectService
from mathapp.subjects.sqlalchemy_subject_repository import SQLAlchemySubjectRepository
from mathapp.subjects.subject_factory import SubjectFactory

class RootComposer:

    def __init__(self, request, db_sqlalchemy):
        self.request = request
        self.db_sqlalchemy = db_sqlalchemy

    def compose_subjects_web_controller(self):
        subject_service = self.compose_subject_service()
        return SubjectsWebController(request = self.request,
                                     subject_service = subject_service)
    
    def compose_subject_service(self):
        subject_factory = self.compose_subject_factory()
        return SubjectService(subject_repository = self.compose_subject_repository(), 
                                subject_factory = subject_factory)

    def compose_subject_repository(self):
        return SQLAlchemySubjectRepository()

    def compose_subject_factory(self):
        return SubjectFactory()
