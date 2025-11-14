from .confest import test_objects, client
from fastapi.testclient import TestClient


def create_question_with_answer(client: TestClient):
    response = client.post(
        "/api/v1/questions",
        json={test_objects["test_object1"][0]: test_objects["test_object1"][1]},
    )

    question_id = response.json().get("id")

    response = client.post(
        f"/api/v1/answers/question/{question_id}",
        json={test_objects["test_object3"][0]: test_objects["test_object3"][1]},
    )

    return response, question_id


def test_create_answer(client):

    response_data, question_id = create_question_with_answer(client=client)
    client.delete(f"/api/v1/questions/{question_id}")

    assert response_data.status_code == 201
    assert response_data.json().get("text")
    assert response_data.json().get("id")
    assert response_data.json().get("created_at")
    assert response_data.json().get("user_id")
    assert response_data.json().get("question_id")
    assert response_data.json().get("text") == test_objects["test_object3"][1]


def test_get_answer_by_id(client):
    response_data, question_id = create_question_with_answer(client=client)
    response = client.get(f"/api/v1/answers/{response_data.json().get("id")}")
    response_data = response_data.json()
    client.delete(f"/api/v1/questions/{question_id}")

    assert response.status_code == 200
    assert response_data.get("text")
    assert response_data.get("id")
    assert response_data.get("created_at")
    assert response_data.get("user_id")
    assert response_data.get("question_id")


def test_delete_answer(client):
    response_data, question_id = create_question_with_answer(client=client)

    response = client.delete(f"/api/v1/answers/{response_data.json().get("id")}")
    client.delete(f"/api/v1/questions/{question_id}")

    response_data = response.json()

    assert response.status_code == 200
    assert response_data.get("text")
    assert response_data.get("id")
    assert response_data.get("created_at")
    assert response_data.get("user_id")
    assert response_data.get("question_id")
