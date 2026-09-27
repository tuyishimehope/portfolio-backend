from fastapi import APIRouter, status

from app.db.dependency import DBSession

from app.service.user.schema import UserCreate, UserRead
from app.service.user.service import create_user


AUTH_ROUTER = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])


@AUTH_ROUTER.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    payload: UserCreate,
    session: DBSession,
) -> UserRead:
    user = create_user(session, payload)
    return UserRead.model_validate(user)