from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from collections.abc import Generator

from app.db.engine import SessionLocal, get_db_session


DBSession = Annotated[Session, Depends(get_db_session)]


def get_db_session() -> Generator[Session, None, None]:
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()