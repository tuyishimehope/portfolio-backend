from fastapi import FastAPI

from app.api.v1.auth.router import AUTH_ROUTER
from app.core.settings import settings


def create_app() -> FastAPI:
    application = FastAPI(title=settings.APP_NAME)
    application.include_router(AUTH_ROUTER)

    @application.get("/health/ready", tags=["Health"])
    def readiness() -> dict[str, str]:
        return {"status": "ready"}

    return application


app = create_app()