from sqlalchemy import text
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.settings import settings


engine = create_engine(url=settings.DATABASE_URL, echo=True)


SessionLocal = sessionmaker(
    bind=engine, 
    class_=Session, 
    autoflush=False, 
    expire_on_commit=False)


def get_db_session():
    with SessionLocal.begin() as session:
        yield session
