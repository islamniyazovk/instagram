from fastapi import FastAPI

from app.api.routes.auth import auth_router
from app.api.routes.posts import posts_router
from app.core.config.settings import settings

app = FastAPI()
app.include_router(auth_router)
app.include_router(posts_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        port=settings.APP_PORT,
        host=settings.APP_HOST,
        reload=settings.DEBUG
    )
