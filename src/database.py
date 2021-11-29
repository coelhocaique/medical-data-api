from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_URL = os.getenv('IP_ADDRESS') if os.getenv('IP_ADDRESS') is not None else 'localhost'

SQLALCHEMY_DATABASE_URL = "postgresql://medical-data:medical-data@%s:5432/medical-data" % DB_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_connection():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
