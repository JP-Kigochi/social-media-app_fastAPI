from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

#UserCreate schema definition
class UserCreate(BaseModel):
    email: EmailStr
    password: str

#UserResponse schema definition
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

#UserResponse schema definition
class UserLogin(BaseModel):
    email: EmailStr
    password: str


#PostBase schema definition
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

#PostCreate schema definition (inherits from PostBase)
class PostCreate(PostBase):
    pass

#Post schema definition (inherits from PostBase)
class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    owner: UserResponse
    class Config:
        orm_mode = True

#PostOut schema definition
class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True


#Vote schema definition
class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1, strict=True)


#Token schema definition
class Token(BaseModel):
    access_token: str
    token_type: str

#Token schema definition
class TokenData(BaseModel):
    id: Optional[str] = None