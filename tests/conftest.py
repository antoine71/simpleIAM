import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "app"))


from sqlalchemy.orm import Session
from app.routers.user import get_db
from app.models.base import Base
from sqlalchemy import create_engine, inspect

import pytest
from fastapi.testclient import TestClient


from app.main import app

db_file = Path("test.db")
if db_file.exists():
    db_file.unlink()

engine = create_engine(f"sqlite:///{db_file}")
Base.metadata.create_all(bind=engine)


def get_test_db():
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_db] = get_test_db


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
