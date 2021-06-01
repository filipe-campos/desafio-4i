from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    full_name: Optional[str] = None
    birthday: Optional[str] = None
    cep: Optional[str] = None
    street: Optional[str] = None
    neighborhood: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None

# Properties to receive via API on Login
class UserLogin(UserBase):
    cpf: str
    password: str


# Properties to receive via API on creation
class UserCreate(UserBase):
    cpf: str
    password: str
    full_name: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
