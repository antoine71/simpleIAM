def test_register_user(client):
    response = client.post(
        "/users/register", json={"email": "user@example.com", "password": "password"}
    )
    assert response.status_code == 200

    response = client.post(
        "/users/register", json={"email": "user@example.com", "password": "password"}
    )
    assert response.status_code == 400


def test_login_user(client):

    response = client.post(
        "/users/login", json={"email": "user@example.com", "password": "password"}
    )
    assert response.status_code == 200

    response = client.post(
        "/users/login", json={"email": "user@example.com", "password": "foo"}
    )
    assert response.status_code == 401
