from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///instance/mathapp.sqlite')

Session = scoped_session(sessionmaker(bind=engine))
