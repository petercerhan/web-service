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
from mathapp.curriculum.data_mapper.lesson.lesson_factory import LessonFactory
from mathapp.curriculum.domain_model.lesson_factory_validating_decorator import LessonFactoryValidatingDecorator

from mathapp.curriculum.data_mapper.lesson_sequence_item.lesson_sequence_item_factory import LessonSequenceItemFactory

from mathapp.curriculum.controller.lesson_intro_web_controller import LessonIntroWebController
from mathapp.curriculum.presenter.lesson_intro_presenter import LessonIntroPresenter
from mathapp.curriculum.interactor.lesson_intro_interactor import LessonIntroInteractor
from mathapp.curriculum.data_mapper.lesson_intro.lesson_intro_factory import LessonIntroFactory

from mathapp.curriculum.controller.concept_tutorial_web_controller import ConceptTutorialWebController
from mathapp.curriculum.presenter.concept_tutorial_presenter import ConceptTutorialPresenter
from mathapp.curriculum.interactor.concept_tutorial_interactor import ConceptTutorialInteractor
from mathapp.curriculum.data_mapper.concept_tutorial.concept_tutorial_factory import ConceptTutorialFactory

from mathapp.curriculum.controller.detail_section_web_controller import DetailSectionWebController
from mathapp.curriculum.presenter.detail_section_presenter import DetailSectionPresenter
from mathapp.curriculum.data_mapper.detail_section.detail_section_factory import DetailSectionFactory
from mathapp.curriculum.data_mapper.detail_section.detail_section_repository import DetailSectionRepository
from mathapp.curriculum.interactor.detail_section_interactor import DetailSectionInteractor

