from sqlalchemy import Column, Integer, String, Date, Boolean

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, index=True, nullable=False)
    number = Column(String(20), unique=True)
    email = Column(String(30), unique=True, index=True, nullable=False)

    name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=False)

    birth_date = Column(Date)
    hashed_password = Column(String)

    is_active = Column(Boolean, default=True)
