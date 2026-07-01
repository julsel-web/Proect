import allure
import pytest

from data.ui_data import CONTACT_FORM_DATA
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage


@allure.epic("UI")
@allure.feature("Contact Us")
@pytest.mark.ui
@allure.title("Пользователь может открыть Contact Us")
def test_contact_us_page_is_opened(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    contact_page = ContactUsPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_contact_us()

    contact_page.should_be_opened()


@allure.epic("UI")
@allure.feature("Contact Us")
@pytest.mark.ui
@allure.title("Пользователь может заполнить форму Contact Us")
def test_user_can_fill_contact_us_form(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    contact_page = ContactUsPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_contact_us()
    contact_page.fill_message_form(CONTACT_FORM_DATA)

    contact_page.should_have_filled_form(CONTACT_FORM_DATA)
