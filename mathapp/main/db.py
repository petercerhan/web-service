from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

default_engine = create_engine('sqlite:///instance/mathapp.sqlite')
Session = scoped_session(sessionmaker(bind=default_engine, autoflush=False))

def override_session(path):
	engine = create_engine(path)
	global Session
	Session = scoped_session(sessionmaker(bind=engine, autoflush=False))
