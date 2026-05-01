import time

import requests
import pytest


def test_get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert len(response.json()) == 100

def test_get_one_post(new_post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{new_post_id}")
    print("Work of test_get_one_post is in test")
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

@pytest.mark.parametrize('login, password', [('admin1', 'test1'), ('admin2', 'test2'), ('admin3', 'test3')])
def test_login(login, password):
    print(f"testing login: {login}")
    print(f"testing password: {password}")