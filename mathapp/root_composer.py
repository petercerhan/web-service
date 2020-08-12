from mathapp.curriculum.controller.course_web_controller import CourseWebController
from mathapp.curriculum.interactor.course_interactor import CourseInteractor
from mathapp.curriculum.data_mapper.course.course_repository import CourseRepository
from mathapp.curriculum.data_mapper.course.course_factory import CourseFactory
from mathapp.sqlalchemy.unit_of_work import UnitOfWork

from mathapp.curriculum.controller.lesson_web_controller import LessonWebController
from mathapp.curriculum.interactor.lesson_interactor import LessonInteractor
from mathapp.curriculum.data_mapper.lesson.lesson_repository import LessonRepository

from mathapp.curriculum.presenter.course_presenter import CoursePresenter

class RootComposer:

    def __init__(self, request, session):
        self._request = request
        self._session = session

        self._unit_of_work = None

    def compose_course_web_controller(self):
        course_interactor = self.compose_course_interactor()
        course_presenter = self.compose_course_presenter()
        return CourseWebController(request = self._request,
                                     course_interactor = course_interactor,
                                     course_presenter = course_presenter)
    
    def compose_course_interactor(self):
        unit_of_work = self.compose_unit_of_work()
        course_factory = self.compose_course_factory()
        course_repository = self.compose_course_repository()
        return CourseInteractor(course_repository = course_repository, 
                                course_factory = course_factory, 
                                unit_of_work_committer = unit_of_work)

    def compose_course_presenter(self):
        return CoursePresenter()

    def compose_course_repository(self):
        unit_of_work = self.compose_unit_of_work()
        return CourseRepository(unit_of_work = unit_of_work, session = self._session)

    def compose_course_factory(self):
        unit_of_work = self.compose_unit_of_work()
        return CourseFactory(unit_of_work = unit_of_work)


    def compose_lesson_web_controller(self):
        lesson_interactor = self.compose_lesson_interactor()
        return LessonWebController(request = self._request, 
                                    lesson_interactor = lesson_interactor)

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
