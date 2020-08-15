from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String
from sqlalchemy import orm

Base = declarative_base()

class ORMUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
    	self.username = username
    	self.password = password
    	self._user = None

    @orm.reconstructor
    def init_on_load(self):
    	self._user = None
        
    # Return the orm-independent model
    def get_model(self, unit_of_work):
        pass

    # Copy id field from orm_model to orm-independent model
    def sync_id(self):
        pass

    # Copy orm-independent model fields into orm_model
    def sync_fields(self):
        pass
    
    def __repr__(self):
        return "<ID(id='%s') User(username='%s') Password(password='%s')>" % (self.id, self.username, self.password)
