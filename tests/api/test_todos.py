import allure
import pytest

from data.api_payloads import POST_PAYLOADS, RESOURCE_SCHEMAS
from utils.assertions import assert_list_response, assert_object_response, assert_required_keys, assert_status_code


@allure.epic("API")
@allure.feature("Todos")
@pytest.mark.api
@allure.title("GET /todos возвращает список задач")
def test_get_todos_returns_list(api_client):
    response = api_client.get_collection("todos")

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_list_response(payload)
    assert_required_keys(payload[0], RESOURCE_SCHEMAS["todos"]["required_keys"])


@allure.epic("API")
@allure.feature("Todos")
@pytest.mark.api
@allure.title("GET /todos/1 возвращает задачу по id")
def test_get_todo_by_id_returns_todo(api_client):
    response = api_client.get_by_id("todos", 1)

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_object_response(payload)
    assert payload["id"] == 1
    assert_required_keys(payload, RESOURCE_SCHEMAS["todos"]["required_keys"])


@allure.epic("API")
@allure.feature("Todos")
@pytest.mark.api
@allure.title("GET /todos/0 возвращает пустой объект")
def test_get_missing_todo_returns_empty_object(api_client):
    response = api_client.get_by_id("todos", 0)

    assert_status_code(response.status_code, 404)
    assert response.json() == {}


@allure.epic("API")
@allure.feature("Todos")
@pytest.mark.api
@allure.title("POST /todos создает задачу")
def test_create_todo(api_client):
    response = api_client.create("todos", POST_PAYLOADS["todos"])

    assert_status_code(response.status_code, 201)
    payload = response.json()
    assert payload["title"] == POST_PAYLOADS["todos"]["title"]
    assert "id" in payload
