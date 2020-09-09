from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy import orm

from mathapp.system.domain_model.session import Session
from mathapp.system.data_mapper.session.session_unit_of_work_decorator import SessionUnitOfWorkDecorator

from mathapp.sqlalchemy.base import Base

class ORMSession(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    revoked = Column(Boolean)
    created_at = Column(DateTime)

    def __init__(self, revoked, created_at):
        self.revoked = revoked
        self.created_at = created_at
        self._session = None

    @orm.reconstructor
    def init_on_load(self):
        self._session = None

    def get_model(self, unit_of_work):
        if self._session is not None:
            return self._session

        unit_of_work_decorator = SessionUnitOfWorkDecorator(unit_of_work = unit_of_work, orm_session = self)

        session = Session(revoked = self.revoked, created_at = self.created_at, unit_of_work = unit_of_work_decorator)
        session._id = self.id

        self._session = session
        return session

    def sync_id(self):
        self._session.id = self.id

    def sync_fields(self):
        self.revoked = self._session._revoked
        self.created_at = self._session._created_at

    def __repr__(self):
        return "<ORMSession ID(id='%s') CreatedAt(created_at='%s') Revoked(revoked='%s')>" % (self.id, self.created_at, self.revoked)
