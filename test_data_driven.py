import pytest
import requests
from test_data import user_ids
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"
@pytest.mark.parametrize("user_id",user_ids)
def test_get_user(base_url,user_id):
    url=f"{base_url}/posts/{user_id}"
    response=requests.get(url)
    assert response.status_code==200
    assert response.json()["id"]==user_id