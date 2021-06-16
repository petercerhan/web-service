from mathapp.curriculum.controller.course_web_controller import CourseWebController
from mathapp.curriculum.interactor.course_interactor import CourseInteractor
from mathapp.curriculum.data_mapper.course.course_repository import CourseRepository
from mathapp.curriculum.data_mapper.course.course_factory import CourseFactory
from mathapp.curriculum.domain_model.course_factory_validating_decorator import CourseFactoryValidatingDecorator
from mathapp.curriculum.presenter.course_presenter import CoursePresenter

from mathapp.curriculum.data_mapper.course_topic.course_topic_factory import CourseTopicFactory

from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer

class CurriculumComposer:

    def __init__(self, 
                 request, 
                 sqlalchemy_session, 
                 infrastructure_service_composer,
                 unit_of_work):
        self._request = request
        self._sqlalchemy_session = sqlalchemy_session
        self._infrastructure_service_composer = infrastructure_service_composer
        self._unit_of_work = unit_of_work

        self._curriculum_repository_composer = CurriculumRepositoryComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session)



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
        course_repository = self.compose_course_repository()
        topic_repository = self._curriculum_repository_composer.compose_topic_repository()
        course_factory = self.compose_course_factory()
        course_topic_factory = CourseTopicFactory(unit_of_work=self._unit_of_work)
        return CourseInteractor(course_repository=course_repository,  
                                topic_repository=topic_repository, 
                                course_factory=course_factory,
                                course_topic_factory=course_topic_factory,
                                unit_of_work_committer=self._unit_of_work)

    def compose_course_repository(self):
        return CourseRepository(unit_of_work = self._unit_of_work, 
                                session = self._sqlalchemy_session)

    def compose_course_factory(self):
        course_repository = self.compose_course_repository()
        course_factory = CourseFactory(unit_of_work = self._unit_of_work)
        return CourseFactoryValidatingDecorator(course_factory = course_factory, 
                                                course_repository = course_repository)






