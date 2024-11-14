from core.jwt import encode_access_token
from core.passwords import validate_password
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas.user import (
    UserCreateInput,
    UserCreateResponse,
    UserLoginInput,
    UserLoginResponse,
)
from service.user import create_user, get_user_by_email
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/register")
def register_user(
    user: UserCreateInput,
    response_model=UserCreateResponse,
    db: Session = Depends(get_db),
):
    create_user(db, user)
    return user


@router.post("/login")
def login_user(
    user: UserLoginInput,
    response_model=UserLoginResponse,
    db: Session = Depends(get_db),
):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not validate_password(user.password, db_user.hashed_password):
        raise HTTPException(401, "Invalid username or password")

    return encode_access_token(str(db_user.id))
