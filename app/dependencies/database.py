from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


engine = create_engine(settings.postgres_sdn)


def get_db():
    with Session(engine) as session:
        yield session
