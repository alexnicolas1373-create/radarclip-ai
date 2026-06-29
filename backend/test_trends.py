from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_trends():
    response = client.get('/trends')
    assert response.status_code == 200
    assert response.json() == {"trends": []}
