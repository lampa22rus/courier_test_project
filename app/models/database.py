from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,async_scoped_session,AsyncSession
from asyncio import current_task
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

SQLALCHEMY_DATABASE_URL = f'{DB_CONNECTION}+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@postgres:5432/{DB_DATABASE}'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_session_factory = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def session_dependency():
    session = async_scoped_session(session_factory=async_session_factory, scopefunc=current_task)
    try:
        yield session
    finally:
        await session.close()
