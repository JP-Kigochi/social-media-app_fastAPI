from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from .config import settings
 
 #'postgresql://<username>:<password>@<ip-address/hostname>/<databasename>'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)


sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)


Base = declarative_base()


#dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()