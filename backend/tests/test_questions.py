from .confest import test_objects, client
from fastapi.testclient import TestClient


def create_question(client: TestClient):
    return client.post(
        "/api/v1/questions",
        json={test_objects["test_object1"][0]: test_objects["test_object1"][1]},
    )


def test_get_all_questions(client):
    ids = []
    response = create_question(client=client)
    ids.append(response.json()["id"])

    response = client.post(
        "/api/v1/questions",
        json={test_objects["test_object2"][0]: test_objects["test_object2"][1]},
    )
    ids.append(response.json()["id"])

    response = client.get("/api/v1/questions")

    for index in ids:
        client.delete(f"/api/v1/questions/{index}")

    assert response.status_code == 200
    assert response.json() != []


def test_create_question(client):
    response = create_question(client=client)
    response_data = response.json()

    question_id = response_data.get("id")
    client.delete(f"/api/v1/questions/{question_id}")

    assert response.status_code == 201
    assert response_data.get("text")
    assert response_data.get("id")
    assert response_data.get("created_at")
    assert response_data.get("text") == test_objects["test_object1"][1]


def test_get_question_by_id(client):
    response = create_question(client=client)
    response_data: dict = response.json()

    question_id = response_data.get("id")

    client.post(
        f"/api/v1/answers/question/{question_id}",
        json={test_objects["test_object3"][0]: test_objects["test_object3"][1]},
    )
    client.post(
        f"/api/v1/answers/question/{question_id}",
        json={test_objects["test_object4"][0]: test_objects["test_object4"][1]},
    )
    response = client.get(
        f"/api/v1/questions/{question_id}",
    )
    response_data = response.json()

    client.delete(f"/api/v1/questions/{question_id}")

    assert response.status_code == 200
    assert response_data.get("id")
    assert response_data.get("text")
    assert response_data.get("created_at")
    assert response_data.get("answers")


def test_delete_question_by_id(client):
    response = create_question(client=client)
    response_data: dict = response.json()

    question_id = response_data.get("id")

    response = client.delete(f"/api/v1/questions/{question_id}")

    assert response.status_code == 200
    assert response_data.get("id")
    assert response_data.get("text")
    assert response_data.get("created_at")
