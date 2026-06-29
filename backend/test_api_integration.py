from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_and_trends_endpoints():
    health = client.get('/health')
    trends = client.get('/trends')

    assert health.status_code == 200
    assert health.json() == {"status": "ok"}
    assert trends.status_code == 200
    assert trends.json() == {"trends": []}
