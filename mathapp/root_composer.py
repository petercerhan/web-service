from mathapp.subjects.subjects_web_controller import SubjectsWebController
from mathapp.subjects.subject_service import SubjectService

class RootComposer:

    def __init__(self, request, db_sqlalchemy):
        self.request = request
        self.db_sqlalchemy = db_sqlalchemy

    def compose_subjects_web_controller(self):
        subject_service = self.compose_subject_service()
        return SubjectsWebController(request = self.request,
                                     subject_service = subject_service)
    
    def compose_subject_service(self):
        return SubjectService()
