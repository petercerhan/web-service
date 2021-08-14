from mathapp.libraries.general_library.errors.mathapp_error import MathAppError
from flask import abort


class ApiErrorHandlingControllerDecorator:

    def __init__(self, decorated_controller):
        self._decorated_controller = decorated_controller


    def __getattr__(self, name):
        def method(**kwargs):
            return self._execute_method(name, **kwargs)
        return method

    def _execute_method(self, name, **kwargs):
        try:
            return getattr(self._decorated_controller, name)(**kwargs)
        except MathAppError as error:
            # return error.message
            abort(404)