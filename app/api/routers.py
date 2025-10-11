from fastapi import APIRouter

from app.core.constants import basic_prefix

auth_router = APIRouter(
    prefix=f"{basic_prefix}/auth",
    tags=["auth"]
)
