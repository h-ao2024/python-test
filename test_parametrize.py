import pytest
import requests
@pytest.mark.parametrize("post_id",[1,2,3,99,100])
def test_get_single_post(post_id):
    url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response=requests.get(url)
    assert response.status_code==200
    data=response.json()
    assert data["id"]==post_id