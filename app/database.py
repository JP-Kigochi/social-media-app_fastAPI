from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
 

 #Initialising the Database URL
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

#Creating the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Creating the local database session
sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)

#Creating the Base
Base = declarative_base()

#Database dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()