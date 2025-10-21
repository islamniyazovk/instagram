from app.core.database import get_db
from starlette.responses import JSONResponse
import traceback
from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.core.constants import basic_prefix
from fastapi.security import OAuth2PasswordRequestForm
