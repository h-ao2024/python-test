import pytest
import requests
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"
@pytest.mark.parametrize("post_id",[1,2,3,99,100])
def test_get_posts(base_url,post_id):
    url=f"{base_url}/posts/{post_id}"
    response = requests.get(url)
    assert response.status_code==200

