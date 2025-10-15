from uuid import uuid4

from fastapi.testclient import TestClient


def test_create_thread(client: TestClient) -> None:
    payload = {"title": "Test Thread", "description": "About tests", "owner": "alice"}

    response = client.post("/api/v1/threads/", json=payload)

    assert response.status_code == 200

    body = response.json()
    assert body["title"] == payload["title"]
    assert body["owner"] == payload["owner"]
    assert "id" in body


def test_create_thread_empty_title(client: TestClient) -> None:
    payload = {"title": "", "description": "About tests", "owner": "alice"}

    response = client.post("/api/v1/threads/", json=payload)

    assert response.status_code == 422


def test_search_threads(client: TestClient) -> None:
    first = client.post("/api/v1/threads/", json={"title": "FastAPI Tips", "description": "About tests", "owner": "bob"})
    second = client.post("/api/v1/threads/", json={"title": "Other topic", "description": "About tests", "owner": "carol"})

    assert first.status_code == 200
    assert second.status_code == 200

    response = client.get("/api/v1/threads/search", params={"q": "Fast"})

    assert response.status_code == 200

    threads = response.json()
    assert len(threads) >= 1


def test_search_threads_not_match(client: TestClient) -> None:
    created = client.post("/api/v1/threads/", json={"title": "Different topic", "description": "About tests", "owner": "alice"})

    assert created.status_code == 200

    response = client.get("/api/v1/threads/search", params={"q": "Nope"})

    assert response.status_code == 200
    assert response.json() == []


def test_search_threads_empty_query(client: TestClient) -> None:
    response = client.get("/api/v1/threads/search", params={"q": ""})

    assert response.status_code == 422


def test_search_threads_overlong_query(client: TestClient) -> None:
    response = client.get("/api/v1/threads/search", params={"q": "x" * 256})

    assert response.status_code == 422


def test_get_thread(client: TestClient) -> None:
    payload = {"title": "Test Thread", "description": "About tests", "owner": "alice"}
    created = client.post("/api/v1/threads/", json=payload)

    assert created.status_code == 200

    thread_id = created.json()["id"]

    response = client.get(f"/api/v1/threads/{thread_id}")

    assert response.status_code == 200

    body = response.json()
    assert body["id"] == thread_id
    assert body["title"] == payload["title"]
    assert body["owner"] == payload["owner"]


def test_get_thread_not_found(client: TestClient) -> None:
    missing_id = uuid4()

    response = client.get(f"/api/v1/threads/{missing_id}")

    assert response.status_code == 404
