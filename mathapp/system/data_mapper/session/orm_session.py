from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship

from mathapp.system.domain_model.session import Session
from mathapp.libraries.data_mapper_library.value_holder import ValueHolder

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.libraries.data_mapper_library.base import Base

class ORMSession(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    revoked = Column(Boolean)
    created_at = Column(DateTime)

    user = relationship('ORMUser')

    def __init__(self, user_id, revoked, created_at):
        self.user_id = user_id
        self.revoked = revoked
        self.created_at = created_at
        self._session = None

    @orm.reconstructor
    def init_on_load(self):
        self._session = None

    def get_model(self, unit_of_work):
        if self._session is not None:
            return self._session

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        user_value_holder = ValueHolder(orm_model=self,
                                         property_name='user',
                                         set_at_init=(self.user_id is not None),
                                         unit_of_work=unit_of_work)

        session = Session(user_value_holder = user_value_holder,
                            revoked = self.revoked, 
                            created_at = self.created_at, 
                            unit_of_work = domain_model_unit_of_work)
        session._id = self.id

        self._session = session
        return session

    def sync_id(self):
        self._session._id = self.id

    def sync_fields(self):
        self.revoked = self._session._revoked
        self.created_at = self._session._created_at

    def __repr__(self):
        return "<ORMSession ID(id='%s') CreatedAt(created_at='%s') Revoked(revoked='%s')>" % (self.id, self.created_at, self.revoked)
