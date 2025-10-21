from pydantic import BaseModel


class PostCreateRequest(BaseModel):
    text: str
    pictures: list[str]


class PostChangeRequest(BaseModel):
    id: int
    pictures: list


class PostDeleteRequest(BaseModel):
    id: int
