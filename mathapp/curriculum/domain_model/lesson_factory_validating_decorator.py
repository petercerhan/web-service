from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

class LessonFactoryValidatingDecorator:

    def __init__(self, lesson_factory, lesson_repository):
        self._lesson_factory = lesson_factory
        self._lesson_repository = lesson_repository

    def create(self, fields):
        name = fields.get('name')
        if name is not None:
            self._check_name_unique(name)

        return self._lesson_factory.create(fields)

    def _check_name_unique(self, name):
        try:
            self._lesson_repository.get_by_name(name)
            raise ValidationError(message = 'Lesson name must be unique')
        except NotFoundError:
            pass
