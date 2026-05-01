import pytest
import requests

@pytest.fixture()
def new_post_id():
    headers = {
        "Content-Type": "application/json",
    }
    body = {"title": "test","body": "test","userId": 1}
    response = requests.post(
        headers=headers,
        json=body,
        url="https://jsonplaceholder.typicode.com/posts",
    )
    print(f"created with status {response.status_code}")
    new_id = response.json()["id"]
    yield new_id
    delete_response = requests.delete(f"https://jsonplaceholder.typicode.com/posts{new_id}")
    print(f"deleted with status code {delete_response.status_code}")