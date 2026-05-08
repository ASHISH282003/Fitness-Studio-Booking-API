from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
    "message": "Fitness Booking API Running"
}


def test_register_user():
    response = client.post(
        "/signup",
        json={
            "name": "Ashish",
            "email": "ashish_test@gmail.com",
            "password": "password123"
        }
    )

    assert response.status_code in [200, 400]


def test_login_user():
    response = client.post(
        "/login",
        data={
            "username": "ashish_test@gmail.com",
            "password": "password123"
        }
    )

    assert response.status_code in [200, 401]


def test_get_classes():
    response = client.get("/classes")

    assert response.status_code == 200