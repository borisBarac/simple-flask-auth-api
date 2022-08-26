# System imports
from pathlib import Path
import pytest
import logging
import sys
from random import randint

# APP imports
from api.app import app
from api.validate import validate_password

logging.basicConfig(level=logging.DEBUG)
my_logger = logging.getLogger()

_my_user = {
    'email': 'boris123@email.com',
    'password': 'password1234'
}

@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True
    yield app.test_client()  # tests run here

def test_login(client):
    response = client.post("/users/login", json = _my_user)
    res_data = response.json['data']
    
    assert res_data != None
    assert res_data['token'] != None
    assert response.status_code == 200

def test_get_user(client):
    response = client.post("/users/login", json = _my_user)
    token = response.json.get('data', {}).get('token', '')
    header = {
        'Authorization': token
    }

    response = client.get("/users/", headers = header)
    res_data = response.json['data']
    res_error = response.json.get('error', None)
    
    assert res_data != None
    assert res_error == None
    assert response.status_code == 200

def test_get_user_no_token(client):
    response = client.get("/users/")
    res_data = response.json['data']
    res_error = response.json['error']
    
    assert res_data == None
    assert res_error != None

def test_register_user(client):
    data = {
        'name': 'John Doe',
        'email':'testUser{}@email.com'.format(randint(0, sys.maxsize)),
        'password':'pass1232321'
    }

    response = client.post("/users/", json = data)
    message = response.json['message']

    assert response.status_code == 201
    assert message != None

def test_register_user_error(client):
    data = {
        'name': 'Boris',
        'email': 'email@email.com',
        'password': 'p'
    }

    response = client.post("/users/", json = data)
    message = response.json['message']

    assert 'Password is invalid' in message
    assert response.status_code == 401

def test_regex():
    res = validate_password("borSSSis123u2913")
    
    assert res == True

def test_index(client):
    response = client.get("/")
    
    assert response.status_code == 200