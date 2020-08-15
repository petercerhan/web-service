from mathapp.curriculum.controller.course_web_controller import CourseWebController
from mathapp.curriculum.interactor.course_interactor import CourseInteractor
from mathapp.curriculum.data_mapper.course.course_repository import CourseRepository
from mathapp.curriculum.data_mapper.course.course_factory import CourseFactory
from mathapp.sqlalchemy.unit_of_work import UnitOfWork

from mathapp.curriculum.controller.lesson_web_controller import LessonWebController
from mathapp.curriculum.interactor.lesson_interactor import LessonInteractor
from mathapp.curriculum.data_mapper.lesson.lesson_repository import LessonRepository

from mathapp.curriculum.presenter.course_presenter import CoursePresenter
from mathapp.curriculum.presenter.lesson_presenter import LessonPresenter

from mathapp.system.controller.auth_web_controller import AuthWebController
from mathapp.system.presenter.auth_presenter import AuthPresenter
from mathapp.system.interactor.auth_interactor import AuthInteractor
from mathapp.system.data_mapper.user.user_repository import UserRepository
from mathapp.system.data_mapper.user.user_factory import UserFactory

class RootComposer:

    def __init__(self, request, session):
        self._request = request
        self._session = session

        self._unit_of_work = None
        self._user_repository = None

    def compose_course_web_controller(self):
        course_interactor = self.compose_course_interactor()
        course_presenter = self.compose_course_presenter()
        return CourseWebController(request = self._request,
                                     course_interactor = course_interactor,
                                     course_presenter = course_presenter)

    def compose_course_presenter(self):
        return CoursePresenter()
    
    def compose_course_interactor(self):
        unit_of_work = self.compose_unit_of_work()
        course_factory = self.compose_course_factory()
        course_repository = self.compose_course_repository()
        return CourseInteractor(course_repository = course_repository, 
                                course_factory = course_factory, 
                                unit_of_work_committer = unit_of_work)


    def compose_course_repository(self):
        unit_of_work = self.compose_unit_of_work()
        return CourseRepository(unit_of_work = unit_of_work, session = self._session)

    def compose_course_factory(self):
        unit_of_work = self.compose_unit_of_work()
        return CourseFactory(unit_of_work = unit_of_work)


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
        presenter = self.compose_auth_presenter()
        interactor = self.compose_auth_interactor()
        return AuthWebController(request = self._request, 
                                 auth_presenter = presenter, 
                                 auth_interactor = interactor)

    def compose_auth_presenter(self):
        return AuthPresenter()

    def compose_auth_interactor(self):
        unit_of_work = self.compose_unit_of_work()
        user_repository = self.compose_user_repository()        
        user_factory = self.compose_user_factory()
        return AuthInteractor(user_repository = user_repository, 
                                user_factory = user_factory,
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



