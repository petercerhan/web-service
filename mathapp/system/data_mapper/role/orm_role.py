from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.libraries.data_mapper_library.base import Base

from mathapp.system.domain_model.role import Role

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMRole(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'role',
        'polymorphic_on': type
    }

    def __init__(self, user_id):
        self._user_id = user_id
        self._role = None

    @orm.reconstructor
    def init_on_load(self):
        self._role = None

    def _set_model(self, model):
        self._role = model

    def get_model(self, unit_of_work):
        if self._role is not None:
            return self._role

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        role = Role(role_type_name=self.type, 
                    unit_of_work=domain_model_unit_of_work)
        role._id = self.id
        self._role = role
        return role

    def sync_id(self):
        self._role._id = self.id

    def sync_fields(self):
        pass
        
    def __repr__(self):
         return f'<Role(id={self.id}, type={self.type})>'





