import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FORM_TITLE = "div.login-form h2"
    EMAIL_INPUT = "input[data-qa='login-email']"
    PASSWORD_INPUT = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    ERROR_MESSAGE = "div.login-form p"
    SIGNUP_NAME_INPUT = "input[data-qa='signup-name']"
    SIGNUP_EMAIL_INPUT = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step("Проверить открытие страницы Signup / Login")
    def should_be_opened(self):
        expect(self.page).to_have_url(f"{self.base_url}/login")
        expect(self.page.locator(self.LOGIN_FORM_TITLE)).to_contain_text("Login to your account")

    @allure.step("Выполнить неуспешный логин")
    def login_with_invalid_credentials(self, email: str, password: str):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Проверить сообщение об ошибке логина")
    def should_show_invalid_login_error(self):
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text("Your email or password is incorrect!")

    @allure.step("Проверить доступность формы регистрации")
    def should_show_signup_form(self):
        expect(self.page.locator(self.SIGNUP_NAME_INPUT)).to_be_visible()
        expect(self.page.locator(self.SIGNUP_EMAIL_INPUT)).to_be_visible()
        expect(self.page.locator(self.SIGNUP_BUTTON)).to_be_visible()
