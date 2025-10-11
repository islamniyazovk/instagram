from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=12)
    email: EmailStr

    name: str = Field(..., min_length=2, max_length=15)
    surname: str = Field(..., min_length=2, max_length=15)

    birth_date: Optional[date] = None
    password: str = Field(..., min_length=6, max_length=12)
