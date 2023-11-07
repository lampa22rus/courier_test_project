from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

Base = declarative_base()

load_dotenv()

# postgresql

# SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://courier:courier@localhost/courier'
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_CONNECTION = os.getenv("DB_CONNECTION")

SQLALCHEMY_DATABASE_URL = f'{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_DATABASE}'



engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def session_dependency():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

