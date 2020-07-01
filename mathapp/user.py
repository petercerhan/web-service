from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    
    def __repr__(self):
        return "<ID(id='%s') User(username='%s') Password(password='%s')>" % (self.id, self.username, self.password)
