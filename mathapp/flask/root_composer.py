from mathapp.curriculum.curriculum_composer import CurriculumComposer


from mathapp.curriculum.controller.course_web_controller import CourseWebController
from mathapp.curriculum.interactor.course_interactor import CourseInteractor
from mathapp.curriculum.data_mapper.course.course_repository import CourseRepository
from mathapp.curriculum.data_mapper.course.course_factory import CourseFactory
from mathapp.curriculum.domain_model.course_factory_validating_decorator import CourseFactoryValidatingDecorator
from mathapp.sqlalchemy.unit_of_work import UnitOfWork

from mathapp.curriculum.controller.lesson_web_controller import LessonWebController
from mathapp.curriculum.interactor.lesson_interactor import LessonInteractor
from mathapp.curriculum.data_mapper.lesson.lesson_repository import LessonRepository

from mathapp.curriculum.presenter.lesson_presenter import LessonPresenter

from mathapp.system.controller.auth_web_controller import AuthWebController
from mathapp.system.presenter.auth_presenter import AuthPresenter
from mathapp.system.interactor.auth_interactor import AuthInteractor
from mathapp.system.data_mapper.user.user_repository import UserRepository
from mathapp.system.data_mapper.user.user_factory import UserFactory

from mathapp.flask.flask_session import FlaskSession

from mathapp.infrastructure_services.encryption_service import EncryptionService

class RootComposer:

    def __init__(self, request, session):
        self._request = request
        self._session = session

        ##Singleton Lifestyle Components

        self._unit_of_work = None
        self._user_repository = None

    def compose_course_web_controller(self):
        unit_of_work = self.compose_unit_of_work()
        curriculum_composer = CurriculumComposer(request=self._request, 
                                                    sqlalchemy_session = self._session,
                                                     unit_of_work = unit_of_work)

        return curriculum_composer.compose_course_web_controller()


    def compose_lesson_web_controller(self):
        lesson_interactor = self.compose_lesson_interactor()
        lesson_presenter = self.compose_lesson_presenter()
        return LessonWebController(request = self._request, 
                                    lesson_interactor = lesson_interactor, 
                                    lesson_presenter = lesson_presenter)

    def compose_lesson_presenter(self):
        return LessonPresenter()

    def compose_lesson_interactor(self):
        repository = self.compose_lesson_repository()
        return LessonInteractor(lesson_repository = repository)


    def compose_lesson_repository(self):
        unit_of_work = self.compose_unit_of_work()
        return LessonRepository(unit_of_work = unit_of_work, 
                                session = self._session)

    def compose_unit_of_work(self):
        if self._unit_of_work is None:
            self._unit_of_work = UnitOfWork(self._session)
            return self._unit_of_work
        else:
            return self._unit_of_work


    def compose_auth_web_controller(self):
        flask_session = self.compose_flask_session()
        presenter = self.compose_auth_presenter()
        interactor = self.compose_auth_interactor()
        return AuthWebController(request = self._request, 
                                 flask_session = flask_session,
                                 auth_presenter = presenter, 
                                 auth_interactor = interactor)

    def compose_auth_presenter(self):
        return AuthPresenter()

    def compose_auth_interactor(self):
        unit_of_work = self.compose_unit_of_work()
        user_repository = self.compose_user_repository()        
        user_factory = self.compose_user_factory()
        encryption_service = self.compose_encryption_service()
        return AuthInteractor(user_repository = user_repository, 
                                user_factory = user_factory,
                                encryption_service = encryption_service,
                                unit_of_work_committer = unit_of_work)

    def compose_user_factory(self):
        unit_of_work = self.compose_unit_of_work()
        user_repository = self.compose_user_repository()
        return UserFactory(unit_of_work = unit_of_work, user_repository = user_repository)

    def compose_user_repository(self):
        if self._user_repository is not None:
            return self._user_repository
        unit_of_work = self.compose_unit_of_work()
        user_repository = UserRepository(unit_of_work = unit_of_work, 
                                            session = self._session)
        self._user_repository = user_repository
        return user_repository

    def compose_flask_session(self):
        return FlaskSession()

    def compose_encryption_service(self):
        return EncryptionService()

