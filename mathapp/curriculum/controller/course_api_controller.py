from flask import (
    request
)
from mathapp.libraries.general_library.errors.mathapp_error import MathAppError

class CourseApiController:

    def __init__(self, 
                 request,
                 course_api_presenter,
                 course_interactor):
        self._request = request
        self._course_api_presenter = course_api_presenter
        self._course_interactor = course_interactor


    def list(self):
        courses = self._course_interactor.list()
        return self._course_api_presenter.list(courses)