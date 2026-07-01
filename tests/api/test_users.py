import allure
import pytest

from data.api_payloads import RESOURCE_SCHEMAS
from utils.assertions import assert_list_response, assert_object_response, assert_required_keys, assert_status_code


@allure.epic("API")
@allure.feature("Users")
@pytest.mark.api
@allure.title("GET /users возвращает список пользователей")
def test_get_users_returns_list(api_client):
    response = api_client.get_collection("users")

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_list_response(payload)
    assert_required_keys(payload[0], RESOURCE_SCHEMAS["users"]["required_keys"])


@allure.epic("API")
@allure.feature("Users")
@pytest.mark.api
@allure.title("GET /users/1 возвращает пользователя по id")
def test_get_user_by_id_returns_user(api_client):
    response = api_client.get_by_id("users", 1)

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_object_response(payload)
    assert payload["id"] == 1
    assert_required_keys(payload, RESOURCE_SCHEMAS["users"]["required_keys"])


@allure.epic("API")
@allure.feature("Users")
@pytest.mark.api
@allure.title("GET /users/0 возвращает пустой объект")
def test_get_missing_user_returns_empty_object(api_client):
    response = api_client.get_by_id("users", 0)

    assert_status_code(response.status_code, 404)
    assert response.json() == {}
