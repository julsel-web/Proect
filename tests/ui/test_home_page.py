import allure
import pytest

from pages.home_page import HomePage


@allure.epic("UI")
@allure.feature("Главная страница")
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Открытие главной страницы Automation Exercise")
def test_home_page_is_opened(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)

    home_page.open_home_page()

    home_page.should_be_opened()


@allure.epic("UI")
@allure.feature("Навигация")
@pytest.mark.ui
@allure.title("Переход из шапки в Products")
def test_user_can_open_products_from_header(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_products()

    assert "/products" in ui_page.url


@allure.epic("UI")
@allure.feature("Навигация")
@pytest.mark.ui
@allure.title("Переход из шапки в Signup / Login")
def test_user_can_open_login_from_header(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_login()

    assert "/login" in ui_page.url


@allure.epic("UI")
@allure.feature("Навигация")
@pytest.mark.ui
@allure.title("Переход из шапки в Contact Us")
def test_user_can_open_contact_us_from_header(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_contact_us()

    assert "/contact_us" in ui_page.url
