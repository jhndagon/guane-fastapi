from starlette.testclient import TestClient
import json

from app.main import app

cliente = TestClient(app)


def test_create_dog():
    response = cliente.post("/api/dogs/john")
    assert response.status_code == 201
    assert 'is_adopted' in response.json()


def test_update_dog():
    json_data = json.JSONEncoder().encode({'is_adopted': True})
    response = cliente.put("/api/dogs/john", data=json_data)
    assert response.status_code == 200
    assert 'is_adopted' in response.json()


def test_read_dog():
    response = cliente.get("/api/dogs/john")
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['is_adopted'] == True


def test_delete_dog():
    response = cliente.delete("/api/dogs/john")
    assert response.status_code == 200
    assert 'is_adopted' in response.json()