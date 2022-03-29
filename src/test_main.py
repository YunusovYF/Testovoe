# Сюда написать тесты
from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_post_create_city():
    response = client.post('/citi')
    assert response.status_code == 404


def test_get_all_users():
    response = client.get('/users')
    assert response.status_code == 200


def test_post_register_user():
    response = client.post(
        '/users',
        json={
            "name": "Alex",
            "surname": "Alexov",
            "age": 64
        }
    )

    assert response.status_code == 200
