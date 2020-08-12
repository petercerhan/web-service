from mathapp.curriculum.interactor.domain_to_data_transforms.course import course_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.course import course_to_enriched_data

import sys

class CourseInteractor:

    def __init__(self, course_repository, course_factory, unit_of_work_committer):
        self._course_repository = course_repository
        self._course_factory = course_factory
        self._unit_of_work_committer = unit_of_work_committer

    def list(self):
        courses = self._course_repository.list()
        courses_data = [course_to_data(course) for course in courses]
        return courses_data
        
    
    def read(self, id):
        course = self._course_repository.get(id=id)
        enriched_course = course_to_enriched_data(course)
        return enriched_course


    def create(self, fields):
        course = self._course_factory.create(fields)
        self._unit_of_work_committer.commit()
        enriched_course = course_to_enriched_data(course)
        return enriched_course


    def update(self, id, fields):
        course = self._course_repository.get(id=id)

        name = fields.get('name')
        if name is not None:
            course.set_name(name)

        lesson_sequence_items = fields.get('lesson_sequence_items')
        if lesson_sequence_items is not None:
            course.sync_lesson_sequence_item_positions(lesson_sequence_items)

        self._unit_of_work_committer.commit()

        enriched_course = course_to_enriched_data(course)
        return course
        
    
    def delete(self, id):
        course = self._course_repository.get(id=id)
        course.delete()
        self._unit_of_work_committer.commit()
        
        enriched_course = course_to_enriched_data(course)
        return course








