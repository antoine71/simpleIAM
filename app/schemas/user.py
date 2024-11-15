from core.passwords import hash_password
from models.user import DbUser
from pydantic import BaseModel, EmailStr


class UserCreateInput(BaseModel):
    email: EmailStr
    password: str

    def to_db_model(self):
        return DbUser(email=self.email, hashed_password=hash_password(self.password))


class UserCreateResponse(BaseModel):
    email: EmailStr


class UserLoginInput(BaseModel):
    email: EmailStr
    password: str


class UserLoginResponse(BaseModel):
    access_token: str
