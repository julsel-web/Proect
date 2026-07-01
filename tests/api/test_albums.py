import allure
import pytest

from data.api_payloads import POST_PAYLOADS, RESOURCE_SCHEMAS
from utils.assertions import assert_list_response, assert_object_response, assert_required_keys, assert_status_code


@allure.epic("API")
@allure.feature("Albums")
@pytest.mark.api
@allure.title("GET /albums возвращает список альбомов")
def test_get_albums_returns_list(api_client):
    response = api_client.get_collection("albums")

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_list_response(payload)
    assert_required_keys(payload[0], RESOURCE_SCHEMAS["albums"]["required_keys"])


@allure.epic("API")
@allure.feature("Albums")
@pytest.mark.api
@allure.title("GET /albums/1 возвращает альбом по id")
def test_get_album_by_id_returns_album(api_client):
    response = api_client.get_by_id("albums", 1)

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_object_response(payload)
    assert payload["id"] == 1
    assert_required_keys(payload, RESOURCE_SCHEMAS["albums"]["required_keys"])


@allure.epic("API")
@allure.feature("Albums")
@pytest.mark.api
@allure.title("POST /albums создает альбом")
def test_create_album(api_client):
    response = api_client.create("albums", POST_PAYLOADS["albums"])

    assert_status_code(response.status_code, 201)
    payload = response.json()
    assert payload["title"] == POST_PAYLOADS["albums"]["title"]
    assert "id" in payload
