import pytest
from fastapi.testclient import TestClient
from main import app
from core.models import db_helper

test_objects = {
    "test_object1": ("text", "Вопрос1"),
    "test_object2": ("text", "Вопрос2"),
    "test_object3": ("text", "Ответ к вопросу1"),
    "test_object4": ("text", "Ответ к вопросу2"),
}


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as client:
        yield client
    db_helper.engine.sync_engine.dispose()
