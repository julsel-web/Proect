from pathlib import Path

import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class ContactUsPage(BasePage):
    CONTACT_FORM = ".contact-form"
    GET_IN_TOUCH_TITLE = "div.contact-form h2.title"
    NAME_INPUT = "input[data-qa='name']"
    EMAIL_INPUT = "input[data-qa='email']"
    SUBJECT_INPUT = "input[data-qa='subject']"
    MESSAGE_TEXTAREA = "textarea[data-qa='message']"
    UPLOAD_INPUT = "input[name='upload_file']"
    SUBMIT_BUTTON = "input[data-qa='submit-button']"
    SUCCESS_MESSAGE = ".contact-form .status.alert.alert-success"
    HOME_BUTTON = "a.btn.btn-success"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step("Проверить открытие страницы Contact Us")
    def should_be_opened(self):
        expect(self.page).to_have_url(f"{self.base_url}/contact_us")
        expect(self.page.locator(self.GET_IN_TOUCH_TITLE)).to_contain_text("Get In Touch")

    @allure.step("Заполнить форму Contact Us")
    def fill_message_form(self, form_data: dict):
        self.fill(self.NAME_INPUT, form_data["name"])
        self.fill(self.EMAIL_INPUT, form_data["email"])
        self.fill(self.SUBJECT_INPUT, form_data["subject"])
        self.fill(self.MESSAGE_TEXTAREA, form_data["message"])
        self.page.locator(self.UPLOAD_INPUT).set_input_files(str(Path(__file__).resolve()))

    @allure.step("Отправить форму Contact Us")
    def submit_message(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.locator(self.SUBMIT_BUTTON).scroll_into_view_if_needed()
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Проверить, что форма Contact Us заполнена")
    def should_have_filled_form(self, form_data: dict):
        expect(self.page.locator(self.NAME_INPUT)).to_have_value(form_data["name"])
        expect(self.page.locator(self.EMAIL_INPUT)).to_have_value(form_data["email"])
        expect(self.page.locator(self.SUBJECT_INPUT)).to_have_value(form_data["subject"])
        expect(self.page.locator(self.MESSAGE_TEXTAREA)).to_have_value(form_data["message"])
        expect(self.page.locator(self.UPLOAD_INPUT)).not_to_have_value("")

    @allure.step("Проверить успешную отправку Contact Us")
    def should_show_success_message(self):
        success_message = self.page.locator(".status.alert.alert-success").filter(has_text="Success!")
        expect(success_message).to_be_visible()
        expect(success_message).to_contain_text("Success!")
        expect(success_message).to_contain_text("submitted successfully")
        expect(self.page.locator(self.HOME_BUTTON)).to_be_visible()
