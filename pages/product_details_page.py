import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    PRODUCT_INFORMATION = ".product-information"
    PRODUCT_NAME = ".product-information h2"
    ADD_TO_CART_BUTTON = "button.cart"
    QUANTITY_INPUT = "#quantity"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step("Проверить страницу карточки товара")
    def should_be_opened(self):
        assert "/product_details/" in self.page.url
        expect(self.page.locator(self.PRODUCT_INFORMATION)).to_be_visible()
        expect(self.page.locator(self.PRODUCT_NAME)).not_to_be_empty()

    @allure.step("Проверить значение количества товара")
    def should_have_default_quantity(self, quantity: str = "1"):
        expect(self.page.locator(self.QUANTITY_INPUT)).to_have_value(quantity)

    @allure.step("Добавить товар в корзину из карточки")
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
