import random

import requests


def get_all_posts():
    response = reques.tsget("https://jsonplaceholder.typicode.com/posts")
    print(response.json())


def create_post():
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
    )

    return response.json()['id']


def put_post():
    changed_title = "TEST2"
    post_id = create_post()
    headers = {
        "Content-Type": "application/json",
    }
    body = {
        "title": changed_title,
    }
    response = requests.patch(
        headers=headers,
        json=body,
        url=f"https://jsonplaceholder.typicode.com/posts/{post_id}",
    )
    assert response.status_code == 200
    assert response.json()['title'] == changed_title


get_all_posts()

put_post()

mas = [random.randint(1, 5) for _ in range(10)]
print(mas)
