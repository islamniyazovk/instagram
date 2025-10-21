from sqlalchemy.orm import relationship

from . import Column, Integer, Base, String, func, DateTime, Boolean


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, index=True, nullable=False)
    number = Column(String(20), unique=True)
    email = Column(String(30), unique=True, index=True, nullable=False)

    name = Column(String(20), nullable=False)

    hashed_password = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    is_active = Column(Boolean, default=True)

    posts = relationship("Post", back_populates="user")
