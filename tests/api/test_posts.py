import allure
import pytest

from data.api_payloads import PATCH_POST_PAYLOAD, POST_PAYLOADS, PUT_POST_PAYLOAD, RESOURCE_SCHEMAS
from utils.assertions import assert_list_response, assert_object_response, assert_required_keys, assert_status_code


@allure.epic("API")
@allure.feature("Posts")
@pytest.mark.api
@pytest.mark.smoke
@allure.title("GET /posts возвращает список постов")
def test_get_posts_returns_list(api_client):
    response = api_client.get_collection("posts")

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_list_response(payload)
    assert_required_keys(payload[0], RESOURCE_SCHEMAS["posts"]["required_keys"])


@allure.epic("API")
@allure.feature("Posts")
@pytest.mark.api
@allure.title("GET /posts/1 возвращает пост по id")
def test_get_post_by_id_returns_post(api_client):
    response = api_client.get_by_id("posts", 1)

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert_object_response(payload)
    assert payload["id"] == 1
    assert_required_keys(payload, RESOURCE_SCHEMAS["posts"]["required_keys"])


@allure.epic("API")
@allure.feature("Posts")
@pytest.mark.api
@allure.title("GET /posts/0 возвращает пустой объект")
def test_get_missing_post_returns_empty_object(api_client):
    response = api_client.get_by_id("posts", 0)

    assert_status_code(response.status_code, 404)
    assert response.json() == {}


@allure.epic("API")
@allure.feature("Posts")
@pytest.mark.api
@allure.title("POST /posts создает новый пост")
def test_create_post(api_client):
    response = api_client.create("posts", POST_PAYLOADS["posts"])

    assert_status_code(response.status_code, 201)
    payload = response.json()
    assert payload["title"] == POST_PAYLOADS["posts"]["title"]
    assert "id" in payload


@allure.epic("API")
@allure.feature("Posts")
@pytest.mark.api
@allure.title("PUT /posts/1 обновляет пост")
def test_put_post_updates_post(api_client):
    response = api_client.update("posts", 1, PUT_POST_PAYLOAD)

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert payload["title"] == PUT_POST_PAYLOAD["title"]
    assert payload["userId"] == PUT_POST_PAYLOAD["userId"]


@allure.epic("API")
@allure.feature("Posts")
@pytest.mark.api
@allure.title("PATCH /posts/1 обновляет только часть поста")
def test_patch_post_updates_post_partially(api_client):
    response = api_client.partial_update("posts", 1, PATCH_POST_PAYLOAD)

    assert_status_code(response.status_code, 200)
    payload = response.json()
    assert payload["title"] == PATCH_POST_PAYLOAD["title"]


@allure.epic("API")
@allure.feature("Posts")
@pytest.mark.api
@allure.title("DELETE /posts/1 удаляет пост")
def test_delete_post(api_client):
    response = api_client.remove("posts", 1)

    assert_status_code(response.status_code, 200)
    assert response.json() == {}
