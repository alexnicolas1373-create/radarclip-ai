from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_auth_register_and_login():
    register = client.post('/auth/register', json={'email': 'user@example.com', 'password': 'secret123', 'name': 'User'})
    assert register.status_code == 201
    login = client.post('/auth/login', data={'username': 'user@example.com', 'password': 'secret123'})
    assert login.status_code == 200
    assert 'access_token' in login.json()
