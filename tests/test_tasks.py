from fastapi import status
import uuid
from datetime import datetime

from models import PriorityEnum


def test_home(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "a never ending midnight sun!"}


def test_get_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_get_tasks(client, sample_task):
    response = client.get("/tasks")
    assert response.status_code == status.HTTP_200_OK
    res_task = response.json()[0]
    assert isinstance(uuid.UUID(res_task["id"]), uuid.UUID)
    assert res_task["title"] == "Learn Testing"
    assert res_task["description"] == "Pytest & FastAPI + TestClient"
    assert res_task["priority"] == "medium"
    assert isinstance(datetime.fromisoformat(res_task["created_at"]), datetime)


def test_get_task_happy(client, sample_task):
    response = client.get(f"/tasks/{sample_task.id}")
    assert response.status_code == status.HTTP_200_OK
    res_task = response.json()
    assert isinstance(uuid.UUID(res_task["id"]), uuid.UUID)
    assert res_task["title"] == "Learn Testing"
    assert res_task["description"] == "Pytest & FastAPI + TestClient"
    assert res_task["priority"] == "medium"
    assert isinstance(datetime.fromisoformat(res_task["created_at"]), datetime)


def test_get_task_unhappy_1(client, sample_task):
    response = client.get(f"/tasks/{uuid.uuid4()}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Task not found"}


def test_get_task_unhappy_2(client):
    response = client.get(f"/tasks/randomstringnotuuid")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_post_task_happy(client):
    payload = {
        "title": "Go for a run",
        "description": None,
        "priority": "low"
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    res_task = response.json()
    assert res_task["title"] == "Go for a run"
    assert res_task["description"] == None
    assert res_task["priority"] == PriorityEnum.LOW
    assert res_task["is_completed"] == False


def test_post_unhappy(client):
    payload = {}
    response = client.post("/tasks", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_put_task(client, sample_task):
    payload = {
        "title": "Go for a run",
        "description": None,
        "priority": "low"
    }
    response = client.put(f"/tasks/{sample_task.id}", json=payload)
    assert response.status_code == status.HTTP_200_OK
    res_task = response.json()
    assert res_task["title"] == "Go for a run"
    assert res_task["description"] == None
    assert res_task["priority"] == PriorityEnum.LOW
    assert res_task["is_completed"] == False


def test_put_unhappy(client, sample_task):
    payload = {}
    response = client.put(f"/tasks/{sample_task.id}", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_patch_task(client, sample_task):
    payload = {
        "title": "Go for a run"
    }
    response = client.patch(f"/tasks/{sample_task.id}", json=payload)
    assert response.status_code == status.HTTP_200_OK
    res_task = response.json()
    assert res_task["title"] == "Go for a run"
    assert res_task["description"] == "Pytest & FastAPI + TestClient"
    assert res_task["priority"] == PriorityEnum.MEDIUM


def test_patch_unhappy(client, sample_task):
    payload = {}
    response = client.patch(f"/tasks/{sample_task.id}", json=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_delete_happy(client, sample_task):
    response = client.delete(f"/tasks/{sample_task.id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    get_response = client.get(f"/tasks/{sample_task.id}")
    assert get_response.status_code == status.HTTP_404_NOT_FOUND

    get_response = client.get("/tasks")
    assert get_response.json() == []


def test_delete_unhappy_1(client):
    response = client.delete(f"/tasks/{uuid.uuid4()}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_unhappy_2(client):
    response = client.delete("/tasks/randomstringnotuuid")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
