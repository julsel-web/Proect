import allure
import pytest

from data.api_payloads import RESOURCE_SCHEMAS
from utils.assertions import assert_list_response, assert_object_response, assert_required_keys, assert_status_code


@allure.epic("API")
@allure.feature("Photos")
@pytest.mark.api
@allure.title("GET /photos возвращает список фотографий")
def test_get_photos_returns_list(api_client):
    response = api_client.get_collection("photos")

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_list_response(payload)
    assert_required_keys(payload[0], RESOURCE_SCHEMAS["photos"]["required_keys"])


@allure.epic("API")
@allure.feature("Photos")
@pytest.mark.api
@allure.title("GET /photos/1 возвращает фотографию по id")
def test_get_photo_by_id_returns_photo(api_client):
    response = api_client.get_by_id("photos", 1)

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_object_response(payload)
    assert payload["id"] == 1
    assert_required_keys(payload, RESOURCE_SCHEMAS["photos"]["required_keys"])


@allure.epic("API")
@allure.feature("Photos")
@pytest.mark.api
@allure.title("GET /photos/0 возвращает пустой объект")
def test_get_missing_photo_returns_empty_object(api_client):
    response = api_client.get_by_id("photos", 0)

    assert_status_code(response.status_code, 404)
    assert response.json() == {}
