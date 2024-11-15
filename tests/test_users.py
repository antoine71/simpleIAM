def test_register_user(client):
    response = client.post(
        "/users/register", json={"email": "user@example.com", "password": "password"}
    )
    assert response.status_code == 200
