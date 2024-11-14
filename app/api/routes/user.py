from core.jwt import encode_access_token
from core.security import validate_password
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas.user import UserCreateInput, UserCreateResponse, UserLoginInput
from service.user import create_user, get_user_by_email
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/register")
async def register_user(user: UserCreateInput, db: Session = Depends(get_db)):
    create_user(db, user)
    return UserCreateResponse(email=user.email)


@router.post("/login")
async def login_user(user: UserLoginInput, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not validate_password(user.password, db_user.pass_hash):
        raise HTTPException(401, "Invalid username or password")

    return encode_access_token(db_user.id)
