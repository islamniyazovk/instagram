from . import Base, Column, Integer, String, ForeignKey, relationship


class Picture(Base):
    __tablename__ = "pictures"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(256), unique=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="picture", lazy="selectin")

    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    post = relationship("Post", back_populates="picture", lazy="selectin")
