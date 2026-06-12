import httpx


login_payload = {
    "email": "user@example.com",
    "password": "123"
}

with httpx.Client(base_url="http://localhost:8000") as client:
    login_response = client.post(
        url="/api/v1/authentication/login",
        json=login_payload
    )

    print(login_response.json())
    print(f"Login status code: {login_response.status_code}\n")

    access_token = login_response.json()["token"]["accessToken"]

    user_response = client.get(
        "/api/v1/users/me",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    print(user_response.json())
    print(f"User get status code: {user_response.status_code}")




