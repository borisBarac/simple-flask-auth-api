import json
from pathlib import Path
import pytest

from api.app import app

@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True
    yield app.test_client()  # tests run here

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200