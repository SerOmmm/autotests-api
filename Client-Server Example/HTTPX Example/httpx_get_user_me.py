import httpx
host_url = "http://localhost:8000"
payload = {
  "email": "test@user.com",
  "password": "123456"
}

jwt_request = httpx.post(f"{host_url}/api/v1/authentication/login", json=payload)
jwt_request_body = jwt_request.json()
print("Bearer Token status code:", jwt_request.status_code)

headers = {"Authorization": f'Bearer {jwt_request_body["token"]["accessToken"]}'}
get_request = httpx.get(f"{host_url}/api/v1/users/me", headers=headers)
print("Get status code:", get_request.status_code)
print("Get body", get_request.json())
