from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from fastapi import HTTPException, status
from typing import Optional

class PostBase(BaseModel):
    title: str
    konten: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @validator("email", "password")
    def check_is_empty(cls, value):
        if value == None:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                details=f"Field is required, can't be empty")
        return value

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TOkenData(BaseModel):
    id: Optional[str] = None