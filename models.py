from sqlalchemy import create_engine, Column, Integer, String, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's sqlite database file
engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Create a base class for our classes definitions
Base = declarative_base()

class Scores(Base):
    __tablename__='pf_Scores'

    id = Column(Integer, primary_key=True)
    score = Column(Integer)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()