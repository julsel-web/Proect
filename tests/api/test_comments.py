import allure
import pytest

from data.api_payloads import POST_PAYLOADS, RESOURCE_SCHEMAS
from utils.assertions import assert_list_response, assert_object_response, assert_required_keys, assert_status_code


@allure.epic("API")
@allure.feature("Comments")
@pytest.mark.api
@allure.title("GET /comments возвращает список комментариев")
def test_get_comments_returns_list(api_client):
    response = api_client.get_collection("comments")

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_list_response(payload)
    assert_required_keys(payload[0], RESOURCE_SCHEMAS["comments"]["required_keys"])


@allure.epic("API")
@allure.feature("Comments")
@pytest.mark.api
@allure.title("GET /comments/1 возвращает комментарий по id")
def test_get_comment_by_id_returns_comment(api_client):
    response = api_client.get_by_id("comments", 1)

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_object_response(payload)
    assert payload["id"] == 1
    assert_required_keys(payload, RESOURCE_SCHEMAS["comments"]["required_keys"])


@allure.epic("API")
@allure.feature("Comments")
@pytest.mark.api
@allure.title("GET /comments/0 возвращает пустой объект")
def test_get_missing_comment_returns_empty_object(api_client):
    response = api_client.get_by_id("comments", 0)

    assert_status_code(response.status_code, 404)
    assert response.json() == {}


@allure.epic("API")
@allure.feature("Comments")
@pytest.mark.api
@allure.title("POST /comments создает комментарий")
def test_create_comment(api_client):
    response = api_client.create("comments", POST_PAYLOADS["comments"])

    assert_status_code(response.status_code, 201)
    payload = response.json()
    assert payload["email"] == POST_PAYLOADS["comments"]["email"]
    assert "id" in payload
