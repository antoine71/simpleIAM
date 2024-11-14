import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "app"))

import pytest
from fastapi.testclient import TestClient



from app.main import app

@pytest.fixture(scope="session")
def client():
    return TestClient(app)
