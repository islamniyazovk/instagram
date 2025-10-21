from . import Column, DateTime, func, Integer, String, Boolean, relationship, Base, ForeignKey


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(1000))

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts", lazy="selectin")

    pictures = relationship("Picture", back_populates="post", cascade="all, delete-orphan", lazy="selectin")

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    is_active = Column(Boolean, default=True)

