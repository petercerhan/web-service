from mathapp.library.errors.validation_error import ValidationError

class Tutorial:

    def __init__(self,
                 name,
                 lesson_value_holder,
                 tutorial_step_list_value_holder,
                 unit_of_work):
        self._id = None
        self._name = name
        self._lesson_value_holder = lesson_value_holder
        self._tutorial_step_list_value_holder = tutorial_step_list_value_holder
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message="Tutorial requires name")

        if not self._name.strip():
            raise ValidationError(message="Invalid name for Tutorial")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_lesson(self):
        return self._lesson_value_holder.get()

    def get_tutorial_steps(self):
        return self._tutorial_step_list_value_holder.get_list()

    def create_tutorial_step(self, tutorial_step_factory, fields):
        max_position = max([x.get_position() for x in self._tutorial_step_list_value_holder.get_list()], default=-1)
        next_position = max_position+1
        display_group = next_position
        tutorial_step = tutorial_step_factory.create(position=next_position,
                                                     display_group=display_group,
                                                     fields=fields)
        self._tutorial_step_list_value_holder.add(tutorial_step)
        return tutorial_step

    def sync_tutorial_step_positions(self, tutorial_steps_data_array):
        tutorial_steps = self._tutorial_step_list_value_holder.get_list()
        for data_item in tutorial_steps_data_array:
            tutorial_step = next(x for x in tutorial_steps if x.get_id() == data_item['id'])
            if tutorial_step is not None:
                tutorial_step.set_position(data_item['position'])

        self._adjust_display_groups(tutorial_steps)

    def _adjust_display_groups(self, tutorial_steps):
        sorted_tutorial_steps = sorted(tutorial_steps, key=lambda x: x.get_position())
        array_length = len(sorted_tutorial_steps)
        display_group_order_broken = False
        for index, tutorial_step in enumerate(sorted_tutorial_steps):
            if display_group_order_broken:                
                tutorial_step.set_display_group(sorted_tutorial_steps[index-1].get_display_group()+1)
            elif index+1 < array_length and tutorial_step.get_display_group() > sorted_tutorial_steps[index+1].get_display_group():
                display_group_order_broken = True
                if index == 0:
                    tutorial_step.set_display_group(0)
                else:
                    tutorial_step.set_display_group(sorted_tutorial_steps[index-1].get_display_group()+1)

    def delete(self):
        self._unit_of_work.register_deleted(self)

    def __repr__(self):
        return "<Tutorial(name='%s') ID(id='%s')>" % (self._name, self._id)



