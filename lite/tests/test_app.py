from starlette.testclient import TestClient
from lite.app import app
from unittest.mock import patch
import pytest
from lite.main import print_all_models


@pytest.mark.django_db
def test_app():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    result = response.json()
    assert result == {"hello": "world", "alls": []}


@pytest.mark.django_db
def test_post():
    client = TestClient(app)
    response = client.post("/create", json={"name": "Shola"})
    assert response.status_code == 201
    assert response.json() == {"status": "Record Created"}
    assert print_all_models().count() == 1