from . import APIRouter, OAuth2PasswordRequestForm, Depends, AsyncSession, JSONResponse, HTTPException, status, \
    IntegrityError, traceback
from app.core.config.logger import logger
from app.core.constants import basic_prefix
from app.core.database import get_db
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserRegister
from app.utils.auth import create_access_token, verify_password, set_password


auth_router = APIRouter(
    prefix=f"{basic_prefix}/auth",
    tags=["auth"]
)


@auth_router.post("/get_token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)) -> JSONResponse:
    repos = UserRepository(db)
    user = await repos.get_by_username(form_data.username)

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

    print(create_data)
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
