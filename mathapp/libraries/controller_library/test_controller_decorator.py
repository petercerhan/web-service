

class TestControllerDecorator:

    def __init__(self, decorated_controller):
      self._decorated_controller = decorated_controller

    def __getattr__(self, name):
        def method(**kwargs):
            return getattr(self._decorated_controller, name)(**kwargs)
        return method
