from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    content: str

class Blog(BlogCreate):
    id: int

    class Config:
        orm_mode = True
