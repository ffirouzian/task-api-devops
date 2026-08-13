from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_task():

    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Test Task"
    assert data["completed"] is False


def test_get_tasks():

    response = client.get("/tasks/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_get_task_not_found():

    response = client.get("/tasks/999999")

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Task not found"
