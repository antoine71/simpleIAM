from models.user import DbUser
from schemas.user import UserCreateInput
from sqlalchemy.orm import Session, select


def create_user(session: Session, user: UserCreateInput):
    db_user = user.to_db_model()
    session.add(db_user)
    session.commit()
    return db_user.id


def get_user_by_email(session: Session, email: str) -> DbUser | None:
    statement = select(DbUser).where(DbUser.email == email)
    result = session.scalar(statement).first()
    return result
