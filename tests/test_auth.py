from conftest import client


def test_register() -> None:
    response = client.post('/api/auth/', json={'username': 'ramisram1s', 'password': 'password'})

    assert response.status_code == 200
    body = response.json()
    assert body['id'] == 1
    assert body['username'] == 'ramisram1s'


def test_login() -> None:
    response = client.post("/api/auth/login", json={'username': 'ramisram1s', 'password': 'password'})

    assert response.status_code == 200
    body = response.json()
    assert body['token_type'] == 'bearer'

    response = client.get('/api/auth/', headers={'Authorization': f'Bearer {body["access_token"]}'})

    assert response.status_code == 200
    assert response.json()['username'] == 'ramisram1s'


def test_info_about_user() -> None:
    user_data = {"username": "testuser", "password": "testpassword"}
    client.post("/api/auth/", json=user_data)
    login_response = client.post("/api/auth/login", json=user_data)
    access_token = login_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("/api/auth/", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]
