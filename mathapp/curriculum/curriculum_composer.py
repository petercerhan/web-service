from mathapp.curriculum.controller.course_web_controller import CourseWebController
from mathapp.curriculum.interactor.course_interactor import CourseInteractor
from mathapp.curriculum.data_mapper.course.course_repository import CourseRepository
from mathapp.curriculum.data_mapper.course.course_factory import CourseFactory
from mathapp.curriculum.domain_model.course_factory_validating_decorator import CourseFactoryValidatingDecorator
from mathapp.curriculum.presenter.course_presenter import CoursePresenter

from mathapp.curriculum.controller.lesson_web_controller import LessonWebController
from mathapp.curriculum.interactor.lesson_interactor import LessonInteractor
from mathapp.curriculum.data_mapper.lesson.lesson_repository import LessonRepository
from mathapp.curriculum.presenter.lesson_presenter import LessonPresenter


class CurriculumComposer:

    def __init__(self, request, sqlalchemy_session, unit_of_work):
        self._request = request
        self._sqlalchemy_session = sqlalchemy_session
        self._unit_of_work = unit_of_work


    ##Course Web Controller

    def compose_course_web_controller(self):
        course_interactor = self.compose_course_interactor()
        course_presenter = self.compose_course_presenter()
        return CourseWebController(request = self._request,
                                     course_interactor = course_interactor,
                                     course_presenter = course_presenter)

    def compose_course_presenter(self):
        return CoursePresenter()
    
    def compose_course_interactor(self):
        course_factory = self.compose_course_factory()
        course_repository = self.compose_course_repository()
        return CourseInteractor(course_repository = course_repository, 
                                course_factory = course_factory, 
                                unit_of_work_committer = self._unit_of_work)

    def compose_course_repository(self):
        return CourseRepository(unit_of_work = self._unit_of_work, 
                                session = self._sqlalchemy_session)

    def compose_course_factory(self):
        course_repository = self.compose_course_repository()
        course_factory = CourseFactory(unit_of_work = self._unit_of_work)
        return CourseFactoryValidatingDecorator(course_factory = course_factory, 
                                                course_repository = course_repository)


    ##Lesson Web Controller

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
        return LessonRepository(unit_of_work = self._unit_of_work, 
                                session = self._sqlalchemy_session)




