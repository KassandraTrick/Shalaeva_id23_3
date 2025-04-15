# app/schemas/user.py

from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    name: str

    class Config:
        from_attributes = True
        from_attributes = True # Add from_attributes

class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int
