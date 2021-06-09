from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data, lesson_to_enriched_data

import sys

class LessonInteractor:
    
    def __init__(self, 
                lesson_repository, 
                lesson_factory, 
                course_repository, 
                unit_of_work_committer):
        self._lesson_repository = lesson_repository
        self._lesson_factory = lesson_factory
        self._course_repository = course_repository
        self._unit_of_work_committer = unit_of_work_committer

    def list(self):
        lessons = self._lesson_repository.list()
        lessons_data = [lesson_to_data(lesson) for lesson in lessons]
        return lessons_data

    def read(self, id):
        lesson = self._lesson_repository.get(id=id)
        return lesson_to_enriched_data(lesson)

    def create(self, fields, add_to_course_id):
        pass

        self._unit_of_work_committer.commit()
        return lesson_to_enriched_data(lesson)

    def update(self, id, fields):
        lesson = self._lesson_repository.get(id=id)

        display_name = fields.get('display_name')
        if display_name is not None:
            lesson.set_display_name(display_name)

        lesson_sections = fields.get('lesson_sections')
        if lesson_sections is not None:
            lesson.sync_lesson_section_positions(lesson_sections)

        self._unit_of_work_committer.commit()

        return lesson_to_enriched_data(lesson)

    def delete(self, id):
        pass

    def delete_lesson_section(self, lesson_id, lesson_section_id):
        lesson = self._lesson_repository.get(id=lesson_id)
        lesson.remove_lesson_section(lesson_section_id)
        self._unit_of_work_committer.commit()
        return lesson_to_enriched_data(lesson)











