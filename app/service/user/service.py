from fastapi import HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.user import User
from app.service.user.schema import UserCreate


password_hasher = PasswordHash.recommended()


def create_user(session: Session, data: UserCreate) -> User:
    normalized_email = str(data.email_address).strip().lower()

    existing_user = session.scalar(
        select(User).where(User.email == normalized_email)
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists",
        )

    user = User(
        name=data.name,
        email_address=normalized_email,
        password_hash=password_hasher.hash(data.password),
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user