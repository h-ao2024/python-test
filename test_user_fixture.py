import requests
import pytest
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"
@pytest.fixture
def user_id():
    return 1
def test_get_user(base_url,user_id):
    url=f"{base_url}/users/{user_id}"
    response=requests.get(url)
    assert response.status_code==200
    assert response.json()["id"]==user_id
