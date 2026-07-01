import allure


@allure.step("Проверить код ответа {actual_status} == {expected_status}")
def assert_status_code(actual_status: int, expected_status: int):
    assert actual_status == expected_status, f"Ожидался статус {expected_status}, получен {actual_status}"


@allure.step("Проверить наличие обязательных ключей в объекте")
def assert_required_keys(payload: dict, required_keys: set[str]):
    missing = required_keys - set(payload.keys())
    assert not missing, f"В ответе отсутствуют ключи: {sorted(missing)}"


@allure.step("Проверить, что ответ содержит список")
def assert_list_response(payload):
    assert isinstance(payload, list), f"Ожидался список, получен {type(payload).__name__}"
    assert payload, "Ответ пустой"


@allure.step("Проверить, что ответ содержит объект")
def assert_object_response(payload):
    assert isinstance(payload, dict), f"Ожидался объект, получен {type(payload).__name__}"
