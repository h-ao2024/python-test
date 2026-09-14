import pytest
import requests

@pytest.fixture
def base_url():
    return "https://httpbin.org"

@pytest.mark.parametrize("username, password", [
    ("admin", "123456"),
    ("admin", "wrong"),
    ("", "123456")
])
def test_login(base_url, username, password):
    url = f"{base_url}/post"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["json"]["username"] == username
    assert json_data["json"]["password"] == password