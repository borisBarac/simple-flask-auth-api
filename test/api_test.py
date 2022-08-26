import json
from pathlib import Path
import pytest

from api.app import app
from api.validate import validate_password

@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True
    yield app.test_client()  # tests run here

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_register_user(client):
    data = {
        'name': 'Boris',
        'email':'email@email.com',
        'password':'password1232321'
    }

    response = client.post("/users/", json = data)

    message = response.json['message']
    assert 'Password is invalid' in message
    assert response.status_code == 401

def test_regex():
    res = validate_password("borSSSis123u2913")
    assert res, True
