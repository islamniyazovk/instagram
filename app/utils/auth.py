from datetime import timedelta, datetime
from typing import Optional

from fastapi import HTTPException, status, Depends
from jose import jwt, JWTError

from app.core.config.settings import settings
from app.core.constants import oauth2_scheme, pwd_context


def create_access_token(data: dict, expires_in_minutes: Optional[int] = 15) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + (timedelta(minutes=expires_in_minutes))
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_token(token: str) -> int:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        sub = payload.get("sub")
        if sub is None:
            raise JWTError("Verify token error")

        return int(sub)

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = verify_token(token)
    user_id = payload.get("sub")

    return {"id": user_id}


def set_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)
