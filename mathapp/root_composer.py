from mathapp.web_controller.subject_web_controller import SubjectWebController
from mathapp.domain.services.subject_service import SubjectService
from mathapp.subjects.subject_repository import SubjectRepository
from mathapp.subjects.subject_factory import SubjectFactory
from mathapp.subjects.unit_of_work import UnitOfWork

class RootComposer:

    def __init__(self, request, session):
        self._request = request
        self._session = session

        self._unit_of_work = None

    def compose_subject_web_controller(self):
        subject_service = self.compose_subject_service()
        return SubjectWebController(request = self._request,
                                     subject_service = subject_service)
    
    def compose_subject_service(self):
        unit_of_work = self.compose_unit_of_work()
        subject_factory = self.compose_subject_factory()
        return SubjectService(subject_repository = self.compose_subject_repository(), 
                                subject_factory = subject_factory, 
                                unit_of_work_committer = unit_of_work)

    def compose_subject_repository(self):
        unit_of_work = self.compose_unit_of_work()
        return SubjectRepository(unit_of_work = unit_of_work, session = self._session)

    def compose_subject_factory(self):
        unit_of_work = self.compose_unit_of_work()
        return SubjectFactory(unit_of_work = unit_of_work)

    def compose_unit_of_work(self):
        if self._unit_of_work is None:
            self._unit_of_work = UnitOfWork(self._session)
            return self._unit_of_work
        else:
            return self._unit_of_work
