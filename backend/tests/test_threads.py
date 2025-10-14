from fastapi.testclient import TestClient


def _create_thread(client: TestClient, *, title: str = "Test Thread", description: str | None = "About tests", owner: str = "alice") -> dict:
    response = client.post(
        "/api/v1/threads/",
        json={"title": title, "description": description, "owner": owner},
    )
    assert response.status_code == 200
    return response.json()


def test_create_and_get_thread(client: TestClient) -> None:
    thread = _create_thread(client)

    response = client.get(f"/api/v1/threads/{thread['id']}")
    assert response.status_code == 200

    body = response.json()
    assert body["id"] == thread["id"]
    assert body["title"] == thread["title"]
    assert body["owner"] == "alice"


def test_search_threads(client: TestClient) -> None:
    matching_thread = _create_thread(client, title="FastAPI Tips", owner="bob")
    _create_thread(client, title="Other topic", owner="carol")

    response = client.get("/api/v1/threads/search", params={"q": "Fast"})
    assert response.status_code == 200

    threads = response.json()
    assert len(threads) == 1
    assert threads[0]["id"] == matching_thread["id"]


def test_search_threads_returns_empty_list_when_no_matches(client: TestClient) -> None:
    _create_thread(client, title="Different topic")

    response = client.get("/api/v1/threads/search", params={"q": "Nope"})
    assert response.status_code == 200
    assert response.json() == []


def test_search_threads_rejects_empty_query(client: TestClient) -> None:
    response = client.get("/api/v1/threads/search", params={"q": ""})
    assert response.status_code == 422


def test_search_threads_rejects_overlong_query(client: TestClient) -> None:
    response = client.get("/api/v1/threads/search", params={"q": "x" * 256})
    assert response.status_code == 422


def test_create_post_and_list_posts(client: TestClient) -> None:
    thread = _create_thread(client)

    post_response = client.post(
        f"/api/v1/threads/{thread['id']}/posts/",
        json={"content": "Hello world", "author": "dave"},
    )
    assert post_response.status_code == 200
    post = post_response.json()
    assert post["thread_id"] == thread["id"]
    assert post["content"] == "Hello world"

    list_response = client.get(f"/api/v1/threads/{thread['id']}/posts/")
    assert list_response.status_code == 200
    posts = list_response.json()
    assert len(posts) == 1
    assert posts[0]["id"] == post["id"]
    assert posts[0]["author"] == "dave"
