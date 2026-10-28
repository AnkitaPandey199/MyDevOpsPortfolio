import pytest

from app import main


@pytest.fixture
def client():
    main.notes.clear()
    main.next_id = 1
    main.app.config["TESTING"] = True
    return main.app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_create_and_get_note(client):
    r = client.post("/notes", json={"text": "hello"})
    assert r.status_code == 201
    note_id = r.get_json()["id"]
    r = client.get(f"/notes/{note_id}")
    assert r.status_code == 200
    assert r.get_json()["text"] == "hello"


def test_create_note_requires_text(client):
    r = client.post("/notes", json={})
    assert r.status_code == 400


def test_delete_note(client):
    note_id = client.post("/notes", json={"text": "x"}).get_json()["id"]
    assert client.delete(f"/notes/{note_id}").status_code == 204
    assert client.get(f"/notes/{note_id}").status_code == 404
