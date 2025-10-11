import traceback
from typing import Any, Coroutine

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.core.config.logger import logger
from app.core.database import get_db
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserRegister
from app.utils.auth import create_access_token, verify_password, set_password
from app.api.routers import auth_router


@auth_router.post("/get_token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)) -> JSONResponse:
    repos = UserRepository(db)
    # form_data.username - это номер, не username. я не хочу трогать базовый класс
    user = await repos.get_by_number(form_data.username)

    if user:
        hashed_password = user.hashed_password

        if not verify_password(form_data.password, hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect credentials")

        access_token = create_access_token({"sub": user.id})
        return JSONResponse({"access_token": access_token, "token_type": "bearer"}, status_code=status.HTTP_200_OK)

    raise HTTPException(status_code=401, detail="Incorrect credentials")


@auth_router.post("/register")
async def register(login_data: UserRegister, db: AsyncSession = Depends(get_db)) -> JSONResponse:
    create_data = login_data.dict()
    create_data["hashed_password"] = set_password(login_data.password)
    create_data.pop("password", None)

    user = User(**create_data)

    try:
        repos = UserRepository(db)
        await repos.create(user)

        token = create_access_token({"sub": user.id})

        return JSONResponse(
            {"success": True, "token": token, "token_type": "bearer"},
            status_code=status.HTTP_201_CREATED
        )
    except IntegrityError:
        return JSONResponse(
            {"success": False, "detail": "Такой пользователь уже существует"},
            status_code=status.HTTP_409_CONFLICT
        )
    except Exception as e:
        logger.error(f"{e}: {traceback.format_exc()}")

        return JSONResponse(
            {"success": False, "detail": "Неизвестная ошибка"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


