import allure
import pytest

from data.ui_data import INVALID_USER
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.epic("UI")
@allure.feature("Авторизация")
@pytest.mark.ui
@allure.title("Неуспешный логин показывает сообщение об ошибке")
def test_invalid_login_shows_error(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    login_page = LoginPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_login()
    login_page.should_be_opened()
    login_page.login_with_invalid_credentials(**INVALID_USER)

    login_page.should_show_invalid_login_error()


@allure.epic("UI")
@allure.feature("Авторизация")
@pytest.mark.ui
@allure.title("Форма регистрации нового пользователя доступна на странице логина")
def test_signup_form_is_visible(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    login_page = LoginPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_login()

    login_page.should_show_signup_form()
