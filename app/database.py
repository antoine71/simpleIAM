from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine(settings.database_sdn)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    with Session(engine) as session:
        yield session
