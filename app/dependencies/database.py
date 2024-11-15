from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine(settings.database_sdn)


def get_db():
    with Session(engine) as session:
        yield session
