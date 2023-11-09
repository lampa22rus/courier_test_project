from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

Base = declarative_base()

load_dotenv()

# SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://courier:courier@localhost/courier'

SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONNECTION")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def session_dependency():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()