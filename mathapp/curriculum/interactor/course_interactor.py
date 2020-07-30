import sys

class CourseInteractor:

    def __init__(self, course_repository, course_factory, unit_of_work_committer):
        self._course_repository = course_repository
        self._course_factory = course_factory
        self._unit_of_work_committer = unit_of_work_committer

    def list(self):
        values = self._course_repository.list()
        return values
    
    
    def read(self, id):
        course = self._course_repository.get(id=id)

        print('course with: %s' % course.get_lesson_sequence_items())

        return course


    def create(self, fields):
        course = self._course_factory.create(fields)
        self._unit_of_work_committer.commit()
        return course


    def update(self, id, fields):
        course = self._course_repository.get(id=id)

        name = fields.get('name')
        if name is not None:
            course.set_name(name)

        self._unit_of_work_committer.commit()

        return course
        
    
    def delete(self, id):
        course = self._course_repository.get(id=id)
        course.delete()
        self._unit_of_work_committer.commit()
        return course








