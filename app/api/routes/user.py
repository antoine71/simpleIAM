from fastapi import APIRouter, Depends
from database import get_db
from crud.user import create_user
from schemas.user import UserCreateInput, UserCreateResponse, UserLoginInput
from sqlalchemy.orm import Session
from core.security import hash_password

router = APIRouter()


@router.post("/register")
async def register_user(user: UserCreateInput, db: Session = Depends(get_db)):
    create_user(db, user)
    return UserCreateResponse(email=user.email)
