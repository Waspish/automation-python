import requests
import pytest

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


def test_get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert len(response.json()) == 100

@pytest.mark.skip(reason="Post aren't really added")
def test_get_one_post(new_post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{new_post_id}")
    assert response.status_code == 200
    assert len(response.json()) == 1

@pytest.mark.smoke
def test_create_post():
    headers = {
        "Content-Type": "application/json",
    }
    body = {
        "title": "test",
        "body": "test",
        "userId": 1
    }
    response = requests.post(
        headers=headers,
        json=body,
        url="https://jsonplaceholder.typicode.com/posts",
    ).json()
    assert response['title'] == body['title']
    assert response['body'] == body['body']
    assert response['userId'] == body['userId']

@pytest.mark.parametrize('login, password', [('admin1', 'test1'), ('admin2', 'test2')])
def test_login(login, password):
    print(f"testing login: {login}")
    print(f"testing password: {password}")