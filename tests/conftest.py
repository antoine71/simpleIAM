import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "app"))


from sqlalchemy.orm import Session
from routers.user import get_db
from sqlalchemy import create_engine
from alembic import command
from alembic.config import Config

import pytest
from fastapi.testclient import TestClient


from main import app


def create_test_db():
    db_file = Path(__file__).parent / "test.db"
    if db_file.exists():
        db_file.unlink()
    engine = create_engine(f"sqlite:///{db_file}")
    return engine


def setup_test_db(engine):
    migrations_path = Path(__file__).parent.parent / "migrations"
    config = Config(str(migrations_path / "alembic.ini"))
    config.set_main_option("script_location", str(migrations_path / "alembic"))
    config.set_main_option("sqlalchemy.url", str(engine.url))
    command.upgrade(config, "head")


engine = create_test_db()
setup_test_db(engine)


def get_test_db():
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_db] = get_test_db


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
