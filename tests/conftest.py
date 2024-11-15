import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "app"))


from alembic.config import Config
from alembic import command
from sqlalchemy.orm import Session
from app.routers.user import get_db
from app.models.user import Base
from sqlalchemy import create_engine, inspect

import pytest
from fastapi.testclient import TestClient


from app.main import app


engine = create_engine("sqlite:///:memory:")


def get_test_db():
    with Session(engine) as session:
        Base.metadata.create_all(bind=engine)
        yield session


app.dependency_overrides[get_db] = get_test_db


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
