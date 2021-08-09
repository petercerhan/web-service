from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.libraries.data_mapper_library.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.system.domain_model.user import User

from mathapp.system.data_mapper.role.orm_role import ORMRole
from mathapp.student.data_mapper.student.orm_student import ORMStudent

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork


from mathapp.libraries.data_mapper_library.list_value_holder import ListValueHolder

class ORMUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    roles = relationship('ORMRole')

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._user = None

    @orm.reconstructor
    def init_on_load(self):
        self._user = None
        
    def get_model(self, unit_of_work):
        if self._user is not None:
            return self._user

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        role_list_value_holder = ListValueHolder(orm_model=self,
                                             property_name='roles',
                                             unit_of_work=unit_of_work)

        user = User(username = self.username, 
                    password = self.password, 
                    role_list_value_holder=role_list_value_holder,
                    unit_of_work = domain_model_unit_of_work)
        user._id = self.id

        self._user = user
        return user

    def sync_id(self):
        self._user.id = self.id

    def sync_fields(self):
        self.username = self._user._username
        self.password = self._user._password
    
    def __repr__(self):
        return "<ORMUser ID(id='%s') Username(username='%s') Password(password='%s')>" % (self.id, self.username, self.password)
