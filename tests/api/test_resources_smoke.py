import allure
import pytest

from utils.assertions import assert_list_response, assert_status_code


@allure.epic("API")
@allure.feature("Smoke")
@pytest.mark.api
@pytest.mark.parametrize("resource", ["posts", "comments", "albums", "photos", "todos", "users"])
@allure.title("Коллекция {resource} отвечает статусом 200 и не пуста")
def test_resource_collection_is_not_empty(api_client, resource):
    response = api_client.get_collection(resource)

    assert_status_code(response.status_code, 200)
    assert_list_response(response.json())