from mathapp.curriculum.data_mapper.text_glyph.text_glyph_factory import TextGlyphFactory
from mathapp.curriculum.data_mapper.formula_glyph.formula_glyph_factory import FormulaGlyphFactory
from mathapp.curriculum.data_mapper.image_glyph.image_glyph_factory import ImageGlyphFactory

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


    ##Lesson Web Controller

    def compose_lesson_web_controller(self):
        lesson_interactor = self.compose_lesson_interactor()
        lesson_presenter = self.compose_lesson_presenter()
        course_interactor = self.compose_course_interactor()
        return LessonWebController(request = self._request, 
                                    lesson_interactor = lesson_interactor, 
                                    lesson_presenter = lesson_presenter, 
                                    course_interactor = course_interactor)

    def compose_lesson_presenter(self):
        return LessonPresenter()

    def compose_lesson_interactor(self):
        repository = self.compose_lesson_repository()
        lesson_factory = self.compose_lesson_factory()
        course_repository = self.compose_course_repository()
        lesson_sequence_item_factory = self.compose_lesson_sequence_item_factory()
        return LessonInteractor(lesson_repository = repository, 
                                lesson_factory = lesson_factory, 
                                course_repository=course_repository, 
                                lesson_sequence_item_factory=lesson_sequence_item_factory,
                                unit_of_work_committer = self._unit_of_work)


    def compose_lesson_repository(self):
        return LessonRepository(unit_of_work = self._unit_of_work, 
                                session = self._sqlalchemy_session)

    def compose_lesson_factory(self):
        lesson_factory = LessonFactory(unit_of_work = self._unit_of_work)
        lesson_repository = self.compose_lesson_repository()
        return LessonFactoryValidatingDecorator(lesson_factory=lesson_factory,
                                                 lesson_repository=lesson_repository)


    def compose_lesson_sequence_item_factory(self):
        return LessonSequenceItemFactory(unit_of_work=self._unit_of_work)


    ##Lesson Intro Web Controller

    def compose_lesson_intro_web_controller(self):
        presenter = self.compose_lesson_intro_presenter()
        detail_section_presenter = self.compose_detail_section_presenter()
        interactor = self.compose_lesson_intro_interactor()
        lesson_interactor = self.compose_lesson_interactor()
        detail_section_interactor = self.compose_detail_section_interactor()
        return LessonIntroWebController(request=self._request, 
                                        lesson_intro_presenter=presenter, 
                                        detail_section_presenter=detail_section_presenter,
                                        lesson_intro_interactor=interactor, 
                                        lesson_interactor=lesson_interactor, 
                                        detail_section_interactor=detail_section_interactor)

    def compose_lesson_intro_presenter(self):
        return LessonIntroPresenter()

    def compose_lesson_intro_interactor(self):
        lesson_repository = self.compose_lesson_repository()
        lesson_intro_factory = self.compose_lesson_intro_factory()
        detail_section_factory = self.compose_detail_section_factory()
        unit_of_work = self._unit_of_work
        return LessonIntroInteractor(lesson_repository=lesson_repository, 
                                    lesson_intro_factory=lesson_intro_factory, 
                                    detail_section_factory=detail_section_factory,
                                    unit_of_work=unit_of_work)

    def compose_lesson_intro_factory(self):
        return LessonIntroFactory(unit_of_work=self._unit_of_work)


    ##Concept Tutorial Web Controller

    def compose_concept_tutorial_web_controller(self):
        presenter = self.compose_concept_tutorial_presenter()
        lesson_interactor = self.compose_lesson_interactor()
        concept_tutorial_interactor = self.compose_concept_tutorial_interactor()
        return ConceptTutorialWebController(request=self._request, 
                                            presenter=presenter,
                                            lesson_interactor=lesson_interactor,
                                            concept_tutorial_interactor=concept_tutorial_interactor)

    def compose_concept_tutorial_presenter(self):
        return ConceptTutorialPresenter(request=self._request)

    def compose_concept_tutorial_interactor(self):
        lesson_repository = self.compose_lesson_repository()
        concept_tutorial_factory = self.compose_concept_tutorial_factory()
        detail_section_factory = self.compose_detail_section_factory()
        unit_of_work = self._unit_of_work
        return ConceptTutorialInteractor(lesson_repository=lesson_repository, 
                                            concept_tutorial_factory=concept_tutorial_factory, 
                                            detail_section_factory=detail_section_factory,
                                            unit_of_work=unit_of_work)


    def compose_concept_tutorial_factory(self):
        return ConceptTutorialFactory(unit_of_work=self._unit_of_work)



    ##Detail Sections

    def compose_detail_section_web_controller(self):
        detail_section_presenter = self.compose_detail_section_presenter()
        detail_section_interactor = self.compose_detail_section_interactor()
        return DetailSectionWebController(request=self._request, 
                                          detail_section_presenter=detail_section_presenter, 
                                          detail_section_interactor=detail_section_interactor)

    def compose_detail_section_interactor(self):
        detail_section_repository = self.compose_detail_section_repository()
        text_glyph_factory = self.compose_text_glyph_factory()
        formula_glyph_factory = self.compose_formula_glyph_factory()
        image_glyph_factory = self.compose_image_glyph_factory()
        file_service = self._infrastructure_service_composer.compose_file_service()
        date_service = self._infrastructure_service_composer.compose_date_service()
        return DetailSectionInteractor(detail_section_repository=detail_section_repository, 
                                        text_glyph_factory=text_glyph_factory, 
                                        formula_glyph_factory=formula_glyph_factory, 
                                        image_glyph_factory=image_glyph_factory, 
                                        file_service=file_service, 
                                        date_service=date_service,
                                        unit_of_work=self._unit_of_work)

    def compose_detail_section_presenter(self):
        file_service = self._infrastructure_service_composer.compose_file_service()        
        return DetailSectionPresenter(file_service=file_service)

    def compose_detail_section_factory(self):
        return DetailSectionFactory(unit_of_work=self._unit_of_work)

    def compose_detail_section_repository(self):
        return DetailSectionRepository(unit_of_work=self._unit_of_work, session = self._sqlalchemy_session)


    ##Detail Glyphs

    def compose_text_glyph_factory(self):
        return TextGlyphFactory(unit_of_work=self._unit_of_work)

    def compose_formula_glyph_factory(self):
        return FormulaGlyphFactory(unit_of_work=self._unit_of_work)

    def compose_image_glyph_factory(self):
        return ImageGlyphFactory(unit_of_work=self._unit_of_work)





