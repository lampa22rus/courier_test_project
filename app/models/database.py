from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,async_scoped_session,AsyncSession
from asyncio import current_task
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv


Base = declarative_base()
load_dotenv()

SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://courier:courier@localhost/courier'
# SQLALCHEMY_DATABASE_URL = os.getenv("FASTAPI_DB_URL")

engine = create_async_engine(SQLALCHEMY_DATABASE_URL,echo=True)

async_session_factory = async_sessionmaker(autocommit=False, autoflush=False, bind=engine,class_=AsyncSession)

async def session_dependency():
    session = async_scoped_session(session_factory=async_session_factory, scopefunc=current_task)
    try:
        yield session
    finally:
        await session.close()
