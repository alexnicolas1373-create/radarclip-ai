from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_start_process():
    response = client.post('/process')
    assert response.status_code == 200
    assert response.json() == {"status": "queued"}
