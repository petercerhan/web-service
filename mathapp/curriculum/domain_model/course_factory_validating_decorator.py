from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

class CourseFactoryValidatingDecorator:
    
    def __init__(self, course_factory, course_repository):
        self._course_factory = course_factory
        self._course_repository = course_repository

    def create(self, fields):
        name = fields.get('name')
        if name is not None:
            self._check_name_unique(name)

        return self._course_factory.create(fields)

    def _check_name_unique(self, name):
        try:
            self._course_repository.get_by_name(name)
            raise ValidationError(message = 'Course name must be unique')
        except NotFoundError:
            return None