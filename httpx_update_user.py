import httpx

from tools.fakers import get_random_email


create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

with httpx.Client(base_url="http://localhost:8000") as client:
    create_user_response = client.post(
        url="/api/v1/users",
        json=create_user_payload
    )
    create_user_response_data = create_user_response.json()
    user_id = create_user_response_data["user"]["id"]
    print(create_user_response_data)
    print(f"Create status code: {create_user_response.status_code}\n")

    login_payload = {
        "email": create_user_payload['email'],
        "password": create_user_payload['password']
    }

    login_response = client.post(
        url="/api/v1/authentication/login",
        json=login_payload
    )

    login_response_data = login_response.json()
    access_token = login_response_data["token"]["accessToken"]
    print(login_response_data)
    print(f"Login status code: {login_response.status_code}\n")

    update_user_payload = {
        "email": get_random_email(),
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }

    update_user_response = client.patch(
        url=f"/api/v1/users/{user_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json=update_user_payload
    )
    print(update_user_response.json())
    print(f"Update user status code: {update_user_response.status_code}\n")





