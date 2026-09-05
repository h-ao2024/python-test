import pytest
import requests
@pytest.fixture
def base_url():
    "返回基础url"
    return "https://jsonplaceholder.typicode.com"
@pytest.fixture
def posts_response(base_url):
    url=f"{base_url}/posts"
    return requests.get(url)
def test_posts_status(posts_response):
    assert posts_response.status_code==200
def test_get_posts(base_url):
    url=f"{base_url}/posts"
    response=requests.get(url)
    assert response.status_code==200