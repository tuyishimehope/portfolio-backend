from fastapi import APIRouter, HTTPException, status

from app.db.dependency import DBSession
from app.service.user.schema import UserCreate, UserLogin, UserRead
from app.service.user.service import authenticate_user, create_user

AUTH_ROUTER = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])


# @AUTH_ROUTER.post(
#     "/register",
#     response_model=UserRead,
#     status_code=status.HTTP_201_CREATED,
# )
def register_user(
    payload: UserCreate,
    session: DBSession,
) -> UserRead:
    user = create_user(session, payload)
    return UserRead.model_validate(user)

@AUTH_ROUTER.post("/login", response_model=UserRead)
def login_user(payload: UserLogin, session: DBSession) -> UserRead:
    user = authenticate_user(session, payload)
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid email or password")
    return UserRead.model_validate(user)
