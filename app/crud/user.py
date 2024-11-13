from sqlalchemy.orm import Session
from models.user import DbUser
from schemas.user import UserCreateInput, UserCreateResponse


def create_user(db: Session, user: UserCreateInput):
    db_user = user.to_db_model()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
