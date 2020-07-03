
class Subject:
    
    def __init__(self, name, unit_of_work):
        self._id = None
        self._name = name
        self._unit_of_work = unit_of_work

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name